import requests
import json

from datetime import datetime
import os

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import base
from models.db_models import Info


class CepAPI():

    API_URL = 'https://viacep.com.br/ws/{}/json/'
    DATABASE_NAME = 'dbcep'

    def __init__(self, cep, city) -> None: # instance the variables to use
        self.cep = self.format_cep(cep)
        self.suggested_city = city
        CepAPI.API_URL = CepAPI.API_URL.replace("{}", self.cep)
    
    def format_cep(self, raw_cep): # format cep to use at API
        return raw_cep.replace(" ", "").replace("-", "")
    
    def request(self): # get datas from API
        response = requests.get(CepAPI.API_URL)
        if response.status_code != 200:
            raise ValueError('Error during request, verify if your cep is valid')
        
        result = self.validate(response.json())
        return result
    
    def validate(self, result): # insert time at created field and write the validation field
        
        result['created'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S").replace('/', '-') # current time as DD-MM-YY HH:mm:ss
        result['validation'] = True if result['localidade'] == self.suggested_city else False

        return result
          
    def database(self): # configure connection and create database
        engine = create_engine(f'sqlite:///{CepAPI.DATABASE_NAME}.db')
        if not os.path.exists(os.path.join(os.getcwd(), f'{CepAPI.DATABASE_NAME}.db')):
            base.metadata.drop_all(bind=engine)
            base.metadata.create_all(bind=engine) 
        
        Conn = sessionmaker(bind=engine)
        connection = Conn()
        return connection

    def save_data(self, data): # save cep info at database
        self.connection = self.database()
        try:
            new_info = Info()
            
            new_info.cep = data['cep']
            new_info.logradouro = data['logradouro']
            new_info.complemento = data['complemento']
            new_info.bairro = data['bairro']
            new_info.localidade = data['localidade']
            new_info.uf = data['uf']
            new_info.ibge = data['ibge']
            new_info.gia = data['gia']
            new_info.ddd = data['ddd']
            new_info.siafi = data['siafi']

            # additional fields
            new_info.created = data['created']
            new_info.validation  = data['validation']

            self.connection.add(new_info)
            self.connection.commit() # saving
        
        except Exception as e:
            print('erro', e)
        
        else:
            print('ok')
