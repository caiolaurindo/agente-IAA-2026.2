
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(override=True)

st.set_page_config(
    page_title="Agente de IA",
)

st.title("Agente de IA")
st.caption("Um assistente inteligente que mantém o contexto da conversa.")

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL")

client = genai.Client(api_key=api_key) if api_key else None

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Olá! Sou seu agente de IA. Pode me fazer uma pergunta!",
        }
    ]

if st.sidebar.button("Nova conversa"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Como posso ajudar?"}
    ]
    st.rerun()

st.sidebar.markdown("### Sobre o projeto")
st.sidebar.write(f"Modelo de linguagem: {model}")
st.sidebar.write("Interface: Streamlit")
st.sidebar.write("Linguagem: Python")
st.sidebar.write("Provedor: Google Gemini")

# Exibe o histórico da conversa
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Recebe uma nova pergunta
if prompt := st.chat_input("Digite sua pergunta..."):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    if not client:
        st.error(
            "Configure GEMINI_API_KEY no arquivo .env "
            "para utilizar o agente."
        )
        st.stop()

    with st.chat_message("assistant"):
        try:
            with st.spinner("Pensando..."):
                response = client.models.generate_content(
                    model=model,
                    contents=[
                        types.Content(
                            role=(
                                "model"
                                if msg["role"] == "assistant"
                                else "user"
                            ),
                            parts=[
                                types.Part.from_text(
                                    text=msg["content"]
                                )
                            ],
                        )
                        for msg in st.session_state.messages
                    ],
                    config=types.GenerateContentConfig(
                        system_instruction=(
                            "Você é um assistente de IA útil, "
                            "educado e didático. "
                            "Responda em português brasileiro."
                        )
                    ),
                )

                answer = (
                    response.text
                    or "Não consegui gerar uma resposta."
                )

            st.markdown(answer)

            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

        except Exception as error:
            st.error(
                "Não foi possível consultar o Gemini. "
                "Verifique a chave da API, o modelo e a conexão."
            )
            print(f"Erro na API: {error}")
