import requests
from typing import Dict, Any

def enviar_request_post(url: str, params: Dict[str, str], data: Dict[str, Any], timeout: int = 5) -> None:
    """
    Envia uma requisição POST e exibe a resposta com tratamento de erros.
    
    Args:
        url: URL do servidor
        params: Parâmetros de query string
        data: Dados JSON a enviar
        timeout: Tempo máximo de espera em segundos
    """
    try:
        resposta = requests.post(url, json=data, params=params, timeout=timeout)
        resposta.raise_for_status()
        
        print(f"Status Code: {resposta.status_code}")
        print(f"URL da Requisição: {resposta.request.url}")
        print("\nResposta JSON:")
        print(resposta.json())
        
    except requests.exceptions.Timeout:
        print("Erro: Requisição excedeu o tempo limite")
    except requests.exceptions.ConnectionError:
        print("Erro: Falha ao conectar ao servidor")
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP {resposta.status_code}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

if __name__ == "__main__":
    url = "https://httpbin.org/post"
    
    params = {
        "dataInicio": "2024-01-01",
        "dataFim": "2024-01-31"
    }
    
    data = {
        "D.N.": "01/02/2000",
        "CPF": "123.456.789-00",
        "Pessoal": {
            "Nome": "Fulano de Tal",
            "Sexo": "Masculino",
            "Nacionalidade": "Brasileiro",
            "Médico": True
        }
    }
    
    enviar_request_post(url, params, data)