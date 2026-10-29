import cv2

img = cv2.imread("boy.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(gray)

print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(203,192,255),2)
    # Corte da imagem para salvar imagem do rosto
    cut_face = img[y:y+h,x:x+w]
    cv2.imwrite("face.jpg",cut_face)

cv2.imshow("IMAGE",img)

cv2.waitKey(0)