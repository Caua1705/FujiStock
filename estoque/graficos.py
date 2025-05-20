import streamlit as st
import plotly.express as px

def grafico_produtos_baixo_estoque(produtos_estoque_baixo):
    grafico_baixo_estoque=px.bar(produtos_estoque_baixo,x="Quantidade",y="Nome",title="Produtos com Baixo Estoque",orientation="h")
    st.plotly_chart(grafico_baixo_estoque)
    