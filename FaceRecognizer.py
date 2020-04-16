import cv2
import os
import numpy as np


def faceDetection(test_img):
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('C:\\Users\\Admin\\Desktop\\I-attendence\\recognize\\haarcascade_frontalface_alt.xml')
    faces = face_cascade.detectMultiScale(gray_img, 1.20, 3)
    
    return faces, gray_img

i=0
def labels_for_training_data(directory):
    faces = []
    faceID = []

    for path, subdirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith('.'):
                print("Skipping system file...")
                continue
            id = os.path.basename(path)
            print(path,"  ========")
            print(id)
            img_path = os.path.join(path, filename)
            print("id : ", id, "img_path : ", img_path)
            test_img = cv2.imread(img_path)
            if test_img is None:
                print("can not load image properly...")
                continue
            faces_rect, gray_img = faceDetection(test_img)
            if len(faces_rect) != 1:
                continue
            (x, y, w, h) = faces_rect[0]
            roi_gray = gray_img[y: y+h, x: x+w]
            faces.append(roi_gray)
            global i
            faceID.append(int(i))
            i=i+1
    return faces, faceID


def train_classifier(faces, faceID):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(faceID))
    return face_recognizer


def draw_rect(test_img, face):
    (x, y, w, h) = face
    cv2.rectangle(test_img, (x, y), (x+w, y+h), (255, 0, 0), 3)


def put_text(test_img, text, x, y):
    cv2.putText(test_img, text, (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
