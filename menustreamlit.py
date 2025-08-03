import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(
    page_title="Portal de Conhecimento IA & ML",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para melhorar a aparência
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
        margin: 20px 0;
    }
    .resource-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #007bff;
        margin: 10px 0;
    }
    .highlight-text {
        background-color: #fff3cd;
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Menu lateral aprimorado
with st.sidebar:
    st.markdown("### 🎯 **Navegação Estratégica**")
    selected = option_menu(
        menu_title=None,
        options=["🏠 Início", "💼 Projetos", "📚 Cursos & Recursos", "🔗 Links Essenciais", "📞 Contato"],
        icons=["house-fill", "briefcase-fill", "book-fill", "link-45deg", "envelope-fill"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "#007bff", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "--hover-color": "#e3f2fd"},
            "nav-link-selected": {"background-color": "#007bff"},
        }
    )

# Conteúdo principal baseado na seleção
if selected == "🏠 Início":
    st.markdown('<h1 class="main-header">🧠 Portal de Excelência em IA & Machine Learning</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Projetos Ativos", "15+", "↗️ 3 novos")
    with col2:
        st.metric("Tecnologias", "Python, ML, AI", "🚀 Avançado")
    with col3:
        st.metric("Certificações", "Em andamento", "📈 Progresso")
    
    st.markdown("""
    ### 🎯 **Missão Crítica: Dominar o Futuro da Inteligência Artificial**
    
    Este espaço foi projetado para acelerar sua jornada em **Data Science, Machine Learning e AI**. 
    Cada seção contém recursos que podem transformar sua trajetória profissional.
    
    ⚡ **Por que isso importa AGORA?**
    - O mercado de IA cresce 40% ao ano
    - Profissionais qualificados ganham até 80% mais
    - Empresas buscam desesperadamente talentos especializados
    """)

elif selected == "💼 Projetos":
    st.markdown('<h2 class="section-header">💼 Portfólio de Projetos Estratégicos</h2>', unsafe_allow_html=True)
    
    # Projetos com links educacionais
    projects = [
        {
            "titulo": "🔍 Análise Preditiva de Mercado",
            "descricao": "Sistema de ML para prever tendências financeiras",
            "tech": "Python, Scikit-learn, Pandas",
            "links": [
                "https://scikit-learn.org/stable/tutorial/index.html",
                "https://pandas.pydata.org/docs/user_guide/index.html"
            ]
        },
        {
            "titulo": "🤖 Chatbot Inteligente com NLP",
            "descricao": "Assistente virtual usando processamento de linguagem natural",
            "tech": "NLTK, spaCy, Transformers",
            "links": [
                "https://huggingface.co/course/chapter1/1",
                "https://spacy.io/usage/spacy-101"
            ]
        },
        {
            "titulo": "📊 Dashboard Analytics Avançado",
            "descricao": "Visualização interativa de dados complexos",
            "tech": "Streamlit, Plotly, Dash",
            "links": [
                "https://docs.streamlit.io/",
                "https://plotly.com/python/"
            ]
        }
    ]
    
    for project in projects:
        with st.expander(f"**{project['titulo']}**"):
            st.write(f"**Descrição:** {project['descricao']}")
            st.write(f"**Tecnologias:** {project['tech']}")
            st.write("**📖 Recursos de Aprendizagem:**")
            for link in project['links']:
                st.markdown(f"- [{link}]({link})")

elif selected == "📚 Cursos & Recursos":
    st.markdown('<h2 class="section-header">📚 Arsenal de Conhecimento</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🐍 Python", "🤖 Machine Learning", "🧠 Deep Learning"])
    
    with tab1:
        st.markdown("""
        ### 🐍 **Python para Data Science - Recursos Críticos**
        
        #### 📖 **Cursos Fundamentais:**
        - [Python.org Official Tutorial](https://docs.python.org/3/tutorial/)
        - [Real Python](https://realpython.com/) - Tutoriais avançados
        - [Automate the Boring Stuff](https://automatetheboringstuff.com/)
        
        #### 🛠️ **Libraries Essenciais:**
        - [NumPy Documentation](https://numpy.org/doc/)
        - [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
        - [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
        """)
    
    with tab2:
        st.markdown("""
        ### 🤖 **Machine Learning - Dominando Algoritmos**
        
        #### 🎓 **Cursos Imperdíveis:**
        - [Coursera ML Course - Andrew Ng](https://www.coursera.org/learn/machine-learning)
        - [Fast.ai Practical Deep Learning](https://course.fast.ai/)
        - [Kaggle Learn](https://www.kaggle.com/learn) - Gratuito e prático
        
        #### 📊 **Datasets para Prática:**
        - [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)
        - [Google Dataset Search](https://datasetsearch.research.google.com/)
        - [AWS Open Data](https://registry.opendata.aws/)
        """)
    
    with tab3:
        st.markdown("""
        ### 🧠 **Deep Learning - O Futuro é Aqui**
        
        #### 🚀 **Frameworks Essenciais:**
        - [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
        - [PyTorch Tutorials](https://pytorch.org/tutorials/)
        - [Keras Documentation](https://keras.io/)
        
        #### 📚 **Livros Fundamentais:**
        - [Deep Learning Book - Ian Goodfellow](https://www.deeplearningbook.org/)
        - [Hands-On ML - Aurélien Géron](https://github.com/ageron/handson-ml2)
        """)

elif selected == "🔗 Links Essenciais":
    st.markdown('<h2 class="section-header">🔗 Rede de Recursos Estratégicos</h2>', unsafe_allow_html=True)
    
    # Organizando links por categoria
    categories = {
        "📊 **Plataformas de Dados**": [
            ("Kaggle", "https://www.kaggle.com/", "Competições e datasets"),
            ("Google Colab", "https://colab.research.google.com/", "Notebooks gratuitos na nuvem"),
            ("Jupyter", "https://jupyter.org/", "Ambiente de desenvolvimento interativo")
        ],
        "🧠 **IA e ML**": [
            ("Hugging Face", "https://huggingface.co/", "Modelos pré-treinados"),
            ("Papers With Code", "https://paperswithcode.com/", "Pesquisas e implementações"),
            ("OpenAI", "https://openai.com/", "APIs e documentação")
        ],
        "💻 **Desenvolvimento**": [
            ("GitHub", "https://github.com/Ralfsantosdev", "Repositórios e projetos"),
            ("Stack Overflow", "https://stackoverflow.com/", "Solução de problemas"),
            ("Python Package Index", "https://pypi.org/", "Bibliotecas Python")
        ],
        "📈 **Visualização**": [
            ("Plotly", "https://plotly.com/python/", "Gráficos interativos"),
            ("Seaborn", "https://seaborn.pydata.org/", "Visualização estatística"),
            ("Streamlit", "https://streamlit.io/", "Apps web para ML")
        ]
    }
    
    for category, links in categories.items():
        st.markdown(f"### {category}")
        cols = st.columns(len(links))
        for i, (name, url, desc) in enumerate(links):
            with cols[i]:
                st.markdown(f"""
                <div class="resource-card">
                    <h4><a href="{url}" target="_blank">{name}</a></h4>
                    <p>{desc}</p>
                </div>
                """, unsafe_allow_html=True)

elif selected == "📞 Contato":
    st.markdown('<h2 class="section-header">📞 Conecte-se Estrategicamente</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🎯 **Networking Profissional**
        
        **Especialização:** Python | Data Science | Machine Learning | AI
        
        **Formação:** Graduação em Inteligência Artificial (em andamento)
        
        **Expertise:**
        - 🐍 Desenvolvimento Python avançado
        - 📊 Análise de dados e visualização
        - 🤖 Implementação de algoritmos ML
        - ✍️ Copywriting técnico e estratégico
        """)
    
    with col2:
        st.markdown("""
        ### 📬 **Canais de Contato**
        
        📧 **Email:ralfsantos7878@gmail.com**
        💼 **LinkedIn**
        🐙 **GitHub: Ralfsantosdev**
        📱 **WhatsApp Business: 74 98109-3631**
        
        > *Pronto para colaborações que transformam dados em insights valiosos*
        """)
    
    st.markdown("---")
    st.markdown("""
    <div class="highlight-text">
    ⚡ <strong>Oportunidade Única:</strong> Conecte-se agora e acelere seus projetos de IA/ML com expertise comprovada
    </div>
    """, unsafe_allow_html=True)