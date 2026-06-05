import cv2
import numpy as np
import random
import pygame
import threading
import math

pygame.mixer.init()

# background music
def mulai_musik():
    pygame.mixer.music.load(
        "gambar_tes/viacheslavstarostin-game-gaming-video-game-music-471936.mp3"
    )
    
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
musik_thread = threading.Thread(
    target = mulai_musik,
    daemon = True
)

musik_thread.start()


#sound effect
try :
    sound_batu = pygame.mixer.Sound(
        "gambar_tes/gamesound-broken-454907.mp3"
    )
    sound_batu.set_volume(0.6)
except :
    print("tidak ada")
    sound_batu = None
    
    
try :
     sound_api = pygame.mixer.Sound(
    "gambar_tes/universfield-powerful-cannon-shot-352459.mp3"
)
     sound_api.set_volume(0.6)

except :
    print("tidak ditemukan")
    sound_api = None

def play_sound(sound) :
    if sound is not None :
        sound.play()
        
#variabel game
camera = cv2.VideoCapture(0)

objects = [] #berisi posisi x.y, kecepatan dan tipe (batu atau api)

spawn_timer = 0
score  = 0

hp = 5

game_over = False

#Erode (berhisin area putih)
def erode(img, size=3):
    pad = size // 2
    padded = np.pad(
        img, pad, mode = "constant", constant_values = 0
    )
    
    h, w = img.shape
    area = []
    
    for y in range(size):
        for x in range(size):
            area.append(
                padded[y:y+h, x:x+w]
            )
    stacked = np.stack(area, axis=0)
    return np.min(stacked, axis=0).astype(np.uint8)

#dilate
def dilate (img, size=3) :
    pad = size //2
    
    padded = np.pad(
        img, pad, mode="constant", constant_values=0
    )
    
    h,w = img.shape
    area = []
    
    for y in range (size):
        for x in range (size):
            area.append(
                padded[y:y+h, x:x+w]
            )
    stacked = np.stack(area, axis=0)
    return np.max(stacked, axis=0).astype(np.uint8)

#overlay png (nempel png ke frame webcam)

def overlay_image(background, overlay, x,y):

    h, w = overlay.shape[:2]
    
    if x<0 :
        overlay = overlay[:, -x:]
        h = overlay.shape[0]
        x= 0
        
    if y < 0:
        overlay = overlay[-y:, :]
        h = overlay.shape[0]
        y=0
        
    if x+w> background.shape[1]:
        overlay = overlay[:, :background.shape[1]-x]
    
    if y+h > background.shape[0]:
        overlay = overlay[:background.shape[0]-y,:]
        
    h,w = overlay.shape[:2]
    if h == 0 or w == 0:
        return background
    
    overlay_rgb = overlay[:, :, :3].astype(np.float32)
    
    alpha = overlay[:, :, 3:4].astype(np.float32) /255.0
    zona = background[y:y+h, x:x+w].astype(np.float32)
    
    result = alpha * overlay_rgb + (1-alpha)* zona
    background[y:y+h, x:x+w] =  result.astype(np.uint8)
    
    return background

def draw_hp(frame, hp, max_hp = 5) :
    bar_w = 30
    bar_h = 20
    
    gap = 8
    
    x0 = 10
    y0 = 55
    
    for i in range(max_hp) :
        x = x0 + i * (bar_w + gap)
        if i < hp :
            color = np.array(
                [0,200,0],
                dtype = np.uint8
            )
        else :
            color = np.array(
                [60,60,60],
                dtype = np.uint8
            )
            
        frame [
            y0:y0+bar_h,
            x:x+bar_w
        ] = color
        
def draw_base (frame) :
    base_y = 570
    
    frame [ base_y : base_y+8, 50:750] = np.array(
        [0,100,255],
        dtype = np.uint8
    )        
    cv2.putText(
        frame, "BASE", (350,568), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,100,255), 2
    )

def dfs_component(mask, visited, start_x, start_y):

    stack = [(start_x, start_y)]

    area = 0

    sum_x = 0
    sum_y = 0

    while stack:

        x, y = stack.pop()

        if (
            x < 0 or
            y < 0 or
            x >= mask.shape[1] or
            y >= mask.shape[0]
        ):
            continue

        if visited[y, x]:
            continue

        if mask[y, x] == 0:
            continue

        visited[y, x] = True

        area += 1

        sum_x += x
        sum_y += y

        stack.append((x+1, y))
        stack.append((x-1, y))
        stack.append((x, y+1))
        stack.append((x, y-1))

    if area == 0:
        return 0, 0, 0

    cx = sum_x // area
    cy = sum_y // area

    return area, cx, cy

#masukkan gambar

shield = cv2.imread(
    "gambar_tes/shield_transparan.png",-1
)

shield = cv2.resize(
    shield, (220,220)
)

batu = cv2.imread(
    "gambar_tes/batu.png",-1
)

api = cv2.imread (
    "gambar_tes/api.png",-1
)

if batu is None :
    batu = np.zeros(
        (60,60,4), dtype=np.uint8
    )
    batu[:, :, :3] = 120
    batu[:, :, 3] =255
    
    
if api is None :
    api = np.zeros(
        (60,60,4), dtype= np.uint8
        
    )
    api[:, :, 2] =220
    api[:,:, 3] =255
    
    
obj_size = 50
batu_img = cv2.resize(
    batu, (obj_size,obj_size )
)

api_img = cv2.resize(
    api, (obj_size, obj_size)
)

prev_x = 0
prev_y = 0

alpha_smooth = 0.8

pos_history = []

parry_threshold = 80 


hand_zona_top = 40
hand_zona_bottom = 110

min_pixel = 40
max_area = 2500

