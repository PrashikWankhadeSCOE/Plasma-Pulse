import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class DonorInformationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("DONOR INFORMATION")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")

        # Background Image
        bg_image = Image.open("../assets/Image.jpg")
        bg_resize = bg_image.resize((self.screen_width, self.screen_height))
        self.bg = ImageTk.PhotoImage(bg_resize)
        self.bg_label = Label(root, image=self.bg)
        self.bg_label.place(x=0, y=0)

        # Headline
        self.headline_label = tk.Label(root, text="DONOR INFORMATION", font=("poppins", 30, "italic bold"),
                                       bg="white", fg="red3")
        self.headline_label.place(x=475, y=50)

        # Textbox
        self.information_text = tk.Label(root, text="Every day, blood donors help patients of all ages: accident "
                                                    "and burn victims, heart surgery and organ transplant patients, "
                                                    "and those battling cancer.", font=("poppins", 12, "italic"),
                                         bg="white", fg="red4", wraplength=400)
        self.information_text.place(x=650, y=100)

        # Initialize variables
        self.namevalue = StringVar()
        self.agevalue = StringVar()
        self.bg_value = StringVar()
        self.address_value = StringVar()
        self.location_value = StringVar()
        self.phoneno_value = StringVar()

        self.gender_flag = IntVar()

        # Form elements
        self.name_label = tk.Label(root, text="Name:", borderwidth=4, font=(15))
        self.name_label.place(x=750, y=250)
        self.name_entry = tk.Entry(root, textvariable=self.namevalue, font=(15))
        self.name_entry.place(x=850, y=250)

        self.age_label = tk.Label(root, text="Age:", borderwidth=4, font=(15))
        self.age_label.place(x=750, y=300)
        self.age_entry = tk.Entry(root, textvariable=self.agevalue, font=(15))
        self.age_entry.place(x=850, y=300)

        self.gender_label = tk.Label(root, text="Gender:", borderwidth=4, font=(15))
        self.gender_label.place(x=750, y=350)

        self.male1 = Radiobutton(text="Male", variable=self.gender_flag, bg="white", fg="black", value=1)
        self.male1.place(x=850, y=350)

        self.female1 = Radiobutton(text="Female", variable=self.gender_flag, bg="white", fg="black", value=2)
        self.female1.place(x=900, y=350)

        self.bloodgroups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

        self.blood_group_label = tk.Label(root, text="Blood Group:", borderwidth=4, font=(15))
        self.blood_group_label.place(x=750, y=400)

        self.blood_group_button = ttk.Combobox(root, values=self.bloodgroups, state="readonly",
                                               textvariable=self.bg_value)
        self.blood_group_button.set("Select Blood Group")
        self.blood_group_button.place(x=860, y=400)

        self.address_label = tk.Label(root, text="Address:", borderwidth=4, font=(15))
        self.address_label.place(x=750, y=450)
        self.address_entry = tk.Entry(root, textvariable=self.address_value, font=(15))
        self.address_entry.place(x=850, y=450)

        self.locations = ["Mumbai", "Pune", "Nashik"]

        self.location_label = tk.Label(root, text="Location:", borderwidth=4, font=(15))
        self.location_label.place(x=750, y=500)

        self.location_button = ttk.Combobox(root, values=self.locations, state="readonly",
                                            textvariable=self.location_value)
        self.location_button.set("Select Location")
        self.location_button.place(x=850, y=500)

        self.contact_no_label = tk.Label(root, text="Contact No.:", borderwidth=4, font=(15))
        self.contact_no_label.place(x=750, y=550)
        self.contact_no_entry = tk.Entry(root, textvariable=self.phoneno_value, font=(15))
        self.contact_no_entry.place(x=850, y=550)

        self.submit_button = tk.Button(root, text="Submit", borderwidth=5 )
        self.submit_button.place(x=850, y=600, width=80)

    # def submit_form(self):
    #     print(f"Name is: {self.namevalue.get()}")
    #     print(f"Age is: {self.agevalue.get()}")
    #     print(f"Gender: {'Male' if self.gender_flag.get() == 1 else 'Female'}")
    #     print(f"Blood Group is: {self.bg_value.get()}")
    #     print(f"Address is: {self.address_value.get()}")
    #     print(f"Location is: {self.location_value.get()}")

    #     contact = self.phoneno_value.get()
    #     flag = 1
    #     if len(contact) != 10:
    #         flag = 0
    #         tk.messagebox.showerror(title="Error", message="Enter 10 digit number")
    #         print("Enter 10 digit number")

    #     submit = self.submit_value.get()
    #     if flag == 1:
    #         tk.messagebox.showinfo(title="Submit", message="Form Submitted")

    # def submit_form(self):
    #     # Validation
    #     if not all([self.namevalue,self.bg, self.phoneno_value]):
    #         messagebox.showerror("Error", "Please fill in all required fields.")
    #         return
    #     if not self.phoneno_value.isdigit() or len(self.phoneno_value) != 10:
    #         messagebox.showerror("Error", "Please enter a valid 10-digit mobile number.")
    #         return
    #     # Form output text
    #     output_text = f"Name: {self.namevalue}\n" \
    #                 f"Mobile No: {int(self.phoneno_value)}\n" \
    #                 f"Age: {self.agevalue}\n" \
    #                 f"Blood Group : {self.bg_value}\n"\
    #                 f"Address : {self.address_value}\n"\
    #                 f"Location: {self.location_value} "
    #     # Get a reference to the Firestore collection
    #     user_profiles_ref = db.collection('user_profiles')
    #     # Create a new user profile entry
    #     user_profile = {
    #         'first_name': self.namevalue,
    #         'mobile_no': self.phoneno_value,
    #         'blood group': self.bg_value,
    #         'age': self.agevalue,
    #         'address': self.address_value,
    #         'Location': self.location_value
    #     }
    #     # Add the user profile to Firestore
    #     new_user_ref = user_profiles_ref.add(user_profile)
    #     # Get the unique ID generated by Firestore
    #     user_id = new_user_ref[1].id
    #     # Display success message
    #     success_message = f"Form submitted successfully.\n\n" \
    #                     f"Firestore User ID: {user_id}\n" \
    #                     f"{output_text}"
    #     messagebox.showinfo("Success", success_message)

if __name__ == "__main__":
    root = tk.Tk()
    donor_form = DonorInformationForm(root)
    root.mainloop()
