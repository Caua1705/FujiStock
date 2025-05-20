import streamlit as st 
import plotly.express as px

def grafico_valor_por_categoria(df_estoque_por_categoria):
    fig=px.bar(df_estoque_por_categoria,x="Categoria",y="Custo Total",title="Valor em Estoque por Categoria")
    st.plotly_chart(fig)
    st.write(df_estoque_por_categoria)