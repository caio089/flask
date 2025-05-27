from main import app

@app.route('/')
def home():
    return 'Olá, mundo! Este é meu primeiro app Flask.'

@app.route('/blog')
def sidebar():
    return 'essa ea pagina do blog'