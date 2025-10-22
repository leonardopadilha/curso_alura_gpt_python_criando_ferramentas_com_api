import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

open_ai_key = os.getenv("OPENAI_API_KEY")
cliente = OpenAI(api_key=open_ai_key)

resposta = cliente.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        { "role": "system", "content": "Listar apenas os nomes dos produtos, sem considerar descrição." },
        { "role": "user", "content": "Liste 3 produtos sustentáveis"}
    ]
)

print(resposta.choices[0].message.content)