import google.generativeai as genai

# importar a chave de API do gemini
api = 'AIzaSyCxrE6u0KsbiAR6vLrBnC5PPqG05wl-bTA'
genai.configure(api_key=api)

# configurar o modelo da IA que vai ser usada
model = genai.GenerativeModel('gemini-1.5-flash')


def content(pergunta):
#perguntar e solicitar resposta a IA
 print('faca uma pergunta a IA')
pergunta = input('')
def content(pergunta):
    response = model.generate_content(pergunta)
    return response.text