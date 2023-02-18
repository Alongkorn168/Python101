from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI = Tk() #จอหลัก
GUI.title('โปรแกรมคำนวณเกรดเฉลี่ย GPA Calculator') #ชื่อโปรแกรม
GUI.geometry('950x600') #ขนาดโปรแกรม

image = PhotoImage(file = "3755243.png")
label = Label(GUI, image = image)
label.place(x=50,y=50)

L1 = Label (GUI,text='โปรแกรมคำนวณเกรดเฉลี่ย GPA Calculator',font=('Tahoma',30),fg='black')
L1.place(x=150,y=70)

#รวมคะแนน
def sum():
    course = selected_option.get()
    score1 = int(scorebox1.get())
    score2 = int(scorebox2.get())
    score3 = int(scorebox3.get())
    score4 = int(scorebox4.get())
    score_sum = score1 + score2 + score3 + score4
#คำนวณเกรด
    if score_sum >= 80:
        grade = 'A'
    elif score_sum >=75:
        grade = 'B+'
    elif score_sum >=70:
        grade = 'B'
    elif score_sum >=65:
        grade = 'C+'
    elif score_sum >=60:
        grade = 'C'
    elif score_sum >=55:
        grade = 'D+'
    elif score_sum >=50:
        grade = 'D'
    else:
        grade = 'F'
#แสดงผล
    messagebox.showinfo('คะแนนรวมและเกรด / Total Score and Grade', 'คะแนนรวมของท่านในกระบวนวิชา ' + course + ' คือ ' + str(score_sum) + ' คะแนน' +'เกรดที่ได้คือเกรด ' + grade )
    messagebox.showinfo('คะแนนรวมและเกรด / Total Score and Grade', 'Your score in ' + course + ' is ' + str(score_sum) + ' points ' +'Your grade is ' + grade )

FB1 = LabelFrame(GUI,text='เลือกรายละเอียดกระบวนวิชา / Select Course', width=200 , height=200)
FB1.place(x=100,y=200)
L2 = Label (FB1,text='กระบวนวิชา / Course',font=('Tahoma',10))
L2.pack(ipadx=10,ipady=10,padx=10,pady=10)
#กำหนดลิสต์ใน dropdown
options = ["001101 - Fundamental English 1","001102 - Fundamental English 2", "204105 - Introduction to Python"]

selected_option = StringVar(FB1)
selected_option.set(options[0])

#สร้าง drop down
dropdown = ttk.Combobox(FB1, values=options)
dropdown.pack(ipadx=40,ipady=5)
###############

#กรอกคะแนน
FB2 = LabelFrame(GUI,text='กรอกคะแนน / Score Input')
FB2.place(x=400,y=200)
#คะแนน1
L2 = Label (FB2,text='คะแนน 1 (25) / Score 1 (25)',font=('Tahoma',10))
L2.pack()

scorebox1 = Spinbox(FB2, from_=0, to=25)
scorebox1.pack()

#คะแนน2
L3 = Label (FB2,text='คะแนน 2 (25) / Score 2 (25)',font=('Tahoma',10))
L3.pack()

scorebox2 = Spinbox(FB2, from_=0, to=25)
scorebox2.pack()

#คะแนน3
L4 = Label (FB2,text='คะแนน 3 (25) / Score 3 (25)',font=('Tahoma',10))
L4.pack()

scorebox3 = Spinbox(FB2, from_=0, to=25)
scorebox3.pack()

#คะแนน4
L5 = Label (FB2,text='คะแนน 4 (25) / Score 4 (25)',font=('Tahoma',10))
L5.pack()

scorebox4 = Spinbox(FB2, from_=0, to=25)
scorebox4.pack()

B2 = ttk.Button(FB2, text='คำนวณ / Calculate', command=sum)
B2.pack(ipadx=20,ipady=20,padx=20,pady=20)

#########

GUI.mainloop()
