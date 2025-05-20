import streamlit as st
from utils.inicializador import inicializar_dados
from estoque.metricas import criar_metricas
from estoque.agrupar_dados import produtos_baixo_estoque
from estoque.graficos import grafico_produtos_baixo_estoque

inicializar_dados()

abas_estoque = st.tabs(["📊 Visão Geral", "📦 Movimentações"])
with abas_estoque[0]:
    st.markdown("## 📊 Visão Geral do Estoque")
    st.markdown("Tenha um panorama rápido e detalhado do seu estoque atual.")
    produtos_estoque_baixo=produtos_baixo_estoque(st.session_state.estoque)
    criar_metricas(st.session_state.catalogo_produtos,st.session_state.estoque,produtos_estoque_baixo)
    col1,col2=st.columns(2)
    with col1:
        grafico_produtos_baixo_estoque(produtos_estoque_baixo)
with abas_estoque[1]:
    st.write(st.session_state.movimentacoes)

