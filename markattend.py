import cv2
import os
import numpy as np
import FaceRecognizer as fr
import requests

confidence=1000
def recognize(file,conn,fac_id,time,subject,sem):

    test_img = cv2.imread('C:\\Users\\Admin\\Desktop\\I-attendence\\attendence\\'+file+'.jpg')
    face_detected, gray_img = fr.faceDetection(test_img)
    print("Face Detected : ", face_detected)

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('C:\\Users\\Admin\\Desktop\\I-attendence\\recognize\\trainedyml\\'+file+'.yml')

    print(fac_id,"----------------------")
    print(file,"********************")
    for face in face_detected:
        userdata = {"facid": fac_id, "data": file,"time":time,"subject":subject,"semester":sem}
        resp = requests.post('http://127.0.0.1/attendence/student_attendence.php', params=userdata)
        print(resp,userdata)

        (x, y, w, h) = face
        roi_gray = gray_img[y:y+h, x:x+w]
        label, confidence = face_recognizer.predict(roi_gray)
        global confident
        confident=confidence
        print("Label : ", label, " Confidence : ", confidence)
        b = bytes(repr(confidence), 'utf-8')
        conn.send(b)
        fr.draw_rect(test_img, face)
        predicted_name = file
        fr.put_text(test_img, predicted_name, x, y)
        resized_img = cv2.resize(test_img, (700, 600))
        #cv2.imshow("Face Detected", test_img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
    
#for (x,y,w,h) in face_detected:
#    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,255,255),1)
