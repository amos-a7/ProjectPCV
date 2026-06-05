# Shield Deflector

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-85C1E2?style=flat&logo=pygame&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Development-blue?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

## 🎮 Description

**Shield Deflector** is an interactive real-time computer vision game that challenges players to use their hand to deflect falling objects. The game combines **OpenCV-based hand detection**, **real-time gesture recognition**, and **dynamic game mechanics** to create an engaging and immersive gaming experience.

Players control a shield using only their webcam, deflecting falling rocks and fireballs while managing health points and accumulating score. The game features smooth hand tracking, audio feedback, and a complete gameplay loop with scoring and progression mechanics.

## ✨ Main Features

### Core Gameplay
- **Real-time Hand Tracking** using HSV color segmentation and morphological operations for robust hand detection
- **Shield Control via Webcam** - shield position follows detected hand centroid in real-time
- **Two Object Types** with different mechanics:
  - 🪨 **Rocks (Batu)** - deflect for +10 score
  - 🔥 **Fireballs (Api)** - parry for +25 score or block for -1 HP damage
- **Dynamic Difficulty** with randomized object spawn rates and velocities
- **Gesture Recognition** - automatic parry detection based on hand velocity threshold

### Game Systems
- **Health Point (HP) System** - 5 starting HP with visual bar indicator
- **Scoring Mechanism** - accumulate points by deflecting objects
- **Real-time Collision Detection** - pixel-perfect shield-object intersection testing
- **Audio Feedback** - background music and sound effects for object deflection
- **Game State Management** - seamless transitions between gameplay and game over states

### Visual & Technical
- **Transparent Sprite Rendering** - manual alpha blending using NumPy for accurate overlay
- **Real-time Mask Visualization** - debug window showing hand detection zone
- **Smooth Hand Tracking** - exponential moving average (EMA) for stable position smoothing
- **Adaptive Morphological Processing** - erode and dilate operations for clean hand segmentation
- **Component-based Filtering** - intelligent contour selection based on area and position scoring

## 🛠️ Technical Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Vision Processing** | OpenCV 4.x | Real-time webcam input and hand detection |
| **Numerical Computation** | NumPy | Image manipulation and mathematical operations |
| **Game Rendering** | OpenCV + NumPy | Frame rendering and sprite overlay |
| **Audio System** | Pygame Mixer | Background music and sound effects |
| **Threading** | Python threading | Asynchronous music playback |

## 📁 Project Structure

```
shield-deflector/
├── game.py                      # Main game loop and core gameplay logic
├── gambar_tes/                  # Asset directory
│   ├── shield_transparan.png    # Shield sprite (PNG with alpha)
│   ├── batu.png                 # Rock sprite (PNG with alpha)
│   ├── api.png                  # Fireball sprite (PNG with alpha)
│   ├── viacheslavstarostin-...  # Background music file
│   └── gamesound-broken-...     # Object hit sound effect
│   └── universfield-...         # Fireball hit sound effect
├── README.md                    # Project documentation
└── .gitignore                   # Git ignore rules
```

## 🚀 Installation Guide

