import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

open_ai_key = os.getenv("OPENAI_API_KEY")
cliente = OpenAI(api_key=open_ai_key)

MODELO = "gpt-4o-mini"

def categoriza_nome_produto(nome_produto, lista_categorias_possiveis):
    prompt_sistema = f""" 
    Você é um categorizador de produtos.
    Você deve assumir as categorias presentes na lista abaixo:

    # Lista de Categorias Válidas
    {lista_categorias_possiveis.split(",")}

    # Formato da Saída
    Produto: Nome do Produto
    Categoria: Apresente a categoria do produto

    # Exemplo de Saída
    Produto: Escova elétrica com recarga solar
    Categoria: Eletrônicos Verdes
    """

    resposta = cliente.chat.completions.create(
        model=MODELO,
        max_tokens=200,
        # temperature=1.0,
        messages=[
            { "role": "system", "content": prompt_sistema },
            { "role": "user", "content": nome_produto }
        ]
    )
    return resposta.choices[0].message.content


categorias_validas = input("Informe as categorias válidas, separando por vírgula: ")

while True:
    nome_produto = input("Digite o nome de um produto: ")
    categoria = categoriza_nome_produto(nome_produto, categorias_validas)
    print(f"Categoria: {categoria}")