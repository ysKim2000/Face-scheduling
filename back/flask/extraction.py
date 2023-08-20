import cv2
import dlib
import numpy as np, os, pickle

path = './'
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
model = dlib.face_recognition_model_vl('dlib_face_recognition_resnet_model_v1.dat')
FACE_DESC = []
FACE_NAME = []
for fn in os.listdir(path):
	if fn.endswith('.jpg'):
		img = cv2.imread(path + fn)[:,:,::-1]
		dets = detector(img, 1)
		for k, d in enumerate(dets):
			shape = sp(img, d)
			face_desc = model.compute_face_descriptor(img, shape, 1)
			FACE_DESC.append(face_desc)
			print('loading...', fn)
			FACE_NAME.append(fn[:fn.index('_')])
pickle.dump((FACE_DESC, FACE_NAME), open('trainset.pk', 'wb'))
