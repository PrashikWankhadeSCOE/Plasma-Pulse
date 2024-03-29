import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


import json
from google.cloud import firestore

import fp  

# Initialize Firestore client
credentials_path = 'setup/your_key.json'
with open(credentials_path) as json_file:
    credentials_info = json.load(json_file)

db = firestore.Client.from_service_account_info(credentials_info)

class DonorInformationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("DONOR INFORMATION")
        self.root.geometry("1000x800")

        # Background Image
        bg_image = Image.open("assets/Image.jpg")
        bg_resize = bg_image.resize((1000,800))
        self.root.resizable(0,0)
        self.bg = ImageTk.PhotoImage(bg_resize)
        self.bg_label = Label(root, image=self.bg)
        self.bg_label.place(x=0, y=0)

        # Headline
        self.headline_label = tk.Label(root, text="DONOR INFORMATION", font=("poppins", 30, "italic bold"),
                                       bg="white", fg="red3")

        self.headline_label.place(x=300, y=50)


        # Textbox
        self.information_text = tk.Label(root, text="Every day, blood donors help patients of all ages: accident "
                                                    "and burn victims, heart surgery and organ transplant patients, "
                                                    "and those battling cancer.", font=("poppins", 12, "italic"),
                                         bg="white", fg="red4", wraplength=400)

        self.information_text.place(x=475, y=120)


        # Initialize variables
        

        # Form elements
        self.name_label = tk.Label(root, text="Name:", borderwidth=4, font=(15))
        self.name_label.place(x=550, y=250)
        self.name_entry = tk.Entry(root, font=(15))
        self.name_entry.place(x=650, y=250)

        self.age_label = tk.Label(root, text="Age:", borderwidth=4, font=(15))
        self.age_label.place(x=550, y=300)
        self.age_entry = tk.Entry(root, font=(15))
        self.age_entry.place(x=650, y=300)

        self.gender_label = tk.Label(root, text="Gender:", borderwidth=4, font=(15))
        self.gender_label.place(x=550, y=350)

        self.gender_entry = tk.Entry(root, font= (15))

        self.gender_entry.place(x=650,y=350)

        self.bloodgroups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

        self.blood_group_label = tk.Label(root, text="Blood Group:", borderwidth=4, font=(15))
        self.blood_group_label.place(x=550, y=400)

        self.blood_group_button = ttk.Combobox(root, values=self.bloodgroups, state="readonly")
        self.blood_group_button.set("Select Blood Group")
        self.blood_group_button.place(x=670, y=400)


        self.address_label = tk.Label(root, text="Address:", borderwidth=4, font=(15))
        self.address_label.place(x=550, y=450)
        self.address_entry = tk.Entry(root, font=(15))
        self.address_entry.place(x=650, y=450)

        self.locations = ["Mumbai", "Pune", "Nashik"]

        self.location_label = tk.Label(root, text="Location:", borderwidth=4, font=(15))
        self.location_label.place(x=550, y=500)

        self.location_button = ttk.Combobox(root, values=self.locations, state="readonly",
                                            )
        self.location_button.set("Select Location")
        self.location_button.place(x=650, y=500)

        self.contact_no_label = tk.Label(root, text="Contact No.:", borderwidth=4, font=(15))
        self.contact_no_label.place(x=550, y=550)
        self.contact_no_entry = tk.Entry(root, font=(15))
        self.contact_no_entry.place(x=650, y=550)

        self.submit_button = tk.Button(root, text="Submit", borderwidth=10,command=self.submit_form)
        self.submit_button.place(x=650, y=600, width=80)

        self.back_button = tk.Button(root,text="Back",borderwidth=5,command=self.go_back)
        self.back_button.place(x=50,y=30)


    def submit_form(self):
        print('submit madhe gela')
    
        # Validation
        namevalue = self.name_entry.get()
        agevalue = self.age_entry.get()
        gendervalue = self.gender_entry.get()
        bg_value = self.blood_group_button.get()
        address_value = self.address_entry.get()
        location_value = self.location_button.get()
        phoneno_value = self.contact_no_entry.get()
        

        if not all([namevalue , agevalue, gendervalue, location_value, phoneno_value]):

            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        if not phoneno_value.isdigit() or len(phoneno_value) != 10:
            messagebox.showerror("Error", "Please enter a valid 10-digit mobile number.")
            return

        # Form output text
        output_text = f"Name: {namevalue}\n" \
                    f"Mobile No: {phoneno_value}\n" \
                    f"Age: {agevalue}\n" \
                    f"Blood Group : {bg_value}\n"\
                    f"Address : {address_value}\n"\
                    f"Gender : {gendervalue}\n"\
                    f"Location: {location_value} "
        # Get a reference to the Firestore collection
        user_profiles_ref = db.collection('user_profiles')
        # Create a new user profile entry
        user_profile = {
            'first_name': namevalue,
            'mobile_no': int(phoneno_value),
            'blood group': bg_value,
            'age': int(agevalue),
            'address': address_value,
            'gender': gendervalue,
            'location': location_value
        }
        # Add the user profile to Firestore
        new_user_ref = user_profiles_ref.add(user_profile)
        # Get the unique ID generated by Firestore
        user_id = new_user_ref[1].id
        # Display success message
        success_message = f"Form submitted successfully.\n\n" \
                        f"Firestore User ID: {user_id}\n" \
                        f"{output_text}"
        messagebox.showinfo("Success", "Thankyou for the donation !")
        self.address_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.contact_no_entry.delete(0, tk.END)



    def go_back(self):
        self.root.destroy()
        fp.MainApp().mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    donor_form = DonorInformationForm(root)
    root.mainloop()
