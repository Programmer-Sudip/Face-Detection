import face_recognition
import cv2
import numpy as np
import cv2
from google.colab.patches import cv2_imshow

face1 = face_recognition.load_image_file("elon.jpg")
face1_encoding = face_recognition.face_encodings(face1)[0]

face2 = face_recognition.load_image_file("Donald Trump.jpg")
face2_encoding = face_recognition.face_encodings(face2)[0]

face3 = face_recognition.load_image_file("jeffbezos.jpg")
face3_encoding = face_recognition.face_encodings(face3)[0]

face4 = face_recognition.load_image_file("sudip.jpeg")
face4_encoding = face_recognition.face_encodings(face4)[0]

face5 = face_recognition.load_image_file("P3.jpg")
face5_encoding = face_recognition.face_encodings(face5)[0]

known_face_encodings = [
    face1_encoding,
    face2_encoding,
    face3_encoding,
    face4_encoding,
    face5_encoding
]

known_face_names = [
    "Elon Musk",
    "Donald Trump",
    "Jeff Bezos",
    "Sudip",
    "Tiblu"
]





import cv2
from google.colab.patches import cv2_imshow
import face_recognition

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

# Process frames from the webcam
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Check if the frame was successfully captured
    if not ret:
        print("Error: Could not capture frame from webcam.")
        break  # Exit the loop if frame capture fails

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # ... (rest of your code remains the same)