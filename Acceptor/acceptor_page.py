from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

window = Tk()
window.title('Tkinter Place Geometry Manager')
window.geometry("1000x800")

label1=Label(text="ACCEPTOR PAGE INFORMATION",bg="black",fg="white",font=("courier",20,"bold"))
label1.place(x=525,y=50,width=400,height=100)

bloodgroups=["A+","A-","B+","B-","AB+","AB-","O+","O-"]

label2 = ttk.Combobox(window,values=bloodgroups,state="readonly")
label2.set("Blood Group")
label2.place(x=500,y=250,width=130, height=60)

location=["Pune","Mumbai","Nashik"]

label3=ttk.Combobox(window,values=location,state="readonly")
label3.set("Location")
label3.place(x=850,y=250,width=100,height=60)



data = [
   ["Pratik","B+","Sinhgad College, Pune, 411041", "Ph.No:9607271171"],
   ["Prashik","A-","Baner, Pune, 411046","Ph.No:1234567890"],
   ["Aashu","O+","Dadar,Mumbai","Ph.No:1234567890"],
   ["Akshat","AB-", "Thane, Mumbai","Ph.No:12345678990"],
]
index=0


def read_data():
   for index, line in enumerate(data):
      tree.insert('', tk.END, iid = index,
         text = line[0], values = line[1:])
columns = ("age", "salary","phno")

tree= ttk.Treeview(window, columns=columns ,height = 20)
tree.place(x=300,y=450)

tree.heading('#0', text='Name')
tree.heading('age', text='Blood Group')
tree.heading('salary', text='Address')
tree.heading('phno',text='Phone Number')

read_data()



window.mainloop()