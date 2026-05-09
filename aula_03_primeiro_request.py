# Biblioteca para fazer requisições HTTP em Python
import requests

# URL alvo da requisição
url = "https://www.google.com"

# Realiza uma requisição GET e armazena a resposta
resposta = requests.get(url)

# Exibe o objeto de resposta (ex: <Response [200]>) e o conteúdo HTML da página
print(resposta, end="\n\n\n\n")
print(resposta.text)

# Salva o HTML retornado em um arquivo local para análise
with open("pagina.google.html", "w", encoding="utf-8") as arquivo:
    arquivo.write(resposta.text)