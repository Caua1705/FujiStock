import streamlit as st
def produtos_baixo_estoque(df_estoque):
    produtos_estoque_baixo=df_estoque.loc[
        ((df_estoque["Unidade"]=="UN") & (df_estoque["Quantidade"]<10)) |
        ((df_estoque["Unidade"]=="KG") & (df_estoque["Quantidade"]<1))]
    produtos_estoque_baixo=produtos_estoque_baixo.sort_values(by="Quantidade",ascending=True)
    return produtos_estoque_baixo

def custo_total_por_categoria(df_estoque):
    df_estoque["Custo Total"]=df_estoque["Quantidade"]*df_estoque["Valor Unitário"]
    df_estoque_por_categoria=df_estoque.groupby("Categoria")["Custo Total"].sum().reset_index().sort_values(by="Custo Total")
    df_estoque_por_categoria=df_estoque_por_categoria.head(4)
    st.write(df_estoque_por_categoria)
    return df_estoque_por_categoria