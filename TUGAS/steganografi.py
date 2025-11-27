import cv2   # Mengimpor library OpenCV untuk memproses gambar

# ------------------------------------------------------------
# 1. Membaca gambar dari file
# ------------------------------------------------------------
img = cv2.imread("img-2.jpeg")   # Membaca gambar bernama input.jpg
if img is None:                  # Mengecek apakah gambar berhasil dibaca
    raise Exception("Gambar tidak ditemukan!")  # Jika gagal, tampilkan error

# ------------------------------------------------------------
# 2. Mengubah gambar dari format BGR ke HSV
#    HSV memudahkan dalam mengatur warna (S = Saturation)
# ------------------------------------------------------------
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Konversi BGR → HSV

# ------------------------------------------------------------
# 3. Memisahkan channel (H, S, V) agar bisa dimodifikasi
# ------------------------------------------------------------
h, s, v = cv2.split(hsv)  # Memisahkan channel warna

# ------------------------------------------------------------
# 4. Menambah nilai saturation supaya warna lebih kuat
# ------------------------------------------------------------
s = cv2.add(s, 40)   # Menambah saturation sebesar 40

# ------------------------------------------------------------
# 5. Menggabungkan kembali channel H, S, V
# ------------------------------------------------------------
hsv_enhanced = cv2.merge([h, s, v])

# ------------------------------------------------------------
# 6. Mengubah kembali dari HSV ke BGR agar bisa disimpan sebagai foto biasa
# ------------------------------------------------------------
result = cv2.cvtColor(hsv_enhanced, cv2.COLOR_HSV2BGR)

# ------------------------------------------------------------
# 7. Menyimpan hasil
# ------------------------------------------------------------
cv2.imwrite("output.jpg", result)

# ------------------------------------------------------------
# 8. Menampilkan hasil di jendela
# ------------------------------------------------------------
# Membuat gambar perbandingan secara horizontal (samping-samping)
comparison = cv2.hconcat([img, result])
cv2.imshow("Perbandingan (Kiri = Asli, Kanan = Hasil)", comparison)   # Jendela perbandingan

cv2.waitKey(0)   # Menunggu sampai tombol ditekan
cv2.destroyAllWindows()  # Menutup semua jendela

print("Selesai! Hasil tersimpan sebagai output.jpg")
