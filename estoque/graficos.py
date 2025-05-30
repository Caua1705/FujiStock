import streamlit as st 
import plotly.express as px

def grafico_valor_por_categoria(df_estoque_por_categoria):
    fig=px.bar(df_estoque_por_categoria,
               x="Custo Total",
               y="Categoria",
               title="Análise do custo total armazenado por categoria",
               orientation="h",
               color="Categoria"
               )
    fig.update_layout(
        xaxis_title="Custo Total (R$)",
        yaxis_title="Categoria",
        yaxis=dict(tickfont=dict(size=14)),
        showlegend=False,
        height=400
    )
    st.plotly_chart(fig,use_container_width=True)
    st.write(df_estoque_por_categoria)