from scipy.spatial import distance

def calculate_mar(landmarks):
    A = distance.euclidean(landmarks[50], landmarks[58])
    B = distance.euclidean(landmarks[52], landmarks[56])
    C = distance.euclidean(landmarks[48], landmarks[54])
    mar = (A + B) / (2.0 * C)
    return mar
