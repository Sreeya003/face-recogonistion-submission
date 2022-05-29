import numpy as np
import face_recognition as fr
import cv2

from simple_facerec import SimpleFacerec

#encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# load camera
video_capture = cv2.VideoCapture(0)




while True:
    ret, frame = video_capture.read()


    #detect faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in  zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
video_capture.release()
cv2.destroyAllwindows()
