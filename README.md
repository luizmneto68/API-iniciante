# Aula 03 – Primeiro Request HTTP com Python (Asimov Academy)

## Descrição

Nesta aula fazemos a nossa primeira requisição HTTP usando Python. Utilizamos a biblioteca `requests` para enviar um `GET` para o Google, inspecionar a resposta e salvar o HTML retornado em um arquivo local.

---

## Conceitos abordados

- Método HTTP **GET**
- Objeto **Response** e o que ele representa
- Acesso ao conteúdo da resposta via `response.text`
- Escrita de arquivo com `open()` e encoding UTF-8

---

## Pré-requisitos

- Python 3.x instalado
- Biblioteca `requests`:

```bash
pip install requests
```

---

## Como executar

```bash
python aula_03_primeiro_request.py
```

---

## O que o código faz

| Passo | O que acontece |
|-------|---------------|
| 1 | Importa a biblioteca `requests` |
| 2 | Define a URL alvo (`https://www.google.com`) |
| 3 | Realiza uma requisição GET e armazena a resposta |
| 4 | Imprime o objeto de resposta (ex: `<Response [200]>`) |
| 5 | Imprime o conteúdo HTML da página no terminal |
| 6 | Salva o HTML em `pagina.google.html` para análise |

---

## Saída esperada no terminal

```
<Response [200]>


<!doctype html><html ...>...</html>
```

---

## Arquivos gerados

| Arquivo | Descrição |
|---------|-----------|
| `pagina.google.html` | HTML retornado pelo Google, salvo localmente para análise |
