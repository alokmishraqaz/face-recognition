import cv2
import os
import numpy as np
import FaceRecognizer as fr



#face_recognizer = cv2.face.LBPHFaceRecognizer_create()
#face_recognizer.read('C:\\Users\\Admin\\Desktop\\I-attendence\\recognizetrainingData.yml')

def train(file):
    print('C:\\Users\\Admin\\Desktop\\I-attendence\\recognize\\data\\'+file+'\\')
    faces, faceID = fr.labels_for_training_data('C:\\Users\\Admin\\Desktop\\I-attendence\\recognize\\data\\'+file+'\\')
    print(faces)
    face_recognizer = fr.train_classifier(faces, faceID)

    face_recognizer.save('C:\\Users\\Admin\\Desktop\\I-attendence\\recognize\\trainedyml\\'+file+'.yml')
    print('C:\\Users\\Admin\\Desktop\\I-attendence\\recognize\\data\\' + file + '\\')

