from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Recognizer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x700+400+50")
        self.root.title("Log-Detect: Face Recognition")
        self.root.resizable(False, False)
        self.root.configure(bg='gray10')
        self.root.iconbitmap(r"Assets\Log.ico")

        # RECOGNIZE BUTTON
        Recognize_Btntn = Button(root, cursor="hand2", text="RECOG", command=self.face_recog, font=("Bebas Neue", 25),
                                 bg="gray8", fg="gray85", relief=FLAT, activebackground="gray10",
                                 activeforeground="gray50")
        Recognize_Btntn.place(x=250, y=300, width=200, height=50)

    # ATTENDACE FUNCTION
    # def mark_attendance(self, db_EntryNum, db_Course, db_Name, db_Year):
    #     with open("Attendance.csv","r+",newline="\n") as f:
    #         myDataList=f.readlines()
    #         name_list=[]
    #         for line in myDataList:
    #             entry=line.split((","))
    #             name_list.append(entry[0])
    #         if((db_EntryNum not in name_list) and (db_Course not in name_list) (db_Name not in name_list) (db_Year not in name_list)):
    #             now=datetime.now()
    #             d1=now.strftime("%d/%m/%Y")
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{db_EntryNum},{db_Course},{db_Name},{db_Year},{dtString},{d1},Preset")

    def mark_attendance(self, i, r, n, d):
        with open("LogDetect.csv ", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%b %d %Y")
                dtString = now.strftime('%I:%M:%S %p')
                f.writelines(f"\n{i},{d},{r},{n},{d1},{dtString},Preset")

    # RECOGNITION FUNCTION
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Admin123",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()

                # my_cursor.execute("select surname from registration where student_num="+str(id))
                # db_Name = my_cursor.fetchone()
                # db_Name = "+".join(db_Name)

                # my_cursor.execute("select course from registration where student_num="+str(id))
                # db_Course = my_cursor.fetchone()
                # db_Course = "+".join(db_Course)

                # my_cursor.execute("select year_sec from registration where student_num="+str(id))
                # db_Year = my_cursor.fetchone()
                # db_Year = "+".join(db_Year)

                # my_cursor.execute("select student_num from registration where student_num="+str(id))
                # db_EntryNum = my_cursor.fetchone()
                # db_EntryNum = "+".join(db_EntryNum)

                my_cursor.execute("Select first_name from face_recog where student_num=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("Select Surname from face_recog where student_num=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("Select Department from face_recog where student_num=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("Select StudentNo from face_recog where student_num=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                #my_cursor.execute("Select Student_No from face_recog where student_num=" + str(id))
                #i = my_cursor.fetchone()
                #i = "+".join(i)



                if confidence > 50:
                    # cv2.putText(img,f"Num:{db_EntryNum}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    # cv2.putText(img,f"Course:{db_Course}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    # cv2.putText(img,f"Surname:{db_Name}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    # cv2.putText(img,f"Yr&Sec:{db_Year}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    # self.mark_attendance(db_EntryNum, db_Course, db_Name, db_Year)
                    cv2.putText(img, f"ID:{i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Surname:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"First Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    self.mark_attendance(i, r, n, d,)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face?", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img


        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            resize=cv2.resize(img, (0,0), fx=1.8, fy=1.5)

            cv2.imshow("Log-Detect: Face Recognition", resize)


            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()















if __name__ == "__main__":
    root = Tk()
    obj = Recognizer(root)
    root.mainloop()