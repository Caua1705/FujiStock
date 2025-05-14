import pandas as pd
import streamlit as st
from pathlib import Path
import plotly.express as px

st.set_page_config(page_title="Estoque Fuji", layout="wide")

# Cabeçalho do App
st.title("🍣 Estoque - Fuji")
st.subheader("Controle e Análise de Estoque")

# Leitura da planilha e suas respectivas abas
caminho_planilha = Path(__file__).parents[1] / "inventário_fuji - 12-05.xlsx"

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

df_estoque_total=pd.concat(dict_tipos_estoque.values())
df_estoque_total_por_categoria=df_estoque_total.groupby("Categoria")["Quantidade"].sum().reset_index()

#Gráfico de barras:
grafico_barrras=px.bar(df_estoque_total_por_categoria,x="Categoria",y="Quantidade")
grafico_barrras.update_layout(
    title="Estoque Total por Categoria",
    xaxis_title="Categoria",
    yaxis_title="Quantidade",
    title_x=0.5  # Centraliza o título
)
st.plotly_chart(grafico_barrras)


col1,col2=st.columns(2)
# Seletor de Tipo de Estoque
with col1:
    tipo_estoque = st.selectbox("📦 Tipo do Estoque", list(dict_tipos_estoque.keys()))
    df_selecionado = dict_tipos_estoque[tipo_estoque]

# Seletor de Categoria
with col2:
    categoria = st.selectbox("🗂️ Categoria", df_selecionado["Categoria"].unique())
    df_agrupado_por_categoria = df_selecionado.loc[df_selecionado["Categoria"] == categoria]


# Exibição dos Dados
st.markdown(f"### 📋 Estoque Atual - {tipo_estoque} - {categoria}")
st.write(df_agrupado_por_categoria)

# Total de Itens
total_itens = df_agrupado_por_categoria["Quantidade"].sum()
st.markdown(f"#### Total de Itens na Categoria **{categoria}**: {total_itens}")
