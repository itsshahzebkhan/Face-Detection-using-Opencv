# step 1 - download haarcascade_frontalface_default.xml file from GitHub.com (link to the file - https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
# step 2 - place the downloaded file into your project folder, next to your main.py file
# step 3 - now start coding
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)
while True:
    _,img=webcam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow("Face detection", img)
    key = cv2.waitKeyEx(10)
    if key == 27:
        break
# note - in order to stop and close your webcam, press the "escape" key on your keyboard
webcam.release()
cv2.destroyAllWindows()