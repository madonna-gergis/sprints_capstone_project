import tkinter as tk
from tkinter import ttk, messagebox
from database import get_all_reservations, delete_reservation

class ReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="All Reservations", font=("Arial", 16, "bold"))
        label.pack(pady=10)

        columns = ("ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=90, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        refresh_btn = tk.Button(btn_frame, text="Refresh", command=self.load_data, width=10)
        refresh_btn.pack(side="left", padx=5)

        edit_btn = tk.Button(btn_frame, text="Edit", command=self.edit_selected, width=10)
        edit_btn.pack(side="left", padx=5)

        delete_btn = tk.Button(btn_frame, text="Delete", command=self.delete_selected, width=10)
        delete_btn.pack(side="left", padx=5)

        back_btn = tk.Button(btn_frame, text="Back to Home", command=lambda: controller.show_frame("HomePage"), width=12)
        back_btn.pack(side="left", padx=5)

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        rows = get_all_reservations()
        for row in rows:
            self.tree.insert("", "end", values=row)

    def delete_selected(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a reservation to delete.")
            return
        
        item_data = self.tree.item(selected_item)["values"]
        res_id = item_data[0]
        
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?"):
            delete_reservation(res_id)
            self.load_data()
            messagebox.showinfo("Success", "Reservation deleted successfully.")

    def edit_selected(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a reservation to edit.")
            return
        
        item_data = self.tree.item(selected_item)["values"]
        edit_page = self.controller.frames["EditReservationPage"]
        edit_page.load_reservation_data(item_data)
        self.controller.show_frame("EditReservationPage")