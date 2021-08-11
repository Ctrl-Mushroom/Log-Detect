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
from tkinter import messagebox
import mysql.connector

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x450+210+150")
        self.root.title("Log-Detect: A Facial Recognition Logbook System")
        self.root.resizable(False, False)
        self.root.configure(bg='gray10')
        self.root.iconbitmap(r"Assets\Log.ico")

        self.var_username = StringVar()
        self.var_password = StringVar()

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_regpass = StringVar()
        self.var_confpass = StringVar()


        bg_img = Label(self.root,bg="gray10", fg="gray10", bd=0, relief=RIDGE )
        bg_img.place(x=100, y=30, width=900, height=390)


        def user_click(event):
            if txt_user.get()=="Email":
                txt_user.delete(0, END)
                txt_user.config(justify='left')

        def user_click1(event):
            if txt_user.get()=="":
                txt_user.insert(0, "Email")
                txt_user.config(justify='center')

        def pass_click(event):
            if txt_pass.get() == "Password":
                txt_pass.delete(0, END)
                txt_pass.config(show="*")
                txt_pass.config(justify='left')


        def pass_click1(event):
            if txt_pass.get() == "":
                txt_pass.config(show="")
                txt_pass.insert(0, "Password")
                txt_pass.config(justify='center')

        ##
        btnl_Login = Frame(bg_img, bd=0, bg="gray40", relief=RIDGE,)
        btnl_Login.place(x=280, y=240)
        btn_login = Button(btnl_Login, text="Log In",cursor="hand2", font=("Bebas Neue", 15, "bold"),fg="white", bg='black', relief=FLAT, activebackground="gray10",activeforeground="gray50", width=25, command=self.logIn)
        btn_login.grid(row=0, column=0, pady=3, padx=3)

        ##
        btn_Create = Frame(bg_img, bd=0, bg="gray40", relief=RIDGE, )
        btn_Create.place(x=305, y=300)
        btn_createacc = Button(btn_Create, text="Create New Account", font=("Bebas Neue", 15, "bold"),fg="white", bg='black', relief=FLAT, activebackground="gray10",activeforeground="gray50", width=20, command=self.register)
        btn_createacc.grid(row=0, column=0, pady=3, padx=3)

        ##
        main_user = Frame(bg_img, bd=2, bg="gray12",relief=RIDGE)
        main_user.place(x=280, y=50)
        txt_user = Entry(main_user, font=("Bebas Neue", 20), width=20, textvariable=self.var_username, relief=FLAT, justify='center')
        txt_user.grid(row=0, column=0, pady=5, padx=3)
        txt_user.insert(0, "Email")
        txt_user.bind("<FocusIn>", user_click)
        txt_user.bind("<FocusOut>", user_click1)
        ##
        main_pass = Frame(bg_img, bd=2, bg="gray12", relief=RIDGE)
        main_pass.place(x=280, y=120)
        txt_pass = Entry(main_pass, font=("Bebas Neue", 20), width=20, textvariable=self.var_password, relief=FLAT, justify='center')
        txt_pass.grid(row=0, column=0, pady=5, padx=3)
        txt_pass.insert(0, "Password")
        txt_pass.bind("<FocusIn>", pass_click)
        txt_pass.bind("<FocusOut>", pass_click1)
