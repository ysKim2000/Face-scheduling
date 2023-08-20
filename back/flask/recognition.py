from os import name
from face_recognition.face_recognition import api
import PIL.Image
import numpy as np

def recognition(img_to_check, known_names, known_face_encodings, tolerance=0.6, show_distance=False):
    unknown_image = api.load_image_file(img_to_check)
    
    if max(unknown_image.shape) > 1600:
        pil_img = PIL.Image.fromarray(unknown_image)
        pil_img.thumbnail((1600, 1600), PIL.Image.LANCZOS) #크기 조절 함수 (일정 비율 맞추어서)
        unknown_image = np.array(pil_img)
        
    unknown_encodings = api.face_encodings(unknown_image)
    
    for unknown_encoding in unknown_encodings:
        distances = api.face_distance(known_face_encodings, unknown_encoding)
        result = list(distances <= tolerance)
        
        if True in result:
            return {name : is_match  for is_match, name in zip(result, known_names) if is_match}
        else:
            return {}
