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
# col1,col2=st.columns(2)
# with col1:
grafico_valor_por_categoria(df_estoque_por_categoria)
# with col2:
st.subheader("Distribuição do Valor em Estoque por Categoria")
colunas_necessarias=produtos_estoque_baixo[["Categoria","Nome","Unidade","Quantidade"]]
st.write(colunas_necessarias)
        # grafico_produtos_baixo_estoque(produtos_estoque_baixo)
        #Quantidade total por categoria
        #Valor total por categoria (custo acumulado)
    # st.warning(f"⚠️ Estoque baixo: **{nome}** com apenas **{qtd:.2f} {unidade}**")
        # st.write(df_estoque_por_categoria)
# with abas_estoque[1]:
#     pass