#######################################################################################
    def closewindow(self):

        bg_img = Label(self.root, bg="gray10", fg="gray10", bd=0, relief=RIDGE)
        bg_img.place(x=100, y=30, width=900, height=390)

        def user_click(event):
            if txt_user.get() == "Email":
                txt_user.delete(0, END)
                txt_user.config(justify='left')

        def user_click1(event):
            if txt_user.get() == "":
                txt_user.insert(0, "Email")
                txt_user.config(justify='center')

        def pass_click(event):
            if txt_pass.get() == "Password":
                txt_pass.delete(0, END)
                txt_pass.config(show="*")
                txt_pass.config(justify='left')

        def pass_click1(event):
            if txt_pass.get() == "":
                txt_pass.config(show="")
                txt_pass.insert(0, "Password")
                txt_pass.config(justify='center')

        ##
        btnl_Login = Frame(bg_img, bd=0, bg="gray40", relief=RIDGE, )
        btnl_Login.place(x=280, y=240)
        btn_login = Button(btnl_Login, text="Log In", cursor="hand2", font=("Bebas Neue", 15, "bold"), fg="white",
                           bg='black', relief=FLAT, activebackground="gray10", activeforeground="gray50", width=25,
                           command=self.logIn)
        btn_login.grid(row=0, column=0, pady=3, padx=3)

        ##
        btn_Create = Frame(bg_img, bd=0, bg="gray40", relief=RIDGE, )
        btn_Create.place(x=305, y=300)
        btn_createacc = Button(btn_Create, text="Create New Account", font=("Bebas Neue", 15, "bold"), fg="white",
                               bg='black', relief=FLAT, activebackground="gray10", activeforeground="gray50", width=20,
                               command=self.register)
        btn_createacc.grid(row=0, column=0, pady=3, padx=3)

        ##
        main_user = Frame(bg_img, bd=2, bg="gray12", relief=RIDGE)
        main_user.place(x=280, y=50)
        txt_user = Entry(main_user, font=("Bebas Neue", 20), width=20, textvariable=self.var_username, relief=FLAT,
                         justify='center')
        txt_user.grid(row=0, column=0, pady=5, padx=3)
        txt_user.insert(0, "Email")
        txt_user.bind("<FocusIn>", user_click)
        txt_user.bind("<FocusOut>", user_click1)
        ##
        main_pass = Frame(bg_img, bd=2, bg="gray12", relief=RIDGE)
        main_pass.place(x=280, y=120)
        txt_pass = Entry(main_pass, font=("Bebas Neue", 20), width=20, textvariable=self.var_password, relief=FLAT,
                         justify='center')
        txt_pass.grid(row=0, column=0, pady=5, padx=3)
        txt_pass.insert(0, "Password")
        txt_pass.bind("<FocusIn>", pass_click)
        txt_pass.bind("<FocusOut>", pass_click1)

##########################################################################################
    def logIn(self):
        if self.var_username.get()=="Email" or self.var_password.get()=="Password":
            messagebox.showerror("Log-Detect: A Facial Recognition Logbook System","Email or Password is Incorrect",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Admin123",
                    database="face_recognizer"
                )
                mycursor = conn.cursor()
                sql = "SELECT Email and Password FROM register WHERE Email = %s AND Password = %s "
                mycursor.execute(sql, (self.var_username.get(), self.var_password.get()))

                if mycursor.fetchall():
                    self.mainwindow()

                else:
                    messagebox.showinfo("Log-Detect: A Facial Recognition Logbook System","Email or Password is Incorrect", parent=self.root)


            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

###########################################################3

    def mainwindow(self):
        # LOGO
        bg_img1 = Label(self.root, bg="gray10", fg="gray10", bd=0, relief=RIDGE)
        bg_img1.place(x=1, y=1, width=1099, height=400)


        Logo = Image.open(r"Assets\Logo.png")
        Logo = Logo.resize((498, 255), Image.ANTIALIAS)
        self.LogoImg = ImageTk.PhotoImage(Logo)

        Logo_Banner = Label(bg_img1, image=self.LogoImg, bg="gray10")
        Logo_Banner.place(x=101, y=50, width=498, height=255)

        # REGISTRATION
        Student_Btntn = Button(bg_img1, cursor="hand2", text="REGISTER", command=self.Registration,font=("Bebas Neue", 25), bg="gray8", fg="gray85", relief=FLAT, activebackground="gray10",activeforeground="gray50")
        Student_Btntn.place(x=700, y=65, width=350, height=50)

        # STUDENT DATA
        Student_Btntn = Button(bg_img1, cursor="hand2", text="STUDENT DATA", command=self.Student_Data,
                               font=("Bebas Neue", 25), bg="gray8", fg="gray85", relief=FLAT, activebackground="gray10",
                               activeforeground="gray50")
        Student_Btntn.place(x=700, y=115, width=350, height=50)

        # TRAIN
        Train_Btntn = Button(bg_img1, cursor="hand2", text="TRAIN DATASET", command=self.Train, font=("Bebas Neue", 25),
                             bg="gray8", fg="gray85", relief=FLAT, activebackground="gray10", activeforeground="gray50")
        Train_Btntn.place(x=700, y=165, width=350, height=50)

        # FACE RECOG
        Recognize_Btntn = Button(bg_img1, cursor="hand2", text="FACE RECOGNIZER", command=self.Recognize,
                                 font=("Bebas Neue", 25), bg="gray8", fg="gray85", relief=FLAT,
                                 activebackground="gray10", activeforeground="gray50")
        Recognize_Btntn.place(x=700, y=215, width=350, height=50)

        # ATTENDANCE
        Attendance_Btntn = Button(bg_img1, cursor="hand2", text="LOGBOOK", command=self.Attendance,font=("Bebas Neue", 25), bg="gray8", fg="gray85", relief=FLAT, activebackground="gray10", activeforeground="gray50")
        Attendance_Btntn.place(x=700, y=265, width=350, height=50)

        # Logout
        EXIT_Btntn = Button(bg_img1, cursor="hand2", text="Log out", font=("Bebas Neue", 25), command=self.logout, bg="gray8", fg="gray85", relief=FLAT, activebackground="gray10", activeforeground="gray50")
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
        self.iExit = tkinter.messagebox.askyesno("Log-Detect: A Facial Recognition Logbook System", "Are you sure you want to log out?", parent=self.root)
        if self.iExit > 0:
            root.withdraw()
            os.system("login.py")
        else:
            return

