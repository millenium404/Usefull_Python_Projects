import os
from tkinter import *
import sqlite3


root = Tk()
root.title('Some cool stuff in here')
mwidth = int(root.winfo_screenwidth() // 3) # Get screen resolution
mheight = int(root.winfo_screenheight() // 1.5) # Get screen resolution
root.geometry(f'{mwidth}x{mheight}') # Set main window size
base_dir = os.path.abspath(os.getcwd())

# Create Database or connect to one
conn = sqlite3.connect('address_book.db')
# Create Cursor
c = conn.cursor()

# Create Table
# c.execute("""CREATE TABLE addresses (
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer)""")

# Frame for registration
frame_1 = LabelFrame(root, text='Register User', padx=50, pady=50)
frame_1.grid(row=0, column=0, padx=10, pady=10)

# Create Text Boxes
f_name = Entry(frame_1, width=30)
f_name.grid(row=0, column=1, padx=20, pady=5)
l_name = Entry(frame_1, width=30)
l_name.grid(row=1, column=1, padx=20, pady=5)
address = Entry(frame_1, width=30)
address.grid(row=2, column=1, padx=20, pady=5)
city = Entry(frame_1, width=30)
city.grid(row=3, column=1, padx=20, pady=5)
state = Entry(frame_1, width=30)
state.grid(row=4, column=1, padx=20, pady=5)
zipcode = Entry(frame_1, width=30)
zipcode.grid(row=5, column=1, padx=20, pady=5)
tboxes_list = [f_name, l_name, address, city, state, zipcode]
delete_box = Entry(frame_1, width=30)
delete_box.grid(row=9, column=1, padx=20, pady=5)

# Create Text Box Labels
f_name_label = Label(frame_1, text='First Name')
f_name_label.grid(row=0, column=0)
l_name_label = Label(frame_1, text='Last Name')
l_name_label.grid(row=1, column=0)
address_label = Label(frame_1, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(frame_1, text='City')
city_label.grid(row=3, column=0)
state_label = Label(frame_1, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(frame_1, text='Zip Code')
zipcode_label.grid(row=5, column=0)
# delete_box_label = Label(frame_1, text='ID Number')
# delete_box.grid(row=9, column=0)


# Delete SQL Record
def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute(f"DELETE from addresses WHERE oid={delete_box.get()}")
    delete_box.delete(0, END)

    conn.commit()
    conn.close()


# Create Submit function and button
def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
   
    # Insert into Table
    c.execute(
        f"INSERT INTO addresses VALUES "
        f"(:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get(),
        })

    conn.commit()
    conn.close()

    # Clear The Text Boxes
    for box in tboxes_list:
        box.delete(0, END)


def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    records_string = ''
    for record in records:
        for item in record:
            records_string += str(item) + ' '
        records_string += '\n'

    query_label = Label(frame_1, text=records_string)
    query_label.grid(row=8, column=0, columnspan=2, pady=10)


submit_btn = Button(frame_1, text='Add Record', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, ipadx=50)
query_btn = Button(frame_1, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, ipadx=50)
delete_btn = Button(frame_1, text='Delete Record', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, ipadx=50)

# Commit Changes
conn.commit()
# Close connection
conn.close()

root.mainloop()