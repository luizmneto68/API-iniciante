# Biblioteca para fazer requisições HTTP em Python
import requests
from pathlib import Path

def baixar_pagina(url: str, arquivo_saida: str = "pagina.google.html", timeout: int = 10) -> bool:
    """
    Faz uma requisição GET e salva o conteúdo HTML em arquivo.
    
    Args:
        url: URL a acessar
        arquivo_saida: Caminho do arquivo para salvar o HTML
        timeout: Tempo máximo de espera em segundos
        
    Returns:
        True se bem-sucedido, False caso contrário
    """
    try:
        resposta = requests.get(url, timeout=timeout)
        resposta.raise_for_status()
        
        print(f"Resposta: {resposta}")
        print(f"Status Code: {resposta.status_code}\n")
        
        Path(arquivo_saida).write_text(resposta.text, encoding="utf-8")
        print(f"✓ HTML salvo em '{arquivo_saida}'")
        return True
        
    except requests.exceptions.Timeout:
        print("✗ Erro: Requisição excedeu o tempo limite")
        return False
    except requests.exceptions.ConnectionError:
        print("✗ Erro: Falha ao conectar ao servidor")
        return False
    except requests.exceptions.HTTPError as e:
        print(f"✗ Erro HTTP {resposta.status_code}: {e}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Erro na requisição: {e}")
        return False
    except IOError as e:
        print(f"✗ Erro ao salvar arquivo: {e}")
        return False

if __name__ == "__main__":
    url = "https://www.google.com"
    baixar_pagina(url)