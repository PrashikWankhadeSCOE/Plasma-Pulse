import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def search():
    selected_blood_group = label2.get()
    selected_location = label3.get()

    # Clear items in the Treeview
    for item in tree.get_children():
        tree.delete(item)

    filtered_data = [line for line in data if line[1] == selected_blood_group]

    if selected_location:
        filtered_data = [line for line in filtered_data if line[2].lower().find(selected_location.lower()) != -1]

    for i, line in enumerate(filtered_data):
        tree.insert('', tk.END, iid=i, text=line[0], values=line[1:], tags=("Treeview",))

window = tk.Tk()
window.title('Tkinter Place Geometry Manager')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.configure(bg="white")

# Background Image
bg_image = Image.open("../assets/acceptor2.jpg")
bg_resize = bg_image.resize((screen_width, screen_height))
bg = ImageTk.PhotoImage(bg_resize)

bg_label = tk.Label(window, image=bg)
bg_label.place(x=0, y=0)

# Styles for Treeview
style = ttk.Style()
style.theme_use("clam")


label1 = tk.Label(text="Welcome to our Blood Donation Acceptor Page", bg="Brown2", fg="white", font=("didot", 40, "bold"), justify="center", wraplength=550, borderwidth=3, relief=tk.RAISED)
label1.place(x=470, y=75, width=500, height=150)

label4 = tk.Label(text="To find potential blood acceptors, please use the dropdown menus to select the blood group and location.", justify="center", wraplength=800, bg="LightSkyBlue3", fg="black", font=("san serif", 30), borderwidth=2, relief=tk.GROOVE)
label4.place(x=615, y=350)

bloodgroups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

label2 = ttk.Combobox(window, values=bloodgroups, state="readonly", font=("Arial", 14))
label2.set("Blood Group")
label2.place(x=770, y=470, width=130, height=60)

location = ["Pune", "Mumbai", "Nashik"]

label3 = ttk.Combobox(window, values=location, state="readonly", font=("Arial", 14))
label3.set("Location")
label3.place(x=970, y=470, width=100, height=60)

# Search Button
search_button = tk.Button(window, text="Search", command=search, font=("Arial", 14))
search_button.place(x=900, y=550, width=80, height=40)

data = [
    ["Pratik", "B+", "Sinhgad College, Pune, 411041", "9607271171"],
    ["Prashik", "A-", "Baner, Pune, 411046", "1234567890"],
    ["Aashu", "O+", "Dadar, Mumbai", "1234567890"],
    ["Akshat", "AB-", "Thane, Mumbai", "12345678990"],
]
index = 0

columns = ("age", "salary", "phno")

tree = ttk.Treeview(window, columns=columns, height=10, style="Treeview")
tree.place(x=600, y=625)

tree.heading('#0', text='Name')
tree.heading('age', text='Blood Group')
tree.heading('salary', text='Address')
tree.heading('phno', text='Phone Number')

window.mainloop()
