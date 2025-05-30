import requests

url ='https://jsonplaceholder.typicode.com/posts'

dados = {
'titulo': 'meu treino',
'nome' : 'caio',
'idade ':18
}
resposta = requests.post(url, json=dados)


if resposta.status_code == 201:
 print('dados postados com sucesso')
 res = resposta.json()
 print(res)
 id_criado = resposta.json()['id']
else:
 print('erro')


url_get = f'https://jsonplaceholder.typicode.com/posts/{id_criado}'

encontrar_get = requests.get(url_get)

if encontrar_get.status_code == 200:
    print('Post encontrado:')
    print(encontrar_get.json())
else:
    print('Não encontrado')

url_pach = f'https://jsonplaceholder.typicode.com/posts/{id_criado}'

encontrar_pach = requests.patch(url_pach)

if encontrar_pach.status_code == 200:
    print('atuazlizado com sucesso')
    print(encontrar_pach.json())
else:
    print('Não encontrado')   

url_delete = f'https://jsonplaceholder.typicode.com/posts/{id_criado}'

encontrar_delete = requests.patch(url_delete)

if encontrar_delete.status_code == 200:
    print('deletado com sucesso')
    print(encontrar_delete.json())
else:
    print('Não encontrado')      