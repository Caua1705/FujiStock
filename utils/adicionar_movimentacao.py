import pandas as pd

def adicionar_movimentacao(dict_dados,df_movimentacoes):
     dict_dados_atualizado=dict_dados.copy()
     dict_dados_atualizado.pop("Texto Botão")
     nova_linha=pd.DataFrame([dict_dados_atualizado])
     return  pd.concat([nova_linha,df_movimentacoes],ignore_index=True)
     
def adicionar_historico_custos(dict_dados,df_historico_custos):
    nova_linha = pd.DataFrame([{
        "Data da Movimentação": dict_dados["Data da Movimentação"],
        "Horário da Movimentação": dict_dados["Horário da Movimentação"],
        "Categoria": dict_dados["Categoria"],
        "Nome": dict_dados["Nome"],
        "Unidade": dict_dados["Unidade"],
        "Quantidade": dict_dados["Quantidade"],
        "Valor Unitário": dict_dados["Valor Unitário"],
        "Fornecedor": dict_dados["Fornecedor"]
    }])
    return pd.concat([nova_linha, df_historico_custos], ignore_index=True)