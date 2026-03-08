import cv2

cam = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('Classifiers/haarcascade_frontalface_default.xml')

face_id = input('\n Enter user id: ')
count = 0

while True:

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('image', img)

    k = cv2.waitKey(1) & 0xff

    # SPACE key press panna capture aagum
    if k == 32:
        for (x,y,w,h) in faces:
            count += 1
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg",
                        gray[y:y+h,x:x+w])
            print("Image captured:", count)

    elif k == 27:
        break

    if count >= 15:
        break

cam.release()
cv2.destroyAllWindows()