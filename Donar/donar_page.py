import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter
from PIL import Image,ImageTk
from tkinter import filedialog

def upload_photo():
    file_path = filedialog.askopenfilename()
    if file_path:
        photo_label.config(text="Photo Uploaded!")


def submit_form():
    print(f"Name is: {namevalue.get()}")
    print(f"Age is: {agevalue.get()}")
    print(f"Blood Group is: {bg_value.get()}")
    print(f"Location is: {location_value.get()}")
    #print(f"Contact no. is: {phoneno_value.get()}")
    print(f"Photo is: {photo_value.get()}")
    contact=phoneno_value.get() 
    flag = 1
    if(len(contact)!=10):
        flag=0
        tkinter.messagebox.showerror(title="Hi", message="Enter 10 digit number")
        print("Enter 10 digit number")
    submit = submit_value.get()
    if(flag==1):
        tkinter.messagebox.showinfo(title="submit",message="Form Submitted")
    
# Create main window
root = tk.Tk()
root.title("DONOR INFORMATION")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

bg_image = Image.open("Image.jpg")
bg_resize = bg_image.resize((screen_width,screen_height))
bg = ImageTk.PhotoImage(bg_resize)

bg_label = Label(root,image=bg)
bg_label.place(x=0,y=0)

# Headline
headline_label = tk.Label(root, text="DONOR INFORMATION", font=("poppins", 30,"italic bold"), bg="white",fg="red3")
headline_label.place(x=475,y=50)

#textbox
information_text =tk.Label(root, text="Every day, blood donors help patients of all ages: accident and burn victims," \
                       "heart surgery and organ transplant patients, and those battling cancer.",font=("poppins",12,"italic"),bg="white",fg="red4",wraplength=400)
information_text.place(x=650,y=100)

namevalue= StringVar()
agevalue= StringVar()
bg_value= StringVar()
location_value = StringVar()
phoneno_value =StringVar()
photo_value= IntVar()
submit_value = StringVar()

# Form elements
name_label = tk.Label(root, text="Name:",borderwidth=4,font=(15))
name_label.place(x=700,y=200)
name_entry = tk.Entry(root,textvariable=namevalue,font=(15))
name_entry.place(x=800,y=200)

age_label = tk.Label(root, text="Age:",borderwidth=4,font=(15))
age_label.place(x=700,y=240)
age_entry = tk.Entry(root,textvariable=agevalue,font=(15))
age_entry.place(x=800,y=240)

bloodgroups = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]

blood_group_label = tk.Label(root, text="Blood Group:",borderwidth=4,font=(15))
blood_group_label.place(x=700,y=280)

blood_group_button = ttk.Combobox(root,values = bloodgroups,state="readonly",textvariable=bg_value)
blood_group_button.set("Select Blood Group")
blood_group_button.place(x=805,y=280)

address_label = tk.Label(root, text="Address:",borderwidth=4,font=(15))
address_label.place(x=700,y=320)
address_entry = tk.Entry(root,textvariable=location_value,font=(15))
address_entry.place(x=800,y=320)

contact_no_label = tk.Label(root, text="Contact No.:",borderwidth=4,font=(15))
contact_no_label.place(x=700,y=360)
contact_no_entry = tk.Entry(root,textvariable=phoneno_value,font=(15))
contact_no_entry.place(x=800,y=360)

upload_button = tk.Button(root, text="Upload Photo", command=upload_photo,borderwidth=4,relief=RAISED,font=(15))
upload_button.place(x=750,y=400)
upload_entry = tk.Entry(root)

photo_label = tk.Label(root, text="",fg="black")
photo_label.place(x=750,y=440)

submit_button = tk.Button(root, text="Submit", command=submit_form, bg="green3", fg="white",borderwidth=5,relief=RAISED,textvariable=submit_value)
submit_button.place(x=750,y=480)

# Run the main loop
root.mainloop()