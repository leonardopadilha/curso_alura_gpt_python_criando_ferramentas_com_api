# =============================================================================
# IMPORTAÇÕES E CONFIGURAÇÕES
# =============================================================================
import os
import json  # Necessário para converter resposta JSON da OpenAI em objeto Python
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Configuração da API OpenAI
open_ai_key = os.getenv("OPENAI_API_KEY")
cliente = OpenAI(api_key=open_ai_key)

MODELO = "gpt-4o-mini"

# =============================================================================
# FUNÇÕES AUXILIARES
# =============================================================================
def carrega(nome_do_arquivo):
    """Carrega conteúdo de arquivo CSV"""
    try:
        with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")

def salva(nome_do_arquivo, conteudo):
    """Salva conteúdo em arquivo TXT"""
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")


def analisar_transacao(lista_transacao):
    """
    ETAPA 1: Análise de Transações
    - Recebe dados CSV como entrada
    - Envia para API OpenAI solicitando análise de fraude
    - Retorna resposta estruturada em formato JSON
    """
    print("1. Executando a análise de transação")

    # Prompt que define as regras de análise e o formato de resposta JSON
    prompt_sistema ="""
    Analise as transações financeiras a seguir e identifique se cada uma delas é uma "Possível Fraude" ou
    deve ser "Aprovada". Adicione um atributo "Status" com um dos valores: "Possível Fraude" ou "Aprovada".

    Cada nova transação deve ser inserida dentro da lista do JSON.

    # Possíveis indicações de fraude
    - Transações com valores muito discrepantes
    - Transações que ocorrem em locais muito distantes um do outro

    Adote o formato de resposta abaixo para compor sua resposta.

    # Formato de Saída
    {
        "transacoes": [
            {
                "id": "id",
                "tipo": "crédito ou débito",
                "estabelecimento": "nome do estabelecimento",
                "horario": "horário da transação",
                "valor": "R$XX,XX",
                "nome_produto": "nome do produto",
                "localizacao": "cidade - estado (País)",
                "status": ""
            }
        ]
    }
    """

    # Prompt que envia os dados CSV e solicita resposta em JSON
    prompt_usuario = f"""Considere o CSV abaixo, onde cada linha é uma transação 
    diferente: {lista_transacao}. Sua resposta deve adotar o #Formato de Resposta (apenas um json sem outros
    comentários)
    """

    # Monta as mensagens para a API OpenAI
    lista_mensagens = [
        { "role": "system", "content": prompt_sistema },
        { "role": "user", "content": prompt_usuario }   
    ]

    # Chama a API OpenAI para análise
    resposta = cliente.chat.completions.create(
        messages = lista_mensagens,
        model = MODELO,
        temperature = 0
    )

    # Processa a resposta da API
    conteudo = resposta.choices[0].message.content.replace("'", '"') # Substitui as aspas simples por aspas duplas
    print("\Conteúdo: ", conteudo)
    json_resultado = json.loads(conteudo) # Converte o conteúdo JSON da API para objeto Python
    print("\nJSON: ", json_resultado)
    return json_resultado


def gerar_parecer(transacao):
    """
    ETAPA 2: Geração de Parecer
    - Recebe transação individual do JSON
    - Gera parecer detalhado apenas para transações suspeitas
    - Retorna justificativa da análise de fraude
    """
    print("2. Gerando um parecer para cada transação")

    # Prompt para gerar parecer detalhado da transação suspeita
    prompt_sistema = f"""
    Para a seguinte transação, forneça um parecer, apenas se o status dela for de "Possível Fraude". Indique no parecer
    uma justificativa para que você identifique uma fraude.
    Transação: {transacao}

    ## Formato de Resposta
    "id": "id",
    "tipo": "crédito ou débito",
    "estabelecimento": "nome do estabelecimento",
    "horario": "horário da transação",
    "valor": R$XX,XX,
    "nome_produto": "nome do produto",
    "localizacao": "cidade - estado (País)",
    "status": "",
    "parecer": "Colocar Não Aplicável se o status for Aprovado"
    """

    lista_mensagens = [
        { "role": "user", "content": prompt_sistema }
    ]

    # Chama API para gerar parecer detalhado
    resposta = cliente.chat.completions.create(
        messages = lista_mensagens,
        model = MODELO
    )

    conteudo = resposta.choices[0].message.content
    print("Finalizou a geração de parecer")
    return conteudo


def gerar_recomendacao(parecer):
    """
    ETAPA 3: Geração de Recomendações
    - Recebe parecer detalhado da transação
    - Gera recomendações técnicas para ação
    - Retorna orientações para equipe de segurança
    """
    print("3. Gerando recomendações")

    # Prompt para gerar recomendações técnicas baseadas no parecer
    prompt_sistema = f"""
    Para a seguinte transação, forneça uma recomendação apropriada baseada no status e nos detalhes da transação: {parecer}

    As recomendações podem ser "Notificar Cliente", "Acionar setor Anti-Fraude" ou "Realizar Verificação Manual".
    Elas devem ser escritas no formato técnico.

    Inclua também uma classificação do tipo de fraude, se aplicável.
    """

    lista_mensagens = [
        { "role": "user", "content": prompt_sistema }
    ]

    # Chama API para gerar recomendações técnicas
    resposta = cliente.chat.completions.create(
        messages = lista_mensagens,
        model = MODELO
    )

    conteudo = resposta.choices[0].message.content
    print("Finalizou a geração de recomendação")
    return conteudo


# =============================================================================
# FLUXO PRINCIPAL: CSV → OpenAI → JSON → Processamento → TXT
# =============================================================================

# ETAPA 1: Carrega dados CSV de entrada
lista_de_transacoes = carrega("./dados/transacoes.csv")

# ETAPA 2: Envia CSV para OpenAI e recebe JSON estruturado com análise de fraude
transacoes_analisadas = analisar_transacao(lista_de_transacoes)

# ETAPA 3: Processa cada transação do JSON retornado
for uma_transacao in transacoes_analisadas["transacoes"]:
    # Só processa transações marcadas como suspeitas
    if uma_transacao["status"] == "Possível Fraude":
        # ETAPA 4: Gera parecer detalhado da transação suspeita
        um_parecer = gerar_parecer(uma_transacao) 
        # print("Parecer: ", um_parecer)
        
        # ETAPA 5: Gera recomendações técnicas baseadas no parecer
        recomendacao = gerar_recomendacao(um_parecer)
        
        # ETAPA 6: Salva resultado final em arquivo TXT
        id_transacao = uma_transacao["id"]
        produto_transacao = uma_transacao["nome_produto"]
        status_transacao = uma_transacao["status"]
        salva(f"./dados/transacao-{id_transacao}-{produto_transacao}-{status_transacao}.txt", recomendacao)

# dump converte o objeto JSON para uma string, indent=4 é para indentar o JSON
# salva("./dados/transacoes-analise.json", json.dumps(transacoes, indent=4))
