import os
import tiktoken
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
open_ai_key = os.getenv("OPENAI_API_KEY")
cliente = OpenAI(api_key=open_ai_key)

MODELO = "gpt-4"
codificador = tiktoken.encoding_for_model(MODELO)

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")

prompt_sistema = f"""
Identifique o perfil de compra para cada cliente a seguir.
O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

prompt_usuario = carrega("./dados/lista_de_compras_100_clientes.csv")

lista_tokens = codificador.encode(prompt_sistema + prompt_usuario)
numero_de_tokens = len(lista_tokens)
print(f"Número de tokens na entrada: {numero_de_tokens}")
tamanho_esperado_saida = 2048

if numero_de_tokens >= 4096 - tamanho_esperado_saida:
    modelo = "gpt-4-1106-preview"

print(f"O modelo selecionado é: {MODELO}")

lista_mensagens = [
    { "role": "system", "content": prompt_sistema },
    { "role": "user", "content": prompt_usuario }
]

resposta = cliente.chat.completions.create(
    messages = lista_mensagens,
    model = MODELO
)

print(resposta.choices[0].message.content)