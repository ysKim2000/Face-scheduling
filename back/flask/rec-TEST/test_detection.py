import face_recognition
import cv2
import numpy as np
from numpy.core.fromnumeric import size

def detect(rgb_small_frame):
    face_locations = []

    face_locations = face_recognition.face_locations(rgb_small_frame)
    return face_locations