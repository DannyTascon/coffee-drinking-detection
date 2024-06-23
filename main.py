import cv2
import pygame
import time
from detector import get_face_landmarks
from utils import calculate_mar
from config import MAR_THRESHOLD, DURATION_THRESHOLD, SOUND_FILE

pygame.mixer.init()
sound = pygame.mixer.Sound(SOUND_FILE)

cap = cv2.VideoCapture(0)
is_drinking = False
is_paused = False
start_time = 0
drink_count = 0  # Counter for the number of times drinking is detected

while True:
    if not is_paused:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces, landmarks_list = get_face_landmarks(gray)
        
        for landmarks in landmarks_list:
            mar = calculate_mar(landmarks)
            print(f"MAR: {mar}")  # Debug: print the Mouth Aspect Ratio (MAR)
            
            if mar > MAR_THRESHOLD:  # Check if MAR exceeds the threshold
                if not is_drinking:
                    start_time = time.time()  # Start the timer
                    is_drinking = True
                    print("Started drinking timer")
                elif time.time() - start_time >= DURATION_THRESHOLD:
                    print("Drinking coffee detected!")
                    sound.play()
                    is_drinking = False  # Reset the drinking flag to avoid repeated alerts
                    drink_count += 1  # Increment the counter
            else:
                if is_drinking:
                    print("Stopped drinking timer")
                is_drinking = False
            
            # Draw the mouth landmarks for visualization
            for (x, y) in landmarks[48:60]:
                cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)
            
            # Draw a rectangle around the face for visualization
            for face in faces:
                cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 2)
        
        cv2.imshow('frame', frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('p'):
        is_paused = not is_paused
        if is_paused:
            print(f"Number of times drinking coffee detected: {drink_count}")

cap.release()
cv2.destroyAllWindows()

