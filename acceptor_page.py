import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class BloodDonationApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Acceptor Page')
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.root.configure(bg="white")

        # Background Image
        bg_image = Image.open("../assets/acceptor2.jpg")
        bg_resize = bg_image.resize((self.screen_width, self.screen_height))
        self.bg = ImageTk.PhotoImage(bg_resize)

        self.bg_label = tk.Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0)

        # Styles for Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.label1 = tk.Label(text='''Blood Needed!                       Be a Beacon of Hope''', bg="Brown2", fg="white",
                               font=("didot", 40, "bold"), justify="center", wraplength=550, borderwidth=3,
                               relief=tk.RAISED)
        self.label1.place(x=470, y=75, width=500, height=150)

        self.label4 = tk.Label(text="To find potential blood Donor's, please use the dropdown menus to select "
                                    "the blood group and location.", justify="center", wraplength=800,
                               bg="LightSkyBlue3", fg="black", font=("san serif", 30), borderwidth=2, relief=tk.GROOVE)
        self.label4.place(x=615, y=300)

        self.bloodgroups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

        self.label2 = ttk.Combobox(self.root, values=self.bloodgroups, state="readonly", font=("Arial", 14))
        self.label2.set("Blood Group")
        self.label2.place(x=780, y=460, width=130, height=60)

        self.location = ["Pune", "Mumbai", "Nashik"]

        self.label3 = ttk.Combobox(self.root, values=self.location, state="readonly", font=("Arial", 14))
        self.label3.set("Location")
        self.label3.place(x=980, y=460, width=100, height=60)
#Back button
        self.back_label = ttk.Button(text="back")
        self.back_label.place(x=50,y=50)

        # Search Button
        self.search_button = tk.Button(self.root, text="Search", command=self.search, font=("Arial", 14))
        self.search_button.place(x=905, y=550, width=80, height=40)

        self.data = [
            ["Pratik", "B+", "Sinhgad College, Pune, 411041", "9607271171"],
            ["Prashik", "A-", "Baner, Pune, 411046", "1234567890"],
            ["Aashu", "O+", "Dadar, Mumbai", "1234567890"],
            ["Akshat", "AB-", "Thane, Mumbai", "12345678990"],
        ]
        self.index = 0

        self.columns = ("age", "salary", "phno")

        self.tree = ttk.Treeview(self.root, columns=self.columns, height=10, style="Treeview")
        self.tree.place(x=600, y=625)

        self.tree.heading('#0', text='Name')
        self.tree.heading('age', text='Blood Group')
        self.tree.heading('salary', text='Address')
        self.tree.heading('phno', text='Phone Number')

    def search(self):
        selected_blood_group = self.label2.get()
        selected_location = self.label3.get()

        # Clear items in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        filtered_data = [line for line in self.data if line[1] == selected_blood_group]

        if selected_location:
            filtered_data = [line for line in filtered_data if line[2].lower().find(selected_location.lower()) != -1]

        for i, line in enumerate(filtered_data):
            self.tree.insert('', tk.END, iid=i, text=line[0], values=line[1:], tags=("Treeview",))

    # def back_fun(self):
        # app = MainApp(self)
        



if __name__ == "__main__":
    window = tk.Tk()
    app = BloodDonationApp(window)
    window.mainloop()
