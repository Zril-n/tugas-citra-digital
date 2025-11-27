# tugas-citra-digital
# ⭐ Manipulasi Citra Digital – Peningkatan Warna (HSV Saturation Boost)

Program ini melakukan **manipulasi citra digital** menggunakan metode **peningkatan Saturation (S)** pada model warna **HSV**.  
Tujuannya adalah membuat gambar terlihat **lebih berwarna**, cerah, dan tetap natural.
---
## 📂 File yang Dibutuhkan
- `steganografi.py` → source code
- `img-2.jpeg` → gambar yang kamu pilih dari file ZIP tugas
- Output otomatis: `output.jpg`
---
## 📦 Instalasi Library
Program ini membutuhkan Python dan OpenCV.

### 1. Install Python 3  
Download dari: https://python.org

### 2. Install OpenCV
Jalankan di terminal / CMD:

```bash
pip install opencv-python
```
---
## ▶️ Cara Menjalankan Program

1. Pastikan file `main.py` dan `img-2.jpeg` berada dalam folder yang sama.
2. Buka terminal / CMD di folder tersebut.
3. Jalankan program:
```bash
python main.py
```
4. Program akan menampilkan:
   - Gambar asli
   - Gambar hasil
   - Perbandingan (asli vs hasil)

5. Hasil manipulasi otomatis tersimpan sebagai:
```
output.jpg
```
---
## 🧠 Penjelasan Singkat Cara Kerja Program

1. Program membaca gambar original.
2. Mengubah gambar dari **BGR → HSV**  
   HSV memisahkan warna menjadi:
   - **H = Hue (jenis warna)**
   - **S = Saturation (kekuatan warna)**
   - **V = Value (kecerahan)**
3. Program menaikkan nilai **S (Saturation)** → gambar jadi lebih berwarna.
4. Channel H, S, V digabung kembali.
5. Gambar dikonversi ke **BGR** agar bisa disimpan sebagai foto normal.
6. Hasil disimpan dan ditampilkan di jendela.
---
## 📸 Tampilan Program
Program menampilkan 3 jendela:
- "Gambar Asli"
- "Gambar Hasil"
- "Perbandingan (Asli vs Hasil)"
---
## 📝 Kontak
Jika terjadi error “gambar tidak ditemukan”, pastikan:
- Nama file gambar adalah **img-2.jpeg**
- File berada pada folder yang sama dengan script
---
## ✔️ Status
Program ini sudah diuji dan bekerja dengan baik.
