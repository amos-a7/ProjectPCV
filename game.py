import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    frame = cv2.flip(frame, 1)
    
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    mask = np.zeros(hsv_frame.shape[:2], dtype=np.uint8)
    
    
    H = hsv_frame[:, :, 0]
    S = hsv_frame[:, :, 1]
    V = hsv_frame[:, :, 2]
    
   
    kondisi_h = (H >= lower_skin[0]) & (H <= upper_skin[0])
    kondisi_s = (S >= lower_skin[1]) & (S <= upper_skin[1])
    kondisi_v = (V >= lower_skin[2]) & (V <= upper_skin[2])
    
    
    kulit_terdeteksi = kondisi_h & kondisi_s & kondisi_v
    
    
    mask[kulit_terdeteksi] = 255
  
    
    
    cv2.imshow('Layar Asli', frame)
    cv2.imshow('Hasil Masking NumPy', mask)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()