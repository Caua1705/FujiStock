import streamlit as st 
import plotly.express as px

def grafico_valor_por_categoria(df_estoque_por_categoria):
    fig=px.bar(df_estoque_por_categoria,
               x="Categoria",
               y="Custo Total",
               title="Valor em Estoque por Categoria",
               orientation="h"
               )
    fig.update_layout(xaxis="Categoria",yaxis="Custo Total",showlegend=True)
    st.plotly_chart(fig,use_container_width=True)
    st.write(df_estoque_por_categoria)