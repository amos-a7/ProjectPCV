# 🛡️ Shield Deflector - Active Parry

## 1. Deskripsi Umum
“Shield Deflector - Active Parry” adalah sebuah mini game interaktif berbasis computer vision di mana pemain menggunakan tangan mereka sebagai tameng energi (shield) untuk melindungi sebuah base di bagian bawah layar.

Game ini menantang pemain untuk merespons proyektil tidak hanya dengan menahan (block) secara pasif, tetapi juga menangkis (parry) proyektil berbahaya menggunakan gerakan ayunan tangan. Seluruh pemrosesan citra, mulai dari segmentasi warna kulit hingga penggabungan visual, diimplementasikan menggunakan komputasi matriks NumPy.

---

## 2. Tujuan Sistem
- Mengimplementasikan deteksi area tangan secara real-time berbasis skin color masking pada ruang warna HSV menggunakan manipulasi matriks NumPy.
- Menerapkan operasi morfologi citra (opening dan closing) untuk membersihkan noise pada citra biner.
- Mengintegrasikan visual senjata (weapon sprite) menggunakan metode alpha blending.
- Membangun sistem gesture recognition dasar (idle/block dan swipe/parry).
- Mengelola interaksi objek melalui collision detection, scoring, dan health points (HP).

---

## 3. Mekanisme Permainan
- **Kontrol Utama:** Kamera membaca posisi tangan secara real-time untuk menggerakkan shield.
- **Target:** Melindungi base dari objek yang jatuh.
- **Tipe Objek:**
  - 🟢 Normal → bisa di-block
  - 🔴 Heavy → harus di-parry
- **Kondisi Permainan:**
  - ✔ Berhasil → skor bertambah
  - ❌ Gagal → HP berkurang
  - ☠️ HP 0 → Game Over

---

## 4. Komponen & Flow Sistem

### Komponen Utama
1. **Hand Tracking & Gesture Detection**
   - HSV segmentation
   - Morphology (erode & dilate)
   - Contour & centroid detection
   - Gesture berbasis pergerakan (delta posisi)

2. **Weapon Overlay**
   - PNG transparan sebagai shield
   - Alpha blending menggunakan NumPy

3. **Falling Object & Interaksi**
   - Spawn objek dari atas
   - Collision detection (bounding box)
   - Logic block vs parry

4. **Scoring & Health**
   - Score bertambah saat sukses
   - HP berkurang saat gagal
   - Ditampilkan real-time

---

### Flow Eksekusi

---

## 5. Teknologi yang Digunakan
- Python
- OpenCV (untuk kamera & display)
- NumPy (core processing & image manipulation)

---

## 6. Progres & Kesesuaian Requirement
- [x] Gesture Detection  
- [x] Second Object  
- [x] Scoring  
- [x] HSV Processing  
- [x] Morphology  
- [x] Overlay  
- [x] Real-time Processing  

---

# Bab 7: Cara Menjalankan Program
doc.add_heading('7. Cara Menjalankan Program', level=1)

# Poin 1
p1 = doc.add_paragraph('1. ')
p1.add_run('Prasyarat:').bold = True
p1.add_run(' Pastikan Python 3.x sudah terpasang di perangkat Anda.')

# Poin 2
p2 = doc.add_paragraph('2. ')
p2.add_run('Instalasi Library:').bold = True
p2.add_run(' Buka terminal/command prompt dan instal dependencies yang dibutuhkan dengan perintah:\n')
p2.add_run('   pip install opencv-python numpy').italic = True

# Poin 3
p3 = doc.add_paragraph('3. ')
p3.add_run('Eksekusi:').bold = True
p3.add_run(' Jalankan file utama program menggunakan perintah:\n')
p3.add_run('   python main.py').italic = True

# Poin 4
p4 = doc.add_paragraph('4. ')
p4.add_run('Kontrol:').bold = True
p4.add_run('\n   • Gerakkan tangan di depan kamera untuk mengontrol shield.')
p4.add_run('\n   • Lakukan gerakan ayunan cepat untuk melakukan Parry.')
p4.add_run('\n   • Tekan tombol \'q\' atau \'Esc\' pada keyboard untuk keluar dari permainan.')
