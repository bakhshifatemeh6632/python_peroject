from tkinter import *
import tkinter.messagebox as messagebox
import sqlite3
import os
import random
import string
import pyperclip

# from PIL import ImageTk, Image

# con = sqlite3.connect("librery_ketab.db")
# c = con.cursor()

# try:
#     c.execute(
#         """CREATE TABLE sabt_karmandan(
#             code_meli INTEGER PRIMARY KEY,
#             name text NOT NULL,
#             Pass text NOT NULL,
#             email text NOT NULL,
#
#             )
#         """
#     )
#     con.commit()
# except sqlite3.OperationalError:
#     print("database already exists")



# sabt=sqlite3.connect("librery_sabt_karamnd")
# sbt=sabt.cursor()
# sbt.execute("""CREATE TABLE librery_sabt_karamnd(cod_meli int  PRIMARY KEY ,name text NOT NULL,email text NOT NULL,pass int NOT NULL)""")
# sabt.commit()
# sabt.close()
main_page = Tk()
main_page.title = "ثبت کاربر"
main_page.geometry("500x500")
main_page.config(bg="white")
username_l = Label(
    main_page, text="نام کاربری", font=("Tahoma", 12), pady=10, bg="white"
)
username_l.place(relx=0.20, rely=0.35)
username_E = Entry(main_page)
username_E.place(relx=0.35, rely=0.38)

# def pass label And Entry
userpass_l = Label(main_page, text="گذر واژه", font=("Tahoma", 12), pady=10, bg="white")
userpass_l.place(relx=0.20, rely=0.42)
userpass_E = Entry(main_page)
userpass_E.place(relx=0.35, rely=0.45)

# def email label And Entry
userEmail_l = Label(main_page, text="ایمیل", font=("Tahoma", 12), pady=10, bg="white")
userEmail_l.place(relx=0.20, rely=0.50)
userEmail_E = Entry(main_page)
userEmail_E.place(relx=0.35, rely=0.52)

# def ID label for Generat password
pass_generate_l = Label(main_page, text="پسورد", font=("Tahoma", 12), pady=10, bg="white")
pass_generate_l.place(relx=0.25, rely=0.14)
pass_generate = Label(main_page, bg="red", width=15)
pass_generate.place(relx=0.35, rely=0.17)

# #def ID label for Generat password
# userID_l_e = Label(main_page, text="ID_user", font=("Tahoma", 12), pady=10, bg="white")
# userID_l_e.place(relx=0.20, rely=0.65)
# user_ID_l_E = Entry(main_page)
# user_ID_l_E.place(relx=0.35, rely=0.67)


# define Exit button function
def exit():
    os.system("python main.py")
def random_string_generator(str_size, allowed_chars):
    return "".join(random.choice(allowed_chars) for x in range(str_size))


def random_ramz():
    chars = (
            string.ascii_letters + string.punctuation + string.digits + string.ascii_lowercase
    )
    size = 8
    ramz = random_string_generator(size, chars)
    pyperclip.copy(ramz)
    pass_generate.config(text=ramz)
    messagebox.showinfo("پسورد ذخیره شد", " کنید paste")


def exit_command():
    main_page.destroy()


# create  Button exit
exit_b = Button(main_page, text="خروج", padx=10, command=exit)
exit_b.place(relx=0.30, rely=0.80)

# creat label user_cod_meli Entry
user_cod_meli_l = Label(
    main_page, text="کدملی", font=("Tahoma", 12), pady=10, bg="white"
)
user_cod_meli_l.place(relx=0.20, rely=0.58)
user_cod_meli_E = Entry(main_page)
user_cod_meli_E.place(relx=0.35, rely=0.60)


# defin username label And Entry
def Add_karmand():
    user_name = username_E.get()
    user_pass = userpass_E.get()
    user_email = userEmail_E.get()
    user_code_meli = user_cod_meli_E.get()


    if (
            len(user_name) == 0
            or len(user_pass) == 0
            or len(user_email) == 0
            or len(user_code_meli) == 0
    ):
        messagebox.showinfo("warning", "هیچ فیلدی نباید خالی باشد")
        return 0
    if len(user_code_meli) != 10:
        user_cod_meli_E.delete(0, END)
        messagebox.showinfo("warning", "کد ملی باید ده رقم باشد")
        return 0
    if len(user_pass) != 8:
        userpass_E.delete(0, END)
        messagebox.showinfo("warning", "پسورد باید هشت رقم باشد")
        return 0
    con = sqlite3.connect('librery_sabt_karamnd')
    c = con.cursor()
    c.execute("SELECT * FROM librery_sabt_karamnd WHERE cod_meli=?", (user_code_meli,))
    exist = c.fetchall()
    if not exist:
        c.execute(
            "INSERT INTO librery_sabt_karamnd(name,Pass,email,cod_meli) VALUES (?, ?, ?,?);",
            (user_name, user_pass, user_email, user_code_meli),
        )
        con.commit()
        messagebox.showinfo("Warning", "کابر جدید ثبت شد")
    else:
        user_cod_meli_E.delete(0, END)
        messagebox.showinfo("Warning", "این کدملی استفاده شده است ")

    # main_page.destroy()



# def Button Login
login_b = Button(main_page, text="ثبت کاربر", padx=10, command=Add_karmand)
login_b.place(relx=0.50, rely=0.80)
login_b = Button(main_page, text="پسورد یونیک ", padx=10, command=random_ramz)
login_b.place(relx=0.60, rely=0.16)

main_page.mainloop()
