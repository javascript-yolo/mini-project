import tkinter as tk
import numpy as np
import face_recognition
from datetime import *
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
import cv2
import os

window=tk.Tk()
window.title("Face recognition system")
window.configure(background="black")

logo = Image.open("0001.png")
logo = logo.resize((50, 47), Image.ANTIALIAS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="black",)
l1.place(x=800, y=10)

titl = tk.Label(
    window, text="Smart College!!", bg="black", fg="green", font=("arial", 27),
)
titl.place(x=875, y=12)


a = tk.Label(
    window,
    text="Welcome to the Face Recognition Based\nAttendance Management System",
    bg="black",
    fg="yellow",
    bd=10,
    font=("arial", 35),
)
a.pack()

ri = Image.open("verifyy.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=300, y=400)

ai = Image.open("aa.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=640, y=400)

vi = Image.open("attendance.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=960, y=400)

qi = Image.open("register.png")
q = ImageTk.PhotoImage(qi)
label4 = Label(window, image=q)
label4.image = q
label4.place(x=1370, y=400)

def entry():
    def Final_csv(file_name):
        f = pd.read_csv(file_name)
        f = f.drop_duplicates(subset=['Name'])
        f.to_csv(file_name, index=False)

    def findEncodings(images):
        encodeList = []

        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markTIMEentry(name, Win_name):
        print("marking entry")
        Win_name += '.csv'
        with open(Win_name, 'r+') as f:
            myDataList = f.readlines()

            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
                if name not in nameList:
                    now = datetime.now()
                    dtString = now.strftime('%H:%M:%S')
                    f.writelines(f'\n{name},{dtString}')

    def cameraENTRY(img, Win_name):
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
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markTIMEentry(name, "ENTRY")

        cv2.imshow(Win_name, img)

    path = 'Training_images'

    images = []
    classNames = []
    myList = os.listdir(path)
    print("my list", myList)

    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print("classnames", classNames)
    print("images", images)
    nameList = []

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()

        cameraENTRY(img, 'ENTRY')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("calling final csv")
    Final_csv("ENTRY.csv")

    cap.release()
    cv2.destroyAllWindows()


b1 = tk.Button(window, text="Entry", font=("Algerian", 20), bg='black', fg='yellow',bd=5, command=entry)
b1.place(relx=0.18,rely=0.6)

def exit():
  def Final_csv(file_name):
    f = pd.read_csv(file_name)
    f = f.drop_duplicates(subset=['Name'])
    f.to_csv(file_name, index=False)


  
