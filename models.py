import google.generativeai as genai
# listar modelos do gemini disponiveis
genai.configure(api_key="AIzaSyCxrE6u0KsbiAR6vLrBnC5PPqG05wl-bTA")
models = genai.list_models()

for model in models:
    print(model.name)
