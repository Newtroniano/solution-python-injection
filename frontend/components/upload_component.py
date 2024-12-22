import streamlit as st
import requests

def upload_file():
    st.subheader("Faça o Upload do Arquivo Excel")
    uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=["xlsx"])

    if uploaded_file is not None:
        if st.button("Fazer Upload"):
            try:
                response = requests.post(
                    "http://127.0.0.1:5000/api/upload",
                    files={"file": uploaded_file},
                )
                if response.status_code == 200:
                    st.success("Arquivo enviado com sucesso!")
                    return response.json()
                else:
                    st.error(f"Erro ao enviar arquivo: {response.text}")
            except Exception as e:
                st.error(f"Ocorreu um erro: {str(e)}")
    return None
