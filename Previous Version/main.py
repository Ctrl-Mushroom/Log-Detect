from tkinter import *
#from tkinter import ttk
from PIL import Image, ImageTk
import os
from registration import Registration
from train import Train
from recognize import Recognizer
from attendance import Attendance
import tkinter as tk
import tkinter.messagebox

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x450+210+150")
        self.root.title("Log-Detect: A Facial Recognition Logbook System")
        self.root.resizable(False, False)
        self.root.configure(bg='gray10')
        self.root.iconbitmap(r"Assets\Log.ico")



        # LOGO
        Logo = Image.open(r"Assets\Logo.png")
        Logo = Logo.resize((498, 255), Image.ANTIALIAS)
        self.LogoImg = ImageTk.PhotoImage(Logo)

        Logo_Banner = Label(self.root, image=self.LogoImg, bg="gray10")
        Logo_Banner.place(x=101, y=50, width=498, height=255)

        # REGISTRATION
        Student_Btntn = Button(root, cursor="hand2", text="REGISTER", command=self.Registration,font=("Bebas Neue", 25), bg="gray8", fg="gray85", relief=FLAT, activebackground="gray10",
                               activeforeground="gray50")
        Student_Btntn.place(x=700, y=65, width=350, height=50)

        # STUDENT DATA
        Student_Btntn = Button(root, cursor="hand2", text="STUDENT DATA", command=self.Student_Data,
                               font=("Bebas Neue", 25), bg="gray8", fg="gray85", relief=FLAT, activebackground="gray10",
                               activeforeground="gray50")
        Student_Btntn.place(x=700, y=115, width=350, height=50)

        # TRAIN
        Train_Btntn = Button(root, cursor="hand2", text="TRAIN DATASET", command=self.Train, font=("Bebas Neue", 25),
                             bg="gray8", fg="gray85", relief=FLAT, activebackground="gray10", activeforeground="gray50")
        Train_Btntn.place(x=700, y=165, width=350, height=50)

        # FACE RECOG
        Recognize_Btntn = Button(root, cursor="hand2", text="FACE RECOGNIZER", command=self.Recognize,
                                 font=("Bebas Neue", 25), bg="gray8", fg="gray85", relief=FLAT,
                                 activebackground="gray10", activeforeground="gray50")
        Recognize_Btntn.place(x=700, y=215, width=350, height=50)

        # ATTENDANCE
        Attendance_Btntn = Button(root, cursor="hand2", text="LOGBOOK", command=self.Attendance,
                                  font=("Bebas Neue", 25), bg="gray8", fg="gray85", relief=FLAT,
                                  activebackground="gray10", activeforeground="gray50")
        Attendance_Btntn.place(x=700, y=265, width=350, height=50)

        # Logout
        EXIT_Btntn = Button(root, cursor="hand2", text="Log out", font=("Bebas Neue", 25), command=self.logout, bg="gray8", fg="gray85",
                            relief=FLAT, activebackground="gray10", activeforeground="gray50")
        EXIT_Btntn.place(x=700, y=315, width=350, height=50)


        # BUTTON FUNCTIONS

    def Registration(self):
        self.new_window = Toplevel(self.root)
        self.app = Registration(self.new_window)

    def Student_Data(self):
        os.startfile("FaceData")

    def Train(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def Recognize(self):
        self.new_window = Toplevel(self.root)
        self.app = Recognizer(self.new_window)

    def Attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def logout(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to Log out:", parent=self.root)
        if self.iExit > 0:
            root.withdraw()
            os.system("login.py")
        else:
            return




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    # Start Maximized
    # root.state("zoomed")
    root.mainloop()



