from tkinter import *
from  tkinter import ttk
import tkinter.messagebox as messagebox
import sqlite3
import os
from PIL import ImageTk, Image

# add_ozve=sqlite3.connect("add_ozve")
# add=add_ozve.cursor()
# add.execute("""CREATE TABLE add_ozve(code_meli int  PRIMARY KEY ,name text NOT NULL,l_name text NOT NULL,Gender text NOT NULL,dad_name text NOT NULL,
# job text NOT NULL,year int NOT NULL,month int NOT NULL,day int NOT NULL,educ text NOT NULL,tell int NOT NULL,phone int NOT NULL,address text NOT NULL)""")
# add_ozve.commit()
# add_ozve.close()
sabt_ozve=Tk()
sabt_ozve.geometry("1000x400")
back="#DAF7A6"
sabt_ozve.config(bg=back)
label_name_ozve=Label(sabt_ozve,bg=back,fg="black",text="نام متقاضی")
label_name_ozve.place(relx=0.08,rely=0.03)
entry_name_ozve=Entry(sabt_ozve)
entry_name_ozve.place(relx=0.05,rely=0.10)
label_lname_ozve=Label(sabt_ozve,bg=back,fg="black",text="نام خانوادگی متقاضی")
label_lname_ozve.place(relx=0.25,rely=0.03)
entry_lname_ozve=Entry(sabt_ozve)
entry_lname_ozve.place(relx=0.25,rely=0.10)
label_sex=Label(sabt_ozve,bg=back,fg="black",text="جنسیت")
label_sex.place(relx=0.50,rely=0.03)
L_gender = ttk.Combobox(
    state="readonly",
    values=["زن", "مرد"])
label_job=Label(sabt_ozve,bg=back,fg="black",text="شغل")
label_job.place(relx=0.10,rely=0.22)
entry_job=Entry(sabt_ozve)
entry_job.place(relx=0.05,rely=0.30)
label_tel=Label(sabt_ozve,bg=back,fg="black",text="تلفن ثابت")
label_tel.place(relx=0.09,rely=0.38)
entry_tel=Entry(sabt_ozve)
entry_tel.place(relx=0.05,rely=0.48)
label_phone=Label(sabt_ozve,bg=back,fg="black",text="تلفن همراه")
label_phone.place(relx=0.30,rely=0.38)
entry_phone=Entry(sabt_ozve)
entry_phone.place(relx=0.26,rely=0.48)
label_addres=Label(sabt_ozve,bg=back,fg="black",text="آدرس")
label_addres.place(relx=0.55,rely=0.40)
entry_addres=Entry(sabt_ozve,width=55)
entry_addres.place(relx=0.45,rely=0.48)
label_year_tavalod=Label(sabt_ozve,bg=back,fg="black",text="سال تولد")
label_year_tavalod.place(relx=0.30,rely=0.22)
entry_year_tavalod=Entry(sabt_ozve)
entry_year_tavalod.place(relx=0.25,rely=0.30)
label_h_b_m =Label(sabt_ozve,bg=back,fg="black",text="ماه تولد")
label_h_b_m.place(relx=0.50,rely=0.22)
h_b_m = ttk.Combobox(
    justify="center",
    state="readonly",
    values=["فروردین",
            "اردیبهشت",
            "خرداد",
            "تیر",
            "مرداد" ,
             "شهریور" ,
            "مهر"  ,
            "آبان",
            "آذر",
            "دی",
            "بهمن" ,
            "اسفند"])
label_h_b_r =Label(sabt_ozve,bg=back,fg="black",text="روز")
label_h_b_r.place(relx=0.70,rely=0.22)
h_b_r = ttk.Combobox(
    justify="center",
    state="readonly",
    values=["1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29" ,
            "30" ,
            "31"  ,
            ])
label_h_b_m =Label(sabt_ozve,bg=back,fg="black",text="تحصیلات")
label_h_b_m.place(relx=0.85,rely=0.22)
educ = ttk.Combobox(
    justify="center",
    state="readonly",
    values=["دیپلم",
            "فوق دیپلم",
            "لیسانس",
            "فوق لیسانس",
            "دکترا",
            "موارد دیگر",

            ])


def add_ozve():
    name_ozve = entry_name_ozve.get()
    family = entry_lname_ozve.get()
    name_dad = entry_name_dad.get()
    gender =L_gender.get()
    cod_meli_o=entry_code_meli.get()
    job=entry_job.get()
    year_o=entry_year_tavalod.get()
    month_o=h_b_m.get()
    day_o=h_b_r.get()
    educ_o=educ.get()
    tell=entry_tel.get()
    phone=entry_phone.get()
    addres=entry_addres.get()
    if    (
          len(name_ozve) == 0
          or len(family) == 0
          or len(name_dad) == 0
          or len(gender) == 0
          or len(cod_meli_o) == 0
          or len(job) == 0
          or len(year_o) == 0
          or len(month_o) == 0
          or len(day_o) == 0
          or len(educ_o) == 0
          or len(tell) == 0
          or len(phone) == 0
          or len(addres) == 0
         ):
      messagebox.showinfo("warning", "هیچ فیلدی نباید خالی باشد")
      return 0
    if  not isinstance(cod_meli_o, int) :
         entry_code_meli.delete(0, END)
         messagebox.showinfo("warning", "کد ملی باید یک عدد ده رقمی باشد")
         return 0

    con = sqlite3.connect('add_ozve')
    c = con.cursor()
    c.execute("SELECT * FROM add_ozve WHERE cod_meli=?", (cod_meli_o,))
    exist = c.fetchall()
    if not exist:
        c.execute(
            "INSERT INTO sabte_book(code_meli,name ,l_name ,Gender ,dad_name ,job ,year ,month ,day ,educ ,tell ,phone ,address ) VALUES (?,?,?,?,?,?,?,?,?,?, ?, ?,?);",
            ( name_ozve,family,name_dad,gender,cod_meli_o,job,year_o,month_o,day_o,educ_o,tell,phone,addres),
        )
        con.commit()
        messagebox.showinfo("انجام شد", "عضو جدید ثبت شد")
    else:
        entry_code_meli.delete(0, END)
        messagebox.showinfo("Warning", "این کد ملی قبلا ثبت شده است ")
label_name_dad=Label(sabt_ozve,bg=back,fg="black",text="نام پدر")
label_name_dad.place(relx=0.68,rely=0.03)
entry_name_dad=Entry(sabt_ozve)
entry_name_dad.place(relx=0.65,rely=0.10)
label_code_meli=Label(sabt_ozve,bg=back,fg="black",text="کد ملی")
label_code_meli.place(relx=0.83,rely=0.03)
entry_code_meli=Entry(sabt_ozve)
entry_code_meli.place(relx=0.80,rely=0.10)
add_ketab=Button(sabt_ozve,bg="red",fg="black",command=add_ozve,text="ثبت متقاضی")
add_ketab.place(relx=0.22,rely=0.65)
#Lb1.pack()
L_gender.place(relx=0.45,rely=0.10)
h_b_m.place(relx=0.45,rely=0.30)
h_b_r.place(relx=0.65,rely=0.30)
educ.place(relx=0.80,rely=0.30)
sabt_ozve.mainloop()