import cv2

img = cv2.imread("avatar.jpg")

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_detected = face_cascade.detectMultiScale(img,
                                              scaleFactor=1.3,
                                              minNeighbors=8)

for x, y , w, h in face_detected:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

resize_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("img", resize_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

