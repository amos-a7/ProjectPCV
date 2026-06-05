# Shield Deflector 🛡️

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-85C1E2?style=flat&logo=pygame&logoColor=white)

> Project game komputer vision bikin sendiri, hehe 🎮

## Apa Sih Shield Deflector?

**Shield Deflector** itu game interaktif yang seru bro! Konsepnya simple: pake webcam lo buat ngontrol shield (perisai), terus deflect batu-batuan dan bola api yang pada jatuh dari atas. Gabungan OpenCV buat hand detection sama game mechanics yang lumayan gampang dipahami.

Jadi basically, lo coba selamet diri sendiri pake hand gesture, nambah score, sampe HP lo abis. Simple tapi adiktif sih wkwkw.

---

## Fitur-fitur Unggulan ✨

### Gameplay Mechanics
- **Hand Tracking Real-time** - Pake HSV color segmentation sama morphological operations buat detect tangan
- **Shield yang ngikutin tangan lo** - Langsung ngikutin centroid tangan
- **Dua jenis object**:
  - 🪨 **Batu (Batu)** - Kena batu +10 poin, gampang kok
  - 🔥 **Bola Api (Api)** - Parry (cepet-cepetan) +25 poin atau block -1 HP
- **Difficulty yang naik seiring waktu** - Spawn rate random, kecepatan bervariasi
- **Parry System** - Gerakan tangan cepat = parry otomatis

### Game Systems
- **Health Point (HP)** - Mulai dari 5 HP, visual bar ada di corner
- **Score System** - Kumpulin poin dengan deflect objects
- **Collision Detection** - Pixel-perfect buat ngecek kena atau engga
- **Audio** - BGM + sound effects buat atmosphere
- **State Management** - Smooth transition ke game over

### Visual & Technical Stuff
- **Transparent Sprite Rendering** - Manual alpha blending pake NumPy
- **Debug Window** - Liat mask detection buat troubleshooting
- **Smooth Tracking** - EMA (Exponential Moving Average) biar stable
- **Morphological Operations** - Erode & dilate buat clean segmentation

---

## Tech Stack 🛠️

| Part | Tech | Fungsi |
|------|------|--------|
| **Vision** | OpenCV 4.x | Webcam input + hand detection |
| **Math** | NumPy | Image manipulation & array operations |
| **Rendering** | OpenCV + NumPy | Frame render & sprite overlay |
| **Audio** | Pygame Mixer | BGM sama sound effects |
| **Threading** | Python threading | Async music playback |

---

## Folder Structure 📁

```
shield-deflector/
├── assets/
│   ├── gambar/
│   │   ├── api.png              # Sprite bola api
│   │   ├── batu.png             # Sprite batu
│   │   └── shield_transparan.png # Sprite shield
│   ├── video/
│   │   └── gameplay_demo.mp4     # Demo gameplay (optional)
│   └── sound/
│       ├── gamesound.mp3        # BGM
│       ├── cannon-shot.mp3      # Sound effect hit
│       └── game-music.mp3       # Alternative BGM
├── game.py                # Main game code
├── README.md              # Ini file (documentation)
├── requirements.txt       # Dependencies
├── .gitignore            # Git config
└── .git/                 # Git repository
```

---

## Instalasi 🚀

