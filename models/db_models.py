from sqlalchemy import Column, Integer,  String, Boolean
from models.base import base


class Info(base):
    __tablename__ = 'informacoes'

    id = Column(Integer, primary_key=True)
    cep = Column(String)
    logradouro = Column(String)
    complemento = Column(String)
    bairro = Column(String)
    localidade = Column(String)
    uf = Column(String)
    ibge = Column(String)
    gia = Column(String)
    ddd = Column(String)
    siafi = Column(String)
    created = Column(String)
    validation = Column(Boolean)

    def __repr__(self):
        return f'Info: {Info}'