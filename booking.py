import tkinter as tk
from tkinter import messagebox
from database import add_reservation

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Book a Flight", font=("Arial", 16, "bold")).pack(pady=10)

        labels = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        self.entries = {}

        for field in labels:
            frame = tk.Frame(self)
            frame.pack(fill="x", padx=20, pady=5)
            
            lbl = tk.Label(frame, text=field, width=15, anchor="w")
            lbl.pack(side="left")
            
            ent = tk.Entry(frame)
            ent.pack(side="right", expand=True, fill="x")
            
            self.entries[field] = ent

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=15)

        submit_btn = tk.Button(self, text="Submit", command=self.submit_booking, width=12)
        submit_btn.pack(in_=btn_frame, side="left", padx=5)

        back_btn = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"), width=12)
        back_btn.pack(in_=btn_frame, side="left", padx=5)

    def submit_booking(self):
        name = self.entries["Name"].get()
        flight_num = self.entries["Flight Number"].get()
        departure = self.entries["Departure"].get()
        destination = self.entries["Destination"].get()
        date = self.entries["Date"].get()
        seat = self.entries["Seat Number"].get()

        if not (name and flight_num and departure and destination and date and seat):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        add_reservation(name, flight_num, departure, destination, date, seat)
        messagebox.showinfo("Success", "Reservation booked successfully!")
        
        for entry in self.entries.values():
            entry.delete(0, tk.END)

        self.controller.show_frame("HomePage")