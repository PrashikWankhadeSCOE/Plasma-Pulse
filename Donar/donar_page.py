import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog


def submit_form():
    print(f"Name is: {namevalue.get()}")
    print(f"Age is: {agevalue.get()}")
    print(f"Gender : {male.get()}")
    print(f"Female : {female.get()}")
    print(f"Blood Group is: {bg_value.get()}")
    print(f"Address is: {address_value.get()}")
    print(f"Location is: {location_value.get()}")
    
    contact=phoneno_value.get() 
    flag = 1
    if(len(contact)!=10):
        flag=0
        tkinter.messagebox.showerror(title="Error", message="Enter 10 digit number")
        print("Enter 10 digit number")
    
    submit = submit_value.get()
    if(flag==1):
        tkinter.messagebox.showinfo(title="Submit",message="Form Submitted")



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
address_value = StringVar()
location_value = StringVar()
phoneno_value =StringVar()
submit_value = StringVar()


gender_flag=IntVar()

# Form elements
name_label = tk.Label(root, text="Name:",borderwidth=4,font=(15))
name_label.place(x=750,y=250)
name_entry = tk.Entry(root,textvariable=namevalue,font=(15))
name_entry.place(x=850,y=250)

age_label = tk.Label(root, text="Age:",borderwidth=4,font=(15))
age_label.place(x=750,y=300)
age_entry = tk.Entry(root,textvariable=agevalue,font=(15))
age_entry.place(x=850,y=300)

gender_label = tk.Label(root,text="Gender:",borderwidth=4,font=(15))
gender_label.place(x=750,y=350)


#Check box
male1=Radiobutton(text="Male",variable=gender_flag,bg="white",fg="black",value=1)
male1.place(x=850,y=350)

female1=Radiobutton(text="Female",variable=gender_flag,bg="white",fg="black",value=2)
female1.place(x=900,y=350)


bloodgroups = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]

blood_group_label = tk.Label(root, text="Blood Group:",borderwidth=4,font=(15))
blood_group_label.place(x=750,y=400)

blood_group_button = ttk.Combobox(root,values = bloodgroups,state="readonly",textvariable=bg_value)
blood_group_button.set("Select Blood Group")
blood_group_button.place(x=860,y=400)

address_label = tk.Label(root, text="Address:",borderwidth=4,font=(15))
address_label.place(x=750,y=450)
address_entry = tk.Entry(root,textvariable=address_value,font=(15))
address_entry.place(x=850,y=450)

locations = ["Mumbai","Pune","Nashik"]

location_label = tk.Label(root,text="Location:",borderwidth=4,font=(15))
location_label.place(x=750,y=500)

location_button = ttk.Combobox(root,values = locations ,state="readonly",textvariable=location_value)
location_button.set("Select Location")
location_button.place(x=850,y=500)

contact_no_label = tk.Label(root, text="Contact No.:",borderwidth=4,font=(15))
contact_no_label.place(x=750,y=550)
contact_no_entry = tk.Entry(root,textvariable=phoneno_value,font=(15))
contact_no_entry.place(x=850,y=550)


submit_button = tk.Button(root, text="Submit",borderwidth=5, command=submit_form)
submit_button.place(x=850,y=600,width=80)

# Run the main loop
root.mainloop()

def submit_button(self):
    # Validation
    if not all([namevalue, bg, phoneno_value]):
        messagebox.showerror("Error", "Please fill in all required fields.")
        return
    if not phoneno_value.isdigit() or len(phoneno_value) != 10:
        messagebox.showerror("Error", "Please enter a valid 10-digit mobile number.")
        return
    # Form output text
    output_text = f"Name: {namevalue}\n" \
                  f"Mobile No: {int(phoneno_value)}\n" \
                  f"Age: {agevalue}\n" \
                  f"Blood Group : {bg_value}\n"\
                  f"Address : {address_value}\n"\
                  f"Location: {location_value} "
    # Get a reference to the Firestore collection
    user_profiles_ref = db.collection('user_profiles')
    # Create a new user profile entry
    user_profile = {
        'first_name': namevalue,
        'mobile_no': phoneno_value,
        'blood group': bg_value,
        'age': agevalue,
        'address': address_value,
        'Location': location_value
    }
    # Add the user profile to Firestore
    new_user_ref = user_profiles_ref.add(user_profile)
    # Get the unique ID generated by Firestore
    user_id = new_user_ref[1].id
    # Display success message
    success_message = f"Form submitted successfully.\n\n" \
                      f"Firestore User ID: {user_id}\n" \
                      f"{output_text}"
    messagebox.showinfo("Success", success_message)