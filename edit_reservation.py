import tkinter as tk
from tkinter import messagebox
from database import update_reservation

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.res_id = None

        tk.Label(self, text="Edit Reservation", font=("Arial", 16, "bold")).pack(pady=10)

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

        update_btn = tk.Button(btn_frame, text="Update", command=self.update_booking, width=12)
        update_btn.pack(side="left", padx=5)

        cancel_btn = tk.Button(btn_frame, text="Cancel", command=lambda: controller.show_frame("ReservationsPage"), width=12)
        cancel_btn.pack(side="left", padx=5)

    def load_reservation_data(self, data):
        self.res_id = data[0]
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        for idx, field in enumerate(fields, start=1):
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, data[idx])

    def update_booking(self):
        name = self.entries["Name"].get()
        flight_num = self.entries["Flight Number"].get()
        departure = self.entries["Departure"].get()
        destination = self.entries["Destination"].get()
        date = self.entries["Date"].get()
        seat = self.entries["Seat Number"].get()

        if not (name and flight_num and departure and destination and date and seat):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        update_reservation(self.res_id, name, flight_num, departure, destination, date, seat)
        messagebox.showinfo("Success", "Reservation updated successfully!")
        
        reservations_page = self.controller.frames["ReservationsPage"]
        reservations_page.load_data()
        self.controller.show_frame("ReservationsPage")