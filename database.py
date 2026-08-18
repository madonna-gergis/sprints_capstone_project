import sqlite3

DB_NAME = "flights.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_reservation(name, flight_number, departure, destination, date, seat_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()

def get_all_reservations():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservations')
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_reservation_by_id(res_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservations WHERE id = ?', (res_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def update_reservation(res_id, name, flight_number, departure, destination, date, seat_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE reservations
        SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
        WHERE id = ?
    ''', (name, flight_number, departure, destination, date, seat_number, res_id))
    conn.commit()
    conn.close()

def delete_reservation(res_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM reservations WHERE id = ?', (res_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Database and table created successfully!")