import requests

url_status = 'https://arapuka.onrender.com/status'
url_comando = 'https://arapuka.onrender.com/comando'
url_resposta = 'https://arapuka.onrender.com/resposta'

#posta mensagem na url /comando
def post_comando(comando):
    # Cabeçalhos da requisição
    headers = {
    'Content-Type': 'text/html'
    }
    try:
        response = requests.post(url_comando, headers=headers, data=comando)
        if response.status_code == 200:
            return "POST realizado com sucesso."
        else:
            return f"Erro no POST request: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Erro no POST request: {e}"       


#posta mensagem em branco na url /resposta, serve para pegar só uma vez o conteúdo
def delete_resposta():
    # Cabeçalhos da requisição
    headers = {
    'Content-Type': 'text/html'
    }
    for i in range(5):
        response = requests.post(url_resposta, headers=headers, data='')
        if response.status_code == 200:
            return 
           

#pega mensagem em qualquer url
# a url eh definida na threading.Thread(target=update_console, args=(new_window['OutputGet'], requisicoes.url_comando))  
def get_resposta(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Erro na solicitação: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Erro na solicitação: {e}"