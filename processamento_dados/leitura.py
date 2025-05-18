import streamlit as st
import pandas as pd

def ler_planilhas(catalogo,estoque,movimentacoes,historico_custos):
    if "catalogo" not in st.session_state:
        st.session_state.catalogo=pd.read_excel(catalogo,date_format="YYYY/MM/DD")
    if "estoque" not in st.session_state:
        st.session_state.estoque=pd.read_excel(estoque,date_format="YYYY/MM/DD")
    if "movimentacoes" not in st.session_state:
        st.session_state.movimentacoes=pd.read_excel(movimentacoes,date_format="YYYY/MM/DD")
    if "historico_custo" not in st.session_state:
        st.session_state.movimentacoes=pd.read_excel(historico_custos,date_format="YYYY/MM/DD")
    return st.session_state.catalogo,st.session_state.estoque,st.session_state.movimentacoes,st.session_state.movimentacoes