import streamlit as st
from datetime import datetime

def coletar_tipo_e_data_movimentacao():
    tipo_movimentacao = st.radio("Tipo de Movimentação", ["Entrada", "Saída"])
    data_movimentacao = st.date_input("Data da Movimentação", value=datetime.today(),format="DD/MM/YYYY")
    data_movimentacao=data_movimentacao.strftime("%Y/%m/%d")
    agora=datetime.now()
    horario_movimentacao=agora.time()
    return {"Data da Movimentação": data_movimentacao,"Horário da Movimentação": horario_movimentacao,"Tipo de Movimentação": tipo_movimentacao}

def coletar_produto_e_categoria(df_catalogo_produtos):
    col1, col2 = st.columns(2)
    with col1:
        nome_produto = st.selectbox("Produto", df_catalogo_produtos["Nome"])
        categoria=df_catalogo_produtos.loc[df_catalogo_produtos["Nome"]==nome_produto,"Categoria"].values[0]
    with col2:
        st.text_input("Categoria", value=categoria, disabled=True)
    return {"Categoria": categoria, "Nome": nome_produto,}

def coletar_quantidade_e_unidade(df_catalogo_produtos, nome_produto, tipo_movimentacao):
    unidade = df_catalogo_produtos.loc[df_catalogo_produtos["Nome"] == nome_produto, "Unidade"].values[0]

    if tipo_movimentacao == "Entrada":
        col1, col2 = st.columns(2)
        with col1:
            valor_unitario = st.number_input("Valor Unitário (R$)", min_value=0.0, format="%.2f")
        with col2:
            quantidade = st.number_input(f"Quantidade ({unidade})", min_value=0.0, format="%.3f")
    else:  
        valor_unitario = 0.0 
        quantidade = st.number_input(f"Quantidade ({unidade})", min_value=0.0, format="%.3f")
    return {"Valor Unitário":valor_unitario,"Quantidade": quantidade,"Unidade": unidade}

def coletar_motivo_e_fornecedor(tipo_movimentacao,df_catalogo_fornecedores):
    if tipo_movimentacao == "Entrada":
        texto_botao="Registrar Entrada"
        col1, col2 = st.columns(2)
        with col1:
            motivo_movimentacao = st.selectbox("Motivo", ["Transferência entre lojas", "Chegada de mercadoria"])
        with col2:
            fornecedor=st.selectbox("Fornecedor",df_catalogo_fornecedores["Fornecedor"])
    else:
        motivo_movimentacao = st.selectbox("Motivo", ["Consumo na casa", "Transferência entre lojas"])
        texto_botao="Registrar Saída"
        fornecedor=""
    return {"Motivo da Movimentação": motivo_movimentacao,"Fornecedor":fornecedor,"Texto Botão": texto_botao}

def coletar_responsavel():
    responsavel = st.selectbox("Responsável", ["Sérgio", "Célia", "Mayra", "Cauã", "Léo"])
    return {"Responsável": responsavel}

def criar_dicionario_dados(dados_movimentacao,dados_produto,dados_quantidade,dados_motivo,dados_responsavel):
    dados_completos={}
    dados_completos.update(dados_movimentacao)
    dados_completos.update(dados_produto)
    dados_completos.update(dados_quantidade)
    dados_completos.update(dados_motivo)
    dados_completos.update(dados_responsavel)
    botao=st.button(dados_motivo["Texto Botão"])
    return dados_completos,botao
