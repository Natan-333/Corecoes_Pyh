import pip._vendor.requests

cep = input("Digite o o nome do usuário: ")
url = f" https://api.github.com/users/"


response = pip._vendor.requests.get(url)


if response.status_code == 200:
    dados = response.json()
    print(f"Nome: {dados['Name']}")
    print(f"Quantidade de Repositorios {dados['repositories']}")
    print(f"Seguiodres {dados['Followers']}")
    
else:
    print("Git não encontrado")