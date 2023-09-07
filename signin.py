from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  db="classdata"
)

cur = mydb.cursor()
if cur:
   pass
else:
    print("Connection not successfull..")
query2 = "select name from students where email=123456"
cur.execute(query2)

table = cur.fetchall()
for row in table:
    pass





#print(table)
def Ok():
    uname = str(e1.get())
    pas=str(e2.get())
    if(uname==row[0]):
       l3=Label(root,text="Login successfull....").place(x=10, y=200)
    else:
       l3=Label(root,text="Login unsuccessfull....").place(x=10, y=200)

root = Tk()
root.title("Login System")
root.geometry("300x400")

global e1
global e2
global e3
global totText
global avgText
global gradeText

un = StringVar()
ps = StringVar()

Label(root, text="Username").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=60)


e1 = Entry(root)
e1.place(x=100, y=10,width=300,height=30)

e2 = Entry(root)
e2.place(x=100, y=70,width=300,height=30)



username = Label(root, text="ssss", textvariable=un).place(x=100, y=110)
passw = Label(root, text="", textvariable=ps).place(x=100, y=140)


Button(root, text="Login", command=Ok ,height = 2, width = 13).place(x=10, y=160)

marks1 = Entry(root)
marks2 = Entry(root)

root.mainloop()
