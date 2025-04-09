
import streamlit as st
from pymongo import MongoClient

# Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["e_shop_brasil"]
collection = db["clientes"]

# Streamlit app
st.title("E-Shop Brasil - Gestão de Clientes")

menu = ["Cadastrar", "Consultar", "Atualizar", "Excluir"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Cadastrar":
    st.subheader("Cadastrar Novo Cliente")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    idade = st.number_input("Idade", min_value=0, step=1)
    if st.button("Salvar"):
        if nome and email:
            collection.insert_one({"nome": nome, "email": email, "idade": idade})
            st.success("Cliente cadastrado com sucesso!")
        else:
            st.warning("Preencha todos os campos.")

elif choice == "Consultar":
    st.subheader("Lista de Clientes")
    clientes = list(collection.find())
    if clientes:
        for c in clientes:
            st.write(f"**Nome:** {c['nome']} | **Email:** {c['email']} | **Idade:** {c['idade']}")
    else:
        st.info("Nenhum cliente encontrado.")

elif choice == "Atualizar":
    st.subheader("Atualizar Cliente")
    clientes = list(collection.find())
    nomes = [c["nome"] for c in clientes]
    nome_selecionado = st.selectbox("Selecione o cliente", nomes)
    cliente = next((c for c in clientes if c["nome"] == nome_selecionado), None)

    if cliente:
        novo_nome = st.text_input("Novo Nome", cliente["nome"])
        novo_email = st.text_input("Novo Email", cliente["email"])
        nova_idade = st.number_input("Nova Idade", min_value=0, value=cliente["idade"], step=1)
        if st.button("Atualizar"):
            collection.update_one({"_id": cliente["_id"]}, {"$set": {"nome": novo_nome, "email": novo_email, "idade": nova_idade}})
            st.success("Cliente atualizado com sucesso.")

elif choice == "Excluir":
    st.subheader("Excluir Cliente")
    clientes = list(collection.find())
    nomes = [c["nome"] for c in clientes]
    nome_selecionado = st.selectbox("Selecione o cliente para excluir", nomes)
    if st.button("Excluir"):
        collection.delete_one({"nome": nome_selecionado})
        st.success("Cliente excluído com sucesso.")
