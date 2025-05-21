import streamlit as st
from utils.inicializador import inicializar_dados
from estoque.metricas import criar_metricas
from estoque.agrupar_dados import produtos_baixo_estoque,custo_total_por_categoria
from estoque.graficos import grafico_valor_por_categoria

st.set_page_config(layout="wide")
inicializar_dados()
st.title("Visão Geral do Estoque")
produtos_estoque_baixo=produtos_baixo_estoque(st.session_state.estoque)
df_estoque_por_categoria=custo_total_por_categoria(st.session_state.estoque)
criar_metricas(st.session_state.catalogo_produtos,st.session_state.estoque,produtos_estoque_baixo)
st.divider()
col1,col2=st.columns(2)
st.write(st.session_state.estoque)
with col1:
    st.subheader("Valor em Estoque por Categoria")
    grafico_valor_por_categoria(df_estoque_por_categoria)
