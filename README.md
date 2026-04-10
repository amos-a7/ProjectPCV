# ProjectPCV
# 🛡️ Shield Deflector - Active Parry

## 1. Deskripsi Umum
[cite_start]“Shield Deflector - Active Parry” adalah sebuah mini game interaktif berbasis computer vision di mana pemain menggunakan tangan mereka sebagai tameng energi (shield) untuk melindungi sebuah Base di bagian bawah layar[cite: 3]. [cite_start]Game ini menantang pemain untuk merespons proyektil tidak hanya dengan menahan (Block) secara pasif, tetapi juga menangkis (Parry) proyektil berbahaya menggunakan gerakan ayunan tangan[cite: 4]. [cite_start]Seluruh pemrosesan citra, mulai dari segmentasi warna kulit hingga penggabungan visual, diimplementasikan secara fundamental menggunakan komputasi matriks NumPy[cite: 5].

---

## 2. Tujuan Sistem
* [cite_start]Mengimplementasikan deteksi area tangan secara real-time berbasis skin color masking pada ruang warna HSV menggunakan algoritma manipulasi matriks NumPy secara manual[cite: 7].
* [cite_start]Menerapkan operasi morfologi citra (Opening dan Closing) secara manual melalui NumPy untuk membersihkan noise pada citra biner[cite: 8].
* [cite_start]Mengintegrasikan visual senjata (Weapon Sprite) ke koordinat objek terdeteksi menggunakan metode Alpha Blending manual[cite: 9].
* [cite_start]Membangun sistem Gesture Recognition dasar yang membedakan posisi statis (Idle/Block) dan gerakan dinamis (Swipe/Parry)[cite: 10].
* [cite_start]Mengelola interaksi antar objek virtual melalui Collision Detection, sistem skor, dan Health Points (HP)[cite: 11].

---

## 3. Mekanisme Permainan
* [cite_start]**Kontrol Utama:** Kamera membaca posisi centroid tangan secara real-time untuk menggerakkan tameng[cite: 13].
* [cite_start]**Target:** Melindungi Base dari objek jatuh[cite: 14].
* [cite_start]**Tipe Objek:** * Normal → bisa diblok[cite: 16].
  * [cite_start]Berat → harus diparry[cite: 17].
* [cite_start]**Kondisi Permainan:** * Berhasil → skor bertambah[cite: 19].
  * [cite_start]Gagal → HP berkurang[cite: 20].
  * [cite_start]HP 0 → Game Over[cite: 21].

---

## 4. Komponen & Flow Sistem

### Komponen Utama
1. [cite_start]**Hand Tracking & Gesture Detection:** Meliputi HSV segmentation (manual NumPy), Morphology (erode & dilate manual), Contour & centroid detection, dan Gesture berbasis pergerakan (delta posisi)[cite: 23, 24, 25, 26, 27].
2. [cite_start]**Weapon Overlay:** Menggunakan PNG transparan sebagai shield dengan proses Alpha blending manual menggunakan NumPy[cite: 28, 29, 30].
3. [cite_start]**Falling Object & Interaksi:** Meliputi sistem Spawn objek dari atas, Collision detection (bounding box), dan Logic block vs parry[cite: 31, 32, 33, 34].
4. [cite_start]**Scoring & Health:** Score bertambah saat sukses, HP berkurang saat gagal, dan semuanya ditampilkan secara real-time[cite: 35, 36, 37, 38].

### Flow Eksekusi
[cite_start]`Capture frame` ➔ `Deteksi tangan` ➔ `Update shield` ➔ `Spawn & update objek` ➔ `Collision check` ➔ `Render & display` ➔ `Game Over jika HP habis`[cite: 39, 40, 41, 42, 43, 44, 45, 46].

---

## 5. Teknologi yang Digunakan
Sistem ini dibangun dengan meminimalisir library tingkat tinggi, dan berfokus pada:
* [cite_start]**Python** [cite: 48]
* [cite_start]**OpenCV** (untuk I/O Kamera dan display) [cite: 49]
* [cite_start]**NumPy** (sebagai *core engine* komputasi matriks dan *image processing*) [cite: 50]

---

## 6. Progres & Kesesuaian Requirement
[cite_start]Status pengembangan fitur saat ini sesuai dengan *requirement* proyek[cite: 51]:
- [x] [cite_start]Gesture Detection [cite: 52]
- [x] [cite_start]Second Object [cite: 53]
- [x] [cite_start]Scoring [cite: 54]
- [x] [cite_start]HSV [cite: 55]
- [x] [cite_start]Morphology [cite: 56]
- [x] [cite_start]Overlay [cite: 57]
- [x] [cite_start]Real-time [cite: 58]

---

## 7. Cara Menjalankan Program
1. **Prasyarat:** Pastikan Python 3.x sudah terpasang di perangkat Anda.
2. **Instalasi Library:** Buka terminal/command prompt dan instal *dependencies* yang dibutuhkan dengan perintah:
   ```bash
   pip install opencv-python numpy
