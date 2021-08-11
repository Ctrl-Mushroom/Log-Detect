from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import cursor
import os
import csv

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+130+40")
        self.root.title("Log-Detect: Attendance")
        self.root.resizable(False, False)
        self.root.iconbitmap(r"Assets\Log.ico")

        # Variables
        self.var_StudentNum = StringVar()
        self.var_StudentNumber = StringVar()
        self.var_Course = StringVar()
        #self.var_YearSec = StringVar()
        self.var_Surname = StringVar()
        self.var_Date = StringVar()
        self.var_Time = StringVar()
        self.var_Status = StringVar()
        self.var_Firstname=StringVar()

        Main_Frame = Frame(root, bg="gray8")
        Main_Frame.place(x=0, y=0, width=1280, height=720)

        # LEFT FRAME
        Left_Frame = LabelFrame(Main_Frame, bg="gray12", fg="gray85", bd=2, relief=RIDGE,font=("Bebas Neue", 20))
        Left_Frame.place(x=15, y=15, width=618, height=690)

        # LEFT UPPER
        Left_Upper_Frame = LabelFrame(Left_Frame, bg="gray12", fg="gray85", bd=2, relief=RIDGE,
                                      text="Logbook Information", font=("Bebas Neue", 20))
        Left_Upper_Frame.place(x=5, y=5, width=605, height=220)

        # STUDENT NUMBER
        Student_Number_Label = Label(Left_Upper_Frame, text="ID Number", bg="gray8", fg="gray85",
                                     font=("Bebas Neue", 12,))
        Student_Number_Label.grid(row=0, column=0, padx=5, sticky=W)

        Student_Number_Entry = ttk.Entry(Left_Upper_Frame, textvariable=self.var_StudentNum, width=20,
                                         font=("Bebas Neue", 12,))
        Student_Number_Entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # COURSE
        Course_Label = Label(Left_Upper_Frame, text="Department", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        Course_Label.grid(row=0, column=2, padx=5, sticky=W)

        Course_Entry = ttk.Entry(Left_Upper_Frame, textvariable=self.var_Course, width=20, font=("Bebas Neue", 12,))
        Course_Entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # SURNAME
        Name_Label = Label(Left_Upper_Frame, text="Surname", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        Name_Label.grid(row=1, column=0, padx=5, sticky=W)

        Name_Entry = ttk.Entry(Left_Upper_Frame, textvariable=self.var_Surname, width=20, font=("Bebas Neue", 12,))
        Name_Entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # FIRST NAME
        Name_Label = Label(Left_Upper_Frame, text="First Name", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        Name_Label.grid(row=1, column=2, padx=5, sticky=W)

        Name_Entry = ttk.Entry(Left_Upper_Frame, textvariable=self.var_Firstname, width=20, font=("Bebas Neue", 12,))
        Name_Entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # YEAR & LEVEL
        #Year_Label = Label(Left_Upper_Frame, text="Year & Section", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        #Year_Label.grid(row=2, column=0, padx=5, sticky=W)

        #Year_Entry = ttk.Entry(Left_Upper_Frame, textvariable=self.var_YearSec, width=20, font=("Bebas Neue", 12,))
        #Year_Entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # DATE
        date_Label = Label(Left_Upper_Frame, text="Date", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        date_Label.grid(row=2, column=0, padx=5, sticky=W)

        date_Entry = ttk.Entry(Left_Upper_Frame, textvariable=self.var_Date, width=20,
                                         font=("Bebas Neue", 12,))
        date_Entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # TIME
        time_Label = Label(Left_Upper_Frame, text="Time", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        time_Label.grid(row=2, column=2, padx=5, sticky=W)

        time_Entry = ttk.Entry(Left_Upper_Frame, textvariable=self.var_Time, width=20,
                                         font=("Bebas Neue", 12,))
        time_Entry.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        # ATTENDACE STATUS
        Status_Label = Label(Left_Upper_Frame, text="Status", bg="gray8", fg="gray85", font=("Bebas Neue", 12,))
        Status_Label.grid(row=3, column=0, padx=5, sticky=W)

        Status_Combo = ttk.Combobox(Left_Upper_Frame, textvariable=self.var_Status, font=("Bebas Neue", 12), width=18,
                                    state="readonly")
        Status_Combo["values"] = ("Select", "Present", "Sick", "Absent")
        Status_Combo.current(0)
        Status_Combo.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        # LEFT LOWER
        Left_Lower_Frame = LabelFrame(Left_Frame, bg="gray12", fg="gray85", bd=2, relief=RIDGE,font=("Bebas Neue", 20))
        Left_Lower_Frame.place(x=5, y=230, width=605, height=420)

        # BUTTON FRAMES
        BtnFrame = Frame(Left_Lower_Frame, bg="gray12", bd=1, relief=RIDGE)
        BtnFrame.place(x=0, y=5, width=600, height=35)

        # IMPORT BUTTON
        ImportBtn = Button(BtnFrame, width=14, command=self.importCSV, text="Import", bg="gray12", fg="gray85",
                           font=("Bebas Neue", 12, "bold"))
        ImportBtn.grid(row=0, column=0)

        # EXPORT BUTTON
        ExportBtn = Button(BtnFrame, width=14, command=self.exportCSV, text="Export", bg="gray12", fg="gray85",
                           font=("Bebas Neue", 12, "bold"))
        ExportBtn.grid(row=0, column=1)

        # UPDATE BUTTON
        UpdateBtn = Button(BtnFrame, width=14, command=self.updateData, text="Update", bg="gray12", fg="gray85",
                           font=("Bebas Neue", 12, "bold"))
        UpdateBtn.grid(row=0, column=2)

        # RESET BUTTON
        ResetBtn = Button(BtnFrame, width=14, command=self.resetData, text="Reset", bg="gray12", fg="gray85",
                          font=("Bebas Neue", 12, "bold"))
        ResetBtn.grid(row=0, column=3)

        # RIGHT FRAME
        Right_Frame = LabelFrame(Main_Frame, bg="gray12", fg="gray85", bd=2, relief=RIDGE,font=("Bebas Neue", 20))
        Right_Frame.place(x=645, y=15, width=618, height=690)

        # RIGHT LOWER
        Right_Lower_Frame = LabelFrame(Right_Frame, bg="gray12", fg="gray85", bd=2, relief=RIDGE,
                                       text="Logbook Details", font=("Bebas Neue", 20))
        Right_Lower_Frame.place(x=5, y=5, width=605, height=645)

        # FRAME
        Scroll_X = ttk.Scrollbar(Right_Lower_Frame, orient=HORIZONTAL)
        Scroll_Y = ttk.Scrollbar(Right_Lower_Frame, orient=VERTICAL)

        self.Attendance_Table = ttk.Treeview(Right_Lower_Frame, columns=(
        "Student_Number", "Course", "Surname", "firstname", "Date", "Time", "Status"), xscrollcommand=Scroll_X.set,yscrollcommand=Scroll_Y.set)
        #, "YearSec"
        Scroll_X.pack(side=BOTTOM, fill=X)
        Scroll_Y.pack(side=RIGHT, fill=Y)
        Scroll_X.config(command=self.Attendance_Table.xview)
        Scroll_Y.config(command=self.Attendance_Table.yview)

        self.Attendance_Table.heading("Student_Number", text="ID Number")
        self.Attendance_Table.heading("Course", text="Department")
        self.Attendance_Table.heading("Surname", text="Surname")
        self.Attendance_Table.heading("firstname", text="First Name")
        #self.Attendance_Table.heading("YearSec", text="Year & Section")
        self.Attendance_Table.heading("Date", text="Date")
        self.Attendance_Table.heading("Time", text="Time")
        self.Attendance_Table.heading("Status", text="Status")
        self.Attendance_Table["show"] = "headings"

        self.Attendance_Table.column("Student_Number", width=150)
        self.Attendance_Table.column("Course", width=100)
        self.Attendance_Table.column("Surname", width=100)
        self.Attendance_Table.column("firstname", width=100)
        #self.Attendance_Table.column("YearSec", width=150)
        self.Attendance_Table.column("Date", width=100)
        self.Attendance_Table.column("Time", widt=100)
        self.Attendance_Table.column("Status", width=100)

        self.Attendance_Table.pack(fill=BOTH, expand=1)
        self.Attendance_Table.bind("<ButtonRelease>", self.get_cursor)

        # FETCH DATA FROM DATABASE

    def fetchData(self, rows):
        self.Attendance_Table.delete(*self.Attendance_Table.get_children())
        for i in rows:
            self.Attendance_Table.insert("", END, values=i)

    # IMPORT CSV
    def importCSV(self):
        try:
            global mydata
            mydata.clear()
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(fln) as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)
        except Exception as es:
            messagebox.showerror("Log-Detect: Attendance", f"Due To :{str(es)}", parent=self.root)

    # EXPORT CSV
    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Log-Detect: Attendance", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Log-Detect: Attendance", "Your data exported to " + os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror("Log-Detect: Attendance", f"Due To :{str(es)}", parent=self.root)

    # export upadte
    def updateData(self):

        id = self.var_StudentNum.get()
        course = self.var_Course.get()
        surname = self.var_Surname.get()
        firstname = self.var_Firstname.get()
        #yrsec = self.var_YearSec.get()
        time = self.var_Time.get()
        date = self.var_Date.get()
        status = self.var_Status.get()

        # write to csv file
        try:
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",filetypes=(("CSV file", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="a", newline="\n") as f:
                fieldnames =["ID Number", "Department", "Surname", "First Name", "Date", "Time", "Status"]
                dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
                dict_writer.writerow({
                    "ID Number": id,
                    "Department": course,
                    "Surname": surname,
                    "First Name": firstname,
                    #"Yr&Sec": yrsec,
                    "Date": date,
                    "Time": time,
                    "Status": status

                })
            messagebox.showinfo("Log-Detect: Attendance", "Your data exported to " + os.path.basename(fln) + " Successfully",
                                parent=self.root)
        except Exception as es:
            messagebox.showerror("Log-Detect: Attendance", f"Due To :{str(es)}", parent=self.root)

    # GET CURSOR
    def get_cursor(self, event=""):
        try:
            cursor_focus = self.Attendance_Table.focus()
            content = self.Attendance_Table.item(cursor_focus)
            data = content["values"]

            self.var_StudentNum.set(data[0]),
            self.var_Course.set(data[1]),
            self.var_Surname.set(data[2]),
            self.var_Firstname.set(data[3]),
            self.var_Date.set(data[4]),
            self.var_Time.set(data[5]),
            self.var_Status.set(data[6])
        except Exception as es:
            messagebox.showerror("Log-Detect: Attendance", f"Due To:{str(es)}", parent=self.root)

    # RESET INPUT
    def resetData(self):
        self.var_Course.set("")
        #self.var_YearSec.set("")
        self.var_StudentNum.set("")
        self.var_Surname.set("")
        self.var_Time.set("")
        self.var_Date.set("")
        self.var_Status.set("")
        self.var_Firstname.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()

