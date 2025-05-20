import streamlit as st
from utils.coletar_dados import (coletar_tipo_e_data_movimentacao,coletar_produto_e_categoria,coletar_quantidade_e_unidade,
                                coletar_motivo_e_fornecedor,coletar_responsavel,criar_dicionario_dados)
from utils.adicionar_movimentacao import adicionar_movimentacao,adicionar_historico_custos
from utils.atualizar_estoque import atualizar_estoque
from utils.inicializador import inicializar_dados


st.title("Nova Movimentação")
#Inicializar Dados
caminho_movimentacoes,caminho_historico_custos,caminho_estoque=inicializar_dados()

#Coletar Dados
dados_movimentacao=coletar_tipo_e_data_movimentacao()
dados_produto=coletar_produto_e_categoria(st.session_state.catalogo_produtos)
dados_quantidade=coletar_quantidade_e_unidade(st.session_state.catalogo_produtos,dados_produto["Nome"],dados_movimentacao["Tipo de Movimentação"])
dados_motivo=coletar_motivo_e_fornecedor(dados_movimentacao["Tipo de Movimentação"],st.session_state.catalogo_fornecedores)
dados_responsavel=coletar_responsavel()
dict_dados,botao=criar_dicionario_dados(dados_movimentacao,dados_produto,dados_quantidade,dados_motivo,dados_responsavel)

if botao: 
    #Adiciona Movimentação
    st.session_state.movimentacoes=adicionar_movimentacao(dict_dados,st.session_state.movimentacoes)
    st.session_state.movimentacoes.to_excel(caminho_movimentacoes,index=False)
    #Adicionar Histórico de Custos
    if dict_dados["Tipo de Movimentação"]=="Entrada":
        st.session_state.historico_custos=adicionar_historico_custos(dict_dados,st.session_state.historico_custos)
        st.session_state.historico_custos.to_excel(caminho_historico_custos,index=False)
    #Atualiza Estoque
    st.session_state.estoque=st.session_state.estoque.fillna(0)
    st.session_state.estoque=atualizar_estoque(dict_dados,st.session_state.estoque)
    st.session_state.estoque.to_excel(caminho_estoque,index=False)
    #Confirma Movimentação
    st.success(f'{dict_dados["Tipo de Movimentação"]} do produto **{dict_dados["Nome"].strip()}** registrada com sucesso!')