from flask import Flask, request
from gemini import content

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    # Tenta pegar do JSON
    if request.is_json:
        data = request.get_json()
        pergunta = data.get('pergunta')
    else:
        # Tenta pegar do formulário (form-data ou x-www-form-urlencoded)
        pergunta = request.form.get('pergunta')

    if pergunta:
        resposta = content(pergunta)
        return resposta, 200
    else:
        return 'Nenhuma pergunta válida.', 400


@app.route('/', methods=['GET'])
def status():
    return 'API funcionando. Use POST para enviar sua pergunta.', 200


if __name__ == '__main__':
    app.run(debug=True)
