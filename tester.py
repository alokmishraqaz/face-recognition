import cv2
import os
import numpy as np
import FaceRecognizer as fr

test_img = cv2.imread('C:\\Users\\Admin\\Desktop\\I-attendence\\recognize\\data\\87.jpg')
face_detected, gray_img = fr.faceDetection(test_img)
print("Face Detected : ", face_detected)

#face_recognizer = cv2.face.LBPHFaceRecognizer_create()
#face_recognizer.read('C:\\Users\\Admin\\Desktop\\I-attendence\\recognizetrainingData.yml')

faces, faceID = fr.labels_for_training_data('C:\\Users\\Admin\\Desktop\\I-attendence\\recognize\\data\\')
print(faces)
face_recognizer = fr.train_classifier(faces, faceID)

face_recognizer.save('C:\\Users\\Admin\\Desktop\\I-attendence\\recognizetrainingData.yml')
name = {0: 'Arjun', 1: 'Viral'}

for face in face_detected:
    (x, y, w, h) = face
    roi_gray = gray_img[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(roi_gray)
    print("Label : ", label, " Confidence : ", confidence)
    fr.draw_rect(test_img, face)
    predicted_name = name[0]
    fr.put_text(test_img, predicted_name, x, y)
    resized_img = cv2.resize(test_img, (700, 600))
    cv2.imshow("Face Detected", test_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    

#for (x,y,w,h) in face_detected:
#    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,255,255),1)
