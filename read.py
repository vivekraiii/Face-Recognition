import cv2 as cv
import datetime
img= cv.imread("D:\OpenCV\image\vk1.jpg")

cv.imshow("Cheemss",img)
cv.waitKey(0)
cv.destroyAllWindows()

# import face_recognition
# cap=cv2.VideoCapture(0)
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# cap.set(3,3000)
# cap.set(4,4000)
# print(cap.get(3))
# print(cap.get(4))
# while(True):
#     ret,frame=cap.read()
#     font=cv2.FONT_HERSHEY_SIMPLEX
#     text="Width: "+str(cap.get(3))+"Height: "+str(cap.get(4))
#     date=str(datetime.datetime.now())
#     cv2.putText(frame,date,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
    
#     cv2.imshow('frame',frame)

#     if cv2.waitKey(1) & 0xff==ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
