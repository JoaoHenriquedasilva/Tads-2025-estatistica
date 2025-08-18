import streamlit as st
from functions.plotly_ts import plot

st.title('Historico de cotação')

st.write('Veja o historico das transações')

ticker = st.sidebar.text_input('Escolha o ticker:',  value = 'AAPL'

)
fig = plot(ticker)
st.plotly_chart(fig)