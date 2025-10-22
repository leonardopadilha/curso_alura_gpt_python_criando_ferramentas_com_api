import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

open_ai_key = os.getenv("OPENAI_API_KEY")
cliente = OpenAI(api_key=open_ai_key)

resposta = cliente.chat.completions.create(
    model="gpt-4o-mini",
    max_tokens=200,
    temperature=1.0,
    n = 3,
    messages=[
        { "role": "system", 
        "content": """ 
            Classifique o produto abaixo em uma das categorias: Higiene Pessoal, Moda ou Casa e dê uma
            breve descrição da categoria.
        """ },
        { "role": "user", 
        "content": """ 
            Escova de dentes de bambu 
        """}
    ]
)

for contador in range(0, 3):
    print(resposta.choices[contador].message.content)
    print("--------------------------------")