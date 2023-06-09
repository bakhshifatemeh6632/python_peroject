from tkinter import *
import random
import sqlite3
import tkinter.messagebox as messagebox
from tkinter import filedialog
import pyperclip
from openpyxl import load_workbook

main_page = Tk()
main_page.title("صفحه اصلی")
main_page.resizable = False
main_page.geometry("750x300")
back = "#F08080"
main_page.config(bg=back)
fram_del = Frame(main_page, bg="red")
fram_del.pack()


def open_excel_file():
    global matn
    file_path = filedialog.askopenfile(filetypes=[("Txt Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(matn)


# creat Data base
try:
    con = sqlite3.connect("user")
    c = con.cursor()
    c.execute(
        """CREATE TABLE user(user_name text  NOT NULL ,email text PRIMARY KEY,pass text NOT NULL)"""
    )
    con.commit()
    con.close()
except:
    pass

frame_insert = Frame(main_page, bg=back)
frame_insert.config(
    width=400,
    height=500,
)
frame_insert.pack(side=LEFT)
frame_delet = Frame(main_page, bg="#C70039")
frame_delet.config(width=400, height=500)
frame_delet.pack(side=RIGHT)


def Run():
    global user_name, email_address, p
    email_address = entry_email.get().strip()
    pass_len = entry_count_pass.get()
    if (
        pass_len != ""
        and email_address != ""
        and "@" in email_address
        and "." in email_address
    ):
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        pass1 = int(pass_len)
        valid_characters = {"@", ".", "_"}
        for character in email_address:
            if character in valid_characters:
                p = "".join(random.sample(s, pass1))
                user_name = email_address.split("@")[1]
                label_info.config(text=email_address, bg="red")
                label_us_pass.config(
                    bg="red", text=f"user: {user_name}.\npassword: {p}"
                )
    else:
        messagebox.showinfo("Warning", "Please enter all the required information")


def search():
    s = entry_email.get()
    if s == "":
        messagebox.showinfo("Warning", "Please enter an email to search for")
        return False
    elif "@" not in s or "." not in s:
        print(s)
        messagebox.showinfo("Warning", "لطفا ایمیل را به درستی وارد نمایید")
        return False
    con = sqlite3.connect("user")
    c = con.cursor()
    c.execute("SELECT user_name,email,pass FROM user WHERE email=?", (s,))
    exist = c.fetchall()
    for x in exist:
        field1_value = x[0]
        field2_value = x[1]
        field3_value = x[2]
        label_info.config(
            text=f"username: {field1_value}\npass: {field3_value}", bg="yellow"
        )
    if exist:
        messagebox.showinfo("Erorr", "کاربری با این ایمیل وجود دارد")
        con.commit()
        con.close()
        entry_email.delete(0, END)
        return True
    if not exist:
        messagebox.showinfo("info", "این ایمیل برای ثبت نام معتبر می باشد")
        label_info.config(text="", bg=back)
        label_us_pass.config(text="", bg=back)
        return False


def Insert():
    con = sqlite3.connect("user")
    c = con.cursor()
    c.execute(
        "INSERT INTO user values(:Username,:USERemail,:Userpassword)",
        {
            "Username": user_name,
            "USERemail": email_address,
            "Userpassword": p,
        },
    )
    con.commit()
    con.close()
    messagebox.showinfo("Warning", "کابر جدید ثبت شد")
    entry_email.delete(0, END)
    entry_count_pass.delete(0, END)
    label_info.config(text="", bg=back)
    label_us_pass.config(text="", bg=back)


def copy():
    global p, matn
    matn = str(pyperclip.copy(p))
    messagebox.showinfo("copy", "پسورد شما کپی شد")


# design_label_caption
label_caption = Label(frame_insert, bg=back, text="Input Email :")
label_caption.place(relx=0.01, rely=0.05)
label_caption_pass = Label(frame_insert, bg=back, text="Input Len password: ")
label_caption_pass.place(relx=0.01, rely=0.13)
# design_label_Show_information
label_info = Label(frame_insert, bg=back)
label_info.place(relx=0.45, rely=0.40)
# design_label_Show_usre_pass
label_us_pass = Label(frame_insert, bg=back)
label_us_pass.place(relx=0.45, rely=0.50)
# design_Entry_for_Email
entry_email = Entry(frame_insert, width=25)
entry_email.place(relx=0.25, rely=0.05)
# design_Entry_for_search
btn_search = Button(frame_insert, bg=back, text="search", command=search)
btn_search.place(relx=0.64, rely=0.05)
# design_Entry_for_count_pass
entry_count_pass = Entry(frame_insert, width=25)
entry_count_pass.place(relx=0.29, rely=0.13)
# design_Entry_for_Delet_account
entry_count_dele = Entry(frame_delet, width=25)
entry_count_dele.place(relx=0.25, rely=0.20)
# design_label_Show_usre_pass
label_us_del = Label(frame_delet, text="Email for del", bg=back)
label_us_del.place(relx=0.05, rely=0.20)
# design_Run_Button
Button_run = Button(frame_insert, text="Run", bg="#C70039", command=Run)
Button_run.place(relx=0.30, rely=0.30)
# design_insert_Button
Button_insert = Button(frame_insert, text="Insert", bg="#C70039", command=Insert)
Button_insert.place(relx=0.46, rely=0.30)
# design_copy_Button
Button_copy = Button(frame_insert, text="copy", bg="#C70039", command=copy)
Button_copy.place(relx=0.57, rely=0.30)
# design_open_Button
Button_copy = Button(
    frame_insert, text="open file", bg="#C70039", command=open_excel_file
)
Button_copy.place(relx=0.67, rely=0.30)


def delete():
    global entry_count_dele
    dele_email = entry_count_dele.get()
    con = sqlite3.connect("user")
    c = con.cursor()
    c.execute("SELECT * FROM user WHERE email=?", (dele_email,))
    exist = c.fetchall()
    if not exist:
        messagebox.showinfo("Erorr", "کاربری با این ایمل وجود ندارد")
    else:
        sql = """DELETE FROM user WHERE email=?"""
        c.execute(sql, (dele_email,))

        con.commit()
        con.close()
        messagebox.showinfo("Warning", "کابر مورد نظر حذف شد")
        entry_count_dele.delete(0, END)


Button_delet = Button(frame_delet, text="Delete", bg=back, command=delete)
Button_delet.place(relx=0.55, rely=0.30)
# design_Exit_Button
Button_exit = Button(frame_insert, text="Exit", command=exit, bg="#C70039")
Button_exit.place(relx=0.38, rely=0.30)

main_page.mainloop()
