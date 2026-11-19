import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
from datetime import date

st.title("Pertemuan 10: Interaksi Streamlit dan Yahoo Finance")

kamus_ticker = {
    'GOOGL': 'Google',
    'AAPL': 'Apple Inc',
    'SBUX': 'Starbucks',
    'MCD': "McDonald's Corp",
    'META': "Meta Platforms Inc",
    'TLKM.JK': "Telkom Indonesia (Persero) Tbk PT",
    'BBNI.JK': 'Bank Negara Indonesia (Persero) Tbk PT',
    'BMRI.JK': 'Bank Mandiri (Persero) Tbk PT',
    'BBRI.JK': 'Bank Rakyat Indonesia (Persero) Tbk PT',
    'NESN': 'Nestle SA'
}

ticker_symbol = st.selectbox(
    'Silahkan pilih kode perusahaan:',
    sorted( kamus_ticker.keys())
)

st.write(kamus_ticker[ticker_symbol])

ticker_data = yf.Ticker(ticker_symbol)
#pilihan_periode = st. selectboc(
# 'Pilih periode:',
#['1D', '5D', '1MO', '3MO', '6MO', '1Y', '2Y']
#)
tgl_mulai = st.date_input(
    'Mulai tanggal',
    value=date.today()
)
tgl_akhir = st.date_input(
    'Sampai tanggal',
    value=date.today()
)
st.write(f'Tanggal mulai: {tgl_mulai}')
st.write(f'Tanggal akhir: {tgl_akhir}')

df_ticker = ticker_data.history(
    start=str(tgl_mulai),
    end=str(tgl_akhir)
)

pilihan_tampil_tabel = st.checkbox('Tampilkan tabel')

if pilihan_tampil_tabel == True:
    st.write("## Lima Data Awal")
    st.write( df_sticker.head() )

st.write(f"## Visualisassi Pergerakan Saham {kamus_ticker[ticker_symbol]}")

pilihan_atribut = st.multiselect(
    'Silahkan pilih atribut yang akan ditampilkan:',
    ['Low', 'High', 'Open', 'Close', 'Volume']
)
#st.write(pilihan_atribut)
grafik = px.line(
    df_ticker,
    y=pilihan_atribut,
    title=f"Harga Saham {kamus_ticker[ticker_symbol]}"
)
st.plotly_chart( grafik)

st.write()

