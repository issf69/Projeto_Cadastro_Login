from model import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib


def retorna_session():
    CONN = "sqlite:///projeto2.db"
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()


class ControllerCadastro():
    @classmethod
    def verifica_dados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2  # Código 2: Nome fora do intervalo esperado
        if len(email) > 200:
            return 3  # Código 3: Email muito longo
        if len(senha) > 100 or len(senha) < 6:
            return 4  # Código 4: Senha fora do intervalo esperado

        return 1  # Código 1: Dados verificados com sucesso

    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = retorna_session()

        # Verifica se o email já existe no banco de dados
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all()
        if len(usuario) > 0:
            return 5  # Código 5: Email já cadastrado

        # Verifica se os dados estão dentro dos limites esperados
        dados_verificados = cls.verifica_dados(nome, email, senha)
        if dados_verificados != 1:
            return dados_verificados

        # Tenta cadastrar a nova pessoa
        try:
            # Hash da senha usando SHA-256
            senha_hash = hashlib.sha256(senha.encode()).hexdigest()
            p1 = Pessoa(nome=nome, email=email, senha=senha_hash)
            session.add(p1)
            session.commit()
            return 1  # Código 1: Cadastro realizado com sucesso

        except Exception as e:
            print(f"Erro ao cadastrar pessoa: {e}")
            session.rollback()
            return 6  # Código 3: Erro ao cadastrar pessoa



class ControllerLogin():
    @classmethod
    def login(clscls, email, senha):
        session = retorna_session()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        logado = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.email == email).filter(Pessoa.senha ==senha).all()
        if len(logado) == 1:
            return {'logado': True, 'id': logado[0].id}
        else:
            return False

print(ControllerLogin.login('meuenail@gmail.com', 'minha senha',))
#print(ControllerCadastro.cadastrar('irene', 'meuemailaqui@gmail.com', 'minha senha'))


# Exemplo de uso do método cadastrar:
#print(ControllerCadastro.cadastrar('Irene', 'outroyrenysylvafranssa@gmail.com', 'irene1234'))

#senha = "minha senha"
 #   string = "minha senha"
#print(type(string))

#print(string)
#print(type(string.encode()))
#print(string.encode())
    #print(hashlib.sha256(senha.encode()))
    #print(hashlib.sha256(senha.encode()).hexdigest())
#senha criptografada