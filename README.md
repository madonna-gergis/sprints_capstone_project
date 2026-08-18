Flight Reservation Desktop Application
A simple and user-friendly Desktop Application built with Python, Tkinter, and SQLite to manage flight reservations.

Features
Book Flight: Add new passenger and flight details.

View Reservations: Display all booked flights in a structured table.

Update Reservation: Modify existing flight and passenger information.

Delete Reservation: Remove flight bookings with confirmation.

Project Structure
flight_reservation_app/
├── main.py              # Main application entry point
├── database.py          # SQLite database setup and query functions
├── home.py              # Home page UI
├── booking.py           # Flight booking page UI
├── reservations.py      # Reservations list page UI
├── edit_reservation.py  # Edit reservation page UI
├── flights.db           # SQLite database file
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation

Technologies Used
Python 3

Tkinter (Graphical User Interface)

SQLite3 (Database Management)

PyInstaller (Standalone Executable Compilation)

How to Run the Project
Clone or download this repository.

Open your terminal and navigate to the project directory:
cd flight_reservation_app

Run the application:
python main.py

Generating Executable (.exe)
To create a standalone Windows executable:

Install PyInstaller:
pip install pyinstaller

Build the .exe file:
pyinstaller --onefile main.py

The executable file will be generated in the dist folder.