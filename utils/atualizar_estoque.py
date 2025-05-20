import pandas as pd

def atualizar_estoque(dict_dados,df_estoque):
    if dict_dados["Nome"] in df_estoque["Nome"].values:
        if dict_dados["Tipo de Movimentação"]=="Entrada":
            df_estoque.loc[df_estoque["Nome"]==dict_dados["Nome"],"Quantidade"]+=dict_dados["Quantidade"]
            df_estoque.loc[df_estoque["Nome"]==dict_dados["Nome"],"Valor Unitário"]=dict_dados["Valor Unitário"]
        elif dict_dados["Tipo de Movimentação"]=="Saída":
            df_estoque.loc[df_estoque["Nome"]==dict_dados["Nome"],"Quantidade"]-=dict_dados["Quantidade"]
        return df_estoque
    else:
        nova_linha = pd.DataFrame([{
        "Categoria": dict_dados["Categoria"],
        "Nome": dict_dados["Nome"],
        "Unidade": dict_dados["Unidade"],
        "Quantidade": dict_dados["Quantidade"],
        "Valor Unitário": dict_dados["Valor Unitário"],}])

        return pd.concat([nova_linha, df_estoque], ignore_index=True)
