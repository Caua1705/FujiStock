import pandas as pd
import streamlit as st
from pathlib import Path
import plotly.express as px

# Leitura da planilha e suas respectivas abas
caminho_planilha = Path(__file__).parent / "inventário_fuji - 12-05.xlsx"

st.set_page_config(page_title="Estoque Fuji", layout="wide")

# Cabeçalho do App
st.title("🍣 Estoque - Fuji")
st.subheader("Controle e Análise de Estoque")

dict_tipos_estoque = {
    "Bebidas Estoque Seco": pd.read_excel(caminho_planilha, sheet_name="Bebidas Estoque Seco", index_col=0),
    "Bebidas Freezer 1": pd.read_excel(caminho_planilha, sheet_name="Bebidas Freezer 1", index_col=0),
    "Bebidas Freezer 2": pd.read_excel(caminho_planilha, sheet_name="Bebidas Freezer 2", index_col=0),
    "Freezer Stella 1": pd.read_excel(caminho_planilha, sheet_name="Freezer Stella 1", index_col=0),
    "Freezer Stella 2": pd.read_excel(caminho_planilha, sheet_name="Freezer Stella 2", index_col=0),
    "Freezer Horizontal 1": pd.read_excel(caminho_planilha, sheet_name="Freezer Horizontal 1", index_col=0),
    "Freezer Horizontal 2": pd.read_excel(caminho_planilha, sheet_name="Freezer Horizontal 2", index_col=0),
    "Freezer Horizontal 3": pd.read_excel(caminho_planilha, sheet_name="Freezer Horizontal 3", index_col=0),
    "Freezer Salão": pd.read_excel(caminho_planilha, sheet_name="Freezer Salão", index_col=0),
}

col1,col2=st.columns(2)
# Seletor de Tipo de Estoque
with col1:
    tipo_estoque = st.selectbox("📦 Tipo do Estoque", list(dict_tipos_estoque.keys()))
    df_selecionado = dict_tipos_estoque[tipo_estoque]

# Seletor de Categoria
with col2:
    categoria = st.selectbox("🗂️ Categoria", df_selecionado["Categoria"].unique())

#Gráfico de barras:
df_grafico=df_selecionado.loc[df_selecionado["Categoria"]==categoria]
grafico_barrras=px.bar(df_grafico,x="Nome",y="Quantidade",)
grafico_barrras.update_layout(
    title="Estoque Total por Categoria",
    xaxis_title="Nome",
    yaxis_title="Quantidade",
    title_x=0.5  # Centraliza o título
)
st.plotly_chart(grafico_barrras,use_container_width=True)

st.divider()

# Exibição dos Dados
st.markdown(f"### 📋 Estoque Atual - {tipo_estoque} - {categoria}")
st.write(df_grafico,use_container_width=True)

st.sidebar.markdown("### 🔍 Pesquisa de Produto")
produto_pesquisa = st.sidebar.text_input("Digite o nome do produto para buscar:", "")
if produto_pesquisa:
    # Busca nos dados gerais (sem filtrar por tipo de estoque ou categoria)
    all_data = pd.concat(dict_tipos_estoque.values())
    df_produto = all_data[all_data["Nome"].str.contains(produto_pesquisa, case=False, na=False)]
    
    if not df_produto.empty:
        # Exibe a quantidade e a tabela do produto
        st.sidebar.write(f"**Quantidade do produto '{produto_pesquisa}':** {df_produto['Quantidade'].sum()}")
    else:
        st.sidebar.warning(f"Produto '{produto_pesquisa}' não encontrado.")