### Prerequisites
- **Python 3.8+** (3.11+ recommended for optimal compatibility)
- **Webcam** for hand detection input
- **Minimum 4GB RAM** for smooth operation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/shield-deflector.git
cd shield-deflector
```

### Step 2: Create Virtual Environment

```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install opencv-python numpy pygame
```

**Dependency Details:**
- `opencv-python==4.8.0+` - Computer vision and image processing
- `numpy==1.24.0+` - Numerical computing and array operations
- `pygame==2.1.0+` - Audio playback via mixer module

### Step 4: Prepare Assets

Ensure all asset files are in the `gambar_tes/` directory:
- Shield sprite: `shield_transparan.png` (220x220)
- Rock sprite: `batu.png` (60x60)
- Fireball sprite: `api.png` (60x60)
- Background music file
- Sound effect files (2 files for rock and fireball hits)

### Step 5: Run the Game

```bash
python game.py
```

## 🎯 How to Play

### Game Objective
Deflect falling objects using your hand-controlled shield for as long as possible while managing your health points.

### Controls

**During Gameplay:**
| Key | Action |
|-----|--------|
| `Hand Movement` | Move shield left/right/up/down |
| `Hand Speed` | Fast motion = Parry (for fireballs) |
| `Q` | Quit game |

**On Game Over:**
| Key | Action |
|-----|--------|
| `R` | Restart game |
| `Q` | Quit to desktop |

### Gameplay Mechanics

#### Shield & Deflection
- Position your hand in front of the camera to control the shield
- The shield automatically tracks your hand's centroid position
- Shield covers a 220x220 pixel area around your hand position

#### Object Types & Scoring

**Rocks (🪨 Batu - Green)**
- Spawn rate: ~65% of all objects
- Speed: 3-5 pixels/frame
- Deflection: **+10 points**
- Damage: Blocks for free (no HP loss)
- Strategy: Easy to handle, focus on hitting fireballs

**Fireballs (🔥 Api - Red)**
- Spawn rate: ~35% of all objects
- Speed: 3-5 pixels/frame
- **Block (Normal)**: -1 HP
- **Parry (Fast Motion)**: **+25 points**
- Strategy: Move your hand quickly to activate parry and earn more points

#### Parry Mechanic
- **Parry Detection:** Automatic when hand velocity exceeds threshold (80 pixels over 4 frames)
- **Visual Feedback:** "PARRY!" label appears in orange when active
- **Damage Negation:** Successfully parry fireballs for bonus points instead of taking damage

#### Health System
- **Starting HP:** 5 points
- **HP Loss:** 1 HP per fireball contact (when not parrying)
- **Game Over:** Triggered when HP reaches 0
- **Visual Indicator:** HP bar at top-left shows remaining health

### Tips & Strategies

1. **Hand Placement:** Keep your hand visible and well-lit for accurate detection
2. **Smooth Movements:** Avoid jerky motions to prevent tracking loss
3. **Parry Windows:** Practice quick hand movements to parry fireballs for maximum points
4. **Positioning:** Anticipate falling objects' trajectories and position shield preemptively
5. **Base Protection:** Ensure no objects reach the base line at y=570 to prevent HP loss

## 🎮 Game Features Deep Dive

### Vision Processing Pipeline

```
Webcam Input (640x480)
    ↓
Frame Resize (160x120) - For speed optimization
    ↓
BGR to HSV Conversion
    ↓
Hand ROI Extraction (Rows 40-110)
    ↓
Color Range Filtering (Skin tone detection)
    ↓
Morphological Operations (Erode → Dilate)
    ↓
Connected Component Analysis
    ↓
Contour Filtering & Scoring
    ↓
Position Smoothing (EMA: 0.8 alpha)
    ↓
Shield Rendering at (cx, cy)
```

### Hand Detection Zone

The game focuses on a specific vertical region for hand detection:
- **Y Range:** Rows 40-110 in 120-pixel high frame
- **X Range:** Full width (0-160 pixels in small frame)
- **Visual Debug:** White horizontal lines in mask window show detection zone boundaries

### Collision Detection

Objects are checked for collision with the shield using bounding box intersection:

```python
collision = (shield_x < object_x < shield_x + shield_width) AND
           (shield_y < object_y < shield_y + shield_height)
