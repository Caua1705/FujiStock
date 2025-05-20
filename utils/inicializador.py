import streamlit as st
import pandas as pd
from pathlib import Path

def ler_planilhas(catalogo,estoque,movimentacoes,historico_custos):
    if "catalogo_produtos" not in st.session_state:
        st.session_state["catalogo_produtos"]=pd.read_excel(catalogo,date_format="YYYY/MM/DD",sheet_name="Produtos")
    if "catalogo_fornecedores" not in st.session_state:
        st.session_state["catalogo_fornecedores"]=pd.read_excel(catalogo,date_format="YYYY/MM/DD",sheet_name="Fornecedores")
    if "estoque" not in st.session_state:
        st.session_state["estoque"]=pd.read_excel(estoque,date_format="YYYY/MM/DD")
    if "movimentacoes" not in st.session_state:
        st.session_state["movimentacoes"]=pd.read_excel(movimentacoes,date_format="YYYY/MM/DD")
    if "historico_custos" not in st.session_state:
        st.session_state["historico_custos"]=pd.read_excel(historico_custos,date_format="YYYY/MM/DD")

def inicializar_dados():
    dir_raiz=Path(__file__).parents[1]
    caminho_catalogo = dir_raiz / "dados" / "catalogo.xlsx"
    caminho_estoque = dir_raiz / "dados" / "estoque_atual.xlsx"
    caminho_movimentacoes = dir_raiz / "dados" / "movimentação_estoque.xlsx"
    caminho_historico_custos = dir_raiz / "dados" / "historico_custos.xlsx"
    ler_planilhas(caminho_catalogo,caminho_estoque,caminho_movimentacoes,caminho_historico_custos)
    return caminho_movimentacoes,caminho_historico_custos,caminho_estoque