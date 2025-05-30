from flask import Flask, request, render_template
from gemini import content  # sua função que chama a IA

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    resposta = ''
    if request.method == 'POST':
        pergunta = request.form.get('pergunta')
        if pergunta:
            resposta = content(pergunta)
            print(f'Pergunta: {pergunta}')   # mostra no terminal
            print(f'Resposta: {resposta}')   # mostra no terminal
    return render_template('index.html', resposta=resposta)

if __name__ == '__main__':
    app.run(debug=True)
