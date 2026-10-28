# Agente de IA com Google Gemini e Streamlit

> **Disciplina:** 2026.2-NSIN-0104 — Inteligência Artificial Aplicada (Noite)  
> **Atividade:** Quiz 03  
> **Professor:** Leonardo Machado Cavalcanti  
> **Equipe:** Grupo 03

### 👥 Integrantes — Grupo 03
- **Adriano José Valença Gomes Filho**
- **Caio Lucas Laurindo da Silva**
- **Moisés Carlos de Araújo Neto**
- **Yasmin Marcelly Vasconcelos de Arruda**

---

Um assistente conversacional interativo desenvolvido em **Python** com interface **Streamlit** e integrado à API oficial do **Google Gemini** (`google-genai`). O agente mantém o histórico e o contexto da conversa durante a sessão, respondendo de forma didática em português brasileiro.

---

##  Funcionalidades

- **Chat interativo em tempo real** com interface web via Streamlit.
- **Memória de conversa (`st.session_state`)**: envia o histórico da sessão para o modelo manter o contexto entre as perguntas.
- **Instrução de sistema personalizada**: configurado para atuar como um assistente útil, educado e didático em português brasileiro.
- **Botão "Nova conversa"**: permite limpar o histórico e reiniciar o diálogo a qualquer momento pela barra lateral.

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — Interface web interativa
- [Google GenAI SDK (`google-genai`)](https://pypi.org/project/google-genai/) — Integração com os modelos Gemini
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Gerenciamento de variáveis de ambiente

---

## 📁 Estrutura do Projeto

```text
agenteIA/
├── app.py              # Aplicação principal Streamlit e integração com o Gemini
├── requirements.txt    # Dependências do projeto
├── .env.example        # Exemplo de configuração das variáveis de ambiente
├── .gitignore          # Arquivos e pastas ignorados pelo Git
└── README.md           # Documentação do projeto
```

---

## 🚀 Como Executar o Projeto Localmente

### 1. Pré-requisitos

- **Python 3.10 ou superior** instalado.
- Uma chave de API do Google Gemini (obtida no [Google AI Studio](https://aistudio.google.com/)).

### 2. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
cd NOME-DO-REPOSITORIO
```

### 3. Criar e ativar o ambiente virtual

**No Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**No Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar as variáveis de ambiente

Copie o arquivo `.env.example` para um novo arquivo chamado `.env`:

**No Windows (PowerShell):**
```powershell
Copy-Item .env.example .env
```

**No Linux / macOS:**
```bash
cp .env.example .env
```

Em seguida, abra o arquivo `.env` e preencha sua chave de API e o modelo desejado:

```env
GEMINI_API_KEY="sua_chave_de_api_aqui"
GEMINI_MODEL=gemini-3.6-flash
```

### 6. Iniciar a aplicação

```bash
streamlit run app.py
```

O navegador abrirá automaticamente em `http://localhost:8501`.

---

## 🧠 Como o Código Funciona (`app.py`)

1. **Carregamento de Configurações**: O `load_dotenv()` lê as variáveis `GEMINI_API_KEY` e `GEMINI_MODEL` definidas no arquivo `.env`.
2. **Inicialização do Cliente**: O cliente `genai.Client(api_key=api_key)` é instanciado caso a chave esteja configurada.
3. **Gerenciamento de Estado**: O histórico de mensagens fica armazenado em `st.session_state.messages`, garantindo que as mensagens anteriores permaneçam na tela a cada interação.
4. **Envio de Contexto ao Gemini**: Quando o usuário envia uma nova pergunta via `st.chat_input`, todas as mensagens da sessão são convertidas em objetos `types.Content` (com papéis `user` e `model`) e enviadas para `client.models.generate_content(...)` junto com um `system_instruction`.
5. **Exibição da Resposta**: A resposta retornada pelo Gemini é renderizada em Markdown na interface e adicionada ao histórico da sessão.

