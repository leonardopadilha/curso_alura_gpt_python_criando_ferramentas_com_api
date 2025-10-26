# 🤖 GPT Python - Criando Ferramentas com API

Este projeto demonstra como criar ferramentas práticas utilizando a API da OpenAI (GPT) em Python. O repositório contém diversos exemplos de automação e análise de dados usando inteligência artificial.

## 📋 Índice

- [Funcionalidades](#-funcionalidades)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Como Usar](#-como-usar)
- [Exemplos de Uso](#-exemplos-de-uso)
- [Arquivos de Dados](#-arquivos-de-dados)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)

## 🚀 Funcionalidades

### 1. **Análise de Sentimentos de Produtos**
- Analisa avaliações de produtos e identifica sentimentos (Positivo, Negativo, Neutro)
- Extrai pontos fortes e fracos dos produtos
- Gera resumos automáticos das avaliações
- Processamento em lote para múltiplos produtos

### 2. **Detecção de Fraude em Transações**
- Analisa transações financeiras em CSV
- Identifica possíveis fraudes baseado em padrões suspeitos
- Gera pareceres detalhados para transações suspeitas
- Fornece recomendações técnicas para ação

### 3. **Categorização de Produtos**
- Categoriza produtos automaticamente
- Interface interativa para categorização em tempo real
- Suporte a categorias personalizadas

### 4. **Análise de Perfil de Clientes**
- Identifica perfis de compra de clientes
- Processa listas de compras em lote
- Seleção automática de modelo baseada no tamanho dos dados

### 5. **Contagem e Otimização de Tokens**
- Calcula custos de tokens para diferentes modelos
- Compara custos entre GPT-4 e GPT-3.5
- Otimização automática de seleção de modelo

## 📁 Estrutura do Projeto

```
gpt_python_criando_ferramentas_api/
├── 📄 main.py                          # Exemplo básico de uso da API
├── 📄 analisador_sentimentos.py        # Análise individual de sentimentos
├── 📄 analisador_sentimentos_lote.py   # Análise em lote de sentimentos
├── 📄 analisador_transacoes.py         # Detecção de fraude em transações
├── 📄 categorizador.py                 # Categorização de produtos
├── 📄 contador_tokens.py               # Contagem e custos de tokens
├── 📄 selecao_modelo.py                # Seleção automática de modelo
├── 📄 categorizador_old.py             # Versão anterior do categorizador
├── 📄 requirements.txt                 # Dependências do projeto
├── 📄 README.md                        # Documentação do projeto
└── 📁 dados/                           # Arquivos de dados de exemplo
    ├── 📄 avaliacoes-*.txt             # Avaliações de produtos
    ├── 📄 transacoes.csv               # Dados de transações financeiras
    └── 📄 lista_de_compras_100_clientes.csv
```

## ⚙️ Pré-requisitos

- Python 3.7 ou superior
- Conta na OpenAI com API key válida
- Acesso à internet para chamadas à API

## 🔧 Instalação

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd gpt_python_criando_ferramentas_api
```

2. **Instale as dependências:**

**Opção 1 - Via requirements.txt (recomendado):**
```bash
pip install -r requirements.txt
```

**Opção 2 - Instalação manual:**
```bash
pip install openai python-dotenv tiktoken
```

## 🔑 Configuração

1. **Crie um arquivo `.env` na raiz do projeto:**
```env
OPENAI_API_KEY=sua_chave_api_aqui
```

2. **Obtenha sua API key:**
   - Acesse [OpenAI Platform](https://platform.openai.com/)
   - Crie uma conta ou faça login
   - Gere uma nova API key em "API Keys"

## 🎯 Como Usar

### Análise de Sentimentos

**Análise Individual:**
```bash
python analisador_sentimentos.py
```

**Análise em Lote:**
```bash
python analisador_sentimentos_lote.py
```

### Detecção de Fraude

```bash
python analisador_transacoes.py
```

### Categorização de Produtos

```bash
python categorizador.py
```

### Análise de Perfil de Clientes

```bash
python selecao_modelo.py
```

### Contagem de Tokens

```bash
python contador_tokens.py
```

## 📊 Exemplos de Uso

### 1. Análise de Sentimentos

O sistema analisa avaliações de produtos e retorna:

```
Nome do Produto: Maquiagem mineral
Resumo das Avaliações: Produto bem avaliado por clientes que valorizam ingredientes naturais e acabamento natural.
Sentimento Geral: Positivo
Pontos fortes:
• Ingredientes naturais e saudáveis
• Acabamento natural e duradouro
• Não irrita peles sensíveis
Pontos fracos:
• Seleção de cores limitada
• Embalagem poderia ser mais prática
• Necessita de retoques ao longo do dia
```

### 2. Detecção de Fraude

O sistema analisa transações e identifica padrões suspeitos:

```json
{
    "transacoes": [
        {
            "id": "9c",
            "tipo": "Crédito",
            "estabelecimento": "Esporte C",
            "horario": "2023-11-21 21:53:28",
            "valor": "R$1103,00",
            "nome_produto": "Artigo Esportivo",
            "localizacao": "Porto Alegre - RS (Brasil)",
            "status": "Possível Fraude"
        }
    ]
}
```

### 3. Categorização de Produtos

```bash
Informe as categorias válidas, separando por vírgula: Eletrônicos, Roupas, Casa, Beleza
Digite o nome de um produto: Escova elétrica com recarga solar
Produto: Escova elétrica com recarga solar
Categoria: Eletrônicos
```

## 📁 Arquivos de Dados

### Avaliações de Produtos
- `avaliacoes-Maquiagem mineral.txt`
- `avaliacoes-Jeans feitos com materiais reciclados.txt`
- `avaliacoes-Camisetas de algodão orgânico.txt`

### Transações Financeiras
- `transacoes.csv` - Dados de transações com ID, tipo, estabelecimento, horário, valor, produto e localização

### Lista de Compras
- `lista_de_compras_100_clientes.csv` - Dados de compras de clientes para análise de perfil

## 🛠️ Tecnologias Utilizadas

- **Python 3.7+** - Linguagem principal
- **OpenAI API** - Integração com modelos GPT
- **tiktoken** - Contagem e otimização de tokens
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **JSON** - Processamento de dados estruturados
- **CSV** - Manipulação de dados tabulares

## 💡 Características Técnicas

- **Tratamento de Erros**: Implementação robusta de tratamento de exceções
- **Otimização de Custos**: Seleção automática de modelos baseada no tamanho dos dados
- **Processamento em Lote**: Suporte para análise de múltiplos itens
- **Formatação Estruturada**: Saídas padronizadas em JSON e texto
- **Configuração Flexível**: Uso de variáveis de ambiente para configuração

## 🔍 Modelos Suportados

- **GPT-4** - Análises complexas e precisas
- **GPT-4o-mini** - Análises rápidas e econômicas
- **GPT-3.5-turbo** - Análises balanceadas entre custo e qualidade

## 🔧 Troubleshooting

### Problemas Comuns

**Erro de Autenticação:**
```
openai.AuthenticationError: Incorrect API key provided
```
- Verifique se a API key está correta no arquivo `.env`
- Confirme se a chave tem permissões adequadas

**Para mais informações sobre códigos de erro:**
📖 [Documentação Oficial de Códigos de Erro da OpenAI](https://platform.openai.com/docs/guides/error-codes)

## 📈 Próximos Passos

- [ ] Implementar interface web
- [ ] Adicionar mais tipos de análise
- [ ] Integração com bancos de dados
- [ ] Sistema de cache para otimização
- [ ] Logs detalhados de execução

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature
3. Fazer commit das mudanças
4. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

**Desenvolvido com ❤️ usando Python e OpenAI API**
