from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
###########################################
import csv
import time

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw=file writer
        fw.writerow(datalist) #datalist = ['pen','pencil','eraser']

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fw=file reader
        data = list(fr)
    return data

###เวลา

def update_time():
    current_time = time.strftime('%H:%M:%S')
    current_date = time.strftime('%d / %m / %y')
    timelabel.config(text=current_time)
    datelabel.config(text=current_date)
    GUI.after(1000, update_time)

GUI = Tk() #จอหลัก
GUI.title('โปรแกรมลงเวลาเข้า-ออกงาน') #ชื่อโปรแกรม
GUI.geometry('600x600') #ขนาดโปรแกรม

L1 = Label (GUI,text='โปรแกรมลงเวลาเข้า-ออกงาน',font=('Tahoma',20),fg='black')
L1.place(x=140,y=70)

datelabel = ttk.Label(GUI, font=('Tahoma', 20))
datelabel.place(x=235,y=120)

timelabel = ttk.Label(GUI, font=('Tahoma', 20))
timelabel.place(x=250,y=150)

LF1 = ttk.LabelFrame(GUI,text='รหัสพนักงาน')
LF1.place(x=100,y=200)

v_data = StringVar() #ตัวแปรพิเศษ
E1 = ttk.Entry(LF1,textvariable=v_data, font=('Tahoma',25))
E1.pack(padx=10,pady=10)

from datetime import datetime

def SaveData1():
    t = datetime.now().strftime('%H:%M:%S')
    d = datetime.now().strftime('%d/%m/%Y')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร
    text = [d,t,'in',data] #[เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูล
    messagebox.showinfo('ลงเวลาเข้างาน', 'รหัส ' + data + ' เข้างาน วันที่ ' + d + ' เวลา ' + t)

def SaveData2():
    t = datetime.now().strftime('%H:%M:%S')
    d = datetime.now().strftime('%d/%m/%Y')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร
    text = [d,t,'out',data] #[เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูล
    messagebox.showinfo('ลงเวลาออกงาน', 'รหัส ' + data + ' ออกงาน วันที่ ' + d + ' เวลา ' + t)

B1=ttk.Button(LF1,text='เข้างาน',command=SaveData1)
B1.pack(ipadx=20, ipady=20)

B2=ttk.Button(LF1, text='ออกงาน',command=SaveData2)
B2.pack(ipadx=20, ipady=20)

update_time()
GUI.mainloop()
