import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Modul 1: Kelas Forex Premium",
    layout="centered",
    page_icon="💼"
)

# CSS untuk desain profesional kelas mahal
st.markdown("""
    <style>
    body {
        background-color: #0f1117;
        color: #ffffff;
    }
    .main {
        background-color: #0f1117;
    }
    .block {
        background-color: #1a1d2b;
        border-left: 5px solid #3b82f6;
        padding: 25px;
        margin-bottom: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 15px rgba(59, 130, 246, 0.3);
    }
    h1, h2, h3 {
        color: #60a5fa;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💼 Modul 1: Kelas Forex Profesional")

tabs = st.tabs(["Market Structure", "SNR", "Order Block", "FVG"])

# Tab 1: Market Structure
with tabs[0]:
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.header("📈 Market Structure")
    st.write("""
    Market Structure adalah **tulang punggung pergerakan harga**.

    🧠 Bayangin market kayak orang jalan:
    - Kalau dia naik gunung → **Uptrend**
    - Kalau dia turun lembah → **Downtrend**
    - Kalau dia mondar-mandir di lapangan → **Sideways**

    ### ✍️ Detailnya:
    - **Uptrend:** Harga bikin titik tertinggi baru (**Higher High**) dan titik rendah lebih tinggi (**Higher Low**)
    - **Downtrend:** Harga bikin titik terendah baru (**Lower Low**) dan puncak yang makin pendek (**Lower High**)
    - **Sideways:** Harga bolak-balik di satu range aja

    ⛳ **Kenapa penting?**  
    Kalau kamu bisa baca struktur ini, kamu tahu kapan harus buy, sell, atau sabar dulu.

    ✨ Pro Tip:  
    Jangan entry kalau market masih sideways & gak jelas arahnya.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 2: SNR
with tabs[1]:
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.header("🧱 Support & Resistance (SNR)")
    st.write("""
    Support dan Resistance itu kayak lantai dan atap harga.

    🪟 **Support** = Area bawah tempat harga sering mantul naik  
    🧱 **Resistance** = Area atas tempat harga sering mantul turun

    ### ✍️ Gimana cara nemuin SNR?
    - Lihat titik-titik di mana harga sering mantul 2-3 kali
    - Tarik garis horizontal → itu jadi area penting

    🔎 **Cara Entry:**
    - Dekat support → cari sinyal Buy
    - Dekat resistance → cari sinyal Sell

    ⚠️ Jangan asal entry cuma karena harga nyentuh garis, selalu tunggu konfirmasi.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 3: Order Block
with tabs[2]:
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.header("🏦 Order Block")
    st.write("""
    Order Block (OB) adalah zona di mana **institusi besar** masuk ke market.

    Biasanya muncul:
    - Sebelum harga naik/turun dengan keras
    - Setelah candle besar muncul tiba-tiba

    ### ✍️ Gimana cara nemuin OB?
    - Cari candle kecil/balance terakhir sebelum lonjakan besar
    - Tandai area open-close candle itu sebagai zona OB

    ✅ Harga sering balik dulu ke OB sebelum lanjut jalan, karena:
    - Market ngisi ulang order
    - Institusi masukin order besar di situ

    ✨ Pro Tip:  
    OB yang valid sering muncul bareng dengan struktur pasar (confluence).
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 4: FVG
with tabs[3]:
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.header("🔍 Fair Value Gap (FVG)")
    st.write("""
    FVG adalah **celah kosong antar candle** yang muncul karena harga gerak terlalu cepat.

    🎯 Biasanya terjadi:
    - Ketika ada candle impulsif yang lompat jauh
    - Ada gap antara harga penutupan sebelumnya dan pembukaan berikutnya

    ### ✍️ Cara pakai FVG:
    - Cari celah antara candle 1, 2, dan 3 (disebut 'imbalance')
    - Tandai zona itu, harga sering balik isi gap dulu sebelum lanjut

    💡 FVG sering jadi zona retracement alami market.

    ✨ Pro Tip:  
    Kalau FVG searah dengan OB dan struktur pasar → potensi entry super valid.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Penutup
st.success("📘 Kamu sudah menyelesaikan Modul 1! Siap lanjut ke strategi lanjutan di Modul 2.")
