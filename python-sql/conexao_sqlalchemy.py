from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

# Substitua pelos seus dados do banco
USER = "postgres"
PASSWORD = ""
HOST = "localhost"  # ou IP do servidor
DB_NAME = "sqlalchemy"

# Criando a conexão
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}')

# Criando a sessao para interagir com o banco de dados
Session = sessionmaker(bind=engine) # Ligamos a sessão à conexão do banco
session = Session()

# criando tabelas
Base = declarative_base()

class Usuario(Base):
  __tablename__ = 'usuarios'

  id = Column("id", Integer, primary_key=True, autoincrement=True)
  nome = Column("nome", String)
  email = Column("email", String)
  senha = Column("senha", String)
  ativo = Column("ativo", Boolean)

  def __init__(self, nome, email, senha, ativo = True):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.ativo = ativo
    

class Livro(Base):
  __tablename__ = 'livros'

  id = Column("id", Integer, primary_key=True, autoincrement=True)
  titulo = Column("titulo", String)
  qtd_paginas = Column("qtd_paginas", Integer)
  dono = Column("dono", ForeignKey("usuarios.id"))

  def __init__(self, titulo, qtd_paginas, dono):
    self.titulo = titulo
    self.qtd_paginas = qtd_paginas
    self.dono = dono
    

Base.metadata.create_all(engine)

# ----------- Create -----------

# usuario = Usuario(nome = 'Lira', email = 'lira@gmail.com', senha = 123)
# session.add(usuario)
# session.commit()

# ----------- Read -----------

# lista_usuarios = session.query(Usuario).all()
# lista_usuarios = session.query(Usuario).first()
# print(lista_usuarios)
usuario_lira = session.query(Usuario).filter_by(email = 'lira@gmail.com').first()
print(usuario_lira)

# ----------- Create Livro -----------
livro = Livro(titulo = 'Nome do vento', qtd_paginas= 10000, dono=usuario_lira.id)
session.add(livro)
session.commit()

# ----------- Update -----------

usuario_lira.nome = 'Joao lira'
session.add(usuario_lira)
session.commit()

# ----------- Delete -----------
try:
  session.delete(usuario_lira)
  session.commit()
except Exception as e:
  print()