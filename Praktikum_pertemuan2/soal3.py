harga_satuan = float(input("Masukkan harga satuan: "))
jumlah = int(input("Masukkan jumlah barang: "))
persen_diskon = float(input("Masukkan persentase diskon (%): "))
subtotal = harga_satuan * jumlah
nominal_diskon = subtotal * persen_diskon / 100
total_bayar = subtotal - nominal_diskon
print(f"Subtotal: Rp{subtotal:,.0f}")
print(f"Diskon ({persen_diskon:.0f}%): Rp{nominal_diskon:,.0f}")
print(f"Total Bayar: Rp{total_bayar:,.0f}")
