import streamlit as st
from datetime import datetime 
import pandas as pd

def coletar_dados_movimentacao(df_catalogo):
    st.subheader("Adicionar Movimentação")
    
    tipo_movimentacao = st.radio("Tipo de Movimentação", ["Entrada", "Saída"])
    data_movimentacao = st.date_input("Data da Movimentação", value=datetime.today(),format="YYYY/MM/DD")
    
    col1, col2 = st.columns(2)
    with col1:
        nome_produto = st.selectbox("Produto", df_catalogo["Nome"])
        categoria=df_catalogo.loc[df_catalogo["Nome"]==nome_produto,"Categoria"].values[0]
    with col2:
        st.text_input("Categoria", value=categoria, disabled=True)

    col1, col2 = st.columns(2)
    with col1:
        custo_unitario = st.number_input("Valor Unitário(R$)", min_value=0.0)
    with col2:
        unidade = df_catalogo.loc[df_catalogo["Nome"] == nome_produto, "Unidade"].values[0]
        quantidade = st.number_input(f"Quantidade ({unidade})", min_value=0.0)
     

    col1, col2 = st.columns(2)
    with col1:
        if tipo_movimentacao == "Entrada":
            motivo_movimentacao = st.selectbox("Motivo", ["Transferência entre lojas", "Chegada de mercadoria"])
            texto_botao="Registrar Entrada"
        else:
            motivo_movimentacao = st.selectbox("Motivo", ["Consumo na casa", "Transferência entre lojas"])
            texto_botao="Registrar Saída"
    with col2:
        fornecedor=st.selectbox("Fornecedor",["Fornecedor X","Fornecedor Y"])

    responsavel = st.selectbox("Responsável", ["Sérgio", "Célia", "Mayra", "Cauã", "Léo"])

    botao=st.button(texto_botao)

    dict_dados={
        "Data da Movimentação": data_movimentacao,
        "Tipo de Movimentação": tipo_movimentacao,
        "Categoria": categoria,
        "Nome": nome_produto,
        "Quantidade": quantidade,
        "Unidade": unidade,
        "Motivo da Movimentação": motivo_movimentacao,
        "Responsável": responsavel,
    }
    return dict_dados,botao

def adicionar_movimentacao(dict_dados,df_movimentacoes):
     nova_linha=pd.DataFrame([dict_dados])
     return  pd.concat([nova_linha,df_movimentacoes])

def atualizar_estoque(dict_dados,df_estoque):
    if dict_dados["Nome"] in df_estoque["Nome"].values:
        if dict_dados["Tipo de Movimentação"]=="Entrada":
            df_estoque.loc[df_estoque["Nome"]==dict_dados["Nome"],"Quantidade"]+=dict_dados["Quantidade"]
        elif dict_dados["Tipo de Movimentação"]=="Saída":
            df_estoque.loc[df_estoque["Nome"]==dict_dados["Nome"],"Quantidade"]-=dict_dados["Quantidade"]
    else:
        nova_linha=pd.DataFrame([{"Categoria":dict_dados["Categoria"],
                                "Nome":dict_dados["Nome"],
                                "Unidade":dict_dados["Unidade"],
                                "Quantidade":dict_dados["Quantidade"]}])
        df_estoque=pd.concat([df_estoque,nova_linha],ignore_index=True)
    return df_estoque
    