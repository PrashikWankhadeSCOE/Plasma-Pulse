from tkinter import *
from PIL import Image,ImageTk
import customtkinter 


#main display
root=Tk()
root.geometry("1000x800")
root.title("Blood Bank Management System")
 

#background color
root.configure(bg="black")
# root.resizable( 0,0 )


#background photo
bg=Image.open("first_page/pix.jpg")
bg_resize=bg.resize((1000,800))
#background_image=Label(image=bg)
bg=ImageTk.PhotoImage(bg)
background_image=Label(image=bg)
#background_image=Label(image=bg)
background_image.place(x=0,y=0)



#importing logo
photo=Image.open("first_page/logo.jpg") 
photo_resize=photo.resize((100,100))
photo_img=ImageTk.PhotoImage(photo_resize)
photo_label=Label(image=photo_img)
photo_label.place(x=250,y=150)

#inserting HEADING
Label(text="Save a life: Donate Blood!",font=("Didot",25,"italic" ,"bold","underline"),bg="white",fg="maroon",pady=15,borderwidth=4).place(x=400,y=170)

#giving info about the website
Label(text='''ABOUT US: Welcome to our Blood Bank Management System website!
      We are dedicated to facilitating the vital process of blood donation and distribution
      to save lives. Our platform offers an efficient and secure way for donors to register,
      and track their donations. For hospitals and blood banks, our system provides
      streamlined inventory management, real-time tracking of blood units, and
      automated alerts for critical shortages.Together, we can make a significant 
      impact in ensuring a steady supply of blood for those in need.''',font=("gadugi",11),bg="white",fg="brown4",pady=15,borderwidth=4,relief=RAISED).place(x=250,y=330)


#DONATE Button
donate_button=Button(root,text="DONATE",font=("Lucida fax",20,"bold"),relief=RAISED,borderwidth=5)

donate_button.config(bg="brown3")
donate_button.place(x=300,y=600)
donate_button.bind('<Double-1>',quit)


#NEED Button
need_button= Button(root,text="NEED",font=("Lucida Fax",20,"bold"),relief=RAISED,borderwidth=5)
need_button.config(bg="brown3")
need_button.place(x=650,y=600)
need_button.bind('<Double-1>',quit)

root.mainloop()


 