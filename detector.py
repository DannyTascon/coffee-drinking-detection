import dlib
import numpy as np

# Load the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def get_face_landmarks(gray_frame):
    faces = detector(gray_frame)
    landmarks_list = []
    for face in faces:
        landmarks = predictor(gray_frame, face)
        landmarks_list.append(np.array([(p.x, p.y) for p in landmarks.parts()]))
    return faces, landmarks_list
