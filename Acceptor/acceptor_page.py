from tkinter import  *
from PIL import Image,ImageTk


window=Tk()
window.title("Acceptor Page")
window.geometry("700x700")

#Background Color
window.configure(bg="white")

#BACKGROUND IMAGE
bg_img=Image.open("blood_bank.png")
bg_resize=bg_img.resize((700 , 700))
bg=ImageTk.PhotoImage(bg_resize)


bg_label=Label(window,image=bg)
bg_label.place(x=0,y=0)

title=Label(window,text="This Is The Acceptor Page Details")
title.pack()


options=["Blood group A+","Blood group B+","Blood group AB+","Blood group A-","Blood group B-","Blood group AB-","Blood group O+","Blood group O-"]
selected_option=StringVar()

for option in options:
    radio_button=Radiobutton(window,text=option,variable=selected_option,value=option)
    radio_button.pack()

get_selected_option_button = Button(window, text="Get Selected Option", command=lambda: print(selected_option.get()))
get_selected_option_button.pack()

window.mainloop()