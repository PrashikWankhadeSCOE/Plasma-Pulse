from tkinter import *
from PIL import Image,ImageTk
import customtkinter 



#main display
root=Tk()
root.geometry("1000x800")
root.title("Blood Bank Management System")
 

#background color
root.configure(bg="black")
root.resizable( 0,0 )


#background photo
bg_img=Image.open("blood_bank_logoo.png")
bg_resize=bg_img.resize((1000,800))
bg=ImageTk.PhotoImage(bg_resize)
background_image=Label(image=bg)
background_image.place(x=0,y=0)



#importing logo
'''photo=Image.open("logoo.png")
photo_resize=photo.resize((100,100))
photo_img=ImageTk.PhotoImage(photo_resize)
photo_label=Label(image=photo_img)
photo_label.place(x=10,y=10)'''

#inserting HEADING
Label(text="Save a life: Donate Blood!",font=("Lucida Fax",18,"italic" ,"bold","underline"),bg="pink1",fg="black",pady=15,borderwidth=4 ,relief=RAISED).place(x=500,y=60)

#giving info about the website
Label(text='''About US: Welcome to our Blood Bank Management System,
           a vital platform dedicated to serving the community of Pune and beyond.
           Located in the heart of Pune, our website offers a seamless experience for
           individuals seeking blood donations, as well as those looking to contribute 
           to the cause of saving lives. Our platform acts as a centralized hub, connecting
           donors with recipients in need, ensuring timely access to life-saving blood products.
           Through our user-friendly interface, donors can register, schedule appointments, 
           and conveniently locate nearby blood donation events. Recipients can search for 
           compatible donors and request blood units as per their specific requirements.
           Beyond facilitating blood donations, our website serves as a catalyst for community wellness. 
           Join us in our mission to make a difference. Together, we can ensure 
           that no life is lost due to a shortage of blood.''',font=("gadugi",10),bg="pink1",fg="black",pady=15,borderwidth=4,relief=RAISED).place(x=200,y=200)


#DONATE Button
donate_button=customtkinter.CTkButton(root,text="DONATE",font=("Lucida fax",15,"bold"))
donate_button.place(x=350,y=550)
donate_button.bind('<Double-1>',quit)


#NEED Button
need_button=customtkinter.CTkButton(root,text="NEED",fg_color="red",font=("Lucida Fax",15,"bold"))
need_button.place(x=650,y=550)
need_button.bind('<Double-1>',quit)

root.mainloop()


# from tkinter import *
# import customtkinter 
# root=Tk()
# root.geometry("400x600") 
# name=Label(text="hello")
# name.pack()
# user_entry=Entry()
# user_entry.pack()
# button=customtkinter.CTkButton(root,text="Submit")
# button.pack()
# root.mainloop()