### Yang Dibutuhkan
- **Python 3.8+** (3.11+ recommended)
- **Webcam** buat hand detection
- **RAM minimal 4GB**

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/shield-deflector.git
cd shield-deflector
```

### Step 2: Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

atau manual:

```bash
pip install opencv-python numpy pygame
```

### Step 4: Prepare Assets

Pastiin semua file ada di folder yang benar:
- Shield: `assets/gambar/shield_transparan.png` (220x220)
- Batu: `assets/gambar/batu.png` (60x60)
- Api: `assets/gambar/api.png` (60x60)
- Semua sound files di `assets/sound/`

### Step 5: Run Game!

```bash
python game.py
```

Done! Selamat main 🎮

---

## Cara Main 🎯

### Tujuan Game
Deflect benda-benda yang jatuh sambil ngelindungi HP lo dari kehabisan.

### Control

**Saat Main:**
| Key | Fungsi |
|-----|--------|
| `Gerakin Tangan` | Gerakin shield kiri/kanan/atas/bawah |
| `Tangan Cepat` | Parry (buat bola api) |
| `Q` | Quit game |

**Game Over:**
| Key | Fungsi |
|-----|--------|
| `R` | Main lagi |
| `Q` | Exit |

### Gameplay Details

#### Shield & Deflection
- Posisikan tangan di depan kamera
- Shield otomatis ngikutin posisi tangan lo
- Area shield 220x220 pixel

#### Object Types & Scoring

**🪨 Batu (Green)**
- Spawn rate: ~65%
- Speed: 3-5 px/frame
- Deflect: **+10 poin**
- Damage: Gratis, gak ada HP loss
- Tips: Batu gampang, fokus ke bola api aja

**🔥 Bola Api (Red)**
- Spawn rate: ~35%
- Speed: 3-5 px/frame
- **Normal Block**: -1 HP
- **Parry (Gerakan Cepat)**: **+25 poin**
- Tips: Gerakin tangan cepet buat parry, dapet poin banyak!

#### Parry Mechanic
- **Trigger**: Kecepatan tangan lebih dari 80 pixel per 4 frames
- **Visual**: Label "PARRY!" warna orange muncul
- **Effect**: Negasi damage + bonus points

#### Health System
- **Starting HP**: 5
- **HP Loss**: 1 HP per fireball (kalo engga parry)
- **Game Over**: HP = 0
- **Visual**: HP bar di top-left

### Pro Tips 💡

1. **Cahaya bagus** - Biar hand detection akurat
2. **Gerakin smooth** - Jangan tiba-tiba jump, biar tracking stabil
3. **Latih parry** - Cepatin reflex lo, dapet poin banyak
4. **Anticipation** - Prediksi object trajectory
5. **Base defense** - Jangan sampe ada object yang sampai y=570

---

## Fitur Detail 🎮

### Vision Pipeline

```
Input Webcam (640x480)
    ↓
Resize ke 160x120 (buat speed)
    ↓
BGR → HSV Conversion
    ↓
Hand ROI Extract (Rows 40-110)
    ↓
Skin Tone Filtering
    ↓
Morphological Ops (Erode → Dilate)
    ↓
Connected Component Analysis
    ↓
Contour Filtering & Scoring
    ↓
Position Smoothing (EMA alpha 0.8)
    ↓
Shield Render di (cx, cy)
```

### Hand Detection Zone
- **Y Range**: Rows 40-110 di frame 120px tinggi
- **X Range**: Full width (0-160px)
- **Debug**: White lines di mask window

### Collision Detection
```python
collision = (shield_x < object_x < shield_x + 220) AND
           (shield_y < object_y < shield_y + 220)
```

---

## Mau Customize? ⚙️

Edit ini di `game.py` buat sesuaiin gameplay:

```python
# Spawn rate (makin kecil = makin sering)
spawn_timer > 30  # Turunin buat lebih susah

# Speed object
speed = random.randint(3, 5)  # Ubah range

# Ukuran object
OBJ_SIZE = 50

# Ukuran shield
shield = cv2.resize(shield, (220, 220))

# HP awal
hp = 5
max_hp = 5

# Parry threshold
PARRY_THRESHOLD = 80

