import json
import urllib.request

#solicitar ao o usuário do CEP
cep = input('Digite o CEP:')

# Construir na URL de consulta
url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    # Fazer a requisição
    response = urllib.request.urlopen(url)

    # Ler o conteudo da resposta
    data = response.read().decode('utf-8')
    
    #   Converter JSON em dicionario Python
    endereco = json.loads(data)

    # Verificar se a consulta foi bem-sucedida 
    if endereco.get('erro'):
        print("CEP ão encontrado")
    else:
        # Armazenar informaçoes em variáveis
        logradouro = endereco['logradouro']
        complemento = endereco['complemento']
        bairro = endereco['bairro']
        cidade = endereco['localidade']
        estado = endereco['uf']
    
        # Exibir informaçoes do endereço na tela
        print(f"Logradouro: {logradouro}")
        print(f"Completamento: {complemento}")
        print(f"Bairro:{bairro}")
        print(f"Cidade:{cidade}")
        print(f"Estado:{estado}")
    
    # Fechar a conexão
    response.close()
except Exception as e:
    print(f"Erro: {e}")
