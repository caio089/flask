from flask import Flask, request, render_template, redirect, url_for, session
from gemini import content
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'caio-campos-um-segredo-bem-seguro'

# Configurações do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///historico.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo da tabela Pesquisa
class Pesquisa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(200), nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)
    nome_usuario = db.Column(db.String(100), nullable=False)

# Rota de login simples
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form.get('nome')
        adm = request.form.get('adm')  # <- pega o checkbox ('on' se marcado, None se não)
        senha_admin = request.form.get('senha_admin')  # <- pega a senha digitada

        if nome:
            session['usuario'] = nome

            # Corrigido: usar senha_admin, não senha_adm
            if adm == 'on' and senha_admin == 'admin123':
                session['admin'] = True
            else:
                session['admin'] = False

            return redirect(url_for('home'))

    return render_template('login.html')



# Rota principal (home)
@app.route('/', methods=['GET', 'POST'])
def home():
    if 'usuario' not in session:
        return redirect(url_for('login'))  # redireciona para login se não estiver logado

    nome = session['usuario']
    resposta = None

    if request.method == 'POST':
        pergunta = request.form.get('pergunta')
        if pergunta:
            nova_pesquisa = Pesquisa(texto=pergunta, nome_usuario=nome)
            db.session.add(nova_pesquisa)
            db.session.commit()
            resposta = content(pergunta)

    # Verifica se é admin e busca o histórico correto
    if session.get('admin'):
        historico = Pesquisa.query.order_by(Pesquisa.data_hora.desc()).all()
        usuarios = db.session.query(Pesquisa.nome_usuario).distinct().all()
    else:
        historico = Pesquisa.query.filter_by(nome_usuario=nome).order_by(Pesquisa.data_hora.desc()).all()
        usuarios = None

    return render_template('index.html', resposta=resposta, historico=historico, usuarios=usuarios)


# Rota para logout (opcional, para testar)
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))


@app.route('/deletar/<int:id>')
def deletar(id):
    pergunta = Pesquisa.query.get_or_404(id)

    # Verifica se é admin ou dono da pergunta
    if session.get('admin') or session['usuario'] == pergunta.nome_usuario:
        db.session.delete(pergunta)
        db.session.commit()

    return redirect(url_for('home'))




# Criação do banco e execução do app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
