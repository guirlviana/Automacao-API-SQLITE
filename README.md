# Automacao-API-SQLITE
Informar um CEP, coletar todos os dados retornados na API e inserir no banco de dados SQLite.

## Tópicos 
- Como usar
- Respostas
- O projeto
# Como usar
Instale as libs e suas versões utilizadas no projeto (estão em requirements.txt)
```
pip install requirements.txt
```
Rode o arquivo main.py, antes, insira o CEP desejado (ex: 04117-091 ou 04117091) e a cidade sugerida (ex: São Paulo)<br>
OBS: Caso não exista um arquivo .db ( e com mesmo nome atribuido na variável DATABASE_NAME em cepAPI\CepAPI.py linha 17)
na pasta onde o programa está sendo rodado, ele irá criar um novo banco de dados, caso contrário, reutilizará do mesmo.

```
from cepAPI import CepAPI

def main():

    app = CepAPI('**your cep**', '**your suggested city**')
    app.save_data(app.request())

if __name__ == '__main__':
    main()
```
# Respostas
Ao rodar a aplicação você receberá:

| Resposta | Resultado |
| ------ | ------ |
| ok |Sucesso (Requisição bem sucedida e salvo com sucesso no banco de dados) |
| ValueError|CEP inválido ou falha na requisição |

# O projeto
O projeto é composto por uma pasta (models) e dois arquivos .py (Arquivo Python)

* models (Pasta para configuração do banco de dados)
  * base.py (Contém a declarative base do SQLalchemy para utilizar no restante do código)
  * db_models.py (Arquivo que contém o modelo da tabela a ser utilizada no banco de dados)

* cepAPI.py (Arquivo Python com a classe CepAPI responsável por acessar a API, configurar banco de dados, e guardar as informações)

* main.py (Arquivo Python que representa o uso da classe na prática)
