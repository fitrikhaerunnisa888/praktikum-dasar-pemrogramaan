def konversi_menit_ke_detik(menit):
    """Mengubah satuan waktu dari menit menjadi detik.
    Parameter:
        menit (int/float): jumlah menit yang akan dikonversi.
    Return:
        int/float: jumlah detik (1 menit = 60 detik).
    """
    detik = menit * 60
    return detik
print(konversi_menit_ke_detik(3))
print(konversi_menit_ke_detik.__doc__)