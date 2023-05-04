import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import streamlit as st
import pandas as pd

def findEncodings(images):
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

def main():
    st.set_page_config(page_title="Face Recognition Attendance System",
                       page_icon=":guardsman:",
                       layout="wide")

    st.title("Face Recognition Attendance System")
    st.markdown("---")

    # select training images folder
    st.sidebar.subheader("Select training images folder")
    folder_path = st.sidebar.text_input("Enter folder path", "Training_images")
    if not os.path.isdir(folder_path):
        st.error(f"{folder_path} is not a valid directory!")
        return
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if not image_files:
        st.error(f"No image files found in {folder_path}!")
        return

    images = []
    classNames = []
    for cl in image_files:
        curImg = cv2.imread(cl)
        images.append(curImg)
        classNames.append(os.path.splitext(os.path.basename(cl))[0])
    encodeListKnown = findEncodings(images)
    st.sidebar.success(f"{len(images)} images found in {folder_path}")

    # start and stop webcam
    st.sidebar.markdown("---")
    st.sidebar.subheader("Webcam")
    start = st.sidebar.checkbox("Start webcam")
    if start:
        cap = cv2.VideoCapture(0)
    else:
        return

    # create attendance log
    log_path = "attendance.csv"
    if not os.path.exists(log_path):
        with open(log_path, 'w') as f:
            f.write("Name,Time\n")
    st.sidebar.success("Attendance log created")
    

    

    # face recognitionstreamlit 
    st.markdown("---")
    st.header("Face Recognition")

    while start:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)

        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
