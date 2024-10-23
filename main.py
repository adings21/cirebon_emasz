import streamlit as st
import pandas as pd
from io import BytesIO
import io

from GenerateTemplateCirebonPayment import mainPayment
from GenerateTemplateCirebonPembelian import mainPembelian
from GenerateTemplateCirebonPenjualan import mainPenjualan
from cleansingCirebon import mainCirebonCleansing

def main():
    st.title("Aplikasi Migrasi Cirebon")

    # Sidebar dengan menu pilihan
    st.sidebar.title('Menu')
    menu = st.sidebar.selectbox('Pilih Menu', ["Generate Template Penjualan", "Generate Template Pembelian", "Generate Template Payment","Cleansing"])

    # Pilihan menu
    if menu == "Generate Template Penjualan":
        mainPenjualan()
    elif menu == "Generate Template Pembelian":
        mainPembelian()
    elif menu == "Generate Template Payment":
        mainPayment()
    elif menu == "Cleansing":
        mainCirebonCleansing()

# Memanggil fungsi utama
if __name__ == "__main__":
    main()
