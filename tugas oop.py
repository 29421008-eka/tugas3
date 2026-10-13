class Produk:
    def __init__(self, nama_produk, harga_produk, jumlah_beli):
        self.nama_produk = nama_produk
        self.harga_produk = harga_produk
        self.jumlah_beli = jumlah_beli

    # Method menampilkan informasi produk
    def tampilkan_produk(self):
        print("Nama Produk :", self.nama_produk)
        print("Harga Produk : Rp", self.harga_produk)
        print("Jumlah Beli :", self.jumlah_beli)

    # Method menghitung total pembelian produk
    def hitung_total(self):
        return self.harga_produk * self.jumlah_beli

    # Method menghitung diskon 5%
    def hitung_diskon(self, total_pembelian):
        if total_pembelian > 5000:
            return total_pembelian * 5 / 100
        else:
            return 0


print("=== SISTEM PEMBELIAN PRODUK ===")

jumlah_produk = int(input("Masukkan jumlah produk yang dibeli: "))

daftar_produk = []

# Perulangan memasukkan data produk
for i in range(jumlah_produk):
    print("\nProduk ke-", i + 1)

    nama = input("Nama produk : ")
    harga = int(input("Harga produk : Rp"))
    jumlah = int(input("Jumlah beli : "))

    produk = Produk(nama, harga, jumlah)
    daftar_produk.append(produk)

# Menampilkan informasi dan menghitung total setiap produk
print("\n=== INFORMASI PRODUK ===")

total_seluruh = 0

for produk in daftar_produk:
    produk.tampilkan_produk()

    total = produk.hitung_total()
    total_seluruh += total

    print("Total Pembelian : Rp", total)
    print()

# Menghitung diskon
produk_terakhir = daftar_produk[0]
diskon = produk_terakhir.hitung_diskon(total_seluruh)

total_bayar = total_seluruh - diskon

# Menampilkan hasil akhir
print("=== HASIL PEMBELIAN ===")
print("Total Pembelian : Rp", total_seluruh)
print("Diskon 5%       : Rp", diskon)
print("Total Bayar     : Rp", total_bayar)