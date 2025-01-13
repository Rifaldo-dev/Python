# Panduan Pembelajaran Python

## 1. Pengenalan Python
### Apa itu Python?
Python adalah bahasa pemrograman tingkat tinggi yang dirancang untuk kemudahan penggunaan, keterbacaan, dan fleksibilitas. Cocok untuk pemula maupun profesional.

### Mengapa Belajar Python?
- **Mudah Dipelajari**: Sintaks yang sederhana dan intuitif.
- **Multifungsi**: Digunakan untuk pengembangan web, data science, pembelajaran mesin, otomatisasi, dan lainnya.
- **Dukungan Komunitas**: Komunitas yang besar dan aktif menyediakan banyak sumber belajar.

### Instalasi Python
1. **Download Python**: [python.org](https://www.python.org/)
2. **IDE yang Direkomendasikan**:
   - VS Code (Visual Studio Code)
   - PyCharm
   - Jupyter Notebook (untuk data science)
3. **Menjalankan Program**:
   - Menggunakan terminal/command prompt: `python script.py`
   - Interaktif dengan Python Shell: `python`

---

## 2. Dasar-Dasar Pemrograman Python
### Sintaks Python
- **Indentasi** digunakan untuk menunjukkan blok kode (bukan kurung kurawal `{}`):
  ```python
  if True:
      print("Ini adalah blok kode")
  ```
- **Komentar**:
  ```python
  # Komentar satu baris
  """ Komentar multi-baris """
  ```

### Tipe Data dan Variabel
- **Tipe Data Dasar**:
  - `int`: Angka bulat
  - `float`: Angka desimal
  - `str`: Teks (string)
  - `bool`: True/False
- **Deklarasi Variabel**:
  ```python
  nama = "Aldo"
  usia = 25
  tinggi = 175.5
  is_active = True
  ```

### Operasi Dasar
- Penjumlahan, Pengurangan, Perkalian, Pembagian:
  ```python
  a = 10
  b = 3
  print(a + b)  # 13
  print(a - b)  # 7
  print(a * b)  # 30
  print(a / b)  # 3.3333
  ```

---

## 3. Struktur Kontrol
### Percabangan (Conditional)
- `if`, `elif`, `else`:
  ```python
  nilai = 85
  if nilai >= 90:
      print("A")
  elif nilai >= 75:
      print("B")
  else:
      print("C")
  ```

### Perulangan (Looping)
- **For Loop**:
  ```python
  for i in range(5):
      print(i)  # 0, 1, 2, 3, 4
  ```
- **While Loop**:
  ```python
  count = 0
  while count < 5:
      print(count)
      count += 1
  ```

---

## 4. Fungsi
- **Fungsi Dasar**:
  ```python
  def sapa(nama):
      return f"Halo, {nama}!"

  print(sapa("Aldo"))
  ```
- **Fungsi dengan Parameter Default**:
  ```python
  def tambah(a, b=5):
      return a + b

  print(tambah(3))  # 8
  ```

---

## 5. Tipe Data Lanjutan
### List
- Digunakan untuk menyimpan koleksi data:
  ```python
  buah = ["apel", "mangga", "jeruk"]
  print(buah[0])  # apel
  ```

### Dictionary
- Struktur data key-value:
  ```python
  data = {"nama": "Aldo", "usia": 25}
  print(data["nama"])  # Aldo
  ```

---

## 6. Pustaka dan Modul
- **Mengimpor Modul**:
  ```python
  import math
  print(math.sqrt(16))  # 4.0
  ```
- **Menggunakan Pustaka Pihak Ketiga**:
  ```python
  # Instal pustaka menggunakan pip
  pip install requests

  import requests
  response = requests.get("https://api.example.com")
  print(response.text)
  ```

---

## 7. Studi Kasus
### Program Sederhana
1. **Kalkulator Sederhana**:
   ```python
   def kalkulator(a, b, operasi):
       if operasi == "+":
           return a + b
       elif operasi == "-":
           return a - b
       elif operasi == "*":
           return a * b
       elif operasi == "/":
           return a / b
       else:
           return "Operasi tidak valid"

   print(kalkulator(10, 5, "+"))
   ```
2. **Penghitung Kata**:
   ```python
   teks = "Belajar Python itu menyenangkan"
   print(len(teks.split()))  # 4
   ```

---

## 8. Tips Belajar Python
- Mulai dengan proyek kecil (contoh: kalkulator, daftar tugas).
- Manfaatkan dokumentasi resmi Python: [https://docs.python.org/](https://docs.python.org/)
- Bergabung dengan komunitas atau forum belajar.
- Gunakan platform belajar online seperti Codecademy, Coursera, atau YouTube.

---

## 9. Sumber Belajar
- **Tutorial Resmi Python**: [https://docs.python.org/tutorial/](https://docs.python.org/tutorial/)
- **W3Schools Python**: [https://www.w3schools.com/python/](https://www.w3schools.com/python/)
- **FreeCodeCamp Python**: [https://www.freecodecamp.org/](https://www.freecodecamp.org/)

Selamat belajar Python! 🚀
