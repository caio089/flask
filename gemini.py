import google.generativeai as genai

# Configurar a chave de API do Gemini
api = 'AIzaSyCxrE6u0KsbiAR6vLrBnC5PPqG05wl-bTA'
genai.configure(api_key=api)

# Escolher o modelo
model = genai.GenerativeModel('gemini-1.5-flash')


# Função para gerar conteúdo
def content(pergunta):
    response = model.generate_content(pergunta)
    return response.text

# Teste 
if __name__ == "__main__":
    pergunta = input("Faça uma pergunta para a IA: ")
    resposta = content(pergunta)
    print("Resposta:", resposta)
