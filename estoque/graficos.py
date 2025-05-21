import streamlit as st 
import plotly.express as px

def grafico_valor_por_categoria(df_estoque_por_categoria):
    fig=px.bar(df_estoque_por_categoria,
               x="Custo Total",
               y="Categoria",
               title="Valor em Estoque por Categoria",
               orientation="h",
               text="Custo Total",
               color="Categoria"
               )
    fig.update_traces(texttemplate="R$ %{x:,.2f}")
    fig.update_layout(
        xaxis_title="Custo Total (R$)",
        yaxis_title="Categoria",
        xaxis_tickformat=",.2f",
        yaxis=dict(tickmode="linear"),
        showlegend=False,
        margin=dict(l=100, r=40, t=80, b=40),
        height=400
    )
    st.plotly_chart(fig,use_container_width=True)
    st.write(df_estoque_por_categoria)