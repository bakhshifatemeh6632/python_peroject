from tkinter import *
import tkinter.messagebox as messagebox
import sqlite3
import os
from PIL import ImageTk, Image
page_asli=Tk()
back="#9FE2BF"
page_asli.geometry("600x450")
page_asli.config(bg=back)
#design_Button
sabt_ozve=Button(page_asli,bg="#FFBF00",width=35,fg="black",text="ثبت عضو جدید")
sabt_ozve.place(relx=0.05,rely=0.05)
sabt_katab=Button(page_asli,bg="#FFBF00",width=35,fg="black",text="ثبت کتاب جدید")
sabt_katab.place(relx=0.55,rely=0.05)
serch_ketab=Button(page_asli,bg="#FFBF00",width=35,fg="black",text="جستجو کتاب")
serch_ketab.place(relx=0.05,rely=0.25)
serch_ozve=Button(page_asli,bg="#FFBF00",width=35,fg="black",text="جستجو کتاب")
serch_ozve.place(relx=0.55,rely=0.25)
#button_back
button_back=Button(page_asli,bg="#FFBF00",fg="black",text="صفحه اصلی")
button_back.place(relx=0.55,rely=0.65)
page_asli.mainloop()