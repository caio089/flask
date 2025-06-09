from flask import Flask, request, render_template
from gemini import content

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    resposta = None

    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            pergunta = data.get('pergunta')
        else:
            pergunta = request.form.get('pergunta')

        if pergunta:
            resposta = content(pergunta)

    return render_template('index.html', resposta=resposta)


if __name__ == '__main__':
    app.run(debug=True)

