import numpy as np
import face_recognition as fr
import cv2

video_capture = cv2.VideoCapture(0)

arun_image = fr.load_image_file("C://Users//dhanu//Downloads//arun.jpg")
arun_face_encoding = fr.face_encodings(arun_image)[0]

dhanush_image = fr.load_image_file("C://Users//dhanu//Downloads//dhanush.jpg")
dhanush_face_encoding = fr.face_encodings(dhanush_image)[0]

known_face_encodings = [arun_face_encoding, dhanush_face_encoding]
known_face_names = ["Arun", "Dhanush"]

while True:
    ret, frame = video_capture.read()

    rgb_frame = frame[:,:,::-1]

    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        matches = fr.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown Face"

        face_distances = fr.face_distance(known_face_encodings, face_encoding)

        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom-35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left +6, bottom-6), font, 1.0, (255, 0, 0), 1)

    cv2.imshow('Face_rec', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

video_capture.release()
cv2.destroyAllWindows() 
