import pandas as pd
import streamlit as st
import datetime


def cadastrar():
    st.header("Fechamento Diário")

    op = ["LOJA IGUATEMI | BA" , "LOJA IGUATEMI || BA" , "LOJA CENTER LAPA BA" , "LOJA BELA VISTA BA" , "LOJA CENTER PIEDADE BA" ,"LOJOA BARRA BA" , "LOJA DIAS DAVILA BA " , "LOJA SALVADOR SHOPPING | BA" , "LOJA SALVADOR SHOPPING | BA" , "LOJA SSA NORTE SHOP BA ", "LOJA PARQUE BAHIA BA" , "LOJA SHOPPING PARALELA BA"]

    nome = st.selectbox("Operação",op)
            
    data = st.date_input("Data",value = datetime.date.today())

    st.subheader("Campo de preenchimento Movel")
        
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

    # Linha 2 - CAMPOS CONTROLE
    col5_controle, col6_controle, col7_controle , col8_controle = st.columns(4)

    with col5_controle:
        controle = st.number_input("CONTROLE RECEITA", help="QUANTIDADE DE ALTA CONTROLE (RECEITA)",step=1)

    with col6_controle:
        controle2 = st.number_input("CONTROLE FÍSICO", help="QUANTIDADE DE ALTA CONTROLE (FÍSICO)",step=1)

    with col7_controle:
        migra_controle = st.number_input("MIGRA PRÉ RECEITA", help="QUANTIDADE DE MIGRA CTRL PRÉ (RECEITA)",step=1)

    with col8_controle:
        migra_controle2 = st.number_input("MIGRA PRÉ FÍSICO", help="QUANTIDADE DE MIGRA CTRL PRÉ (FÍSICO)",step=1)

    fixal4 = st.number_input("B2B MOVEL(FÍSICO)",help="QUANTIDADE DE B2B MOVEL(FÍSICO)",step=1)

    receitaf = st.number_input("RECEITA FIXA(B2B)",help="QUANTIDADE DE RECEITA FIXA(B2B)",step=1)


    #Segundo campo de preenchimento 

    st.subheader("Campo de preenchimento Fixa")

    #PRIMEIRA LINHA

    col9_fixa, col10_fixa, col11_fixa , col12_fixa = st.columns(4)

    with col9_fixa:
        fixaet = st.number_input("RECEITA FIXA(EXT)", help= " QUANTIDADE DE RECEITA FIXA(VENDA EXT)",step=1 )

    with col10_fixa:
        fixaet2 = st.number_input("FÍSICO FIXA(EXT)", help= " QUANTIDADE DE FÍSICO FIXA(VENDA EXT)",step=1 )

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
        IPTV =  st.number_input("RECEITA IPTV",help="QUANTIDADE DE RECEITA IPVT",step=1)


    #TERCEIRO CAMPO DE PREEENCHIMENTO 

    st.subheader("Campo de preenchimento  Terminas")

    st.text("ACESSÓRIOS/APARELHOS")
    #PRIMEIRA LINHA 

    col17_tm,col18_tm , col19_tm , col20_tm = st.columns(4)

    with col17_tm: 
        aparelho1 = st.number_input("RECEITA APARELHOS" , help= "QUANTIDADE DE RECEITA APARELHOS",step=1) 

    with col18_tm:
        aparelho2 = st.number_input("FÍSICO APARELHOS" , help= "QUANTIDADE DE RECEITA APARELHOS",step=1) 

    with col19_tm:
        acessorios = st.number_input("RECEITA ACESSÓRIOS" , help= "QUANTIDADE DE RECEITA ACESSÓRIOS",step=1)

    with col20_tm:
        acessorios2 = st.number_input("FÍSICO ACESSÓRIOS" , help= "QUANTIDADE DE FÍSICO ACESSÓRIOS",step=1)

    #SEGUNDA LINHA

    col21_tm, col22_tm , col23_tm , col24_tm = st.columns(4)
        
    with col21_tm :
        attach = st.number_input("ATTACH" , help= "QUANTIDADE DE ATTACH",step=1)   

    with col22_tm:
        up = st.number_input("RECEITA UP > R$70" , help= "QUANTIDADE DE RECEITA UP > R$70",step=1)  

    with col23_tm:
        up2 = st.number_input("FÍSICO UP > R$70" , help= "QUANTIDADE DE FÍSICO UP > R$70",step=1)  

    #TECEIRA LINHA

    st.text("SEGUROS/SVAS")

    col25_tm, col26_tm , col27_tm , col28_tm = st.columns(4)

    with col25_tm:
        seguros = st.number_input("RECEITA SEGUROS" , help= "QUANTIDADE DE RECEITA SEGUROS",step=1)

    with col26_tm: 
        seguros2 = st.number_input("FÍSICO SEGUROS" , help= "QUANTIDADE DE FÍSICO SEGUROS",step=1)

    with col27_tm:
        sva = st.number_input("RECEITA SVA" , help= "QUANTIDADE DE FÍSICO SVA",step=1)

    with col28_tm:
        sva2 = st.number_input("FÍSICO SVA" , help= "QUANTIDADE DE RECEITA SVA",step=1)


    #QUARTA LINHA

    col29_tm, col30_tm , col31_tm , col32_tm = st.columns(4)

    with col29_tm :
        novosn = st.number_input("RECEITA NNEG" , help= "QUANTIDADE DE RECEITA NNEG",step=1)

    with col30_tm :
        novosn2 = st.number_input("FÍSICOS NNEG" , help= "QUANTIDADE DE FÍSICOS NNEG",step=1)

    senha = st.number_input("SENHAS GSS" , help= "QUANTIDADE DE SENHAS GSS",step=1)


    if st.button("Cadastrar"):
            
            st.session_state.planilha_fechamento = pd.DataFrame({
                "OPERAÇÃO": [nome],
                "DATA": [data],
                "ALTA PÓS PURO(RECEITA)": [alta],
                "ALTA PÓS PURO (FÍSICO)": [alta2],
                "MIGRA PRÉ/CTRL PURO(RECEITA)": [migra],
                "MIGRA PRÉ/CTRL PURO(FÍSICO)": [migra2],
                "ALTA CONTROLE (RECEITA)": [controle],
                "ALTA CONTROLE (FÍSICO)": [controle2],
                "MIGRA CTRL PRÉ (RECEITA)": [migra_controle],
                "MIGRA CTRL PRÉ (FÍSICO)": [migra_controle2],
                "RECEITA FIXA(VENDA EXT)": [fixaet],
                "RECEITA FÍSICO(VENDA EXT)": [fixaet2],
                "FÍSICO VIVO TOTAL(VENDA EXT)": [fixaet3],
                "B2B FÍXA(FÍSICO)": [fixaet4],
                "RECEITA FIXA(LOJA)": [fixal],
                "FÍSICO FIXA(LOJA)": [fixal2],
                "FÍSICO VIVO TOTAL(LOJA)": [fixal3],
                "RECEITA IPTV" : [IPTV] ,
                "B2B MOVEL(FÍSICO)": [fixal4],
                "RECEITA APARELHOS": [aparelho1],
                "FÍSICO APARELHOS": [aparelho2],
                "RECEITA ACESSÓRIOS": [acessorios],
                "FÍSICOS ACESSÓRIOS": [acessorios2],
                "ATTACH": [attach],
                "RECEITA UP > R$ 70": [up],
                "FÍSICO UP > R$ 70": [up2],
                "RECEITA SEGUROS": [seguros],
                "FÍSICOS SEGUROS": [seguros2],
                "FÍSICO SVA": [sva],
                "RECEITA SVA": [sva2],
                "RECEITA NNEG": [novosn],
                "FÍSICOS NNEG": [novosn2],
                "SENHAS GSS": [senha],
            })
                            
            st.session_state.nova_planilha = pd.read_excel(st.session_state.arquivo)
            st.session_state.novo = pd.concat([st.session_state.nova_planilha, st.session_state.planilha_fechamento], ignore_index=True)
            st.session_state.novo.to_excel(st.session_state.arquivo,index=False)
            st.success("Cadastro realizado com sucesso!")
            