import cv2

img = cv2.imread("4friends.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = faces_cascade.detectMultiScale(gray)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(252, 186, 3),2)

cv2.imshow("FRIENDS",img)

cv2.waitKey(0)