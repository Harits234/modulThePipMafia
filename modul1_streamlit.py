import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Modul 1: Edukasi Forex Bocil Pro",
    layout="centered",
    page_icon="📚"
)

st.markdown("""
<style>
h1, h2, h3 {
    color: #1F4E79;
}
.stApp {
    background-color: #F3F9FF;
}
.block {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 0px 10px #dbeafe;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("📚 Modul 1: Dasar-Dasar Forex Super Gampang")

st.write("Selamat datang di kelas forex untuk pemula banget! Kita belajar bareng yuk kayak bayi lagi belajar jalan. Materinya ringan tapi penting!")

# ---- Market Structure
with st.container():
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.header("🧩 Apa Itu Market Structure?")
    st.write("""
    Market Structure itu kayak bentuk jalan di market. Ada 3 jenis:
    
    - **Uptrend (Naik):** Harga bikin titik tertinggi baru (Higher High)
    - **Downtrend (Turun):** Harga makin rendah (Lower Low)
    - **Sideways (Datar):** Harga mondar-mandir doang
    
    **Cara lihatnya:**  
    Kalau harga bikin naik-turun yang naik terus ➜ itu naik.  
    Kalau turun-turun ➜ berarti tren turun.
    
    **Contoh gampang:**  
    Bayangin harga itu kayak orang nanjak gunung → dia terus bikin jejak lebih tinggi dari sebelumnya.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---- SNR
with st.container():
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.header("🏗️ Apa Itu SNR (Support & Resistance)?")
    st.write("""
    SNR itu kayak **lantai dan atap** buat harga.

    - **Support:** Tempat harga sering mantul naik ➜ kayak lantai
    - **Resistance:** Tempat harga sering mantul turun ➜ kayak atap

    **Cara pakai:**  
    Gambar garis di tempat harga sering mantul.  
    Kalau harga nyentuh support ➜ siap-siap Buy.  
    Kalau nyentuh resistance ➜ siap-siap Sell.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Order Block
with st.container():
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.header("🧱 Apa Itu Order Block?")
    st.write("""
    Order Block itu zona di mana **pemain besar (big player)** naruh banyak order.

    Biasanya muncul sebelum harga **naik/jatuh tajam**.

    **Cara cari Order Block:**  
    - Lihat candle besar naik/turun setelah candle kecil  
    - Tandai area candle kecil → itu zona OB

    **Strategi:**  
    Tunggu harga masuk ke OB ➜ baru ambil posisi Buy atau Sell.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---- FVG
with st.container():
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.header("🧯 Apa Itu FVG (Fair Value Gap)?")
    st.write("""
    FVG itu kayak **celah kosong antar candle** karena harga terlalu cepat gerak.

    Biasanya muncul antara 3 candle:
    - Candle 1 naik
    - Candle 2 lompat
    - Candle 3 lanjut naik → Nah, tengahnya kosong (gap)

    **Cara pakai:**  
    Cari gap yang belum "diisi" harga.  
    Biasanya harga bakal balik ke celah itu dulu ➜ baru lanjut gerak.

    Jadi FVG itu kayak lubang di jalan, dan harga sering balik buat nutup lubang itu dulu.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Closing
st.success("Selesai! Kamu udah paham dasar-dasarnya. Next kita bisa lanjut Modul 2 ya! 🚀")

