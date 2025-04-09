# 🛒 E-Shop Brasil – Gestão de Clientes

Projeto desenvolvido como aplicação prática para a disciplina de Banco de Dados / Big Data no curso de Gestão de Tecnologia da Informação.

## 📋 Descrição

Sistema de cadastro, consulta, atualização e exclusão de clientes usando:

- **MongoDB** como banco de dados NoSQL  
- **Streamlit** como interface web  
- **Docker** para empacotar e executar facilmente o projeto

---

## 🔧 Tecnologias utilizadas

- [Python 3.9+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [MongoDB](https://www.mongodb.com/)
- [Docker](https://www.docker.com/)

---

## 🚀 Funcionalidades

- ✅ Cadastrar clientes  
- ✅ Listar clientes cadastrados  
- ✅ Atualizar informações de clientes  
- ✅ Excluir clientes do banco

---

## 📁 Estrutura do projeto

e-shop-brasil/
├── app.py               # Aplicação principal Streamlit  
├── Dockerfile           # Dockerfile para containerizar o app  
├── requirements.txt     # Dependências do projeto  
├── .gitignore           # Arquivos ignorados pelo Git  
└── README.md            # Este arquivo

---

## 🐳 Como executar com Docker

1. Certifique-se de que o **MongoDB** está rodando (local ou via Docker):

docker run -d -p 27017:27017 --name mongodb mongo

2. Depois, construa e execute o app:

docker build -t e-shop-brasil-app .  
docker run -d -p 8501:8501 --name streamlit_app --link mongodb e-shop-brasil-app

3. Acesse a aplicação no navegador:  
http://localhost:8501

---

## 💻 Como executar localmente (sem Docker)

pip install -r requirements.txt  
streamlit run app.py

---

## 👨‍💻 Autor

Pedro Henrique da Silva Francisco  
https://github.com/pedro-h7
