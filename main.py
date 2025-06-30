import streamlit as st
import pandas as pd



st.header("Fechamento Diário")


arquivo = "dados.xlsx"

nome = st.text_input("LLPP/GERENTE DE ARÉA: ")

meta = st.text_input("Meta/Dia")

real = st.text_input("Real/Dia")




if st.button("Cadastrar"):
    if nome and meta and real:
            
            planilha = pd.DataFrame({"LLPP/GERENTE DE ARÉA:" : [nome], "Meta/Dia" : [meta]  , "Real:" : [real]})
            frame = pd.read_excel(arquivo)
            novo = pd.concat([frame, planilha], ignore_index=True)
            novo.to_excel(arquivo,index=False)
    else:
          st.error("Preencha todos os dados solicitados ")


    







st.dataframe(novo)