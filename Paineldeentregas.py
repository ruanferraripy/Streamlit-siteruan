# Ler os dados
# Lista de categorias
# Construir o selecbox (categoria)
# Lista de tipos de veiculo
# Construir o selectbox (Tipo de veiculo)
# Filtrar os meus dados (Filtrado)
# Calcular metricas
# Exibir as metricas
# Agrupar os dados por Estado
# Exibir gráfico de barras
# Exibir tabela filtrado

import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Painel de Entregas', layout='wide')

st.title("Painel de Entregas")

# Ler os dados
Entregas = pd.read_excel("Entregas.xlsx")   

# Lista de categorias
categorias = ['Todos'] + list(Entregas['Categoria'].unique())
categora_selecionada = st.selectbox("Selecione a categoria", categorias)

# Lista de tipo de veiculo
tiposdeveiculos =  ['Todos'] + list(Entregas['Veiculo'].unique())
veiculo_selecionado = st.selectbox('Selecione o tipo de veículo', tiposdeveiculos)

# Calcular metricas
st.subheader("Total de Entregas")
st.text(f"{len(Entregas)}")

st.subheader("Soma do valor do frete")
soma_fretes = Entregas['Valor_Frete'].sum()
st.text(f'R$ {soma_fretes:,.2f}')

estado = Entregas.groupby('Estado_Entrega')['Cliente'].count().reset_index()
st.bar_chart(data=estado, x='Estado_Entrega', y='Cliente')

dados_filtrados = Entregas[(Entregas['Categoria'] == categora_selecionada) & (Entregas['Veiculo'] == veiculo_selecionado)]
st.dataframe(dados_filtrados)