###############################################################3#########################################################

    def register(self):
        # LOGO

        bg_img2 = Label(self.root, bg="gray10", fg="gray10", bd=0, relief=RIDGE)
        bg_img2.place(x=1, y=1, width=1099, height=400)

        bg_img3 = Label(bg_img2, bg="gray10", fg="gray10", bd=2, relief=RIDGE)
        bg_img3.place(x=150, y=30, width=800, height=371)

########################################
        def user_lname(event):
            if txt_lname.get()=="Surname":
                txt_lname.delete(0, END)
                txt_lname.config(justify='left')

        def user_lname1(event):
            if txt_lname.get()=="":
                txt_lname.insert(0, "Surname")
                txt_lname.config(justify='center')

        main_lname = Frame(bg_img2, bd=2, bg="gray12", relief=RIDGE)
        main_lname.place(x=220, y=80)
        txt_lname = Entry(main_lname, font=("Bebas Neue", 20), width=20, textvariable=self.var_lname, relief=FLAT,justify='center')
        txt_lname.grid(row=0, column=0, pady=5, padx=3)
        txt_lname.insert(0, "Surname")
        txt_lname.bind("<FocusIn>", user_lname)
        txt_lname.bind("<FocusOut>", user_lname1)
###########################################
        def user_fname(event):
            if txt_fname.get()=="First Name":
                txt_fname.delete(0, END)
                txt_fname.config(justify='left')
        def user_fname1(event):
            if txt_fname.get()=="":
                txt_fname.insert(0, "First Name")
                txt_fname.config(justify='center')

        main_fname = Frame(bg_img2, bd=2, bg="gray12", relief=RIDGE)
        main_fname.place(x=560, y=80)
        txt_fname = Entry(main_fname, font=("Bebas Neue", 20), width=20, textvariable=self.var_fname, relief=FLAT,justify='center')
        txt_fname.grid(row=0, column=0, pady=5, padx=3)
        txt_fname.insert(0, "First Name")
        txt_fname.bind("<FocusIn>", user_fname)
        txt_fname.bind("<FocusOut>", user_fname1)

###########################################
        def user_contact(event):
            if txt_contact.get()=="Contact Number":
                txt_contact.delete(0, END)
                txt_contact.config(justify='left')
        def user_contact1(event):
            if txt_contact.get()=="":
                txt_contact.insert(0, "Contact Number")
                txt_contact.config(justify='center')

        main_contact = Frame(bg_img2, bd=2, bg="gray12", relief=RIDGE)
        main_contact.place(x=220, y=140)
        txt_contact = Entry(main_contact, font=("Bebas Neue", 20), width=20, textvariable=self.var_contact, relief=FLAT,justify='center')
        txt_contact.grid(row=0, column=0, pady=5, padx=3)
        txt_contact.insert(0, "Contact Number")
        txt_contact.bind("<FocusIn>", user_contact)
        txt_contact.bind("<FocusOut>", user_contact1)
#######################################################
        def user_Email(event):
            if txt_email.get()=="Email":
                txt_email.delete(0, END)
                txt_email.config(justify='left')
        def user_Email1(event):
            if txt_email.get()=="":
                txt_email.insert(0, "Email")
                txt_email.config(justify='center')

        main_email = Frame(bg_img2, bd=2, bg="gray12", relief=RIDGE)
        main_email.place(x=560, y=140)
        txt_email = Entry(main_email, font=("Bebas Neue", 20), width=20, textvariable=self.var_email, relief=FLAT,justify='center')
        txt_email.grid(row=0, column=0, pady=5, padx=3)
        txt_email.insert(0, "Email")
        txt_email.bind("<FocusIn>", user_Email)
        txt_email.bind("<FocusOut>", user_Email1)