# Detection zone
HAND_ROI_TOP = 40
HAND_ROI_BOTTOM = 110
```

### Point System
```python
score += 10   # Batu deflect
score += 25   # Fireball parry
hp -= 1       # Fireball block
```

### Skin Tone HSV
Fine-tune untuk kulit lo:
```python
lower_skin1 = np.array([0,  30, 60])
upper_skin1 = np.array([20, 255, 255])
lower_skin2 = np.array([160, 30, 60])
upper_skin2 = np.array([180, 255, 255])
```

---

## Performa 📊

| Metric | Value | Note |
|--------|-------|------|
| **Target FPS** | 30+ | Smooth |
| **Hand Detection Latency** | <50ms | Real-time |
| **Display Size** | 800x600 | Optimal |
| **Processing Size** | 160x120 | Fast |
| **Position Smoothing** | 0.8 alpha | Stable |

---

## Gambar & Video Demo 📸🎬

### Screenshots

Ini screenshot gameplay:

![Gameplay Demo](assets/gambar/gameplay_screenshot.png)

### Video Demo

Lihat gameplay dalam aksi:

[![Gameplay Demo](Asset/demo_game/Screenshot.png)](Asset/demo_game/Screen%20Recording%202026-06-05%20233855%20(1).mp4)

> **Catatan**: Ganti `gameplay_screenshot.png` dan `gameplay_demo.mp4` pake file punya lo sendiri!

### Cara Nambahin Screenshot/Video Sendiri

1. **Untuk Screenshot**:
   - Ambil screenshot saat main game
   - Save di `assets/gambar/` folder
   - Update nama file di section ini

2. **Untuk Video**:
   - Record gameplay pake screen recorder (OBS, ShareX, dll)
   - Save di `assets/video/` folder
   - Update link di section ini

3. **Edit README.md**:
   ```markdown
   ![Gameplay](assets/gambar/screenshot_lo.png)
   [![Video](assets/gambar/thumbnail.png)](assets/video/video_lo.mp4)
   ```

---

## Kalau Ada Masalah 🐛

### Hand gak ketdetect

**Solusi**:
1. Pastiin cahaya bagus, jangan gelap
2. Adjust HSV range buat skin tone
3. Ubah `HAND_ROI_TOP` dan `HAND_ROI_BOTTOM`
4. Tangan deket kamera (15-30cm ideal)

### Gak ada suara

**Solusi**:
1. Cek file audio ada di folder
2. Volume system gak muted
3. Verify file path di kode
4. Pygame mixer initialized dengan baik

### FPS rendah / lag

**Solusi**:
1. Close app yang lain
2. Turunin resolusi `(800, 600)`
3. Naikin `spawn_timer` value
4. Off debug mask window saat main
5. Update OpenCV & NumPy

### Webcam gak terdetect

**Solusi**:
1. Cek device ID (biasanya 0, coba 1)
2. Pastiin webcam gak dipakai app lain
3. Grant camera permission di system
4. Update camera driver
5. Check koneksi USB (kalo external)

---

## Educational Value 🎓

Project ini pelajaran praktis tentang:
- **Computer Vision**: HSV, morphological ops, contour analysis
- **Real-time Processing**: Frame-by-frame analysis
- **Game Development**: State management, collision detection
- **Audio Programming**: Mixer-based playback
- **Image Processing**: Alpha blending, sprite rendering
- **Python**: Threading, NumPy, OpenCV

---

## Credits & License 📝

- **License**: MIT
- **Author**: Amos (Teknik Komputer, Semester 4)
- **Libraries**: OpenCV, NumPy, Pygame

---

## Future Ideas (Mungkin) 🚀

- [ ] Easy/Normal/Hard difficulty
- [ ] Multiple game modes
- [ ] Enemy variety
- [ ] High score leaderboard
- [ ] Audio settings
- [ ] Full-screen mode
- [ ] Multiplayer (2 player)
- [ ] Particle effects
- [ ] Advanced gesture recognition

---

## Kontak & Support 📞

Ada bug atau saran? Bisa:
- Buka issue di GitHub
- Email: [your-email@example.com]
- Discord: [Your Discord]

---

**Made with ❤️ and OpenCV** ☕

Semoga seru! Good luck bro! 🎮✨
