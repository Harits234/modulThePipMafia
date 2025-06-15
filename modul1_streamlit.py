import streamlit as st

st.set_page_config(layout="wide", page_title="Modul 1: Belajar Forex Ala Dewa", page_icon="📘")

# Custom CSS for dark theme with blue highlights
st.markdown("""
    <style>
    body {
        background-color: #0D1117;
        color: #C9D1D9;
    }
    .stTabs [data-baseweb="tab-list"] {
        background-color: #161B22;
        color: #58A6FF;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 18px;
    }
    .stMarkdown, .stImage {
        background-color: #0D1117;
        padding: 1rem;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📘 Modul 1: Pengenalan Dasar Trading Forex")
st.markdown("Selamat datang di kelas profesional ala dewa! Di modul ini, kamu akan belajar fondasi paling penting dalam dunia trading dengan cara yang **sangat simpel, padat, dan visual**. Yuk mulai!")

# Tab layout
tabs = st.tabs(["📊 Market Structure", "📏 SNR (Support & Resistance)", "📦 Order Block", "📉 FVG (Fair Value Gap)"])

with tabs[0]:
    st.header("📊 Apa itu Market Structure?")
    st.markdown("""
    Market structure tuh kayak **peta jalan** di chart. Ini cara paling dasar buat baca arah pergerakan harga. Ada 3 bentuk utama:
    
    - **Uptrend (Bullish)**: Harga terus bikin _Higher High (HH)_ dan _Higher Low (HL)_.
    - **Downtrend (Bearish)**: Harga terus bikin _Lower High (LH)_ dan _Lower Low (LL)_.
    - **Sideways / Range**: Harga gerak naik-turun dalam range aja, gak jelas arahnya.
    
    Dengan paham struktur ini, kita bisa tau apakah harus fokus cari peluang **buy**, **sell**, atau **wait**.
    """)
    st.image("assets/market_structure.jpg", caption="Contoh Market Structure (Trend & Range)", use_column_width=True)

with tabs[1]:
    st.header("📏 Apa itu Support & Resistance?")
    st.markdown("""
    Ini dua level paling sakti di dunia trading.
    
    - **Support** = area lantai, tempat harga sering mantul ke atas.
    - **Resistance** = area atap, tempat harga sering terpental ke bawah.
    
    Cara makainya gampang: beli di support, jual di resistance. Tapi tetap harus lihat konfirmasi ya.
    """)
    st.image("assets/snr.jpg", caption="Contoh Support dan Resistance di Chart", use_column_width=True)

with tabs[2]:
    st.header("📦 Apa itu Order Block?")
    st.markdown("""
    Order Block adalah **zona bekas transaksi besar dari smart money (institusi)**. Biasanya muncul sebelum harga naik/turun tajam.
    
    Ada 2 jenis:
    - **Bullish Order Block**: Candle bearish sebelum rally naik
    - **Bearish Order Block**: Candle bullish sebelum harga drop
    
    Kita bisa entry saat harga balik ke zona ini.
    """)
    st.image("assets/order_block.png", caption="Contoh Bearish Order Block", use_column_width=True)

with tabs[3]:
    st.header("📉 Apa itu FVG (Fair Value Gap)?")
    st.markdown("""
    FVG adalah celah antara 3 candle berurutan yang tidak saling menyentuh. Artinya ada ketidakseimbangan harga.
    
    Contohnya:
    - Candle 1 naik
    - Candle 2 juga naik tapi gak nyentuh low candle sebelumnya
    - Candle 3 lanjut naik
    
    Nah, FVG biasanya bakal **diisi ulang dulu** sebelum lanjut ke arah sebelumnya. Cocok banget buat **entry pullback**.
    """)
    st.image("assets/fvg.png", caption="Contoh Fair Value Gap Bullish & Bearish", use_column_width=True)
