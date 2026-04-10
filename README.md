# 🛡️ Shield Deflector - Active Parry

## 1. Deskripsi Umum
“Shield Deflector - Active Parry” adalah sebuah mini game interaktif berbasis computer vision di mana pemain menggunakan tangan mereka sebagai tameng energi (shield) untuk melindungi sebuah Base di bagian bawah layar. Game ini menantang pemain untuk merespons proyektil tidak hanya dengan menahan (Block) secara pasif, tetapi juga menangkis (Parry) proyektil berbahaya menggunakan gerakan ayunan tangan. Seluruh pemrosesan citra, mulai dari segmentasi warna kulit hingga penggabungan visual, diimplementasikan secara fundamental menggunakan komputasi matriks NumPy.

---

## 2. Tujuan Sistem
* Mengimplementasikan deteksi area tangan secara real-time berbasis skin color masking pada ruang warna HSV menggunakan algoritma manipulasi matriks NumPy secara manual.
* Menerapkan operasi morfologi citra (Opening dan Closing) secara manual melalui NumPy untuk membersihkan noise pada citra biner.
* Mengintegrasikan visual senjata (Weapon Sprite) ke koordinat objek terdeteksi menggunakan metode Alpha Blending manual.
* Membangun sistem Gesture Recognition dasar yang membedakan posisi statis (Idle/Block) dan gerakan dinamis (Swipe/Parry).
* Mengelola interaksi antar objek virtual melalui Collision Detection, sistem skor, dan Health Points (HP).

---

## 3. Mekanisme Permainan
* **Kontrol Utama:** Kamera membaca posisi centroid tangan secara real-time untuk menggerakkan tameng.
* **Target:** Melindungi Base dari objek jatuh.
* **Tipe Objek:** * Normal → bisa diblok.
  * Berat → harus diparry.
* **Kondisi Permainan:** * Berhasil → skor bertambah.
  * Gagal → HP berkurang.
  * HP 0 → Game Over.

---

## 4. Komponen & Flow Sistem

### Komponen Utama
1. **Hand Tracking & Gesture Detection:** Meliputi HSV segmentation (manual NumPy), Morphology (erode & dilate manual), Contour & centroid detection, dan Gesture berbasis pergerakan (delta posisi).
2. **Weapon Overlay:** Menggunakan PNG transparan sebagai shield dengan proses Alpha blending manual menggunakan NumPy.
3. **Falling Object & Interaksi:** Meliputi sistem Spawn objek dari atas, Collision detection (bounding box), dan Logic block vs parry.
4. **Scoring & Health:** Score bertambah saat sukses, HP berkurang saat gagal, dan semuanya ditampilkan secara real-time.

### Flow Eksekusi
`Capture frame` ➔ `Deteksi tangan` ➔ `Update shield` ➔ `Spawn & update objek` ➔ `Collision check` ➔ `Render & display` ➔ `Game Over jika HP habis`.

---

## 5. Teknologi yang Digunakan
Sistem ini dibangun dengan meminimalisir library tingkat tinggi, dan berfokus pada:
* **Python**
* **OpenCV** (untuk I/O Kamera dan display)
* **NumPy** (sebagai *core engine* komputasi matriks dan *image processing*)

---

## 6. Progres & Kesesuaian Requirement
Status pengembangan fitur saat ini sesuai dengan *requirement* proyek:
- [x] Gesture Detection
- [x] Second Object
- [x] Scoring
- [x] HSV
- [x] Morphology
- [x] Overlay
- [x] Real-time

---

## 7. Cara Menjalankan Program
1. **Prasyarat:** Pastikan Python 3.x sudah terpasang di perangkat Anda.
2. **Instalasi Library:** Buka terminal/command prompt dan instal *dependencies* yang dibutuhkan dengan perintah:
   ```bash
   pip install opencv-python numpy
