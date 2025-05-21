import streamlit as st 
import plotly.express as px

def grafico_valor_por_categoria(df_estoque_por_categoria):
    fig=px.bar(df_estoque_por_categoria,
               x="Custo Total",
               y="Categoria",
               title="Valor em Estoque por Categoria",
               orientation="h"
               )
    fig.update_layout(xaxis_title="Custo Total",yaxis_title="Categoria",showlegend=True)
    st.plotly_chart(fig,use_container_width=True)
    st.write(df_estoque_por_categoria)