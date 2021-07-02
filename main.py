from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

# window set up
root = Tk()
root.geometry("500x300")
root.config(bg="#d00000")
root.title("Login Form")


class LoginForm:
    def __init__(self, master):
        self.lbl_user = Label(master, text="Username Entry:", bg="#d00000", fg="#ffba08", font="Consolas 12 bold")
        self.lbl_user.place(x=50, y=50)
        self.ent_user = Entry(master)
        self.ent_user.place(x=230, y=50)
        self.lbl_passwd = Label(master, text="Password Entry:", bg="#d00000", fg="#ffba08", font="Consolas 12 bold")
        self.lbl_passwd.place(x=50, y=100)
        self.ent_passwd = Entry(master)
        self.ent_passwd.place(x=230, y=100)
        self.btn_exit = Button(master, text="Exit", borderwidth=10, font="Consolas 12 bold", bg="#d00000", fg="#ffba08",
                               highlightthickness=0, command=self.exit_program)
        self.btn_exit.place(x=50, y=150)
        self.btn_clear = Button(master, text="Clear", borderwidth=10, font="Consolas 12 bold", bg="#d00000",
                                fg="#ffba08", highlightthickness=0, command=self.clear_input)
        self.btn_clear.place(x=300, y=150)
        self.btn_login = Button(master, text="Login", borderwidth=10, font="Consolas 12 bold", bg="#d00000",
                                fg="#ffba08", highlightthickness=0, command=self.login)
        self.btn_login.place(x=175, y=150)
        self.btn_register = Button(master, text="Register As New User", borderwidth=10, font="Consolas 12 bold",
                                   bg="#d00000",
                                   fg="#ffba08", highlightthickness=0, command=self.new_user)
        self.btn_register.place(x=105, y=225)

    def login(self):
        # If paswword is enetered by the
        # user
        if self.ent_passwd.get():
            db = mysql.connect(host="localhost",
                               user="lifechoices",
                               password="@Lifechoices1234",
                               db="Hospital")
            cursor = db.cursor()

        # If no password is enetered by the
        # user
        else:
            db = mysql.connect(host="localhost",
                               user="lifechoices",
                               db="Hospital")
            cursor = db.cursor()

        # A Table in the database
        savequery = "select * from Login"

        try:
            cursor.execute(savequery)
            myresult = cursor.fetchall()

            # Printing the result of the
            # query
            for x in myresult:
                if x[1] == str(self.ent_passwd.get()) and x[0] == str(self.ent_user.get()):
                    messagebox.showinfo("Success", "You Have Logged In Successfully")
                    root.withdraw()
                    self.menu_window()
                else:
                    db.rollback()
                    messagebox.showerror("Error", "Incorrect Password or Username")

        except ValueError:
            pass

    def clear_input(self):
        self.ent_user.delete(0, END)
        self.ent_passwd.delete(0, END)

    def exit_program(self):
        return root.destroy()

    def new_user(self):
        db = mysql.connect(
            host="localhost",
            user="lifechoices",
            passwd="@Lifechoices1234",
            database="Hospital"
        )

        cursor = db.cursor()

        query = "INSERT INTO Login (userName, Password) VALUES (%s, %s)"
        values = (self.ent_user.get(), self.ent_passwd.get())

        cursor.execute(query, values)

        db.commit()

        try:
            entry = int(self.ent_passwd.get())
            if entry != str(self.ent_passwd.get()):
                messagebox.showinfo("Success", "You Have Successfully Registered Your Username and Password")
                root.withdraw()
                self.menu_window()
        except ValueError:
            messagebox.showerror("Error", "Please Enter A Numeric Password")

    def menu_window(self):
        menu = Toplevel()
        menu.geometry("250x250")
        menu.title("Menu")
        menu.config(bg="#007200")

        lbl = Label(menu, text="Hello World!", bg="#007200", fg="#ccff33", font="Consolas 12 bold")
        lbl.place(x=70, y=100)

        menu.mainloop()


LoginForm(root)
# run the program
root.mainloop()
