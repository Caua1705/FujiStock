import streamlit as st

def criar_metricas(df_catalogo_produtos,df_estoque,produtos_estoque_baixo):
    col1,col2,col3,col4=st.columns(4)
    with col1:
        valor_total_estoque=df_estoque["Custo Total"].sum()
        st.metric("Valor Total do Estoque",f"R$ {valor_total_estoque:.2f}")
    with col2:
        st.metric("Produtos Cadastrados",f"{len(df_catalogo_produtos["Nome"]):03d}")
    with col3:
        st.metric("Produtos em Estoque",f"{len(df_estoque["Nome"]):03d}")
    with col4:
        st.metric("Produtos com Estoque Baixo",f"{len(produtos_estoque_baixo):03d}")
