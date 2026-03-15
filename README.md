📚 Tutor Particular IA (Gemini 2.0)Este projeto é um assistente de estudos personalizado que utiliza a API do Google Gemini para gerar materiais didáticos (resumos, questões e analogias) com base no nível de escolaridade do usuário.🚀 Tecnologias UtilizadasPython 3.12+Streamlit: Interface web rápida e intuitiva.Google GenAI SDK: Integração com o modelo Gemini 2.0 Flash.Python-dotenv: Gerenciamento de variáveis de ambiente.🛠️ Como Executar Localmente1. Clonar o Repositóriogit clone [https://github.com/seu-usuario/projeto-tutor-ia.git](https://github.com/seu-usuario/projeto-tutor-ia.git)
cd projeto-tutor-ia
2. Configurar Ambiente Virtualpython3 -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
.\venv\Scripts\activate   # Windows
3. Instalar Dependênciaspip install google-genai streamlit
4. Configurar Chave de APICrie uma variável de ambiente no seu terminal:export GEMINI_API_KEY="SUA_CHAVE_AQUI"
5. Iniciar a Aplicaçãostreamlit run app.py
📝 FuncionalidadesResumos Didáticos: Explicações estruturadas sobre qualquer tema.Simulados: Geração de questões de múltipla escolha com gabarito.Analogias: Explicações complexas simplificadas por meio de comparações criativas.Desenvolvido para fins educacionais utilizando Engenharia de Prompt.