import os
from openai import OpenAI
from dotenv import load_dotenv
import openai

load_dotenv()

open_ai_key = os.getenv("OPENAI_API_KEY")
cliente = OpenAI(api_key=open_ai_key)

MODELO = "gpt-4o-mini"

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")

def analisador_sentimentos(produto):
    prompt_sistema = f"""
    Você é um analisador de sentimentos de avaliações de produtos.
    Escreva um parágrafo com até 50 palavras resumindo as avaliações e depois atribua qual o sentimento geral
    para o produto.
    Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

    # Formato de Saída
    Nome do Produto:
    Resumo das Avaliações:
    Sentimento Geral: [Utilize aqui apenas Positivo, Negativo ou Neutro]
    Pontos fortes: Lista com 3 bullets
    Pontos fracos: Lista com 3 bullets
    """

    prompt_usuario = carrega(f"./dados/avaliacoes-{produto}.txt")
    print(f"Iniciou a análise de sentimentos do produto: {produto}")

    lista_mensagens = [
        { "role": "system", "content": prompt_sistema },
        { "role": "user", "content": prompt_usuario }
    ]

    try:
        resposta = cliente.chat.completions.create(
            messages = lista_mensagens,
            model = MODELO
        )
        texto_resposta = resposta.choices[0].message.content
        salva(f"./dados/analise-{produto}.txt", texto_resposta)
    except openai.AuthenticationError as e:
        print(f"Erro de autenticação: {e}")
    except openai.OpenAIError as e:
        print(f"Erro de API: {e}")

analisador_sentimentos("Maquiagem mineral")

