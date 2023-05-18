from tkinter import *
from  tkinter import ttk
import tkinter.messagebox as messagebox
import sqlite3
import os
from PIL import ImageTk, Image

# sabt_book=sqlite3.connect("sabte_book")
# sbt=sabt_book.cursor()
# sbt.execute("""CREATE TABLE sabte_book(shabak int  PRIMARY KEY ,name_book text NOT NULL,name_Autor text NOT NULL,catgory text NOT NULL)""")
# sabt_book.commit()
# sabt_book.close()
sabt_ketab=Tk()
sabt_ketab.geometry("700x400")
back="#DAF7A6"
sabt_ketab.config(bg=back)
label_name_ketab=Label(sabt_ketab,bg=back,fg="black",text="نام کتاب")
label_name_ketab.place(relx=0.08,rely=0.05)
entry_name_ketab=Entry(sabt_ketab)
entry_name_ketab.place(relx=0.05,rely=0.10)
label_category=Label(sabt_ketab,bg=back,fg="black",text="دسته بندی کتاب")
label_category.place(relx=0.27,rely=0.05)
Lb1 = ttk.Combobox(
    state="readonly",
    values=["روانشناسی", "درسی", "سیاسی","تاریخی" ,"رمان"]

)
def add_ketab():
    book_name = entry_name_ketab.get()
    name_Autor = entry_name_Autor.get()
    cat_book = Lb1.get()
    shabak_book =entry_shabak_ketab.get()
    if (
            len(book_name) == 0
            or len(name_Autor) == 0
            or len(cat_book) == 0
            or len(shabak_book) == 0
    ):
        messagebox.showinfo("warning", "هیچ فیلدی نباید خالی باشد")
        return 0
    if len(shabak_book) != 13 or not isinstance(shabak_book, int) :
        entry_shabak_ketab.delete(0, END)
        messagebox.showinfo("warning", "شابک باید یک عدد سیزده رقمی باشد")
        return 0
    # if not isinstance(shabak_book, int) :
    #     #shabak_book.delete(0, END)
    #     messagebox.showinfo("warning", "َشابک باید رقم باشد")
    #     return 0



    con = sqlite3.connect('sabte_book')
    c = con.cursor()
    c.execute("SELECT * FROM sabte_book WHERE shabak=?", (shabak_book,))
    exist = c.fetchall()
    if not exist:
        c.execute(
            "INSERT INTO sabte_book(shabak,name_book,name_Autor,catgory) VALUES (?, ?, ?,?);",
            (shabak_book,book_name, name_Autor, cat_book),
        )
        con.commit()
        messagebox.showinfo("انجام شد", "کتاب جدید ثبت شد")
    else:
        entry_shabak_ketab.delete(0, END)
        messagebox.showinfo("Warning", "این شابک قبلا ثبت شده است ")
label_name_Autor=Label(sabt_ketab,bg=back,fg="black",text="نام نویسنده")
label_name_Autor.place(relx=0.55,rely=0.05)
entry_name_Autor=Entry(sabt_ketab)
entry_name_Autor.place(relx=0.50,rely=0.10)
shabak_ketab=Label(sabt_ketab,bg=back,fg="black",text="شابک کتاب")
shabak_ketab.place(relx=0.75,rely=0.05)
entry_shabak_ketab=Entry(sabt_ketab)
entry_shabak_ketab.place(relx=0.70,rely=0.10)
add_ketab=Button(sabt_ketab,bg="red",fg="black",command=add_ketab,text="ثبت کتاب")
add_ketab.place(relx=0.15,rely=0.65)
#Lb1.pack()
Lb1.place(relx=0.25,rely=0.10)
sabt_ketab.mainloop()