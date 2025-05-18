import streamlit as st
from pathlib import Path
from processamento_dados.leitura import ler_planilhas
from processamento_dados.adicionar import coletar_dados_movimentacao,adicionar_movimentacao,atualizar_estoque

st.set_page_config(page_title="Estoque Fuji", layout="wide")

st.title("🍣 Estoque - Fuji")

caminho_catalogo = Path(__file__).parent / "dados" / "catalogo_produtos.xlsx"
caminho_estoque = Path(__file__).parent / "dados" / "estoque_atual.xlsx"
caminho_movimentacoes = Path(__file__).parent / "dados" / "movimentação_estoque.xlsx"
caminho_historico_custos = Path(__file__).parent / "dados" / "historico_custos.xlsx"

abas = st.tabs(["Estoque Atual", "Histórico de Movimentações", "Nova Movimentação","Histórico de Custos"])

st.session_state.catalogo,st.session_state.estoque,st.session_state.movimentacoes,st.session_state.movimentacoes=ler_planilhas(caminho_catalogo,caminho_estoque,caminho_movimentacoes,caminho_historico_custos)

with abas[2]: 
    dict_dados,botao=coletar_dados_movimentacao(st.session_state.catalogo)
    if botao: 
        #Adiciona Movimentação
        st.session_state.movimentacoes=adicionar_movimentacao(dict_dados,st.session_state.movimentacoes)
        st.session_state.movimentacoes.to_excel(caminho_movimentacoes,index=False)
        #Atualiza Estoque
        st.session_state.estoque=st.session_state.estoque.fillna(0)
        st.session_state.estoque=atualizar_estoque(dict_dados,st.session_state.estoque)
        st.session_state.estoque.to_excel(caminho_estoque,index=False)
        st.success(f'{dict_dados["Tipo de Movimentação"]} do produto **{dict_dados["Nome"].strip()}** registrada com sucesso!')

with abas[0]:
    st.write(st.session_state.estoque)

with abas[1]:
    st.write(st.session_state.movimentacoes)
with abas[3]:
    pass
