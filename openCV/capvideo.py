import cv2

vid = cv2.VideoCapture(0)

base_frame = None


while True:
    check, frame = vid.read()

    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey_frame = cv2.GaussianBlur(grey_frame,(21,21),0)
    if base_frame is None:
        base_frame = grey_frame
        continue

    diff = cv2.absdiff(base_frame, grey_frame)

    threshold = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]

    threshold = cv2.dilate(threshold, None, iterations=2)

    (cnts,_) = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 9000:
            continue
        else:
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    cv2.imshow("diff", diff)
    cv2.imshow("final-re", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

vid.release()

cv2.destroyAllWindows()

