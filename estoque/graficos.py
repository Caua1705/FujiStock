import streamlit as st 
import plotly.express as px

def grafico_valor_por_categoria(df_estoque_por_categoria):
    fig=px.pie(df_estoque_por_categoria,
               names="Categoria",
               values="Custo Total",
               title="Valor em Estoque por Categoria")
    fig.update_layout(xaxis_title="Categoria",
                      yaxis_title="Custo Total",
                      showlegend=True)
    st.plotly_chart(fig)
    st.write(df_estoque_por_categoria)