#######################################################
        def user_Pass(event):
            if txt_regpass.get()=="Password":
                txt_regpass.delete(0, END)
                txt_regpass.config(show="*")
                txt_regpass.config(justify='left')
        def user_Pass1(event):
            if txt_regpass.get()=="":
                txt_regpass.config(show="")
                txt_regpass.insert(0, "Password")
                txt_regpass.config(justify='center')


        main_regpass = Frame(bg_img2, bd=2, bg="gray12", relief=RIDGE)
        main_regpass.place(x=220, y=200)
        txt_regpass = Entry(main_regpass, font=("Bebas Neue", 20), width=20, textvariable=self.var_regpass, relief=FLAT,justify='center')
        txt_regpass.grid(row=0, column=0, pady=5, padx=3)
        txt_regpass.insert(0, "Password")
        txt_regpass.bind("<FocusIn>", user_Pass)
        txt_regpass.bind("<FocusOut>", user_Pass1)
#######################################################
        def user_cPass(event):
            if txt_cpass.get()=="Confirm Password":
                txt_cpass.delete(0, END)
                txt_cpass.config(show="*")
                txt_cpass.config(justify='left')
        def user_cPass1(event):
            if txt_cpass.get()=="":
                txt_cpass.config(show="")
                txt_cpass.insert(0, "Confirm Password")
                txt_cpass.config(justify='center')

        main_cregpass = Frame(bg_img2, bd=2, bg="gray12", relief=RIDGE)
        main_cregpass.place(x=560, y=200)
        txt_cpass = Entry(main_cregpass, font=("Bebas Neue", 20), width=20, textvariable=self.var_confpass, relief=FLAT,justify='center')
        txt_cpass.grid(row=0, column=0, pady=5, padx=3)
        txt_cpass.insert(0, "Confirm Password")
        txt_cpass.bind("<FocusIn>", user_cPass)
        txt_cpass.bind("<FocusOut>", user_cPass1)

#######################
        btnl_register = Frame(bg_img2, bd=0, bg="gray40", relief=RIDGE,)
        btnl_register.place(x=240, y=310)
        btn_register = Button(btnl_register, text="Register",cursor="hand2", font=("Bebas Neue", 15, "bold"),fg="white", bg='black', relief=FLAT, activebackground="gray10",activeforeground="gray50", width=20, command=self.accregister)
        btn_register.grid(row=0, column=0, pady=3, padx=3)

#######################
        btn_rLogin = Frame(bg_img2, bd=0, bg="gray40", relief=RIDGE,)
        btn_rLogin.place(x=580, y=310)
        btn_rlogin = Button(btn_rLogin, text="Log In",cursor="hand2", font=("Bebas Neue", 15, "bold"),fg="white", bg='black', relief=FLAT, activebackground="gray10",activeforeground="gray50", width=20, command=self.reset)
        btn_rlogin.grid(row=0, column=0, pady=3, padx=3)


#############################
        btn_exit = Button(bg_img2, text="X", font=("Calibri (Body)", 15), bd=0, fg='white',activebackground='red', bg='gray10',command=self.reset)
        btn_exit.place(x=920, y=35)
#############################
    def reset(self):
        root.withdraw()
        os.system("login.py")


    def accregister(self):
        if self.var_lname.get()=="" or self.var_fname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_regpass.get=="" or self.var_confpass.get=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        elif self.var_regpass.get()==self.var_confpass.get():
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Admin123",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s)", (
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_regpass.get()

                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Log-Detect: A Facial Recognition Logbook System", "Register Success", parent=self.root)
                self.var_fname.set("")
                self.var_lname.set("")
                self.var_contact.set("")
                self.var_email.set("")
                self.var_regpass.set("")
                self.var_confpass.set("")
                self.register()





            except Exception as es:
                messagebox.showerror("Log-Detect: A Facial Recognition Logbook System",f"Due To :{str(es)}",parent=self.root)

        else:
            messagebox.showerror("Log-Detect: A Facial Recognition Logbook System", "Password not same", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    # Start Maximized
    # root.state("zoomed")
    root.mainloop()



