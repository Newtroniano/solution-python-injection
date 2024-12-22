import streamlit as st
import requests
from components.upload_component import upload_file
import pandas as pd
st.title("Upload de Arquivo para API")
BASE_URL ="http://localhost:5000/api"
uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=["xlsx"])



if uploaded_file is not None:
    if st.button("Fazer Upload"):
        try:
            response = requests.post(
                "http://localhost:5000/api/upload",
                files={"file": uploaded_file},
            )
            if response.status_code == 200:
                st.success("Arquivo enviado com sucesso!")
                st.json(response.json())
            else:
                st.error(f"Erro ao enviar arquivo: {response.text}")
        except Exception as e:
            st.error(f"Ocorreu um erro: {str(e)}")
    st.title("Painel de Upload")


st.markdown("---")
st.subheader("Visualizar Registros")

table_name_view = st.text_input("Nome da Tabela para Visualizar", placeholder="Ex.: jogos")

if st.button("Carregar Dados"):
    if table_name_view:
        try:
            response = requests.get(f"{BASE_URL}/{table_name_view}")
            print(f"{BASE_URL}/{table_name_view}")
           
            if response.status_code == 200:
                data = response.json()
                columns = data.get('prod', {}).get('columns', [])
                records = data.get('prod', {}).get('records', [])
                
                print(data.get('prod', {}).get('columns', []))
                if records:
                    df = pd.DataFrame(records, columns=columns)
                    st.write(f"Exibindo registros da tabela '{table_name_view}'")
                    st.dataframe(df) 
                else:
                    st.warning(f"Nenhum registro encontrado na tabela '{table_name_view}'.")
            else:
                st.error(f"Erro ao buscar registros: {response.json().get('error')}")
        except Exception as e:
            st.error(f"Ocorreu um erro: {str(e)}")
    else:
        st.warning("Por favor, insira o nome de uma tabela.")

# st.title("Painel de Upload")
# result = upload_file()
# if result:
#     st.write("Resultado do Backend:", result)