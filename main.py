import numpy as np
import face_recognition as fr
import cv2

from simple_facerec import SimpleFacerec # import the SimpleFacerec module

#encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/") # Load face encoding from images in the "images/" folder

# load camera
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read() #read the frame from webcam
    
    face_locations, face_names = sfr.detect_known_faces(frame) #detect faces
    # Iterate over detected faces and their corresponding names
    for face_loc, name in  zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)  # Write the name above the face rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4) # Draw a rectangle around the detected face

    cv2.imshow("Frame", frame) #Display the frame 

    key = cv2.waitKey(1) # click on the esc key to exit
    if key == 27:
        break
video_capture.release()
cv2.destroyAllwindows()
#realease the webcam and destroy all the OpenCV Windows
