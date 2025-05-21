import streamlit as st
import plotly.express as px

def grafico_valor_por_categoria(df_estoque_por_categoria):
    fig = px.bar(
        df_estoque_por_categoria,
        x="Custo Total",
        y="Categoria",
        orientation="h",
        color="Categoria",
        title="Análise do custo total armazenado por categoria",
        text="Custo Total"
    )

    fig.update_traces(
        texttemplate="R$ %{text:,.2f}",
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Custo Total (R$)",
        yaxis_title="Categoria",
        showlegend=False,
        height=400,
        yaxis=dict(
            tickfont=dict(size=14, family='Arial Black', color='black')
        )
    )

    st.plotly_chart(fig, use_container_width=True)
    st.write(df_estoque_por_categoria)