import face_recognition
import cv2
import numpy as np

def recognitize(frame, face_locations):
    # Load a sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file("./min.png")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

    # obama_image2 = face_recognition.load_image_file("./jiny.png")
    # obama_face_encoding2 = face_recognition.face_encodings(obama_image2)[0]

    known_face_encodings = [
        obama_face_encoding,
        # obama_face_encoding2,
        # biden_face_encoding
    ]
    known_face_names = [
        "Minhyeok",
        # "jiny"
    ]

    # Initialize some variables
    face_encodings = []
    face_names = []

    face_encodings = face_recognition.face_encodings(frame, face_locations)   ########################

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    return face_names 

