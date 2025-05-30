from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá mundo'

@app.route('/post', methods=['POST'])
def post():
    dados = request.get_json()

    nome = dados.get('nome')
    idade = dados.get('idade')

    return f'''
    <h1>Dados recebidos!</h1>
    <p>Nome: {nome}</p>
    <p>Idade: {idade}</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
