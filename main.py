from cepAPI import CepAPI

def main():

    app = CepAPI('**your cep**', '**your suggested city**')
    app.save_data(app.request())

if __name__ == '__main__':
    main()