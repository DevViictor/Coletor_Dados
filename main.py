import streamlit as st
import pandas as pd
import datetime

st.session_state.setdefault("arquivo", "dados.xlsx")
try:
    st.session_state.setdefault("novo", pd.read_excel(st.session_state.arquivo))
except FileNotFoundError:
    st.session_state["novo"] = pd.DataFrame()

janela = st.sidebar.radio("Guia de Navegação",["Cadastro","Fechamento Diario(Planilha)"])

if janela == "Cadastro":

    st.header("Fechamento Diário")

    st.subheader("Preechimento Movel")

    op = ["SHOPPING IGUATEMI1" , "SHOPPING IGUATEMI2" , "SHOPPING LAPA" , "SHOPPING BELA VISTA" , "SHOPPING SALVADOR"]

    nome = st.selectbox("Operação",op)

    
    data = st.date_input("Data",value = datetime.date.today())



# Linha 1 - CAMPOS PÓS
col1_controle, col2_controle, col3_controle, col4_controle = st.columns(4)

with col1_controle:
    alta = st.text_input("ALTA PÓS RECEITA", help="ALTA PÓS PURO (RECEITA)")

with col2_controle:
    alta2 = st.text_input("ALTA PÓS FÍSICO", help="ALTA PÓS PURO (FÍSICO)")

with col3_controle:
    migra = st.text_input("MIGRA PRÉ RECEITA", help="MIGRA PRÉ/CTRL PURO (RECEITA)")

with col4_controle:
    migra2 = st.text_input("MIGRA PRÉ FÍSICO", help="MIGRA PRÉ/CTRL PURO (FÍSICO)")


# Linha 2 - PORTABILIDADES
st.text_input("Portabilidade", help="Quantidade de Portabilitade")


# Linha 3 - CAMPOS CONTROLE
col5_controle, col6_controle, col7_controle , col8_controle = st.columns(4)

with col5_controle:
    controle = st.text_input("CONTROLE RECEITA", help="ALTA CONTROLE (RECEITA)")

with col6_controle:
    controle2 = st.text_input("CONTROLE FÍSICO", help="ALTA CONTROLE (FÍSICO)")

with col7_controle:
    migra_controle = st.text_input("MIGRA CRL PRÉ RECEITA", help="MIGRA CTRL PRÉ (RECEITA)")

with col8_controle:
    migra_controle = st.text_input("MIGRA CRL PRÉ FÍSICO", help="MIGRA CTRL PRÉ (Físico)")


    
if st.button("Cadastrar"):
            
            if nome and data and alta and alta2:
                
                st.session_state.planilha_fechamento = pd.DataFrame({"OPERAÇÃO" : [nome]
                                                                    , "DATA" : [data]  ,
                                                                    "ALTA PÓS PURO(RECEITA) " : [alta],
                                                                    "ALTA PÓS PURO (FÍSICO) " : [alta2],
                                                                    "MIGRA PRÉ/CTRL PURO(RECEITA)" : [migra],
                                                                    "MIGRA PRÉ/CTRL PURO(FÍSICO)" : [migra2], 
                                                                    })
                st.session_state.nova_planilha = pd.read_excel(st.session_state.arquivo)
                st.session_state.novo = pd.concat([st.session_state.nova_planilha, st.session_state.planilha_fechamento], ignore_index=True)
                st.session_state.novo.to_excel(st.session_state.arquivo,index=False)
                st.success("Cadastro realizado com sucesso!")

            else:
                st.error("Preencha todos os dados solicitados! ")


        
elif janela == "Fechamento Diario(Planilha)":
     
     st.header("Fechameneto Diário")

     st.dataframe(st.session_state.novo)