```

## 🐛 Troubleshooting

### Hand Detection Issues

**Problem:** Hand not detected / tracking is unstable

**Solutions:**
1. Ensure good lighting (avoid shadows)
2. Increase skin tone range in HSV filtering
3. Adjust `HAND_ROI_TOP` and `HAND_ROI_BOTTOM` constants for different body parts
4. Try adjusting `MIN_PIXELS` and `MAX_AREA` thresholds
5. Move hand closer to camera (15-30cm optimal distance)

### Audio Issues

**Problem:** No sound effects or music playing

**Solutions:**
1. Verify audio files exist in `gambar_tes/` directory
2. Check system volume is not muted
3. Ensure `pygame.mixer` initialization succeeds (no errors in console)
4. Verify file paths are correct in code
5. Try different audio formats if supported

### Performance Issues

**Problem:** Low FPS or laggy gameplay

**Solutions:**
1. Close unnecessary background applications
2. Reduce frame resolution (edit `(800, 600)` in code)
3. Decrease spawn rate by increasing `spawn_timer` threshold
4. Disable mask visualization window during gameplay
5. Update OpenCV and NumPy to latest versions

### Webcam Issues

**Problem:** Webcam not recognized / "ret is False"

**Solutions:**
1. Check camera device ID (usually 0, try 1 if not working)
2. Ensure no other application is using the webcam
3. Grant camera permissions in system settings
4. Try updating camera drivers
5. Verify USB connection if external camera

## ⚙️ Configuration & Customization

### Game Constants

Edit these values in `game.py` to customize gameplay:

```python
# Spawn Rate (lower = more frequent)
spawn_timer > 30  # Change 30 to lower value for harder game

# Object Speed Range
speed = random.randint(3, 5)  # Change range for difficulty

# Object Size
OBJ_SIZE = 50  # Change for larger/smaller objects

# Shield Size
shield = cv2.resize(shield, (220, 220))  # Change dimensions

# Health System
hp = 5  # Starting health
max_hp = 5  # Maximum health

# Parry Threshold
PARRY_THRESHOLD = 80  # Pixel distance for parry activation

# Hand Detection Zone
HAND_ROI_TOP = 40
HAND_ROI_BOTTOM = 110
```

### Scoring Multipliers

```python
# Adjust point values
score += 10   # Rock deflection points
score += 25   # Fireball parry points
hp -= 1       # Fireball block damage
```

### HSV Color Range

Fine-tune skin tone detection:

```python
lower_skin1 = np.array([0,  30, 60])
upper_skin1 = np.array([20, 255, 255])
lower_skin2 = np.array([160, 30, 60])
upper_skin2 = np.array([180, 255, 255])
```

## 📊 Performance Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| **Target FPS** | 30+ | Smooth gameplay |
| **Hand Detection Latency** | <50ms | Real-time feedback |
| **Frame Size** | 800x600 | Optimal display |
| **Processing Size** | 160x120 | Fast computation |
| **Position Smoothing** | 0.8 alpha | Stable tracking |

## 🎓 Educational Context

This project demonstrates practical applications of:
- **Computer Vision:** HSV segmentation, morphological operations, contour analysis
- **Real-time Processing:** Frame-by-frame video analysis
- **Game Development:** State management, collision detection, scoring systems
- **Audio Programming:** Mixer-based sound playback
- **Image Processing:** Manual alpha blending, sprite rendering
- **Python Programming:** Threading, NumPy arrays, OpenCV API

## 📝 License

This project is licensed under the **MIT License** - see LICENSE file for details.

## 👤 Author

**Harol**  
*Computer Vision & Game Development Enthusiast*

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

### Development Setup

```bash
# Clone and setup
git clone <repository>
cd shield-deflector
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Make changes and test
python game.py

# Commit with descriptive message
git add .
git commit -m "feat: add new feature description"
git push origin main
```

## 🎯 Future Enhancements

- [ ] Difficulty levels (Easy, Normal, Hard)
- [ ] Multiple game modes (Survival, Time Attack)
- [ ] Enemy variety (different object types with unique behaviors)
- [ ] Leaderboard system with persistent high scores
- [ ] Sound settings and audio customization
- [ ] Full-screen mode and resolution options
- [ ] Mobile camera input support
- [ ] Multiplayer mode (two players)
- [ ] Visual effects (particles, screen shake)
- [ ] Advanced gesture recognition (swipe, grab gestures)

## 📞 Support & Contact

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [your-email@example.com]
- Discord: [Your Discord Server]

## 🙏 Acknowledgments

- OpenCV community for excellent computer vision library
- NumPy for efficient numerical computing
- Pygame for audio subsystem
- Asset creators and sound designers

---

**Last Updated:** June 2026  
**Version:** 1.0.0  
**Status:** Active Development
