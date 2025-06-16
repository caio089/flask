from flask import Flask, request, render_template
from gemini import content
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///historico.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Pesquisa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(200), nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)



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
            # 🆕 SALVAR NO BANCO
            nova_pesquisa = Pesquisa(texto=pergunta)
            db.session.add(nova_pesquisa)
            db.session.commit()

            resposta = content(pergunta)

    # 🆕 PEGAR O HISTÓRICO PARA MOSTRAR NO HTML
    historico = Pesquisa.query.order_by(Pesquisa.data_hora.desc()).all()

    return render_template('index.html', resposta=resposta, historico=historico)


if __name__ == '__main__':
 with app.app_context():
    db.create_all()
    app.run(debug=True)

