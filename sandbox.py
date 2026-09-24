import streamlit as st

st.title("Islamic Banking Sandbox")
st.subheader("Simulasi Kalkulator Bagi Hasil (Mudharabah)")

modal = st.number_input("Masukkan Jumlah Modal (Rp):", min_value=0, step=1000000)
estimasi_untung = st.number_input("Estimasi Keuntungan Proyek (Rp):", min_value=0, step=500000)

nisbah_nasabah = st.slider("Porsi Bagi Hasil Nasabah (%):", 0, 100, 60)
nisbah_bank = 100 - nisbah_nasabah

st.write(f"Porsi Bagi Hasil Bank: **{nisbah_bank}%**")

if st.button("Hitung Simulasi"):
    untung_nasabah = estimasi_untung * (nisbah_nasabah / 100)
    untung_bank = estimasi_untung * (nisbah_bank / 100)
    
    st.success(f"Keuntungan Nasabah: Rp {untung_nasabah:,.0f}")
    st.info(f"Keuntungan Bank: Rp {untung_bank:,.0f}")