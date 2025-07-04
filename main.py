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

    st.subheader("Campo de preenchimento Movel")

    op = ["SHOPPING IGUATEMI1" , "SHOPPING IGUATEMI2" , "SHOPPING LAPA" , "SHOPPING BELA VISTA" , "SHOPPING SALVADOR"]

    nome = st.selectbox("Operação",op)

    
    data = st.date_input("Data",value = datetime.date.today())

    # Linha 1 - CAMPOS PÓS
    col1_controle, col2_controle, col3_controle, col4_controle = st.columns(4)

    with col1_controle:
        alta = st.number_input("ALTA PÓS RECEITA", help="QUANTIDADE DE ALTA PÓS PURO (RECEITA)",step=1)

    with col2_controle:
        alta2 = st.number_input("ALTA PÓS FÍSICO", help="QUANTIDADE DE ALTA PÓS PURO (FÍSICO)",step=1)

    with col3_controle:
        migra = st.number_input("MIGRA PRÉ RECEITA", help="QUANTIDADE DE MIGRA PRÉ/CTRL PURO (RECEITA)",step=1)

    with col4_controle:
        migra2 = st.number_input("MIGRA PRÉ FÍSICO", help="QUANTIDADE DE MIGRA PRÉ/CTRL PURO (FÍSICO)",step=1)


    # Linha 2 - PORTABILIDADES
    portabilidade = st.number_input("Portabilidade", help="QUANTIDADE DE PORTABILIDADE",step=1)


    # Linha 3 - CAMPOS CONTROLE
    col5_controle, col6_controle, col7_controle , col8_controle = st.columns(4)

    with col5_controle:
        controle = st.number_input("CONTROLE RECEITA", help="QUANTIDADE DE ALTA CONTROLE (RECEITA)",step=1)

    with col6_controle:
        controle2 = st.number_input("CONTROLE FÍSICO", help="QUANTIDADE DE ALTA CONTROLE (FÍSICO)",step=1)

    with col7_controle:
        migra_controle = st.number_input("MIGRA PRÉ RECEITA", help="QUANTIDADE DE MIGRA CTRL PRÉ (RECEITA)",step=1)

    with col8_controle:
        migra_controle2 = st.number_input("MIGRA PRÉ FÍSICO", help="QUANTIDADE DE MIGRA CTRL PRÉ (FÍSICO)",step=1)

    #Segundo campo de preenchimento 

    st.subheader("Campo de preenchimento Fixa")

    #PRIMEIRA LINHA

    col9_fixa, col10_fixa, col11_fixa , col12_fixa = st.columns(4)

    with col9_fixa:
        fixaet = st.number_input("RECEITA FIXA(EXT)", help= " QUANTIDADE DE RECEITA FIXA(VENDA EXT)",step=1 )

    with col10_fixa:
        fixaet = st.number_input("FÍSICO FIXA(EXT)", help= " QUANTIDADE DE FÍSICO FIXA(VENDA EXT)",step=1 )

    with col11_fixa:
        fixaet3 = st.number_input("FÍSICO VIVO TOTAL(EXT)", help= " QUANTIDADE DE FÍSICO VIVO TOTAL FIXA(VENDA EXT)" ,step=1)

    with col12_fixa:
        fixaet4 = st.number_input("B2B FÍXA(FÍSICO)", help= " QUANTIDADE DE B2B FÍXA(FÍSICO)",step=1)

    #SEGUNDA LINHA

    col13_fixa, col14_fixa, col15_fixa , col16_fixa = st.columns(4)
        
    with col13_fixa:
        fixal = st.number_input("RECEITA FIXA(LOJA)",help="QUANTIDADE DE RECEITA FIXA(LOJA)",step=1)

    with col14_fixa:
        fixal2 = st.number_input("FÍSICO FIXA(LOJA)",help="QUANTIDADE DE FÍSICO FIXA(LOJA)",step=1)
    
    with col15_fixa:
        fixal3 = st.number_input("FÍSICO VIVO TOTAL(LOJA)",help="QUANTIDADE DE FÍSICO VIVO TOTAL(LOJA)",step=1)

    with col16_fixa:
        fixal4 = st.number_input("B2B MOVEL(FÍSICO)",help="QUANTIDADE DE B2B MOVEL(FÍSICO)",step=1)

    #TERCEIRO CAMPO DE PREEENCHIMENTO 

    

    if st.button("Cadastrar"):
            
            if nome and data and alta and alta2:
                
                st.session_state.planilha_fechamento = pd.DataFrame({"OPERAÇÃO" : [nome]
                                                                    , "DATA" : [data]  ,
                                                                    "ALTA PÓS PURO(RECEITA) " : [alta],
                                                                    "ALTA PÓS PURO (FÍSICO) " : [alta2],
                                                                    "MIGRA PRÉ/CTRL PURO(RECEITA)" : [migra],
                                                                    "MIGRA PRÉ/CTRL PURO(FÍSICO)" : [migra2], 
                                                                    "ALTA CONTROLE (RECEITA)" : [controle],
                                                                    "ALTA CONTROLE (FÍSICO)" : [controle2] , 
                                                                    "MIGRA CTRL PRÉ (RECEITA)" : [migra_controle] , 
                                                                    "MIGRA CTRL PRÉ (FÍSICO)" : [migra_controle2] , 
                                                                    "PORTABILIDADE" : [portabilidade]


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
