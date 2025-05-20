import streamlit as st

def criar_metricas(df_catalogo_produtos,df_estoque,produtos_estoque_baixo):
    col1,col2,col3,col4=st.columns(4)
    with col1:
        valor_estoque=(df_estoque["Quantidade"] * df_estoque["Valor Unitário"]).sum()
        st.metric("Valor Total do Estoque",f"R$ {valor_estoque:.2f}")
    with col2:
        st.metric("Produtos Cadastrados",len(df_catalogo_produtos["Nome"]))
    with col3:
        st.metric("Produtos em Estoque",len(df_estoque["Nome"]))
    with col4:
        st.metric("Produtos com Estoque Baixo",len(produtos_estoque_baixo))
