from tkinter import *


class LogDetect:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400+500+150")
        self.root.title("LogDetect - Draft")
        self.root.resizable(False, False)
        self.root.configure(bg='gray')
        #self.root.iconbitmap(r"Assets\Log.ico")

        #Logo
        Logo = Label(self.root,bg="white")
        Logo.place(x=160, y=20, width=80, height=80)

        #Logo Text
        Logotxt = Label(self.root, text=" LogDetect", font=("Bebas Neue", 10),fg="white", bg="gray")
        Logotxt.place(x=150, y=100, width=100, height=20)

        #LogIn Button

        LogInBtn = Button(root, cursor="hand2", text="LogIn", font=("Bebas Neue", 10), bg="white", fg="black", relief=FLAT, activebackground="gray10",activeforeground="gray50")
        LogInBtn.place(x=80, y=140, width=100, height=30)

        #SignUp Button
        SignUpBtn = Button(root, cursor="hand2", text="SignUp", font=("Bebas Neue", 10), bg="black", fg="white", relief=FLAT, activebackground="gray10",activeforeground="gray50")
        SignUpBtn.place(x=220, y=140, width=100, height=30)

        #StudentId Entry
        StudIdEnt =Entry(root, font=("Bebas Neue", 10,))
        StudIdEnt.place(x=80, y=200, width=240, height=20)

        #StudentId Text
        StudIdtxt = Label(root, text="Student ID", font=("Bebas Neue", 10),fg="white", bg="gray")
        StudIdtxt.place(x=150, y=220, width=100, height=20)

        #Password Entry
        PassEnt = Entry(root, font=("Bebas Neue", 10,))
        PassEnt.place(x=80, y=250, width=240, height=20)

        #Password Text
        Passtxt = Label(root, text="Password", font=("Bebas Neue", 10), fg="white", bg="gray")
        Passtxt.place(x=150, y=270, width=100, height=20)

        #Show Password Radio
        ShwPassBtn = Radiobutton(root, text="Show Password", bg="gray", value="yes")
        ShwPassBtn.place(x=80, y=300, width=100, height=20)

        #Forgat Password Button
        ForPassBtn = Button(root, cursor="hand2", text="Forgat Password?", font=("Bebas Neue", 10), bg="gray", fg="white", relief=FLAT, activebackground="gray10",activeforeground="gray50")
        ForPassBtn.place(x=230, y=295, width=110, height=30)

        #Facebook Button
        FacebookBtn = Button(root, cursor="hand2", font=("Bebas Neue", 10), bg="White",
                            fg="white", relief=FLAT, activebackground="gray10", activeforeground="gray50")
        FacebookBtn.place(x=150, y=350, width=30, height=30)

        #Discord Button
        DiscordBtn = Button(root, cursor="hand2", font=("Bebas Neue", 10), bg="White",
                             fg="white", relief=FLAT, activebackground="gray10", activeforeground="gray50")
        DiscordBtn.place(x=190, y=350, width=30, height=30)

        #Twitter Button
        TwitterBtn = Button(root, cursor="hand2", font=("Bebas Neue", 10), bg="White",
                            fg="white", relief=FLAT, activebackground="gray10", activeforeground="gray50")
        TwitterBtn.place(x=230, y=350, width=30, height=30)


if __name__ == "__main__":
    root = Tk()
    obj = LogDetect(root)
    # Start Maximized
    # root.state("zoomed")
    root.mainloop()
