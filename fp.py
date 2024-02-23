import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
#from Donar.donar_page import DonorInformationForm
from acceptor_page import BloodDonationApp

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.title("Blood Bank Management System")
        self.configure(bg="black")
        self.create_widgets()

    def create_widgets(self):
        self.bg_image = Image.open("assets/pix.jpg")
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0,y=0)

        self.logo_image = Image.open("assets/logo.jpg")
        self.logo_image = ImageTk.PhotoImage(self.logo_image.resize((200, 200)))
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.place(x=500, y=150)

        self.heading_label = tk.Label(self, text="Save a life: Donate Blood!", font=("Didot", 40, "italic", "bold", "underline"), bg="white", fg="maroon", pady=15, borderwidth=4)
        self.heading_label.place(x=750, y=170)

        self.about_label = tk.Label(self, text='''ABOUT US: Welcome to our Blood Bank Management System website!
      We are dedicated to facilitating the vital process of blood donation and distribution
      to save lives. Our platform offers an efficient and secure way for donors to register,
      and track their donations. For hospitals and blood banks, our system provides
      streamlined inventory management, real-time tracking of blood units, and
      automated alerts for critical shortages.Together, we can make a significant 
      impact in ensuring a steady supply of blood for those in need.''', font=("gadugi", 15), bg="white", fg="brown4", pady=15, borderwidth=4, relief=tk.RAISED)
        self.about_label.place(x=500, y=470)

        self.donate_button = tk.Button(self, text="DONATE", font=("Lucida fax", 30, "bold"), relief=tk.RAISED, borderwidth=5)
        self.donate_button.config(bg="brown3")
        self.donate_button.place(x=600, y=870)
        self.donate_button.bind('<Double-1>', self.quit)

        self.need_button = tk.Button(self, text="NEED", font=("Lucida Fax", 30, "bold"), relief=tk.RAISED, borderwidth=5, command=self.acceptor_page)
        self.need_button.config(bg="brown3")
        self.need_button.place(x=1050, y=870)
        self.need_button.bind('<Double-1>', self.quit)

    def acceptor_page(self):
        app = BloodDonationApp(self)
        # app.mainloop()
        
    #def donor_page(self):
    #    app = DonorInformationForm(self)
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()