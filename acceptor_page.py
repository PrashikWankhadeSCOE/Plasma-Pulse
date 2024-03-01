import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import credentials, firestore

import fp

# Constants for JSON Keys
FIRST_NAME_KEY = 'first_name'
BLOOD_GROUP_KEY = 'blood group'
ADDRESS_KEY = 'address'
LOCATION_KEY = 'location'
MOBILE_NO_KEY = 'mobile_no'

def initialize_firebase_app():
    if not firebase_admin._apps:
        # Initialize the default app only if it's not already initialized
        cred = credentials.Certificate("setup/your_key.json")
        firebase_admin.initialize_app(cred)

class BloodDonationApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Acceptor Page')
        self.root.geometry("1000x800")
        self.root.configure(bg="white")

        # Initialize Firestore
        
        initialize_firebase_app()
        self.db = firestore.client()

        # Background Image
        bg_image = Image.open("assets/acceptor2.jpg")
        bg_resize = bg_image.resize((1000, 800))  # Set the desired window size
        self.bg = ImageTk.PhotoImage(bg_resize)

        self.bg_label = tk.Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0)


        # Styles for Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.label1 = tk.Label(text='''   Blood Needed!                                        Be a Beacon of Hope''', bg="Brown2", fg="white",
                               font=("didot", 28, "bold"), justify="center", wraplength=550, borderwidth=3,
                               relief=tk.RAISED)
        self.label1.place(x=300, y=75, width=400, height=100)

        self.label4 = tk.Label(text="To find potential blood Donor's," 
                                    "please use the dropdown menus to select "
                                    "the blood group and location.", justify="center", wraplength=685,
                               bg="LightSkyBlue3", fg="black", font=("san serif", 20), borderwidth=2, relief=tk.GROOVE)
        self.label4.place(x=170, y=230)

        self.bloodgroups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

        self.label2 = ttk.Combobox(self.root, values=self.bloodgroups, state="readonly", font=("Arial", 14))
        self.label2.set("Blood Group")
        self.label2.place(x=500, y=330, width=130, height=60)

        self.location = ["Pune", "Mumbai", "Nashik"]

        self.label3 = ttk.Combobox(self.root, values=self.location, state="readonly", font=("Arial", 14))
        self.label3.set("Location")
        self.label3.place(x=770, y=330, width=100, height=60)

        # Back button
        self.back_label = ttk.Button(text="back",command=self.go_back)
        self.back_label.place(x=35, y=50)

        # Search Button
        self.search_button = tk.Button(self.root, text="Search", command=self.search, font=("Arial", 14))
        self.search_button.place(x=655, y=420, width=80, height=40)

        self.data = []

        self.columns = ("age", "salary", "phno")

        self.tree = ttk.Treeview(self.root, columns=self.columns, style="Treeview")
        self.tree.place(x=400, y=490)

        self.tree.heading('#0', text='Name')
        self.tree.heading('age', text='Blood Group')
        self.tree.heading('salary', text='Address')
        self.tree.heading('phno', text='Phone Number')

        self.tree.column('#0', width=100, minwidth=100, stretch=tk.NO)
        self.tree.column('age', width=100, minwidth=100, stretch=tk.NO)
        self.tree.column('salary', width=200, minwidth=100, stretch=tk.NO)
        self.tree.column('phno', width=150, minwidth=100, stretch=tk.NO)

        self.tree.tag_configure("Treeview", background="white", foreground="black", font=("Arial", 12))


    

    def search(self):
        try:
            selected_blood_group = self.label2.get()
            selected_location = self.label3.get()
            
            # Clear items in the Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Fetch data from Firestore
            user_profiles_ref = self.db.collection('user_profiles')
            user_profiles = user_profiles_ref.stream()

            # Display records
            count = 1
            for user_profile in user_profiles:
                user_data = user_profile.to_dict()

                if user_data[BLOOD_GROUP_KEY] == selected_blood_group and user_data[LOCATION_KEY] == selected_location or user_data[BLOOD_GROUP_KEY] == selected_blood_group :

                    self.data.append([
                        user_data[FIRST_NAME_KEY],
                        user_data[BLOOD_GROUP_KEY],
                        f"{user_data[ADDRESS_KEY]}, {user_data[LOCATION_KEY]}",
                        user_data[MOBILE_NO_KEY]
                    ])
                    self.tree.insert('', tk.END, iid=count, text=user_data[FIRST_NAME_KEY], values=(
                        user_data[BLOOD_GROUP_KEY],
                        f"{user_data[ADDRESS_KEY]}, {user_data[LOCATION_KEY]}",
                        user_data[MOBILE_NO_KEY]
                    ), tags=("Treeview",))
                    count += 1

        except Exception as e:
            print(f"Error: {e}")

    def go_back(self):
        # Close the current window
        self.root.destroy()
        fp.MainApp().mainloop()

    def fetch(self):
        user_profiles_ref = self.db.collection('user_profiles')
        user_profiles = user_profiles_ref.stream()

        # Clear items in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Display records
        count = 1
        for user_profile in user_profiles:
            user_data = user_profile.to_dict()
            self.data.append([
                user_data[FIRST_NAME_KEY],
                user_data[BLOOD_GROUP_KEY],
                f"{user_data[ADDRESS_KEY]}, {user_data[LOCATION_KEY]}",
                user_data[MOBILE_NO_KEY]
            ])
            self.tree.insert('', tk.END, iid=count, text=user_data[FIRST_NAME_KEY], values=(
                user_data[BLOOD_GROUP_KEY],
                f"{user_data[ADDRESS_KEY]}, {user_data[LOCATION_KEY]}",
                user_data[MOBILE_NO_KEY]
            ), tags=("Treeview",))
            count += 1

if __name__ == "__main__":
    window = tk.Tk()
    app = BloodDonationApp(window)
    app.fetch()  # Fetch and display initial records
    window.mainloop()
