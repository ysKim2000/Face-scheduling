import numpy as np
from face_recognition.face_recognition import api
import os
import re
import matplotlib.pyplot as plt
def face_search(image):
    face_bounding_box = api.face_locations(image, model='hog')
    return face_bounding_box[0]

def image_files_in_folder(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if re.match(r'.*\.(jpg|jpeg|png)', f, flags=re.I)]

def face_detection_folder(folder):
    imgs = [api.load_image_file(file) for file in image_files_in_folder(folder)] 
    face_locations = [face_search(i) for i in imgs]
    detected_Faces = []
    
    for img in imgs:
        if face_locations:            
            for face in face_locations:
                img = np.array(img[face[0]: face[2], face[3]: face[1], :]).copy()
                detected_Faces.append(img)
                print('Face Image Shape : {}'.format(img.shape))
            
        else:
            print("얼굴이 검출되지 않았습니다.")
            return None

    return detected_Faces

def face_detection_img(img):
    face = face_search(img)
    img = np.array(img[face[0]: face[2], face[3]: face[1], :]).copy()
    print('Face Image Shape : {}'.format(img.shape))
    return img
