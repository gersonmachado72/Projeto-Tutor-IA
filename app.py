# ==========================================
# PROJETO 1: Assistente de Estudos Personalizado
# Foco: Prompt Engineering e Interface Web
# ==========================================

import streamlit as st
import google.generativeai as genai
import os

# 1. Configuração da API do Gemini
# Tentamos pegar a chave da variável de ambiente que configuramos no terminal
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    st.error("Chave da API não encontrada. Configure a variável GEMINI_API_KEY no terminal.")
    st.stop()

genai.configure(api_key=API_KEY)

# 2. Configuração da Interface com Streamlit
st.set_page_config(page_title="Tutor IA", page_icon="📚")
st.title("📚 Seu Tutor Particular com IA")
st.markdown("Aprenda qualquer assunto no seu próprio ritmo!")

# 3. Entradas do Usuário
tema = st.text_input("Qual assunto você quer estudar hoje?", placeholder="Ex: Revolução Francesa, Fotossíntese, Frações...")
nivel = st.selectbox("Qual o seu nível de escolaridade?", ["Ensino Fundamental", "Ensino Médio", "Ensino Superior", "Curioso/Geral"])
formato = st.radio("O que você deseja gerar?", ["Resumo Explicativo", "Questões de Múltipla Escolha", "Analogia Simples"])

# 4. Ação principal ao clicar no botão
if st.button("Gerar Material de Estudo"):
    if tema:
        with st.spinner("O Tutor está preparando o material..."):
            try:
                # Escolhendo o modelo (gemini-2.5-flash é ótimo e rápido)
                model = genai.GenerativeModel("gemini-2.5-flash")
                
                # AQUI ENTRA O PROMPT ENGINEERING (Engenharia de Prompt)
                # Damos um papel (persona), contexto e formato de saída para a IA
                prompt_sistema = f"""
                Você é um professor particular extremamente didático e paciente.
                O aluno está no nível: {nivel}.
                O tema da aula de hoje é: '{tema}'.
                
                Instruções específicas baseadas na escolha do aluno:
                """
                
                if formato == "Resumo Explicativo":
                    prompt_sistema += "Crie um resumo detalhado, mas fácil de entender. Use tópicos. Ao final, faça 2 perguntas reflexivas para verificar se o aluno entendeu."
                elif formato == "Questões de Múltipla Escolha":
                    prompt_sistema += "Crie 3 questões de múltipla escolha sobre o tema, com 4 alternativas (A, B, C, D). Forneça o gabarito comentado apenas no final do texto."
                else:
                    prompt_sistema += "Explique o conceito usando uma analogia criativa do dia a dia. Por exemplo, se for sobre células, compare com uma fábrica. Seja criativo!"
                
                # Chamando a API
                resposta = model.generate_content(prompt_sistema)
                
                # Exibindo o resultado na interface
                st.success("Pronto! Aqui está o seu material:")
                st.markdown(resposta.text)
                
            except Exception as e:
                st.error(f"Ocorreu um erro ao comunicar com a IA: {e}")
    else:
        st.warning("Por favor, digite um assunto para começarmos.")