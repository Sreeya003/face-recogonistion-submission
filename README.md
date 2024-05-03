This Python face recognition system uses OpenCV and the face_recognition module to recognize faces in real-time through a camera stream. Initializing the model with a custom class called SimpleFacerec, the system imports and encodes face photos, detects frames, matches observed faces against known encoded faces, and identifies detected faces using bounding boxes and relevant names.

**Steps to run the code and the work process:**

1)Install the required libraries.

2)Create a folder and upload the jpg or png files of the person along with the name to be displayed as the file name.

3)Run the code using the command prompt.

4)The web cam will open and start capturing video frames.

5)It enters a loop that continuously takes video frames from the camera.

6)It extracts the location and name of each detected face, then labels the rectangle surrounding the face with the extracted information.

7)It shows the updated frame with face rectangles and labels.

8)The execution stops when we enter the esc key.
