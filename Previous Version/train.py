from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x700+400+50")
        self.root.title("Log-Detect: Training")
        self.root.resizable(False, False)
        self.root.configure(bg='gray10')
        self.root.iconbitmap(r"Assets\Log.ico")

        # TRAIN BUTTON
        Train_Btntn = Button(root, cursor="hand2", text="TRAIN", command=self.train_classifier, font=("Bebas Neue", 25),bg="gray8", fg="gray85", relief=FLAT, activebackground="gray10", activeforeground="gray50")
        Train_Btntn.place(x=250, y=300, width=200, height=50)

    def train_classifier(self):
        data_dir = ("FaceData")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            #cv2.imshow("Traning", imageNp)
            #cv2.waitKey(1) == 13

        ids = np.array(ids)

        # TRAIN THEN SAVE

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        #cv2.destroyAllWindows()
        messagebox.showinfo("Log-Detect: Training", "Training datasets completed!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()