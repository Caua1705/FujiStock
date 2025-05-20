def produtos_baixo_estoque(df_estoque):
    produtos_estoque_baixo=df_estoque.loc[
        ((df_estoque["Unidade"]=="UN") & (df_estoque["Quantidade"]<10)) |
        ((df_estoque["Unidade"]=="KG") & (df_estoque["Quantidade"]<1))]
    produtos_estoque_baixo=produtos_estoque_baixo.sort_values(by="Quantidade",ascending=True)
    return produtos_estoque_baixo