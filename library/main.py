from tkinter import *
import tkinter.messagebox as messagebox
import sqlite3
import os
from PIL import ImageTk, Image
# sabt=sqlite3.connect("librery_Account")
# sbt=sabt.cursor()
# sbt.execute("""CREATE TABLE sabt_karbar(cod_meli int  PRIMARY KEY ,name text NOT NULL,lastname text NOT NULL ,email text NOT NULL)""")
# sabt.commit()
# sabt.close()
main_page=Tk()
main_page.title="صفحه ورود"
main_page.geometry("500x500")
main_page.config(bg="white")
#def username label And Entry
username_l=Label(main_page,text="نام کاربری",font=("Tahoma",12),pady=10,bg="white")
username_l.place(relx=0.20,rely=0.35)
username_E=Entry(main_page)
username_E.place(relx=0.35,rely=0.38)
#def pass label And Entry
userpass_l=Label(main_page,text="گذر واژه",font=("Tahoma",12),pady=10,bg="white")
userpass_l.place(relx=0.20,rely=0.42)
userpass_E=Entry(main_page)
userpass_E.place(relx=0.35,rely=0.45)
#def Button Login
login_b=Button(main_page,text="ورود",padx=10)
login_b.place(relx=0.45,rely=0.55)
#def Button sabt_karabar
add_karabar=Button(main_page,text="ثبت کاربر",padx=10)
add_karabar.place(relx=0.60,rely=0.55)
#def_Button exit
exit_b=Button(main_page,text="خروج",padx=10,command=exit)
exit_b.place(relx=0.30,rely=0.55)
#Image
ax=Image.open('p1.png')
ax=ax.resize((200,100),Image.LANCZOS)
userIMG=ImageTk.PhotoImage(ax)
img_label=Label(main_page,image=userIMG)
img_label.place(relx=0.30,rely=0.10)
main_page.mainloop()