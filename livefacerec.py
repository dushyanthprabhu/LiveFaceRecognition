import face_recognition
#from PIL import Image, ImageDraw
import cv2
import os
#import numpy
import speak as spk
known_face_encodings = []
kfe=[]
nameL=[]
def faceencoding():

    for path,subdir,fname in os.walk(directory):
        for f in fname:
            img_path=os.path.join(path,f)
            img = face_recognition.load_image_file(img_path)
            face_encoding = face_recognition.face_encodings(img)[0]
            known_face_encodings.append(face_encoding)
        return  known_face_encodings


known_face_names = [
  "Monisha",
  "Vasu",
  "Reona",
  "Riya",
  "Dushyanth",
  "Raghav"
]

directory="C:/Users/asus/Desktop/face_recognition_examples-master/img/new"
kfe=faceencoding()


cam=cv2.VideoCapture(0)

while True:
    rect,test_image=cam.read()
    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)
    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(kfe, face_encoding)

        name = "Unknown Person"
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            #print(name)
        if name=="Unknown Person":
            spk.tts("sorry I do not recognize you" )
        else:
            if name not in nameL:   
                spk.tts("hello  "+name)
                nameL.append(name)
                print(name)
cam.release()

