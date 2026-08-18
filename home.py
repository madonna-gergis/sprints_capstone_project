import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Flight Reservation System", font=("Arial", 18, "bold"))
        label.pack(pady=30)

        btn_book = tk.Button(
            self, 
            text="Book Flight", 
            font=("Arial", 12), 
            width=20, 
            command=lambda: controller.show_frame("BookingPage")
        )
        btn_book.pack(pady=10)

        btn_view = tk.Button(
            self, 
            text="View Reservations", 
            font=("Arial", 12), 
            width=20, 
            command=lambda: controller.show_frame("ReservationsPage")
        )
        btn_view.pack(pady=10)