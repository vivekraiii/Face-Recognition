import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
path='images'
images=[]
classnames=[]
mylist=os.listdir(path)
for clas in mylist:
    curimg=cv2.imread(f'{path}/{clas}')
    images.append(curimg)
    classnames.append(clas.split(".")[0])

print(classnames)

def encodings(images):
    encodelist=[ ]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encoding=face_recognition.face_encodings(img)[0]
        encodelist.append(encoding)

        # for items in encoding:
        #     encodelist.append(items)
    return encodelist


def markattendance(name):
    with open("Attendence.csv","r++") as f:
        mydatalist=f.readlines()
        namelist=[]
        for line in mydatalist:
            entry=line.split(",")
            namelist.append(entry[0])
        if name not in namelist:
            now=datetime.now()
            dtstring=now.strftime("%H:%M:%S")
            f.writelines(f'\n{name},{dtstring}')
        








encodelistknown=encodings(images)
print(type(encodelistknown))
print(type(encodelistknown[0]))
print("Encoding Complete")


cap=cv2.VideoCapture(0)
while True:
    success,frames=cap.read()
    imgs=cv2.resize(frames,(0,0),None,0.25,0.25)
    imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

    faceframe=face_recognition.face_locations(imgs)
    encoding=face_recognition.face_encodings(imgs,faceframe)



    for encodeface,faceloc in zip(encoding,faceframe):
        matches=face_recognition.compare_faces(encodelistknown,encodeface)
        facedis=face_recognition.face_distance(encodelistknown,encodeface)
        matchindex=np.argmin(facedis)
        if matches[matchindex]:
            name=classnames[matchindex].upper()
            print(name)
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(frames,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(frames,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(frames,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markattendance(name)





    cv2.imshow('frame',frames)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cap.release()

    






