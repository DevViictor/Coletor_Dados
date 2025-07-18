import streamlit as st
import pandas as pd
import datetime
from cadastro import cadastrar

st.session_state.setdefault("arquivo", "dados.xlsx")
try:
    st.session_state.setdefault("novo", pd.read_excel(st.session_state.arquivo))
except FileNotFoundError:
    st.session_state["novo"] = pd.DataFrame()

if "DATA" in st.session_state.novo.columns:
    st.session_state.novo["DATA"] = pd.to_datetime(st.session_state.novo["DATA"])


#FILTRO DE DADOS:

#DADOS DA PLANILHA SELECIONADO
acumulado = st.session_state["novo"]

altaposg = acumulado["ALTA PÓS PURO(RECEITA)"].sum()
altaposf = acumulado["ALTA PÓS PURO (FÍSICO)"].sum()

migraprér = acumulado["MIGRA PRÉ/CTRL PURO(RECEITA)"].sum()
migrapréf = acumulado["MIGRA PRÉ/CTRL PURO(FÍSICO)"].sum()

controler = acumulado["ALTA CONTROLE (RECEITA)"].sum()
controlef = acumulado["ALTA CONTROLE (FÍSICO)"].sum()

migracrlr = acumulado["MIGRA CTRL PRÉ (RECEITA)"].sum()
migracrlf = acumulado["MIGRA CTRL PRÉ (FÍSICO)"].sum()

fixar = acumulado["RECEITA FIXA(VENDA EXT)"].sum()
fixaf = acumulado["RECEITA FÍSICO(VENDA EXT)"].sum()

vivot = acumulado["FÍSICO VIVO TOTAL(VENDA EXT)"].sum()
vivotl= acumulado["FÍSICO VIVO TOTAL(LOJA)"].sum()

b2bf = acumulado["B2B FÍXA(FÍSICO)"].sum()
b2bm = acumulado["B2B MOVEL(FÍSICO)"].sum()

lojar = acumulado["RECEITA FIXA(LOJA)"].sum()
lojaf = acumulado["FÍSICO FIXA(LOJA)"].sum()

iptvr = acumulado["RECEITA IPTV"].sum()

apr = acumulado["RECEITA APARELHOS"].sum()
apf = acumulado["FÍSICO APARELHOS"].sum()

acr = acumulado["RECEITA ACESSÓRIOS"].sum()
acf = acumulado["FÍSICOS ACESSÓRIOS"].sum()

attch = acumulado["ATTACH"].sum()

upr = acumulado["RECEITA UP > R$ 70"].sum()
upf = acumulado["FÍSICO UP > R$ 70"].sum()

seguror = acumulado["RECEITA SEGUROS"].sum()
segurof =acumulado["FÍSICOS SEGUROS"].sum()

svaf = acumulado["FÍSICO SVA"].sum()
svar =acumulado["RECEITA SVA"].sum()

nngr = acumulado["RECEITA NNEG"].sum()
nngf = acumulado["FÍSICOS NNEG"].sum()

gss = acumulado["SENHAS GSS"].sum()

#DATAFRAME DOS DADOS FILTRADOS
acumulado_vivo = pd.DataFrame ({

    "Alta Pós Puro(Receita)":[altaposg],
    "ALTA PÓS PURO(FÍSICO)" :[altaposf],
    "MIGRA PRÉ/CTRL PURO(RECEITA)" :[migraprér],
    "MIGRA PRÉ/CTRL PURO(FÍSICO)" : [migrapréf],
    "ALTA CONTROLE (RECEITA)" : [controler] , 
    "ALTA CONTROLE (FÍSICO)" : [controlef] , 
    "MIGRA CTRL PRÉ (RECEITA)": [migracrlr],
    "MIGRA CTRL PRÉ (FÍSICO)": [migracrlf] ,
    "RECEITA FIXA(VENDA EXT)": [fixar],
    "RECEITA FÍSICO(VENDA EXT)": [fixaf],
    "FÍSICO VIVO TOTAL(VENDA EXT)": [vivot],
    "B2B FÍXA(FÍSICO)": [b2bf],
    "RECEITA FIXA(LOJA)": [lojar],
    "FÍSICO FIXA(LOJA)": [lojaf],
    "FÍSICO VIVO TOTAL(LOJA)": [vivotl],
    "RECEITA IPTV": [iptvr],
    "B2B MOVEL(FÍSICO)": [b2bm],
    "RECEITA APARELHOS": [apr],
    "FÍSICO APARELHOS": [apf],
    "RECEITA ACESSÓRIOS": [acr],
    "FÍSICOS ACESSÓRIOS": [acf],
    "ATTACH": [attch],
    "RECEITA UP > R$ 70": [upr],
    "FÍSICO UP > R$ 70": [upf],
    "RECEITA SEGUROS": [seguror],
    "FÍSICOS SEGUROS": [segurof],
    "FÍSICO SVA": [svaf],
    "RECEITA SVA": [svar],
    "RECEITA NNEG": [nngr],
    "FÍSICOS NNEG": [nngf],
    "SENHAS GSS": [gss],
})

#GRÁFICO DOS DADOS
grafico_geral = acumulado_vivo.melt(value_name="Total",var_name="Tipo")

st.sidebar.title("Menu")
janela = st.sidebar.radio("Escolha a página",["Cadastro","Resultado Diário"])

if janela == "Cadastro":
    cadastrar()

elif janela == "Resultado Diário":
                st.header("Fechameneto Diário")
                st.dataframe(st.session_state.novo)

            
                    

                
    
        

    
    

    

