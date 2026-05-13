import requests

url = "https://httpbin.org/post"

Params = {
    "dataInicio" : "2024-01-01",
    "dataFim" : "2024-01-31"
}


data = {
    "D.N." : "01/02/2000",
    "CPF" : "123.456.789-00",
    "Pessoal": {
        "Nome" : "Fulano de Tal",
        "Sexo" : "Masculino",
        "Nacionalidade" : "Brasileiro",
        "Medidco" : True
    }
}        

resposta = requests.post(url, json=data, params=Params)

print("Status Code: " + str(resposta.status_code))
print("\n")
print(resposta.json())
print("\n")
print(resposta.request.url)
print("\n")