shield_x = 400
shield_y = 300

#main loop
while True :
    ret, frame = camera.read()
    
    if not ret :
        break
    
    frame = cv2.flip(frame, 1)
    frame_display = cv2.resize(
        frame,
        (800,600)
    )
    
    draw_base(frame_display)
    
    if game_over:

        overlay_go = frame_display.copy()

        overlay_go[
            150:450,
            150:650
        ] = np.array(
            [20,20,20],
            dtype=np.uint8
        )

        frame_display = (
            0.7 * overlay_go +
            0.3 * frame_display
        ).astype(np.uint8)

        cv2.putText(
            frame_display,
            "GAME OVER",
            (220,290),
            cv2.FONT_HERSHEY_DUPLEX,
            2.5,
            (0,0,220),
            4
        )

        cv2.putText(
            frame_display,
            f"Final Score: {score}",
            (290,360),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (255,255,255),
            2
        )

        cv2.putText(
            frame_display,
            "Tekan R untuk restart",
            (230,420),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (200,200,200),
            1
        )

        cv2.imshow(
            "Shield Deflector",
            frame_display
        )

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

        if key == ord("r"):

            objects = []
            spawn_timer = 0
            score = 0
            hp = 5
            game_over = False

            pos_history.clear()

            prev_x = 0
            prev_y = 0

            pygame.mixer.music.play(-1)

        continue

    spawn_timer += 1

    if spawn_timer > 30 :
        x = random.randint(60, 740)
        
        speed = random.randint(3,5)
        otype = 1 if random.random() < 0.35 else 0
        
        objects.append(
            {"x": x, "y": 0, "speed": speed, "type": "fire" if otype == 1 else "rock"}
        )
        
        spawn_timer = 0
        
    for obj in objects :
        obj["y"] += obj["speed"]
            
        
    frame_small = cv2.resize(
        frame,
        (160,120)
    )

    hsv_full = cv2.cvtColor(
        frame_small,
        cv2.COLOR_BGR2HSV
    )

    hsv = hsv_full[
        hand_zona_top:hand_zona_bottom, :
    ]

    lower_skin1 = np.array(
        [0, 30, 60],
        dtype=np.uint8
    )

    upper_skin1 = np.array(
        [20, 255, 255],
        dtype=np.uint8
    )

    lower_skin2 = np.array(
        [160, 30, 60],
        dtype=np.uint8
    )

    upper_skin2 = np.array(
        [180, 255, 255],
        dtype=np.uint8
    )

    H = hsv[:, :, 0]
    S = hsv[:, :, 1]
    V = hsv[:, :, 2]

    mask1 = (
        (H >= lower_skin1[0]) & (H <= upper_skin1[0]) &
        
        (S >= lower_skin1[1]) & (S <= upper_skin1[1]) &
        
        (V >= lower_skin1[2]) & (V <= upper_skin1[2])
        
    )

    mask2 = (
        (H >= lower_skin2[0]) & (H <= upper_skin2[0]) &
        
        (S >= lower_skin2[1]) & (S <= upper_skin2[1]) &
        
        (V >= lower_skin2[2]) & (V <= upper_skin2[2])
        
    )

    mask = (mask1 | mask2).astype(np.uint8) * 255

    mask = erode(mask)
    mask = dilate(mask)

    mask = dilate(mask)
    mask = erode(mask)

    visited = np.zeros_like(mask, dtype=bool)

    big_area = 0
    big_cx = None
    big_cy = None

    for y in range(mask.shape[0]):
        for x in range(mask.shape[1]):

            if mask[y, x] == 255 and not visited[y, x]:

                area, cx, cy = dfs_component(
                    mask,
                    visited,
                    x,
                    y
                )

                if min_pixel <= area <= max_area:

                    if area > big_area:

                        big_area = area
                        big_cx = cx
                        big_cy = cy

    if big_cx is not None:

        hand_x = int(
            big_cx * frame_display.shape[1] / mask.shape[1]
        )

        hand_y = int(
            big_cy * frame_display.shape[0] / mask.shape[0]
        )

        pos_history.append(
            (hand_x, hand_y)
        )

        if len(pos_history) > 5:
            pos_history.pop(0)

        if len(pos_history) >= 2:

            old_x, old_y = pos_history[0]

            dx = hand_x - old_x
            dy = hand_y - old_y

            speed = math.sqrt(
                dx * dx + dy * dy
            )

        else:

            speed = 0

        shield_x = hand_x
        shield_y = hand_y

        prev_x = hand_x
        prev_y = hand_y
        
    new_objects = []

    for obj in objects:

        shield_hit = (
            abs(obj["x"] - shield_x) < 40 and
            abs(obj["y"] - shield_y) < 40
        )

        if shield_hit:

            if speed > parry_threshold:

                score += 1

            continue

        if obj["y"] > 550:

            hp -= 1

            continue

        new_objects.append(obj)

    objects = new_objects

    if hp <= 0:

        game_over = True

        pygame.mixer.music.stop()
        
    for obj in objects:

        if obj["type"] == "rock":

            overlay_image(
                frame_display,
                batu_img,
                obj["x"],
                obj["y"]
            )

        else:

            overlay_image(
                frame_display,
                api_img,
                obj["x"],
                obj["y"]
            )
            
    overlay_image(
        frame_display,
        shield,
        shield_x - 110,
        shield_y - 110
    )
    
    cv2.putText(
        frame_display,
        f"Score: {score}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,255,255),
        2
    )
    
    draw_hp(frame_display, hp)
    
    cv2.imshow(
        "Shield Deflector",
        frame_display
    )
    
    key = cv2.waitKey(1)

    if key == ord("q") :
        break



camera.release()

cv2.destroyAllWindows()

pygame.quit()
