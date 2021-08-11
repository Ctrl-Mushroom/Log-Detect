from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2


class Registration:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+130+40")
        self.root.title("Log-Detect: Registration")
        self.root.resizable(False, False)
        self.root.iconbitmap(r"Assets\Log.ico")

        # Variables
        self.var_Course = StringVar()
        self.var_SchoolStatus = StringVar()
        self.var_AdmStatus = StringVar()
        self.var_YearSec = StringVar()
        self.var_StudentNum = StringVar()
        self.var_Surname = StringVar()
        self.var_Firstname = StringVar()
        self.var_MI = StringVar()
        self.var_Contact = StringVar()
        self.var_Email = StringVar()
        self.var_Sex = StringVar()
        self.var_Address = StringVar()
        self.var_City = StringVar()
        self.serchTxt_var = StringVar()
        self.serch_var = StringVar()
        self.var_StudentNumber = StringVar()

        Main_Frame = Frame(root, bg="gray8")
        Main_Frame.place(x=0, y=0, width=1280, height=720)

        # LEFT FRAME
        Left_Frame = LabelFrame(Main_Frame, bg="gray12", fg="gray85", bd=2, relief=RIDGE,font=("Bebas Neue", 20))#text="TBD"
        Left_Frame.place(x=15, y=15, width=618, height=690)

        # LEFT UPPER
        Left_Upper_Frame = LabelFrame(Left_Frame, bg="gray12", fg="gray85", bd=2, relief=RIDGE,
                                      text="School Information", font=("Bebas Neue", 20))
        Left_Upper_Frame.place(x=5, y=5, width=605, height=170)

        # COURSE
        Course_Label = Label(Left_Upper_Frame, text="Department", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        Course_Label.grid(row=0, column=0, padx=5, sticky=W)

        Course_Combo = ttk.Combobox(Left_Upper_Frame, textvariable=self.var_Course, font=("Bebas Neue", 12), width=15,
                                    state="readonly")
        Course_Combo["values"] = ("Select", "CpE", "IT", "HM", "OA")
        Course_Combo.current(0)
        Course_Combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # YEAR & LEVEL
        Year_Label = Label(Left_Upper_Frame, text="Year & Section", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        Year_Label.grid(row=0, column=2, padx=5, sticky=W)

        Year_Combo = ttk.Combobox(Left_Upper_Frame, textvariable=self.var_YearSec, font=("Bebas Neue", 12), width=15,
                                  state="readonly")
        Year_Combo["values"] = ("Select", "1-1", "1-2", "2-1", "2-2", "3-1", "3-2", "4-1", "4-2")
        Year_Combo.current(0)
        Year_Combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # SCHOOLASTIC STATUS
        Schlstc_Status_Label = Label(Left_Upper_Frame, text="Scholastic Status", bg="gray8", fg="gray85",font=("Bebas Neue", 12,))
        Schlstc_Status_Label.grid(row=1, column=0, padx=5, sticky=W)

        Schlstc_Status_Combo = ttk.Combobox(Left_Upper_Frame, textvariable=self.var_SchoolStatus,font=("Bebas Neue", 12), width=15, state="readonly")
        Schlstc_Status_Combo["values"] = ("Select", "Regular", "Irregular", "Warning")
        Schlstc_Status_Combo.current(0)
        Schlstc_Status_Combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # ADMISSION STATUS
        Admssn_Status_Label = Label(Left_Upper_Frame, text="Admission Status", bg="gray8", fg="gray85",font=("Bebas Neue", 12,))
        Admssn_Status_Label.grid(row=1, column=2, padx=5, sticky=W)

        Admssn_Status_Combo = ttk.Combobox(Left_Upper_Frame, textvariable=self.var_AdmStatus, font=("Bebas Neue", 12),width=15, state="readonly")
        Admssn_Status_Combo["values"] = ("Select", "Continuing", "Graduated", "Expelled", "Dropped-Out")
        Admssn_Status_Combo.current(0)
        Admssn_Status_Combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Id No.
        Student_Number_Label = Label(Left_Upper_Frame, text="Roll no.", bg="gray8", fg="gray85",font=("Bebas Neue", 12,))
        Student_Number_Label.grid(row=2, column=0, padx=5, sticky=W)

        Student_Number_Entry = ttk.Entry(Left_Upper_Frame, textvariable=self.var_StudentNum, width=17,font=("Bebas Neue", 12,))
        Student_Number_Entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # student number
        Student_Number_Label = Label(Left_Upper_Frame, text="ID number", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        Student_Number_Label.grid(row=2, column=2, padx=5, sticky=W)

        Student_Number_Entry = ttk.Entry(Left_Upper_Frame, textvariable=self.var_StudentNumber, width=17,
                                         font=("Bebas Neue", 12,))
        Student_Number_Entry.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        # LEFT LOWER
        Left_Lower_Frame = LabelFrame(Left_Frame, bg="gray12", fg="gray85", bd=2, relief=RIDGE,
                                      text="Personal Information", font=("Bebas Neue", 20))
        Left_Lower_Frame.place(x=5, y=175, width=605, height=370)

        # SURNAME
        Surname_Label = Label(Left_Lower_Frame, text="Surname", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        Surname_Label.grid(row=0, column=0, padx=5, sticky=W)

        Surname_Entry = ttk.Entry(Left_Lower_Frame, textvariable=self.var_Surname, width=18, font=("Bebas Neue", 12,))
        Surname_Entry.grid(row=0, column=1, padx=2,pady=10, sticky=W)

        # MIDDLENAME
        Middle_Name_Label = Label(Left_Lower_Frame, text="Middle Name", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        Middle_Name_Label.grid(row=1, column=0, padx=5, sticky=W)

        Middle_Name_Entry = ttk.Entry(Left_Lower_Frame, textvariable=self.var_MI, width=18, font=("Bebas Neue", 12,))
        Middle_Name_Entry.grid(row=1, column=1, padx=2,pady=5, sticky=W)

        # CONTACT NUMBER
        Contact_Number_Label = Label(Left_Lower_Frame, text="Contact Number", bg="gray8", fg="gray85",
                                     font=("Bebas Neue", 12,))
        Contact_Number_Label.grid(row=2, column=0, padx=5, sticky=W)

        Contact_Number_Entry = ttk.Entry(Left_Lower_Frame, width=18, textvariable=self.var_Contact,
                                         font=("Bebas Neue", 12,))
        Contact_Number_Entry.grid(row=2, column=1, padx=2,pady=10, sticky=W)

        # ADDRESS
        Adress_Label = Label(Left_Lower_Frame, text="Address", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        Adress_Label.grid(row=3, column=0, padx=5, sticky=W)

        Adress_Entry = ttk.Entry(Left_Lower_Frame, width=31, textvariable=self.var_Address, font=("Bebas Neue", 12,))
        Adress_Entry.grid(row=3, column=1, padx=2, pady=5, sticky=W)


        # CITY
        City_Label = Label(Left_Lower_Frame, text="City", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        City_Label.grid(row=4, column=0, padx=5, sticky=W)

        City_Combo = ttk.Combobox(Left_Lower_Frame, textvariable=self.var_City, font=("Bebas Neue", 12), width=16,
                                  state="readonly")
        City_Combo["values"] = ("Select", "Pasay", "Parañaque", "Las Piñas")
        City_Combo.current(0)
        City_Combo.grid(row=4, column=1, padx=2,pady=10, sticky=W)

        # LEFT LOWER
        Left_Left_Lower_Frame = LabelFrame(Left_Frame, bg="gray12", fg="gray85", bd=0, relief=RIDGE,)
        Left_Left_Lower_Frame.place(x=315, y=210)

        # FIRSTNAME
        First_Name_Label = Label(Left_Left_Lower_Frame, text="First Name", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        First_Name_Label.grid(row=0, column=0, padx=4, sticky=W)

        First_Name_Entry = ttk.Entry(Left_Left_Lower_Frame, width=18, textvariable=self.var_Firstname,
                                     font=("Bebas Neue", 12,))
        First_Name_Entry.grid(row=0, column=1, padx=0,pady=10, sticky=W)

        # SEX
        Sex_Label = Label(Left_Left_Lower_Frame, text="Sex", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        Sex_Label.grid(row=1, column=0, padx=4, sticky=W)

        Sex_Combo = ttk.Combobox(Left_Left_Lower_Frame, textvariable=self.var_Sex, font=("Bebas Neue", 12), width=16,
                                 state="readonly")
        Sex_Combo["values"] = ("Select", "Male", "Female", "Others")
        Sex_Combo.current(0)
        Sex_Combo.grid(row=1, column=1, padx=0, pady=5, sticky=W)

        # EMAIL
        Email_Label = Label(Left_Left_Lower_Frame, text="Email Address", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        Email_Label.grid(row=2, column=0, padx=4, sticky=W)

        Email_Entry = ttk.Entry(Left_Left_Lower_Frame, width=18, textvariable=self.var_Email, font=("Bebas Neue", 12,))
        Email_Entry.grid(row=2, column=1, padx=0, pady=10, sticky=W)



        # RADIO BUTTONS
        self.var_Radio1 = StringVar()
        RadioBtn = ttk.Radiobutton(Left_Lower_Frame, variable=self.var_Radio1, text="Take Photo sample", value="Yes")
        RadioBtn.grid(row=5, column=0,padx=5, pady=10)

        RadioBtn2 = ttk.Radiobutton(Left_Lower_Frame, variable=self.var_Radio1, text="No Photo sample", value="No")
        RadioBtn2.grid(row=5, column=1)

        # BUTTON FRAMES
        BtnFrame = Frame(Left_Lower_Frame, bg="gray12", relief=RIDGE)
        BtnFrame.place(x=0, y=250, width=600, height=40)

        # SAVE BUTTON
        SaveBtn = Button(BtnFrame, width=14, command=self.add_data, text="Save", bg="gray12", fg="gray85",
                         font=("Bebas Neue", 12, "bold"))
        SaveBtn.grid(row=0, column=0)

        # UPDATE BUTTON
        UpdateBtn = Button(BtnFrame, width=14, command=self.update_data, text="Update", bg="gray12", fg="gray85",
                           font=("Bebas Neue", 12, "bold"))
        UpdateBtn.grid(row=0, column=1)

        # DELETE BUTTON
        DeleteBtn = Button(BtnFrame, width=14, command=self.delete_data, text="Delete", bg="gray12", fg="gray85",
                           font=("Bebas Neue", 12, "bold"))
        DeleteBtn.grid(row=0, column=2)

        # RESET BUTTON
        ResetBtn = Button(BtnFrame, width=14, command=self.reset_data, text="Reset", bg="gray12", fg="gray85",
                          font=("Bebas Neue", 12, "bold"))
        ResetBtn.grid(row=0, column=3)

        # BUTTON FRAMES 2
        BtnFrame2 = Frame(Left_Lower_Frame, bg="gray12", relief=RIDGE) #, bd=2
        BtnFrame2.place(x=0, y=285, width=599, height=35)

        # TAKE PHOTO
        TakePhoto = Button(BtnFrame2, width=29, command=self.generate_dataset, text="Take Photo", bg="gray12",
                           fg="gray85", font=("Bebas Neue", 12, "bold"))
        TakePhoto.grid(row=0, column=0)

        # UPDATE PHOTO
        UpdatePhoto = Button(BtnFrame2, width=29, command=self.generate_dataset,  text="Update Photo", bg="gray12", fg="gray85",
                             font=("Bebas Neue", 12, "bold"))
        UpdatePhoto.grid(row=0, column=1)

        # RIGHT FRAME
        Right_Frame = LabelFrame(Main_Frame, bg="gray12", fg="gray85", bd=2, relief=RIDGE,font=("Bebas Neue", 20))
        Right_Frame.place(x=645, y=15, width=618, height=690)

        # RIGHT UPPER
        Right_Upper_Frame = LabelFrame(Right_Frame, bg="gray12", fg="gray85", bd=2, relief=RIDGE, text="Search",
                                       font=("Bebas Neue", 20))
        Right_Upper_Frame.place(x=5, y=5, width=605, height=150)

        # SEARCH
        Search_Label = Label(Right_Upper_Frame, text="Search By:", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        Search_Label.grid(row=0, column=0, padx=2, sticky=W)

        Search_Combo = ttk.Combobox(Right_Upper_Frame,textvariable=self.serch_var, font=("Bebas Neue", 12), width=15, state="readonly")
        Search_Combo["values"] = ("Select", "Surname", "StudentNo", "Department")
        Search_Combo.current(0)
        Search_Combo.grid(row=0, column=1, padx=2, pady=30, sticky=W)

        # SEARCH BAR
        Search_Entry = ttk.Entry(Right_Upper_Frame, width=15, textvariable=self.serchTxt_var, font=("Bebas Neue", 12,))
        Search_Entry.grid(row=0, column=2, padx=2, sticky=W)

        # SEARCH BUTTON
        SearchBtn = Button(Right_Upper_Frame, width=10,command=self.search_data, text="Search", bg="gray12", fg="gray85",
                           font=("Bebas Neue", 13))
        SearchBtn.grid(row=0, column=3)

        # SHOW ALL BUTTON
        ShowAllBtn = Button(Right_Upper_Frame, width=10,command=self.showall, text="Show All", bg="gray12", fg="gray85",
                            font=("Bebas Neue", 13))
        ShowAllBtn.grid(row=0, column=4, padx=5)

        # RIGHT LOWER
        Right_Lower_Frame = LabelFrame(Right_Frame, bg="gray12", fg="gray85", bd=2, relief=RIDGE, text="RESULTS",
                                       font=("Bebas Neue", 20))
        Right_Lower_Frame.place(x=5, y=155, width=605, height=530)

        # FRAME

        Scroll_X = ttk.Scrollbar(Right_Lower_Frame, orient=HORIZONTAL)
        Scroll_Y = ttk.Scrollbar(Right_Lower_Frame, orient=VERTICAL)

        self.Registration_Table = ttk.Treeview(Right_Lower_Frame, columns=(
        "Student_Num","StudentNo","Department", "Schl_Sts", "Adm_Sts", "YearSec", "Surname", "First_Name", "Middle_Initial",
        "Contact", "Email", "Sex", "Address", "City", "Photo"), xscrollcommand=Scroll_X.set,
                                               yscrollcommand=Scroll_Y.set)

        Scroll_X.pack(side=BOTTOM, fill=X)
        Scroll_Y.pack(side=RIGHT, fill=Y)
        Scroll_X.config(command=self.Registration_Table.xview)
        Scroll_Y.config(command=self.Registration_Table.yview)

        self.Registration_Table.heading("Student_Num", text="Roll No.")
        self.Registration_Table.heading("StudentNo", text="Student Number")
        self.Registration_Table.heading("Department", text="Department")
        self.Registration_Table.heading("Schl_Sts", text="Schoolastic Status")
        self.Registration_Table.heading("Adm_Sts", text="Admission Status")
        self.Registration_Table.heading("YearSec", text="Year & Section")
        self.Registration_Table.heading("Surname", text="Surname")
        self.Registration_Table.heading("First_Name", text="First Name")
        self.Registration_Table.heading("Middle_Initial", text="M.I")
        self.Registration_Table.heading("Contact", text="Contact Number")
        self.Registration_Table.heading("Email", text="Email Address")
        self.Registration_Table.heading("Sex", text="Sex")
        self.Registration_Table.heading("Address", text="Address")
        self.Registration_Table.heading("City", text="City")
        self.Registration_Table.heading("Photo", text="Photo")
        self.Registration_Table["show"] = "headings"

        self.Registration_Table.column("Student_Num", width=100)
        self.Registration_Table.column("StudentNo", width=150)
        self.Registration_Table.column("Department", width=100)
        self.Registration_Table.column("Schl_Sts", width=150)
        self.Registration_Table.column("Adm_Sts", width=150)
        self.Registration_Table.column("YearSec", width=150)
        self.Registration_Table.column("Surname", width=100)
        self.Registration_Table.column("First_Name", width=100)
        self.Registration_Table.column("Middle_Initial", width=100)
        self.Registration_Table.column("Contact", width=100)
        self.Registration_Table.column("Email", width=100)
        self.Registration_Table.column("Sex", width=100)
        self.Registration_Table.column("Address", width=100)
        self.Registration_Table.column("City", widt=100)
        self.Registration_Table.column("Photo", width=100)

        self.Registration_Table.pack(fill=BOTH, expand=1)
        self.Registration_Table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    ##########################
    def showall(self):
        self.Registration_Table.heading("Student_Num", text="Roll No.")
        self.Registration_Table.heading("StudentNo", text="Student Number")
        self.Registration_Table.heading("Department", text="Department")
        self.Registration_Table.heading("Schl_Sts", text="Schoolastic Status")
        self.Registration_Table.heading("Adm_Sts", text="Admission Status")
        self.Registration_Table.heading("YearSec", text="Year & Section")
        self.Registration_Table.heading("Surname", text="Surname")
        self.Registration_Table.heading("First_Name", text="First Name")
        self.Registration_Table.heading("Middle_Initial", text="M.I")
        self.Registration_Table.heading("Contact", text="Contact Number")
        self.Registration_Table.heading("Email", text="Email Address")
        self.Registration_Table.heading("Sex", text="Sex")
        self.Registration_Table.heading("Address", text="Address")
        self.Registration_Table.heading("City", text="City")
        self.Registration_Table.heading("Photo", text="Photo")
        self.Registration_Table["show"] = "headings"

        self.Registration_Table.column("Student_Num", width=100)
        self.Registration_Table.column("StudentNo", width=150)
        self.Registration_Table.column("Department", width=100)
        self.Registration_Table.column("Schl_Sts", width=150)
        self.Registration_Table.column("Adm_Sts", width=150)
        self.Registration_Table.column("YearSec", width=150)
        self.Registration_Table.column("Surname", width=100)
        self.Registration_Table.column("First_Name", width=100)
        self.Registration_Table.column("Middle_Initial", width=100)
        self.Registration_Table.column("Contact", width=100)
        self.Registration_Table.column("Email", width=100)
        self.Registration_Table.column("Sex", width=100)
        self.Registration_Table.column("Address", width=100)
        self.Registration_Table.column("City", widt=100)
        self.Registration_Table.column("Photo", width=100)

        self.Registration_Table.pack(fill=BOTH, expand=1)
        self.Registration_Table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # ADD DATA TO DATA BASE

    def add_data(self):
        if self.var_Course.get() == "Select" or self.var_StudentNum.get() == "" or self.var_StudentNumber.get() == "":
            messagebox.showerror("Log-Detect: Registration", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Admin123",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into face_recog values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_StudentNum.get(),
                    self.var_StudentNumber.get(),
                    self.var_Course.get(),
                    self.var_SchoolStatus.get(),
                    self.var_AdmStatus.get(),
                    self.var_YearSec.get(),
                    self.var_Surname.get(),
                    self.var_Firstname.get(),
                    self.var_MI.get(),
                    self.var_Contact.get(),
                    self.var_Email.get(),
                    self.var_Sex.get(),
                    self.var_Address.get(),
                    self.var_City.get(),
                    self.var_Radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Log-Detect: Registration", "Student Info has been added Successfully", parent=self.root)
                self.reset_data()
            except Exception as es:
                messagebox.showerror("Log-Detect: Registrationr", f"Due to:{str(es)}", parent=self.root)

    # FETCH DATA FROM DATABASE
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Admin123",
            database="face_recognizer"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from face_recog")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.Registration_Table.delete(*self.Registration_Table.get_children())
            for i in data:
                self.Registration_Table.insert('', END, values=i)

            conn.commit()
        conn.close()

    # GET CURSOR
    def get_cursor(self, event=""):
        try:
            cursor_focus = self.Registration_Table.focus()
            content = self.Registration_Table.item(cursor_focus)
            data = content["values"]

            self.var_StudentNum.set(data[0])
            self.var_StudentNumber.set(data[1])
            self.var_Course.set(data[2]),
            self.var_SchoolStatus.set(data[3]),
            self.var_AdmStatus.set(data[4]),
            self.var_YearSec.set(data[5]),
            self.var_Surname.set(data[6]),
            self.var_Firstname.set(data[7]),
            self.var_MI.set(data[8]),
            self.var_Contact.set(data[9]),
            self.var_Email.set(data[10]),
            self.var_Sex.set(data[11]),
            self.var_Address.set(data[12]),
            self.var_City.set(data[13]),
            self.var_Radio1.set(data[14])
        except Exception as es:
            messagebox.showerror("Log-Detect: Registration", f"Due To:{str(es)}", parent=self.root)

    # UPDATE DATA
    def update_data(self):
        if self.var_Course.get() == "Select" or self.var_SchoolStatus.get() == "" or self.var_AdmStatus.get() == "":
            messagebox.showerror("Log-Detect: Registration", "All Fields are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Log-Detect: Registration", "Do you want to update this student Info?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Admin123",
                        database="face_recognizer"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("update face_recog set Department=%s, school_status=%s, adm_status=%s, year_sec=%s, Surname=%s, first_name=%s, middle_initial=%s, contact_number=%s, email=%s, sex=%s, address=%s, city=%s, photo=%s where  student_num=%s",
                        (

                            self.var_Course.get(),
                            self.var_SchoolStatus.get(),
                            self.var_AdmStatus.get(),
                            self.var_YearSec.get(),
                            self.var_Surname.get(),
                            self.var_Firstname.get(),
                            self.var_MI.get(),
                            self.var_Contact.get(),
                            self.var_Email.get(),
                            self.var_Sex.get(),
                            self.var_Address.get(),
                            self.var_City.get(),
                            self.var_Radio1.get(),
                            self.var_StudentNum.get()

                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Log-Detect: Registration", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Log-Detect: Registration", f"Due To:{str(es)}", parent=self.root)

    # DELETE DATA
    def delete_data(self):
        if self.var_StudentNum.get() == "":
            messagebox.showerror("Log-Detect: Registration", "Student Roll or id number must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Log-Detect: Registration", "Do you want to delete this student info?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Admin123",
                        database="face_recognizer"
                    )
                    my_cursor = conn.cursor()
                    sql = "delete from face_recog where student_num=%s"
                    val = (self.var_StudentNum.get(),)
                    my_cursor.execute(sql, val)
                    self.showall()
                    #self.reset_data()
                else:
                    if not delete:
                        return

                conn.commit()


                messagebox.showinfo("Log-Detect: Registration", "Successfully Deleted student Info", parent=self.root)
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Log-Detect: Registration", f"Due To:{str(es)}", parent=self.root)

    # RESET INPUT
    def reset_data(self):
        self.var_Course.set("Select")
        self.var_SchoolStatus.set("Select")
        self.var_AdmStatus.set("Select")
        self.var_YearSec.set("Select")
        self.var_StudentNum.set("")
        self.var_StudentNumber.set("")
        self.var_Surname.set("")
        self.var_Firstname.set("")
        self.var_MI.set("")
        self.var_Contact.set("")
        self.var_Email.set("")
        self.var_Sex.set("Select")
        self.var_Address.set("")
        self.var_City.set("Select")
        self.var_Radio1.set("")

    # TAKE PHOTO SAMPLES
    def generate_dataset(self):
        if self.var_Course.get() == "Select" or self.var_SchoolStatus.get() == "" or self.var_AdmStatus.get() == "":
            messagebox.showerror("Log-Detect: Registration", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Admin123",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from face_recog")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1

                my_cursor.execute(
                    "update face_recog set Department=%s, school_status=%s, adm_status=%s, year_sec=%s, Surname=%s, first_name=%s, middle_initial=%s, contact_number=%s, email=%s, sex=%s, address=%s, city=%s, photo=%s where  student_num=%s",
                    (

                        self.var_Course.get(),
                        self.var_SchoolStatus.get(),
                        self.var_AdmStatus.get(),
                        self.var_YearSec.get(),
                        self.var_Surname.get(),
                        self.var_Firstname.get(),
                        self.var_MI.get(),
                        self.var_Contact.get(),
                        self.var_Email.get(),
                        self.var_Sex.get(),
                        self.var_Address.get(),
                        self.var_City.get(),
                        self.var_Radio1.get(),
                        self.var_StudentNum.get()

                    ))
                conn.commit()
                self.fetch_data()

                conn.close()

                face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                # eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        id_num = self.var_StudentNum.get()
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (600,550))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        FaceData_path = "FaceData/user." + str(id_num) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(FaceData_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Log-Detect: A Facial Recognition Logbook System", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 20:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Log-Detect: A Facial Recognition Logbook System", "Face Data Stored")

            except Exception as es:
                messagebox.showerror("Log-Detect: Registration", f"Due To:{str(es)}", parent=self.root)

        # =================search ===================
    def search_data(self):
        if self.serchTxt_var.get() == "" or self.serch_var.get() == "Select Option":
            messagebox.showerror("Log-Detect: Registration", "Select Combo option and enter entry box", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Admin123",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from face_recog where " + str(self.serch_var.get()) + " LIKE '%" + str(self.serchTxt_var.get()) + "%'")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.Registration_Table.delete(*self.Registration_Table.get_children())
                    for i in rows:
                        self.Registration_Table.insert("", END, values=i)
                else:
                    messagebox.showerror("Log-Detect: Registration", "Data Not Found", parent=self.root)
                    conn.commit()
                conn.close()
            except Exception as es:
                    messagebox.showerror("Log-Detect: Registration", f"Due To :{str(es)}", parent=self.root)





if __name__ == "__main__":
    root = Tk()
    obj = Registration(root)
    root.mainloop()



