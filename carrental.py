import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import datetime
from tkcalendar import *
import pymysql
from tkinter import messagebox
from datetime import date
import time

window = Tk()
window.geometry('1350x750')
window.configure(bg = "#262626")
window.resizable(0,0)
window.title("CAR RENTAL SYSTEM")

#CAR
id = tk.StringVar()
brand = tk.StringVar()
year_model = tk.StringVar()
color = tk.StringVar()
plate_no = tk.StringVar()
car_seats = tk.StringVar()
auto_manual = tk.StringVar()
preferred_gas = tk.StringVar()
tinted = tk.StringVar()
prpd = tk.StringVar()
penpd = tk.StringVar()

#CUSTOMER REGISTRATION
fname = tk.StringVar()
lname = tk.StringVar()
address = tk.StringVar()
contact = tk.IntVar()

#RENT FUNCTION
carid = tk.StringVar()
rentid = tk.StringVar()
customerid = tk.StringVar()
rentdate = tk.StringVar()
returndate = tk.StringVar()
totaldays = tk.StringVar()
priceperday = tk.StringVar()
penaltyperday = tk.StringVar()
totalpayment = tk.StringVar()

#RETURN FUNCTION
returnid = tk.StringVar()
penaltydays = tk.StringVar()
amountp = tk.StringVar()

#SEARCH FUNCTION
search_by = tk.StringVar()

#CLEAR WINDOW AFTER EXITING THE USED WINDOW
def clear_window():
    global clear_frame

    clear_frame = tk.Frame(window, border=12, bg="#262626")
    clear_frame.place(x=200, y=0, width=1080, height=1000)

def clear1_window():
    global clear1_frame

    clear1_frame = tk.Frame(window, border=12, bg="#262626")
    clear1_frame.place(x=0, y=0, width=1500, height=1000)

#FRONT INTERFACE OF THE SYSTEM
def front():
    global front_frame

    front_frame = tk.Frame (window, border = 12, bg = "#262626", relief = tk.GROOVE)
    front_frame.place (x = 250, y = 90, width = 830, height = 620)

    l1 = Label (window, text = "CAPSTONE 1", fg = "white", bg = '#262626')
    l1.config (font = ("Lato", 20))
    l1.place (x = 550, y = 350)

    l2 = Label (window, text = "CAR RENTAL SYSTEM", fg = "white", bg = '#262626')
    l2.config (font = ("Fairplay Display", 50))
    l2.place (x = 300, y = 250)

    l4 = Label (window , text = "2023 ", fg = "white", bg = '#262626')
    l4.config (font = ("Lato", 20))
    l4.place (x = 620, y = 650)

                                                #REGISTRATION

#REGISTRATION OF THE CUSTOMER
def registerCustomer():
    clear_window()

    titlelabel = tk.Label(window, text = "Car Rental System", font = ("Arial", 30, "bold"), border = 12, relief = tk.GROOVE, bg = "lightgray", width = 30)

    titlelabel.place(x = 270, y = 10)

    detail_frame = tk.LabelFrame (window, text = "Enter Details", font = ("Arial", 20), border = 12, relief = tk.GROOVE,
                                 bg = "lightgray")
    detail_frame.place (x = 200, y = 90, width = 920, height = 620)

    fname_lbl = tk.Label (detail_frame, text = "First Name", font = ("Arial", 15), bg = "lightgray")
    fname_lbl.grid (row = 0, column = 0, padx = 2, pady = 2)
    fname_lbl.place (x = 10, y = 105)

    fname_ent = tk.Entry (detail_frame, border=7, font=("Arial", 15), textvariable = fname)
    fname_ent.grid (row = 0, column = 1, padx = 2, pady = 2)
    fname_ent.place (x = 150, y = 100)

    lname_lbl = tk.Label (detail_frame, text = "Last Name", font = ("Arial", 15), bg = "lightgray")
    lname_lbl.grid (row = 1, column = 0, padx = 2, pady = 2)
    lname_lbl.place (x = 10, y = 155)

    lname_ent = tk.Entry (detail_frame, border = 7, font = ("Arial", 15), textvariable = lname)
    lname_ent.grid (row = 1, column = 1, padx = 2, pady = 2)
    lname_ent.place (x= 150, y = 150)

    address_lbl = tk.Label(detail_frame, text = "Address", font = ("Arial", 15), bg = "lightgray")
    address_lbl.grid(row = 3, column = 0, padx = 2, pady = 2)
    address_lbl.place(x = 10, y = 205)

    address_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = address)
    address_ent.grid(row = 3, column = 1, padx = 2, pady = 2)
    address_ent.place(x = 150, y = 200)

    contact_lbl = tk.Label (detail_frame, text = "Contact No.", font=("Arial", 15), bg="lightgray")
    contact_lbl.grid (row=2, column=0, padx=2, pady=2)
    contact_lbl.place (x = 10, y = 255)

    contact_ent = tk.Entry (detail_frame, border=7, font = ("Arial", 15), textvariable = contact)
    contact_ent.insert(0, "Enter valid integer - ")
    contact_ent.grid (row = 2, column = 1, padx = 2, pady = 2)
    contact_ent.place (x = 150, y = 250)

    submit_btn = tk.Button(detail_frame, bg = "lightgray", text = "Submit", border = 3 , command = submitRegistration, font = ("Arial", 10),
                        width = 10, height = 2)
    submit_btn.grid (row = 0, column = 0, padx = 2, pady = 2)
    submit_btn.place (x = 275, y = 300)

    back_btn = tk.Button(detail_frame, bg = "lightgray", text = "Back", border = 3, command = back_register, font = ("Arial", 10), width = 10, height = 2)
    back_btn.grid(row = 0, column = 0, padx = 0, pady = 2)
    back_btn.place(x = 150, y = 300)

    l1 = Label (detail_frame, text = "REGISTRATION", fg = "GRAY", bg = 'lightgray')
    l1.config (font = ("Lato", 25))
    l1.place (x = 10, y = 45)

#SUBMISSION OF REGISTRATION
def submitRegistration():
    if fname.get() == "" or lname.get() == "" or address.get() == "" or contact.get() == "":
        messagebox.showerror("Error", "Please fill all the fields")
    else:
        messagebox.showinfo("Information", "Registration Completed")
        messagebox.askokcancel("Redirect", "Redirecting you to Customer Interface")
        customer_button_window()
        conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "carrental")
        curr = conn.cursor()
        curr.execute("INSERT INTO customertable VALUES(%s, %s, %s, %s, %s)", (id.get, fname.get(), lname.get(), address.get(), contact.get()))
        conn.commit()
        conn.close()

                                                #CUSTOMER

#CUSTOMER INTERFACE
def customer_button_window():

    clear_window()

    admin_frame = tk.Frame(window, border = 12, bg = "lightgray", relief = tk.GROOVE)
    admin_frame.place(x = 200, y = 90, width = 920, height = 620)

    titlelabel = tk.Label(window, text = "Car Rental System", font = ("Arial", 30, "bold"), border = 12, relief = tk.GROOVE, bg = "lightgray", width = 30)

    titlelabel.place(x = 270, y = 10)

    btn1 = tk.Button(admin_frame, bg = "lightgray", text = "Rent Car", border = 7, font = ("Arial", 10), width = 20, height = 2, command = customer_rent_car)

    btn1.grid(row = 0, column = 0, padx = 2, pady = 2)
    btn1.place(x = 10, y = 290)

    btn2 = tk.Button(admin_frame, bg = "lightgray", text = "Return Car", border = 7, command = customer_return_car, font = ("Arial", 10), width = 20, height = 2)

    btn2.grid(row = 0, column = 0, padx = 2, pady = 2)
    btn2.place(x = 10, y = 350)

    back_btn = tk.Button(admin_frame, bg="lightgray", text="Back", border=7, command=back, font=("Arial", 10),
                         width=20, height=2)
    back_btn.grid(row=0, column=0, padx=2, pady=2)
    back_btn.place(x=10, y=410)

    exit_btn = tk.Button(admin_frame, bg = "lightgray", text = "Exit", border = 7, command = exit_button, font = ("Arial", 10), width = 20, height = 2)
    exit_btn.grid(row = 0, column = 0, padx = 2, pady = 2)
    exit_btn.place(x = 10, y = 470)

    l1 = Label (admin_frame, text = "CUSTOMER INTERFACE", fg = "GRAY", bg = 'lightgray')
    l1.config (font = ("Lato", 25))
    l1.place (x = 470, y = 10)

#CUSTOMER TRANSACTION OF RENTING CAR
def customer_rent_car():
    clear_window()

    global car_table1, customer_table, search_entry1, search_entry, rentdate_ent, returndate_ent, totaldays_ent, totaldays, priceperday_ent, car_table, customerdata_frame, detail_frame, main_frame, data_frame
    detail_frame = tk.LabelFrame(window, text = "Rent Car", font = ("Arial", 20), border = 12, relief = tk.GROOVE,
                                 bg = "lightgray")
    detail_frame.place(x = 20, y = 90, width = 420, height = 620)

    data_frame = tk.Frame(window, border = 12, bg = "lightgray", relief = tk.GROOVE)
    data_frame.place(x = 475, y = 90, width = 810, height = 360)

    customerdata_frame = tk.Frame(window, border = 12, bg = "lightgray", relief = tk.GROOVE)
    customerdata_frame.place(x = 475, y = 450, width = 810, height = 260)

    carid_lbl = tk.Label(detail_frame, text = "Car ID", font = ("Arial", 15), bg = "lightgray")
    carid_lbl.place(x= 5, y = 0)

    carid_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = carid)
    carid_ent.place(x = 150, y = 0)

    customerid_lbl = tk.Label(detail_frame, text="Customer ID", font=("Arial", 15), bg="lightgray")
    customerid_lbl.place(x= 5, y = 30)

    customerid_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = customerid)
    customerid_ent.place(x = 150, y = 30)

    carbrand_lbl = tk.Label(detail_frame, text = "Brand", font = ("Arial", 15), bg ="lightgray")
    carbrand_lbl.place(x = 5, y = 60)

    carbrand_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable= brand)
    carbrand_ent.place(x = 150, y = 60)

    yearmodel_lbl = tk.Label(detail_frame, text="Year Model", font=("Arial", 15), bg ="lightgray")
    yearmodel_lbl.place(x = 5, y = 90)

    yearmodel_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = year_model)
    yearmodel_ent.place(x = 150, y = 90)

    color_lbl = tk.Label(detail_frame, text = "Color", font = ("Arial", 15), bg = "lightgray")
    color_lbl.place(x = 5, y = 120)

    color_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = color)
    color_ent.place(x = 150, y = 120)

    plateno_lbl = tk.Label(detail_frame, text = "Plate No", font = ("Arial", 15), bg = "lightgray")
    plateno_lbl.place(x = 5, y = 150)

    plateno_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = plate_no)
    plateno_ent.place(x = 150, y = 150)

    carseats_lbl = tk.Label(detail_frame, text = "Car Seats", font = ("Arial", 15), bg = "lightgray")
    carseats_lbl.place(x = 5, y = 180)

    carseats_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = car_seats)
    carseats_ent.place(x = 150, y = 180)

    a_m_lbl = tk.Label(detail_frame, text = "Auto / Manual", font = ("Arial", 15), bg = "lightgray")
    a_m_lbl.place(x = 5, y = 210)

    a_m_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = auto_manual)
    a_m_ent.place(x = 150, y = 210)

    gas_lbl = tk.Label(detail_frame, text = "Preferred Gas", font = ("Arial", 15), bg = "lightgray")
    gas_lbl.place(x = 5, y = 240)

    gas_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = preferred_gas)
    gas_ent.place(x = 150, y = 240)

    tinted_lbl = tk.Label(detail_frame, text = "Tinted", font = ("Arial", 15), bg = "lightgray")
    tinted_lbl.place(x = 5, y = 270)

    tinted_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = tinted)
    tinted_ent.place(x = 150, y = 270)

    rentdate_lbl = tk.Label(detail_frame, text = "Date of Rent", font = ("Arial", 15), bg = "lightgray")
    rentdate_lbl.place(x = 5, y = 300)

    rentdate_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = rentdate)
    rentdate_ent.insert(0, "YYYY-MM-DD")
    rentdate_ent.place(x = 150, y = 300)

    returndate_lbl = tk.Label(detail_frame, text = "Date of Return", font = ("Arial", 15), bg = "lightgray")
    returndate_lbl.place(x = 5, y = 330)

    returndate_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = returndate)
    returndate_ent.insert(0, "YYYY-MM-DD")
    returndate_ent.place(x = 150, y = 330)

    totaldays_lbl = tk.Label(detail_frame, text = "Total Days", font = ("Arial", 15), bg = "lightgray")
    totaldays_lbl.place(x = 5, y = 360)

    totaldays_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = totaldays)
    totaldays_ent.place(x = 150, y = 360)

    priceperday_lbl = tk.Label(detail_frame, text = "Price per day", font = ("Arial", 15), bg = "lightgray")
    priceperday_lbl.place(x = 5, y = 390)

    priceperday_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = priceperday)
    priceperday_ent.place(x = 150, y = 390)

    penaltyperday_lbl = tk.Label(detail_frame, text = "Penalty per day", font = ("Arial", 15), bg = "lightgray")
    penaltyperday_lbl.place(x = 5, y = 420)

    penaltyperday_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = penaltyperday)
    penaltyperday_ent.place(x = 150, y = 420)

    totalpayment_lbl = tk.Label(detail_frame, text = "Total Payment", font = ("Arial", 15), bg = "lightgray")
    totalpayment_lbl.place(x = 5, y = 450)

    totalpayment_ent = tk.Entry(detail_frame, border = 7, font = ("Arial", 15), textvariable = totalpayment)
    totalpayment_ent.place(x = 150, y = 450)

    btn_frame = tk.Frame(detail_frame, bg = "lightgray", border = 10, relief = tk.GROOVE)
    btn_frame.place(x = 40, y = 500, width = 340, height = 65)

    back_btn = tk.Button(detail_frame, border = 1, font = ("Arial", 10), text = "Back", command = back_rent, width = 5, height = 1)
    back_btn.place(x = 0, y = 550)

    calc_btn = tk.Button(btn_frame, bg = "lightgray", text = "Calculate Days", border = 7, command = lambda: calculate_function(rentdate_ent, returndate_ent)
                         ,font = ("Arial", 10), width = 10, height = 1 )
    calc_btn.grid(row = 0, column = 0, padx = 2, pady = 2)

    rent_btn = tk.Button(btn_frame, bg = "lightgray", text = "Rent", border = 7, command = rent_function,
                           font = ("Arial", 10), width = 7, height = 1)
    rent_btn.grid(row = 0, column = 2, padx = 2, pady = 2)

    calcamount_btn = tk.Button(btn_frame, bg = "lightgray", text = "Calculate Payment", border = 7, command = lambda: calculateamount_function(priceperday, totaldays),
                         font = ("Arial", 10), width = 13, height = 1)
    calcamount_btn.grid(row = 0, column = 3, padx = 2, pady = 2)

    search_frame = tk.Frame(data_frame, bg = "lightgray", border = 10, relief = tk.GROOVE)
    search_frame.pack(side = tk.TOP, fill = tk.X)

    search_lbl = tk.Label(search_frame, text = "Search", bg = "lightgray", font = ("Arial", 14))
    search_lbl.grid(row = 0, column = 0, padx = 12, pady = 2)

    search_entry = tk.Entry(search_frame, font = ("Arial", 10))
    search_entry.insert(0, "Search for Brand")
    search_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

    search_btn = tk.Button(search_frame, text = "Search", font = ("Arial", 13), border = 9, width = 14, bg = "lightgray",
                           command = searchfunction)
    search_btn.grid(row = 0, column = 2, padx = 12, pady = 2)

    showAll_btn = tk.Button(search_frame, text = "Show All", font = ("Arial", 13), border = 9, width = 14, bg = "lightgray",
                            command = showall)
    showAll_btn.grid(row = 0, column = 3, padx = 12, pady = 2)

    search_frame1 = tk.Frame(customerdata_frame, bg = "lightgray", border = 10, relief = tk.GROOVE)
    search_frame1.pack(side = tk.TOP, fill = tk.X)

    search_lbl = tk.Label(search_frame1, text = "Search", bg = "lightgray", font = ("Arial", 14))
    search_lbl.grid(row = 0, column = 0, padx = 12, pady = 2)

    search_entry1 = tk.Entry(search_frame1, font = ("Arial", 10))
    search_entry1.insert(0, "Search for Last Name")
    search_entry1.grid(row = 0, column = 1, padx = 5, pady = 5)

    search_btn = tk.Button(search_frame1, text = "Search", font = ("Arial", 13), border = 9, width = 14, bg = "lightgray", command = search_customer_data)

    search_btn.grid(row = 0, column = 2, padx = 12, pady = 2)

    showAll_btn = tk.Button(search_frame1, text = "Show All", font = ("Arial", 13), border = 9, width = 14, bg = "lightgray",
                            command = showall_customer)
    showAll_btn.grid(row = 0, column = 3, padx = 12, pady = 2)

    main_frame = tk.Frame(data_frame, bg = "lightgray", border = 11, relief = tk.GROOVE)
    main_frame.pack(fill = tk.BOTH, expand = True)

    y_scroll = tk.Scrollbar(data_frame, orient = tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame, orient = tk.HORIZONTAL)

    car_table1 = ttk.Treeview(main_frame, columns = (
    "ID", "Brand", "Year Model", "Color", "Plate No.", "Car Seats", "Auto / Manual", "Preferred Gas", "Tinted",
    "Price per Day", "Penalty per Day"), yscrollcommand = y_scroll.set, xscrollcommand = x_scroll.set)

    y_scroll.config(command = car_table1.yview)
    x_scroll.config(command = car_table1.xview)

    y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
    x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

    car_table1.heading("ID", text = "ID")
    car_table1.heading("Brand", text = "Brand")
    car_table1.heading("Year Model", text = "Year Model")
    car_table1.heading("Color", text = "Color")
    car_table1.heading("Plate No.", text = "Plate No.")
    car_table1.heading("Car Seats", text = "Car Seats")
    car_table1.heading("Auto / Manual", text = "Auto / Manual")
    car_table1.heading("Preferred Gas", text = "Preferred Gas")
    car_table1.heading("Tinted", text = "Tinted")
    car_table1.heading("Price per Day", text = "Price per Day")
    car_table1.heading("Penalty per Day", text = "Penalty per Day")

    car_table1['show'] = "headings"
    car_table1.column("ID", width = 100)
    car_table1.column("Brand", width = 100)
    car_table1.column("Year Model", width = 100)
    car_table1.column("Color", width = 100)
    car_table1.column("Plate No.", width = 100)
    car_table1.column("Car Seats", width = 100)
    car_table1.column("Auto / Manual", width = 100)
    car_table1.column("Preferred Gas", width = 100)
    car_table1.column("Tinted", width = 100)
    car_table1.column("Price per Day", width = 100)
    car_table1.column("Penalty per Day", width = 100)

    car_table1.pack(fill = tk.BOTH, expand = True)

    fetch_data1_car()

    car_table1.bind("<ButtonRelease -1>", get_data1_car)

    customer_table = ttk.Treeview(customerdata_frame, columns = ("ID", "First Name", "Last Name", "Address", "Contact No"))

    customer_table.heading("ID", text="ID")
    customer_table.heading("First Name", text="First Name")
    customer_table.heading("Last Name", text="Last Name")
    customer_table.heading("Address", text="Address")
    customer_table.heading("Contact No", text="Contact No")

    customer_table['show'] = "headings"
    customer_table.column("ID", width=50)
    customer_table.column("First Name", width=75)
    customer_table.column("Last Name", width=75)
    customer_table.column("Address", width=75)
    customer_table.column("Contact No", width=75)

    customer_table.pack(fill=tk.BOTH, expand=True)
    fetch_data1_customer()

def showall():
    fetch_data1_car()

def searchfunction():
    lookup_record = search_entry.get()
    for record in car_table1.get_children():
        car_table1.delete(record)
    conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "carrental")
    curr = conn.cursor()
    curr.execute("SELECT  * from cartable WHERE brand = %s",(lookup_record))
    rows = curr.fetchall()
    global count
    count = 0
    for record in rows:
        if count % 2 == 0:
            car_table1.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10]),
                           tags=('evenrow',))
        else:
            car_table1.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10]),
                           tags=('oddrow',))
        count += 1
    conn.commit()
    conn.close()

def search_customer_data():
    search_record = search_entry1.get()
    for record in customer_table.get_children():
        customer_table.delete(record)
    conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "carrental")
    curr = conn.cursor()
    curr.execute("SELECT  * from customertable WHERE lname = %s",(search_record))
    rows = curr.fetchall()
    global count
    count = 0
    for record in rows:
        if count % 2 == 0:
            customer_table.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4]),
                           tags=('evenrow',))
        else:
            customer_table.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4]),
                           tags=('oddrow',))
        count += 1
    conn.commit()
    conn.close()

def showall_customer():
    fetch_data1_customer()

def fetch_data1_customer():
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT * FROM customertable")
    rows = curr.fetchall()
    if len(rows) != 0:
        customer_table.delete(*customer_table.get_children())
    for row in rows:
        customer_table.insert('', tk.END, values=row)
    conn.commit()
    conn.close()

def get_data1_customer():
    cursor_row = customer_table.focus()
    content = customer_table.item(cursor_row)

    row = content['values']
    customerid.set(row[1])

def fetch_data1_car():
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT * FROM cartable")
    rows = curr.fetchall()
    if len(rows) != 0:
        car_table1.delete(*car_table1.get_children())
    for row in rows:
        car_table1.insert('', tk.END, values=row)
    conn.commit()
    conn.close()

def get_data1_car(event):
    cursor_row = car_table1.focus()
    content = car_table1.item(cursor_row)

    row = content['values']
    carid.set(row[0])
    brand.set(row[1])
    year_model.set(row[2])
    color.set(row[3])
    plate_no.set(row[4])
    car_seats.set(row[5])
    auto_manual.set(row[6])
    preferred_gas.set(row[7])
    tinted.set(row[8])
    penaltyperday.set(row[10])

def rent_function():
    if carid.get() == "" or customerid.get() == "" or brand.get() == "" or year_model.get() == "" or color.get() == "" or \
            plate_no.get() == "" or car_seats.get() == "" or auto_manual.get() == "" or preferred_gas.get() == "" or \
                tinted.get() == "" or rentdate.get() == "" or returndate.get() == "" or totaldays.get() == "" or priceperday.get() == "" or\
                    penaltyperday.get() == "" or totalpayment.get() == "":
        messagebox.showerror("Error", "Please fill all the fields")
    else:
        res = messagebox.askyesno("Rent Car", "Confirm Rent?")
        if res == True:
            messagebox.showinfo("Success", "Car Rented Successfully!")
            messagebox.showinfo("Countdown", "Thank you for using the system.")
            conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
            curr = conn.cursor()
            curr.execute("INSERT INTO renttable VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                 (rentid.get, carid.get(), customerid.get(), brand.get(), year_model.get(), color.get(),
                  plate_no.get(), car_seats.get(), auto_manual.get(), preferred_gas.get(), tinted.get(),
                  rentdate.get(), returndate.get(), totaldays.get(), priceperday.get(), penaltyperday.get(), totalpayment.get()))
            curr.execute("DELETE from cartable WHERE carid = %s", (carid.get()))
            conn.commit()
            fetch_data1_car()
            conn.close()
            time.sleep(1)
            window.quit()
        elif res == False:
            pass
        else:
            pass

#CALCULATING OF TOTAL DAYS
def calculate_function(rentdate_ent, returndate_ent):
    year_1, month_1, day_1 = rentdate_ent.get().split("-")
    year_2, month_2, day_2 = returndate_ent.get().split("-")
    difference = date(int(year_2), int(month_2), int(day_2)) - date(int(year_1), int(month_1), int(day_1))
    messagebox.showinfo("Total Days", f"{difference.days} days.")

#CALCULATING OF TOTAL PAYMENT
def calculateamount_function(priceperday_ent, totaldays_ent):
    total_days = totaldays_ent.get()
    price_perday = priceperday_ent.get()
    amount = int(total_days) * int(price_perday)
    messagebox.showinfo("Total Payment", f"{amount} total")

#CUSTOMER TRANSACTION OF RETURNING CAR
def customer_return_car():
    global rentedcars1_table, search_entry2, customer_table, return_table, car_table1, search_entry_return, detail_frame, returndata_frame, rentdata_frame
    detail_frame = tk.LabelFrame(window, text="Return Car", font=("Arial", 20), border=12, relief=tk.GROOVE,
                                 bg="lightgray")
    detail_frame.place(x=20, y=90, width=420, height=620)

    returndata_frame = tk.Frame(window, border=12, bg="lightgray", relief=tk.GROOVE)
    returndata_frame.place(x=475, y=450, width=810, height=260)

    rentdata_frame = tk.Frame(window, border=12, bg="lightgray", relief=tk.GROOVE)
    rentdata_frame.place(x=475, y=90, width=810, height=360)

    rentid_lbl = tk.Label(detail_frame, text="Rent ID", font=("Arial", 15), bg="lightgray")
    rentid_lbl.place(x=5, y=0)

    rentid_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=rentid)
    rentid_ent.place(x=150, y=0)

    carid_lbl = tk.Label(detail_frame, text="Car ID", font=("Arial", 15), bg="lightgray")
    carid_lbl.place(x=5, y=30)

    carid_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=carid)
    carid_ent.place(x=150, y=30)

    customerid_lbl = tk.Label(detail_frame, text="Customer ID", font=("Arial", 15), bg="lightgray")
    customerid_lbl.place(x=5, y=60)

    customerid_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=customerid)
    customerid_ent.place(x=150, y=60)

    brand_lbl = tk.Label(detail_frame, text="Brand", font=("Arial", 15), bg="lightgray")
    brand_lbl.place(x=5, y=90)

    brand_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=brand)
    brand_ent.place(x=150, y=90)

    yearmodel_lbl = tk.Label(detail_frame, text="Year Model", font=("Arial", 15), bg="lightgray")
    yearmodel_lbl.place(x=5, y=120)

    yearmodel_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=year_model)
    yearmodel_ent.place(x=150, y=120)

    color_lbl = tk.Label(detail_frame, text="Color", font=("Arial", 15), bg="lightgray")
    color_lbl.place(x=5, y=150)

    color_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=color)
    color_ent.place(x=150, y=150)

    plateno_lbl = tk.Label(detail_frame, text="Plate No", font=("Arial", 15), bg="lightgray")
    plateno_lbl.place(x=5, y=180)

    plateno_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=plate_no)
    plateno_ent.place(x=150, y=180)

    carseats_lbl = tk.Label(detail_frame, text="Car Seats", font=("Arial", 15), bg="lightgray")
    carseats_lbl.place(x=5, y=210)

    carseats_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=car_seats)
    carseats_ent.place(x=150, y=210)

    a_m_lbl = tk.Label(detail_frame, text="Auto / Manual", font=("Arial", 15), bg="lightgray")
    a_m_lbl.place(x=5, y=240)

    a_m_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=auto_manual)
    a_m_ent.place(x=150, y=240)

    gas_lbl = tk.Label(detail_frame, text="Preferred Gas", font=("Arial", 15), bg="lightgray")
    gas_lbl.place(x=5, y=270)

    gas_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=preferred_gas)
    gas_ent.place(x=150, y=270)

    tinted_lbl = tk.Label(detail_frame, text="Tinted", font=("Arial", 15), bg="lightgray")
    tinted_lbl.place(x=5, y=300)

    tinted_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=tinted)
    tinted_ent.place(x=150, y=300)

    rentdate_lbl = tk.Label(detail_frame, text="Rent Date", font=("Arial", 15), bg="lightgray")
    rentdate_lbl.place(x=5, y=330)

    rentdate_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=rentdate)
    rentdate_ent.place(x=150, y=330)

    returndate_lbl = tk.Label(detail_frame, text="Return Date", font=("Arial", 15), bg="lightgray")
    returndate_lbl.place(x=5, y=360)

    returndate_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=returndate)
    returndate_ent.place(x=150, y=360)

    amountp_lbl = tk.Label(detail_frame, text="Amount Payment", font=("Arial", 15), bg="lightgray")
    amountp_lbl.place(x=5, y=390)

    amountp_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=amountp)
    amountp_ent.insert(0, "GRAND TOTAL HERE")
    amountp_ent.place(x=150, y=390)

    penpd_lbl = tk.Label(detail_frame, text="Penalty per day", font=("Arial", 15), bg="lightgray")
    penpd_lbl.place(x=5, y=420)

    penpd_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=penaltyperday)
    penpd_ent.place(x=150, y=420)

    penaltydays_lbl = tk.Label(detail_frame, text="Penalty Days", font=("Arial", 15), bg="lightgray")
    penaltydays_lbl.place(x=5, y=450)

    penaltydays_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=penaltydays)
    penaltydays_ent.place(x=150, y=450)

    tp_lbl = tk.Label(detail_frame, text="Total Payment", font=("Arial", 15), bg="lightgray")
    tp_lbl.place(x=5, y=480)

    tp_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=totalpayment)
    tp_ent.place(x=150, y=480)

    btn_frame = tk.Frame(detail_frame, bg="lightgray", border=10, relief=tk.GROOVE)
    btn_frame.place(x=22, y=520, width=340, height=50)

    back_btn = tk.Button(btn_frame, bg = "lightgray", text = "Back", border = 3, command = back_return, font=("Arial", 10), width = 7, height = 1)
    back_btn.place(x = 10, y = 0)

    return_btn = tk.Button(btn_frame, bg="lightgray", text="Return", border=3, command=return_function,
                         font=("Arial", 10), width=7, height=1)
    return_btn.place(x= 230, y = 0)

    calcpay_btn = tk.Button(btn_frame, bg="lightgray", text="Calculate Payment", border=3, command= lambda: calc_payment(penaltyperday, penaltydays, totalpayment),
                         font=("Arial", 10), width=15, height=1)
    calcpay_btn.place(x= 80, y = 0)

    search_frame = tk.Frame(rentdata_frame, bg="lightgray", border=10, relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP, fill=tk.X)

    search_lbl = tk.Label(search_frame, text="Search", bg="lightgray", font=("Arial", 14))
    search_lbl.grid(row=0, column=0, padx=12, pady=2)

    search_entry2 = tk.Entry(search_frame, font=("Arial", 10))
    search_entry2.insert(0, "Search for Customer ID")
    search_entry2.grid(row=0, column=1, padx=5, pady=5)

    search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), border=9, width=14, bg="lightgray",
                           command=search_customerid_rent_function)
    search_btn.grid(row=0, column=2, padx=12, pady=2)

    showAll_btn = tk.Button(search_frame, text="Show All", font=("Arial", 13), border=9, width=14, bg="lightgray",
                            command=showall_customerdata_rent_function)
    showAll_btn.grid(row=0, column=3, padx=12, pady=2)

    search_frame1 = tk.Frame(returndata_frame, bg="lightgray", border=10, relief=tk.GROOVE)
    search_frame1.pack(side=tk.TOP, fill=tk.X)

    search_lbl = tk.Label(search_frame1, text="Search", bg="lightgray", font=("Arial", 14))
    search_lbl.grid(row=0, column=0, padx=12, pady=2)

    search_entry_return = tk.Entry(search_frame1, font=("Arial", 10))
    search_entry_return.insert(0, "Search for Customer ID")
    search_entry_return.grid(row=0, column=1, padx=5, pady=5)

    search_btn = tk.Button(search_frame1, text="Search", font=("Arial", 13), border=9, width=14, bg="lightgray",
                           command=search_customerid_return_table)

    search_btn.grid(row=0, column=2, padx=12, pady=2)

    showAll_btn = tk.Button(search_frame1, text="Show All", font=("Arial", 13), border=9, width=14, bg="lightgray",
                            command=showall_returndata)
    showAll_btn.grid(row=0, column=3, padx=12, pady=2)

    main_frame = tk.Frame(rentdata_frame, bg="lightgray", border=11, relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH, expand=True)

    y_scroll = tk.Scrollbar(rentdata_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(rentdata_frame, orient=tk.HORIZONTAL)

    rentedcars1_table = ttk.Treeview(main_frame, columns=(
        "ID", "Car ID", "Customer ID", "Brand", "Year Model", "Color",  "Plate No",
        "Car Seats", "Auto / Manual", "Preferred Gas", "Tinted", "Date of Rent", "Date of Return", "Total Days", "Price per day",
        "Penalty per day", "Total Payment"),yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command=rentedcars1_table.yview)
    x_scroll.config(command=rentedcars1_table.xview)

    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    rentedcars1_table.heading("ID", text="ID")
    rentedcars1_table.heading("Car ID", text="Car ID")
    rentedcars1_table.heading("Customer ID", text="Customer ID")
    rentedcars1_table.heading("Brand", text = "Brand")
    rentedcars1_table.heading("Year Model", text = "Year Model")
    rentedcars1_table.heading("Color", text = "Color")
    rentedcars1_table.heading("Plate No", text = "Plate No")
    rentedcars1_table.heading("Car Seats", text = "Car Seats")
    rentedcars1_table.heading("Auto / Manual", text = "Auto / Manual")
    rentedcars1_table.heading("Preferred Gas", text = "Preferred Gas")
    rentedcars1_table.heading("Tinted", text = "Tinted")
    rentedcars1_table.heading("Date of Rent", text="Date of Rent")
    rentedcars1_table.heading("Date of Return", text="Date of Return")
    rentedcars1_table.heading("Total Days", text="Total Days")
    rentedcars1_table.heading("Price per day", text="Price per day")
    rentedcars1_table.heading("Penalty per day", text="Penalty per day")
    rentedcars1_table.heading("Total Payment", text="Total Payment")

    rentedcars1_table['show'] = "headings"
    rentedcars1_table.column("ID", width=30)
    rentedcars1_table.column("Car ID", width=50)
    rentedcars1_table.column("Customer ID", width=75)
    rentedcars1_table.column("Brand", width = 100)
    rentedcars1_table.column("Year Model", width = 100)
    rentedcars1_table.column("Color", width = 100)
    rentedcars1_table.column("Plate No", width = 100)
    rentedcars1_table.column("Car Seats", width = 100)
    rentedcars1_table.column("Auto / Manual", width = 100)
    rentedcars1_table.column("Preferred Gas", width = 100)
    rentedcars1_table.column("Tinted", width = 100)
    rentedcars1_table.column("Date of Rent", width=100)
    rentedcars1_table.column("Date of Return", width=100)
    rentedcars1_table.column("Total Days", width=100)
    rentedcars1_table.column("Price per day", width=100)
    rentedcars1_table.column("Penalty per day", width=100)
    rentedcars1_table.column("Total Payment", width=100)

    rentedcars1_table.pack(fill=tk.BOTH, expand=True)

    fetch_data1_rentedcars()
    rentedcars1_table.bind("<ButtonRelease -1>", get_data1_rentedcars)
    y_scroll = tk.Scrollbar(returndata_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(returndata_frame, orient=tk.HORIZONTAL)

    return_table = ttk.Treeview(returndata_frame,
                                  columns=("ID", "Rent ID", "Car ID", "Customer ID", "Date of Rent", "Date of Return",
                                           "Amount of Payment", "Penalty per day", "No of Penalty Days", "Total Payment"),  yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command= return_table.yview)
    x_scroll.config(command= return_table.xview)

    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    return_table.heading("ID", text="ID")
    return_table.heading("Rent ID", text = "Rent ID")
    return_table.heading("Car ID", text= "Car ID")
    return_table.heading("Customer ID", text="Customer ID")
    return_table.heading("Date of Rent", text="Date of Rent")
    return_table.heading("Date of Return", text="Date of Return")
    return_table.heading("Amount of Payment", text="Amount of Payment")
    return_table.heading("Penalty per day", text="Penalty per day")
    return_table.heading("No of Penalty Days", text="No of Penalty Days")
    return_table.heading("Total Payment", text="Total Payment")

    return_table['show'] = "headings"
    return_table.column("ID", width=30)
    return_table.column("Rent ID", width = 50)
    return_table.column("Car ID", width=50)
    return_table.column("Customer ID", width=75)
    return_table.column("Date of Rent", width=100)
    return_table.column("Date of Return", width=100)
    return_table.column("Amount of Payment", width=100)
    return_table.column("Penalty per day", width=100)
    return_table.column("No of Penalty Days", width=125)
    return_table.column("Total Payment", width=100)

    return_table.pack(fill=tk.BOTH, expand=True)
    fetch_data1_returnedcars()

#CALCULATING OF AMOUNT PAYMENT OR GRAND TOTAL INCLUDING THE PENALTY
def calc_payment(penpd_ent, penaltydays_ent, totalpayment_ent):
    if penaltydays_ent == 0:
        pass
    else:
        pen_pd = penpd_ent.get()
        penalty_days = penaltydays_ent.get()
        total_p = totalpayment_ent.get()
        total = int(total_p) + int(pen_pd) * int(penalty_days)
        messagebox.showinfo("Total Payment", f"{total} total")

def search_customerid_rent_function():
    lookup_record = search_entry2.get()
    for record in rentedcars1_table.get_children():
        rentedcars1_table.delete(record)
    conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "carrental")
    curr = conn.cursor()
    curr.execute("SELECT  * from renttable WHERE customerid = %s",(lookup_record))
    rows = curr.fetchall()
    global count
    count = 0
    for record in rows:
        if count % 2 == 0:
            rentedcars1_table.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                           tags=('evenrow',))
        else:
            rentedcars1_table.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                           tags=('oddrow',))
        count += 1
    conn.commit()
    conn.close()

def showall_customerdata_rent_function():
    fetch_data1_rentedcars()

def search_customerid_return_table():
    lookup_record = search_entry_return.get()
    for record in return_table.get_children():
        return_table.delete(record)
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT  * from returntable WHERE customerid = %s", (lookup_record))
    rows = curr.fetchall()
    global count
    count = 0
    for record in rows:
        if count % 2 == 0:
            return_table.insert(parent='', index='end', iid=count, text='',
                                     values=(
                                     record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                     record[7], record[8]),
                                     tags=('evenrow',))
        else:
            return_table.insert(parent='', index='end', iid=count, text='',
                                     values=(
                                     record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                     record[7], record[8]),
                                     tags=('oddrow',))
        count += 1
    conn.commit()
    conn.close()

def showall_returndata():
    fetch_return_table()

def fetch_return_table():
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT * FROM returntable")
    rows = curr.fetchall()
    if len(rows) != 0:
        return_table.delete(*return_table.get_children())
        for row in rows:
            return_table.insert('', tk.END, values=row)
        conn.commit()
    conn.close()

def return_function():
    if penaltydays.get() == "" or totalpayment.get() == "":
        messagebox.showerror("Error", "Please fill all the fields")
    else:
        res = messagebox.askyesno("Return Car", "Confirm Return?")
        if res == True:
            messagebox.showinfo("Success", "Car Returned Successfully!")
            messagebox.showinfo("Countdown", "Thank you for using the system.")
            conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
            curr = conn.cursor()
            curr.execute("INSERT INTO cartable VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                id.get, brand.get(), year_model.get(), color.get(), plate_no.get(), car_seats.get(), auto_manual.get(),
                preferred_gas.get(), tinted.get(), priceperday.get(), penaltyperday.get()))
            curr.execute("DELETE from renttable WHERE rentid = %s", (rentid.get()))
            curr.execute("INSERT INTO returntable VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(id.get, rentid.get(), carid.get(),
                                                                                          customerid.get(), rentdate.get(), returndate.get(),
                                                                                          amountp.get(), penaltyperday.get(), penaltydays.get(),
                                                                                          totalpayment.get()))
            conn.commit()
            fetch_data1_rentedcars()
            fetch_data1_returnedcars()
            conn.close()
            time.sleep(1)
            window.quit()
        elif res == False:
            pass
        else:
            pass
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT * FROM renttable")
    rows = curr.fetchall()
    if len(rows) != 0:
        rentedcars1_table.delete(*rentedcars1_table.get_children())
        for row in rows:
            rentedcars1_table.insert('', tk.END, values=row)
        conn.commit()
    conn.close()

def fetch_data1_rentedcars():
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT * FROM renttable")
    rows = curr.fetchall()
    if len(rows) != 0:
        rentedcars1_table.delete(*rentedcars1_table.get_children())
        for row in rows:
            rentedcars1_table.insert('', tk.END, values=row)
        conn.commit()
    conn.close()

def get_data1_rentedcars(event):
    cursor_row = rentedcars1_table.focus()
    content = rentedcars1_table.item(cursor_row)

    row = content['values']
    rentid.set(row[0])
    carid.set(row[1])
    customerid.set(row[2])
    brand.set(row[3])
    year_model.set(row[4])
    color.set(row[5])
    plate_no.set(row[6])
    car_seats.set(row[7])
    auto_manual.set(row[8])
    preferred_gas.set(row[9])
    tinted.set(row[10])
    rentdate.set(row[11])
    returndate.set(row[12])
    totaldays.set(row[13])
    priceperday.set(row[14])
    penaltyperday.set(row[15])
    totalpayment.set(row[16])

def fetch_data1_returnedcars():
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT * FROM returntable")
    rows = curr.fetchall()
    if len(rows) != 0:
        return_table.delete(*return_table.get_children())
        for row in rows:
            return_table.insert('', tk.END, values=row)
        conn.commit()
    conn.close()

def get_data_returnedcars(event):
    cursor_row = return_table.focus()
    content = return_table.item(cursor_row)

    row = content['values']
    rentid.set(row[0])
    carid.set(row[1])
    customerid.set(row[2])
    brand.set(row[3])
    year_model.set(row[4])
    color.set(row[5])
    plate_no.set(row[6])
    car_seats.set(row[7])
    auto_manual.set(row[8])
    preferred_gas.set(row[9])
    tinted.set(row[10])
    rentdate.set(row[11])
    returndate.set(row[12])
    amountp.set(row[13])
    penaltyperday.set(row[15])
    totalpayment.set(row[16])

                                                #ADMINISTRATOR

#LOGIN INTERFACE FOR THE ADMINISTRATOR
def adminLogin():
    global username_ent, password_ent
    clear_window()

    titlelabel = tk.Label(window, text = "Car Rental System", font = ("Arial", 30, "bold"), border = 12, relief = tk.GROOVE, bg = "lightgray", width = 30)

    titlelabel.place(x = 270, y = 10)

    detail_frame = tk.LabelFrame(window, text="Login", font=("Arial", 20), border=12, relief=tk.GROOVE,
                                 bg="lightgray")
    detail_frame.place(x = 200, y = 90, width = 920, height = 620)

    username_lbl = tk.Label(detail_frame, text="Username", font=("Arial", 15), bg="lightgray")
    username_lbl.grid(row=0, column=0, padx=2, pady=2)
    username_lbl.place(x = 10, y = 105)

    username_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15))
    username_ent.grid(row=0, column=1, padx=2, pady=2)
    username_ent.place(x=150, y=100)

    password_lbl = tk.Label(detail_frame, text="Password", font=("Arial", 15), bg="lightgray")
    password_lbl.grid(row=1, column=0, padx=2, pady=2)
    password_lbl.place(x=10, y=155)

    password_ent = tk.Entry(detail_frame, show = "*", border=7, font=("Arial", 15))
    password_ent.grid(row=1, column=1, padx=2, pady=2)
    password_ent.place(x=150, y=150)

    submit_btn = tk.Button(detail_frame, bg="lightgray", text="Submit", border = 3 , command=nextAdmin, font=("Arial", 10),
                        width=10, height=2)
    submit_btn.grid(row=0, column=0, padx=2, pady=2)
    submit_btn.place(x = 285, y = 220)

    back_btn = tk.Button(detail_frame, bg = "lightgray", text = "Back", border = 3, command = back, font=("Arial", 10), width = 10, height = 2)
    back_btn.grid(row = 0, column = 0, padx = 0, pady = 2)
    back_btn.place(x = 150, y = 220)

    l1 = Label (detail_frame, text = "ADMIN INTERFACE", fg = "GRAY", bg = 'lightgray')
    l1.config (font = ("Lato", 25))
    l1.place (x = 500, y = 10)

#VALIDATING IF THE ADMINISTRATOR'S INPUT WAS CORRECT
def nextAdmin():
    if username_ent.get() == "admin" and password_ent.get() == "admin":
        messagebox.showinfo("ADMINISTRATOR", "LOGIN SUCCESSFULLY")
        admin_button_window()
    else:
        messagebox.showerror("LOGIN FAILED", "PLEASE TRY AGAIN")

#ADMIN INTERFACE
def admin_button_window():
    admin_frame = tk.Frame(window, border=12, bg="lightgray", relief=tk.GROOVE)
    admin_frame.place(x=200, y=90, width=920, height=620)

    titlelabel = tk.Label(window, text="Car Rental System", font=("Arial", 30, "bold"), border=12, relief=tk.GROOVE,
                           bg="lightgray", width = 30)
    titlelabel.place(x= 270, y = 10)

    btn1 = tk.Button(admin_frame, bg = "lightgray", text = "Manage Customer Details", border = 7, command = adminCustomerInterface, font = ("Arial", 10), width = 20, height = 2)
    btn1.grid(row=0, column=0, padx=2, pady=2)
    btn1.place(x = 10, y = 230)

    btn2 = tk.Button(admin_frame, bg = "lightgray", text = "Manage Car Details", border = 7, command = adminCarInterface, font = ("Arial", 10), width = 20, height = 2)
    btn2.grid(row=0, column=0, padx=2, pady=2)
    btn2.place(x = 10, y = 290)

    btn3 = tk.Button(admin_frame, bg = "lightgray", text = "List of Rented Cars", border = 7, command = list_of_rented_cars, font = ("Arial", 10), width = 20, height = 2)
    btn3.grid(row=0, column=0, padx=2, pady=2)
    btn3.place(x = 10, y = 350)

    btn4 = tk.Button(admin_frame, bg = "lightgray", text = "List of Returned Cars", border = 7, command = list_of_returned_cars, font = ("Arial", 10), width = 20, height = 2)
    btn4.grid(row=0, column=0, padx=2, pady=2)
    btn4.place(x = 10, y = 410)

    back_btn = tk.Button(admin_frame, bg = "lightgray", text = "Back", border = 7, command = back, font=("Arial", 10), width = 20, height = 2)
    back_btn.grid(row = 0, column = 0, padx = 2, pady = 2)
    back_btn.place(x = 10, y = 470)

    btn5 = tk.Button(admin_frame, bg="lightgray", text="Exit", border=7, command = exit_button, font=("Arial", 10), width=20, height=2)

    btn5.grid(row=0, column=0, padx=2, pady=2)
    btn5.place(x=10, y= 530)

    l1 = Label (admin_frame, text = "ADMIN INTERFACE", fg = "GRAY", bg = 'lightgray')
    l1.config (font = ("Lato", 25))
    l1.place (x = 550, y = 45)

def exit_button():
    exit()

#FOR UPDATING AND DELETING CUSTOMER
#LISTS OF THE CUSTOMERS WHO REGISTERED USING THE SYSTEM
def adminCustomerInterface():
    global customer_table, search_entry_customer, detail_frame, data_frame
    detail_frame = tk.LabelFrame(window, text="Customer Details", font=("Arial", 20), border=12, relief=tk.GROOVE,
                                 bg="lightgray")
    detail_frame.place(x=20, y=90, width=420, height=620)

    data_frame = tk.Frame(window, border=12, bg="lightgray", relief=tk.GROOVE)
    data_frame.place(x=475, y=90, width=810, height=620)

    id_lbl = tk.Label(detail_frame, text="ID", font=("Arial", 15), bg="lightgray")
    id_lbl.grid(row=0, column=0, padx=2, pady=2)

    id_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=id)
    id_ent.grid(row=0, column=1, padx=2, pady=2)

    fname_lbl = tk.Label(detail_frame, text="First Name", font=("Arial", 15), bg="lightgray")
    fname_lbl.grid(row=1, column=0, padx=2, pady=2)

    fname_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=fname)
    fname_ent.grid(row=1, column=1, padx=2, pady=2)

    lname_lbl = tk.Label(detail_frame, text="Last Name", font=("Arial", 15), bg="lightgray")
    lname_lbl.grid(row=2, column=0, padx=2, pady=2)

    lname_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable = lname)
    lname_ent.grid(row=2, column=1, padx=2, pady=2)

    address_lbl = tk.Label(detail_frame, text="Address", font=("Arial", 15), bg="lightgray")
    address_lbl.grid(row=3, column=0, padx=2, pady=2)

    address_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable = address)
    address_ent.grid(row=3, column=1, padx=2, pady=2)

    contact_lbl = tk.Label(detail_frame, text="Contact No.", font=("Arial", 15), bg="lightgray")
    contact_lbl.grid(row=4, column=0, padx=2, pady=2)

    contact_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=contact)
    contact_ent.grid(row=4, column=1, padx=2, pady=2)

    btn_frame = tk.Frame(detail_frame, bg="lightgray", border=10, relief=tk.GROOVE)
    btn_frame.place(x=22, y=450, width=340, height=80)

    back_btn = tk.Button(detail_frame, bg = "lightgray", text = "Back", border = 3, command = back_customeradmin, font=("Arial", 10), width = 10, height = 1)
    back_btn.grid(row = 0, column = 0, padx = 0, pady = 2)
    back_btn.place(x = 5, y = 530)

    update_btn = tk.Button(btn_frame, bg="lightgray", text="Update Details", border=7, command= update_function_customer, font=("Arial", 10), width= 12, height=2)
    update_btn.grid(row=0, column=0, padx=2, pady=2)

    delete_btn = tk.Button(btn_frame, bg="lightgray", text="Delete Customer", border=7, command=delete_function_customer, font=("Arial", 10), width = 12, height=2)
    delete_btn.grid(row=0, column=1, padx=2, pady=2)

    clear_btn = tk.Button(btn_frame, bg="lightgray", text="Clear", border=7, command=clear_function_customer, font=("Arial", 10),
                          width=6, height=2)
    clear_btn.grid(row=0, column=2, padx=2, pady=2)

    search_frame = tk.Frame(data_frame, bg="lightgray", border=10, relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP, fill=tk.X)

    search_lbl = tk.Label(search_frame, text="Search", bg="lightgray", font=("Arial", 14))
    search_lbl.grid(row=0, column=0, padx=12, pady=2)

    search_entry_customer = tk.Entry(search_frame, font=("Arial", 10))
    search_entry_customer.insert(0, "Search for Last Name")
    search_entry_customer.grid(row=0, column=1, padx=5, pady=5)

    search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), border=9, width=14, bg="lightgray",
                           command=search_function_customer)
    search_btn.grid(row=0, column=2, padx=12, pady=2)

    showAll_btn = tk.Button(search_frame, text="Show All", font=("Arial", 13), border=9, width=14, bg="lightgray",
                            command= showall_function_customer)
    showAll_btn.grid(row=0, column=3, padx=12, pady=2)

    main_frame = tk.Frame(data_frame, bg="lightgray", border=11, relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH, expand=True)

    y_scroll = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame, orient=tk.HORIZONTAL)

    customer_table = ttk.Treeview(main_frame, columns=(
        "ID", "First Name", "Last Name", "Address", "Contact No"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command=customer_table.yview)
    x_scroll.config(command=customer_table.xview)

    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    customer_table.heading("ID", text="ID")
    customer_table.heading("First Name", text="First Name")
    customer_table.heading("Last Name", text="Last Name")
    customer_table.heading("Address", text="Address")
    customer_table.heading("Contact No", text="Contact No")

    customer_table['show'] = "headings"
    customer_table.column("ID", width=100)
    customer_table.column("First Name", width=100)
    customer_table.column("Last Name", width=100)
    customer_table.column("Address", width=100)
    customer_table.column("Contact No", width=100)

    customer_table.pack(fill=tk.BOTH, expand=True)

    fetch_data_customer()

    customer_table.bind("<ButtonRelease -1>", get_data_customer)

#FOR UPDATING CUSTOMER DETAILS
def update_function_customer():
    if fname.get() == "" or lname.get() == "" or address.get() == "" or contact.get() == "":
        messagebox.showerror("Error", "Please fill all the fields")
    else:
        res = messagebox.askquestion("Confirm", "Confirm Update?")
        if res == True:
            conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
            curr = conn.cursor()
            curr.execute("update customertable set fname = %s, lname = %s, address = %s, contactnumber = %s where customerid = %s",(fname.get(), lname.get(), address.get(), contact.get(), id.get()))
            conn.commit()
            fetch_data_customer()
            conn.close()
        elif res == False:
            pass
        else:
            pass
        conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
        curr = conn.cursor()
        curr.execute(
            "update customertable set fname = %s, lname = %s, address = %s, contactnumber = %s where customerid = %s",
            (fname.get(), lname.get(), address.get(), contact.get(), id.get()))
        conn.commit()
        fetch_data_customer()
        conn.close()

#FOR DELETING CUSTOMER DETAILS
def delete_function_customer():
    if fname.get() == "" or lname.get() == "" or address.get() == "" or contact.get() == "":
        messagebox.showerror("Error", "Unable to delete. Please fill all the fields.")
    else:
        res = messagebox.askquestion("Confirm", "Are you sure you want to delete?")
        if res == True:
            conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
            curr = conn.cursor()
            curr.execute("DELETE from customertable WHERE contactnumber = %s", (contact.get()))
            conn.commit()
            fetch_data_customer()
            conn.close()
        elif res == False:
            pass
        else:
            pass
        conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
        curr = conn.cursor()
        curr.execute("DELETE from customertable WHERE contactnumber = %s", (contact.get()))
        conn.commit()
        fetch_data_customer()
        conn.close()

def clear_function_customer():
    id.set("")
    fname.set("")
    lname.set("")
    address.set("")
    contact.set("")

def search_function_customer():
    lookup_record_customer = search_entry_customer.get()
    for record in customer_table.get_children():
        customer_table.delete(record)
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT  * from customertable WHERE lname = %s", (lookup_record_customer))
    rows = curr.fetchall()

    global count
    count = 0
    for record in rows:
        if count % 2 == 0:
            customer_table.insert(parent='', index='end', iid=count, text='',
                                  values=(record[0], record[1], record[2], record[3], record[4]),
                                  tags=('evenrow',))
        else:
            customer_table.insert(parent='', index='end', iid=count, text='',
                                  values=(record[0], record[1], record[2], record[3], record[4]),
                                  tags=('oddrow',))
        count += 1
    conn.commit()
    conn.close()

def showall_function_customer():
    fetch_data_customer()

def fetch_data_customer():
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT * FROM customertable")
    rows = curr.fetchall()
    if len(rows) != 0:
        customer_table.delete(*customer_table.get_children())
        for row in rows:
            customer_table.insert('', tk.END, values=row)
        conn.commit()
    conn.close()

def get_data_customer(event):
    cursor_row = customer_table.focus()
    content = customer_table.item(cursor_row)

    row = content['values']
    id.set(row[0])
    fname.set(row[1])
    lname.set(row[2])
    address.set(row[3])
    contact.set(row[4])

#LISTS OF RENTED CARS AND THEIR DETAILS
def list_of_rented_cars():
    global rentedcars_table, search_entry_returnedcars, search_entry_rentedcars, data_frame
    data_frame = tk.Frame(window, border=12, bg="lightgray", relief=tk.GROOVE)
    data_frame.place(x=200, y=90, width=920, height=620)

    search_frame = tk.Frame(data_frame, bg="lightgray", border=10, relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP, fill=tk.X)

    search_lbl = tk.Label(search_frame, text="Search", bg="lightgray", font=("Arial", 14))
    search_lbl.grid(row=0, column=0, padx=12, pady=2)

    search_entry_rentedcars = tk.Entry(search_frame, font=("Arial", 10))
    search_entry_rentedcars.insert(0, "Search for Car ID")
    search_entry_rentedcars.grid(row=0, column=1, padx=5, pady=5)

    back_btn = tk.Button(window, bg = "lightgray", border = 3, text = "Back", width = 10, command = back_listofrented)
    back_btn.place(x = 230, y = 650)

    search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), border=9, width=14, bg="lightgray",
                           command=search_rentedcars)
    search_btn.grid(row=0, column=2, padx=12, pady=2)

    showAll_btn = tk.Button(search_frame, text="Show All", font=("Arial", 13), border=9, width=14, bg="lightgray",
                            command=showall_rentedcars)
    showAll_btn.grid(row=0, column=3, padx=12, pady=2)

    main_frame = tk.Frame(data_frame, bg="lightgray", border=11, relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH, expand=True)

    y_scroll = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame, orient=tk.HORIZONTAL)

    rentedcars_table = ttk.Treeview(main_frame, columns=(
        "ID", "Car ID", "Customer ID", "Brand", "Year Model",
        "Color", "Plate No", "Car Seats", "Auto / Manual",
        "Preferred Gas", "Tinted", "Date of Rent", "Date of Return", "Total Days", "Price per day", "Penalty per day", "Total Payment"),
                                    yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command=rentedcars_table.yview)
    x_scroll.config(command=rentedcars_table.xview)

    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    rentedcars_table.heading("ID", text="ID")
    rentedcars_table.heading("Car ID", text="Car ID")
    rentedcars_table.heading("Customer ID", text="Customer ID")
    rentedcars_table.heading("Brand", text="Brand")
    rentedcars_table.heading("Year Model", text="Year Model")
    rentedcars_table.heading("Color", text="Color")
    rentedcars_table.heading("Plate No", text="Plate No")
    rentedcars_table.heading("Car Seats", text="Car Seats")
    rentedcars_table.heading("Auto / Manual", text="Auto / Manual")
    rentedcars_table.heading("Preferred Gas", text="Preferred Gas")
    rentedcars_table.heading("Tinted", text="Tinted")
    rentedcars_table.heading("Date of Rent", text="Date of Rent")
    rentedcars_table.heading("Date of Return", text="Date of Return")
    rentedcars_table.heading("Total Days", text="Total Days")
    rentedcars_table.heading("Price per day", text="Price per day")
    rentedcars_table.heading("Penalty per day", text="Penalty per day")
    rentedcars_table.heading("Total Payment", text= "Total Payment")

    rentedcars_table['show'] = "headings"
    rentedcars_table.column("ID", width=100)
    rentedcars_table.column("Car ID", width=100)
    rentedcars_table.column("Customer ID", width=100)
    rentedcars_table.column("Brand", width = 100)
    rentedcars_table.column("Year Model", width = 100)
    rentedcars_table.column("Color", width = 100)
    rentedcars_table.column("Plate No", width = 100)
    rentedcars_table.column("Car Seats", width = 100)
    rentedcars_table.column("Auto / Manual", width = 100)
    rentedcars_table.column("Preferred Gas", width = 100)
    rentedcars_table.column("Tinted", width = 100)
    rentedcars_table.column("Date of Rent", width=100)
    rentedcars_table.column("Date of Return", width=100)
    rentedcars_table.column("Total Days", width=100)
    rentedcars_table.column("Price per day", width=100)
    rentedcars_table.column("Penalty per day", width=100)
    rentedcars_table.column("Total Payment", width=100)

    rentedcars_table.pack(fill=tk.BOTH, expand=True)

    fetch_data_rentedcars()

def fetch_data_rentedcars():
    conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "carrental")
    curr = conn.cursor()
    curr.execute("SELECT * FROM renttable")
    rows = curr.fetchall()
    if len(rows) != 0:
        rentedcars_table.delete(*rentedcars_table.get_children())
    for row in rows:
        rentedcars_table.insert('', tk.END, values = row)
    conn.commit()
    conn.close()

#LIST OF RETURNED CARS AND THEIR DETAILS
def list_of_returned_cars():
    global returnedcars_table, search_entry_returnedcars, data_frame
    data_frame = tk.Frame(window, border=12, bg="lightgray", relief=tk.GROOVE)
    data_frame.place(x=200, y=90, width=920, height=620)

    search_frame = tk.Frame(data_frame, bg="lightgray", border=10, relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP, fill=tk.X)

    search_lbl = tk.Label(search_frame, text="Search", bg="lightgray", font=("Arial", 14))
    search_lbl.grid(row=0, column=0, padx=12, pady=2)

    search_entry_returnedcars = tk.Entry(search_frame, font=("Arial", 10))
    search_entry_returnedcars.insert (0, "Search for Customer ID")
    search_entry_returnedcars.grid(row=0, column=1, padx=5, pady=5)

    back_btn = tk.Button(window, bg = "lightgray", border = 3, text = "Back", width = 10, command = back_listofreturned)
    back_btn.place(x = 230, y = 650)

    search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), border=9, width=14, bg="lightgray",
                           command=search_returnedcars)
    search_btn.grid(row=0, column=2, padx=12, pady=2)

    showAll_btn = tk.Button(search_frame, text="Show All", font=("Arial", 13), border=9, width=14, bg="lightgray",
                            command=showall_returnedcars)
    showAll_btn.grid(row=0, column=3, padx=12, pady=2)

    main_frame = tk.Frame(data_frame, bg="lightgray", border=11, relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH, expand=True)

    y_scroll = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame, orient=tk.HORIZONTAL)

    returnedcars_table = ttk.Treeview(main_frame, columns=(
        "ID", "Rent ID", "Car ID", "Customer ID", "Date of Rent", "Date of Return", "Amount of Payment",
        "Penalty per day", "No of Penalty Days", "Total Payment"),
                                    yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command=returnedcars_table.yview)
    x_scroll.config(command=returnedcars_table.xview)

    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    returnedcars_table.heading("ID", text="ID")
    returnedcars_table.heading("Rent ID", text="Rent ID")
    returnedcars_table.heading("Car ID", text="Car ID")
    returnedcars_table.heading("Customer ID", text="Customer ID")
    returnedcars_table.heading("Date of Rent", text="Date of Rent")
    returnedcars_table.heading("Date of Return", text="Date of Return")
    returnedcars_table.heading("Amount of Payment", text="Amount of Payment")
    returnedcars_table.heading("Penalty per day", text="Penalty per day")
    returnedcars_table.heading("No of Penalty Days", text="No of Penalty Days")
    returnedcars_table.heading("Total Payment", text="Total Payment")

    returnedcars_table['show'] = "headings"
    returnedcars_table.column("ID", width=100)
    returnedcars_table.column("Rent ID", width=100)
    returnedcars_table.column("Car ID", width=100)
    returnedcars_table.column("Customer ID", width=100)
    returnedcars_table.column("Date of Rent", width=100)
    returnedcars_table.column("Date of Return", width=100)
    returnedcars_table.column("Amount of Payment", width=120)
    returnedcars_table.column("Penalty per day", width=100)
    returnedcars_table.column("No of Penalty Days", width=120)
    returnedcars_table.column("Total Payment", width=100)

    returnedcars_table.pack(fill=tk.BOTH, expand=True)

    fetch_data_returnedcars()

def search_rentedcars():
    lookup_record = search_entry_rentedcars.get()
    for record in rentedcars_table.get_children():
        rentedcars_table.delete(record)
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT  * from renttable WHERE carid = %s", (lookup_record))
    rows = curr.fetchall()

    global count
    count = 0
    for record in rows:
        if count % 2 == 0:
            rentedcars_table.insert(parent='', index='end', iid=count, text='',
                                      values=(
                                      record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                      record[7], record[8], record[9], record[10], record[11], record[11], record[12],
                                      record[13], record[14], record[15], record[16]),
                                      tags=('evenrow',))
        else:
            rentedcars_table.insert(parent='', index='end', iid=count, text='',
                                      values=(
                                      record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                      record[7], record[8],record[9], record[10], record[11], record[12], record[13],
                                      record[14], record[15], record[16]),
                                      tags=('oddrow',))
        count += 1
    conn.commit()
    conn.close()

def showall_rentedcars():
    fetch_rentedcars()

def fetch_rentedcars():
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT * FROM renttable")
    rows = curr.fetchall()
    if len(rows) != 0:
        rentedcars_table.delete(*rentedcars_table.get_children())
    for row in rows:
        rentedcars_table.insert('', tk.END, values=row)
    conn.commit()
    conn.close()

def search_returnedcars():
    lookup_record = search_entry_returnedcars.get()
    for record in returnedcars_table.get_children():
        returnedcars_table.delete(record)
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT  * from returntable WHERE customerid = %s", (lookup_record))
    rows = curr.fetchall()

    global count
    count = 0
    for record in rows:
        if count % 2 == 0:
            returnedcars_table.insert(parent='', index='end', iid=count, text='',
                                  values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]),
                                  tags=('evenrow',))
        else:
            returnedcars_table.insert(parent='', index='end', iid=count, text='',
                                  values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],
                                          record[9]),
                                  tags=('oddrow',))
        count += 1
    conn.commit()
    conn.close()

def showall_returnedcars():
    fetch_returnedcars()

def fetch_returnedcars():
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT * FROM returntable")
    rows = curr.fetchall()
    if len(rows) != 0:
        returnedcars_table.delete(*returnedcars_table.get_children())
    for row in rows:
        returnedcars_table.insert('', tk.END, values=row)
    conn.commit()
    conn.close()

def fetch_data_returnedcars():
    conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
    curr = conn.cursor()
    curr.execute("SELECT * FROM returntable")
    rows = curr.fetchall()
    if len(rows) != 0:
        returnedcars_table.delete(*returnedcars_table.get_children())
    for row in rows:
        returnedcars_table.insert('', tk.END, values=row)
    conn.commit()
    conn.close()

#FOR ADDING, UPDATING, AND DELETING CAR DETAILS
#LISTS OF CARS IN THE SYSTEM
def adminCarInterface():
    global detail_frame, data_frame, main_frame, search_entry, car_table, btn_frame
    detail_frame = tk.LabelFrame(window, text="Car Details", font=("Arial", 20), border=12, relief=tk.GROOVE,
                                 bg="lightgray")
    detail_frame.place(x=20, y=90, width=420, height=620)

    data_frame = tk.Frame(window, border=12, bg="lightgray", relief=tk.GROOVE)
    data_frame.place(x=475, y=90, width=810, height=620)

    brand_lbl = tk.Label(detail_frame, text="Brand", font=("Arial", 15), bg="lightgray")
    brand_lbl.grid(row=0, column=0, padx=2, pady=2)

    brand_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=brand)
    brand_ent.grid(row=0, column=1, padx=2, pady=2)

    yearmodel_lbl = tk.Label(detail_frame, text="Year Model", font=("Arial", 15), bg="lightgray")
    yearmodel_lbl.grid(row=1, column=0, padx=2, pady=2)

    yearmodel_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=year_model)
    yearmodel_ent.grid(row=1, column=1, padx=2, pady=2)

    color_lbl = tk.Label(detail_frame, text="Color", font=("Arial", 15), bg="lightgray")
    color_lbl.grid(row=2, column=0, padx=2, pady=2)

    brand_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=color)
    brand_ent.grid(row=2, column=1, padx=2, pady=2)

    plate_lbl = tk.Label(detail_frame, text="Plate No.", font=("Arial", 15), bg="lightgray")
    plate_lbl.grid(row=3, column=0, padx=2, pady=2)

    plate_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=plate_no)
    plate_ent.grid(row=3, column=1, padx=2, pady=2)

    carseats_lbl = tk.Label(detail_frame, text="Car Seats", font=("Arial", 15), bg="lightgray")
    carseats_lbl.grid(row=4, column=0, padx=2, pady=2)

    carseats_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=car_seats)
    carseats_ent.grid(row=4, column=1, padx=2, pady=2)

    am_lbl = tk.Label(detail_frame, text="Auto / Manual", font=("Arial", 15), bg="lightgray")
    am_lbl.grid(row=5, column=0, padx=2, pady=2)

    am_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=auto_manual)
    am_ent.grid(row=5, column=1, padx=2, pady=2)

    pg_lbl = tk.Label(detail_frame, text="Preferred Gas", font=("Arial", 15), bg="lightgray")
    pg_lbl.grid(row=6, column=0, padx=2, pady=2)

    pg_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=preferred_gas)
    pg_ent.grid(row=6, column=1, padx=2, pady=2)

    tinted_lbl = tk.Label(detail_frame, text="Tinted", font=("Arial", 15), bg="lightgray")
    tinted_lbl.grid(row=7, column=0, padx=2, pady=2)

    tinted_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=tinted)
    tinted_ent.grid(row=7, column=1, padx=2, pady=2)

    ppd_lbl = tk.Label(detail_frame, text="Price per day", font=("Arial", 15), bg="lightgray")
    ppd_lbl.grid(row=8, column=0, padx=2, pady=2)

    prpd_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=prpd)
    prpd_ent.grid(row=8, column=1, padx=2, pady=2)

    penpd_lbl = tk.Label(detail_frame, text="Penalty per day", font=("Arial", 15), bg="lightgray")
    penpd_lbl.grid(row=9, column=0, padx=2, pady=2)

    penpd_ent = tk.Entry(detail_frame, border=7, font=("Arial", 15), textvariable=penpd)
    penpd_ent.grid(row=9, column=1, padx=2, pady=2)

    btn_frame = tk.Frame(detail_frame, bg="lightgray", border=10, relief=tk.GROOVE)
    btn_frame.place(x=22, y=450, width=340, height=80)

    add_btn = tk.Button(btn_frame, bg="lightgray", text="Add Car", border=7, command=add_function_car, font=("Arial", 10),
                        width=7, height=2)
    add_btn.grid(row=0, column=0, padx=2, pady=2)

    delete_btn = tk.Button(btn_frame, bg="lightgray", text="Delete Car", border=7, command=delete_function_car,
                           font=("Arial", 10), width=7, height=2)
    delete_btn.grid(row=0, column=2, padx=2, pady=2)

    update_btn = tk.Button(btn_frame, bg="lightgray", text="Update Car", border=7, command=update_function_car,
                           font=("Arial", 10), width=8, height=2)
    update_btn.grid(row=0, column=1, padx=2, pady=2)


    clear_btn = tk.Button(btn_frame, bg="lightgray", text="Clear", border=7, command=clear_function_car, font=("Arial", 10),
                          width=5, height=2)
    clear_btn.grid(row=0, column=3, padx=2, pady=2)

    back_btn = tk.Button(detail_frame, bg = "lightgray", text = "Back", border = 3, command = back_caradmin, font=("Arial", 10), width = 10, height = 1)
    back_btn.grid(row = 0, column = 0, padx = 0, pady = 2)
    back_btn.place(x = 30, y = 530)

    search_frame = tk.Frame(data_frame, bg="lightgray", border=10, relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP, fill=tk.X)

    search_lbl = tk.Label(search_frame, text="Search", bg="lightgray", font=("Arial", 14))
    search_lbl.grid(row=0, column=0, padx=12, pady=2)

    search_entry = tk.Entry(search_frame, font=("Arial", 10))
    search_entry.insert(0, "Search for Brand")
    search_entry.grid(row=0, column=1, padx=5, pady=5)

    search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), border=9, width=14, bg="lightgray",
                           command=search_function_car)
    search_btn.grid(row=0, column=2, padx=12, pady=2)

    showAll_btn = tk.Button(search_frame, text="Show All", font=("Arial", 13), border=9, width=14, bg="lightgray",
                            command=showall_function)
    showAll_btn.grid(row=0, column=3, padx=12, pady=2)

    main_frame = tk.Frame(data_frame, bg="lightgray", border=11, relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH, expand=True)

    y_scroll = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame, orient=tk.HORIZONTAL)

    car_table = ttk.Treeview(main_frame, columns=(
    "ID", "Brand", "Year Model", "Color", "Plate No.", "Car Seats", "Auto / Manual", "Preferred Gas", "Tinted",
    "Price per Day", "Penalty per Day"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command=car_table.yview)
    x_scroll.config(command=car_table.xview)

    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    car_table.heading("ID", text="ID")
    car_table.heading("Brand", text="Brand")
    car_table.heading("Year Model", text="Year Model")
    car_table.heading("Color", text="Color")
    car_table.heading("Plate No.", text="Plate No.")
    car_table.heading("Car Seats", text="Car Seats")
    car_table.heading("Auto / Manual", text="Auto / Manual")
    car_table.heading("Preferred Gas", text="Preferred Gas")
    car_table.heading("Tinted", text="Tinted")
    car_table.heading("Price per Day", text="Price per Day")
    car_table.heading("Penalty per Day", text="Penalty per Day")

    car_table['show'] = "headings"
    car_table.column("ID", width=100)
    car_table.column("Brand", width=100)
    car_table.column("Year Model", width=100)
    car_table.column("Color", width=100)
    car_table.column("Plate No.", width=100)
    car_table.column("Car Seats", width=100)
    car_table.column("Auto / Manual", width=100)
    car_table.column("Preferred Gas", width=100)
    car_table.column("Tinted", width=100)
    car_table.column("Price per Day", width=100)
    car_table.column("Penalty per Day", width=100)

    car_table.pack(fill=tk.BOTH, expand=True)

    fetch_data_car()

    car_table.bind("<ButtonRelease -1>", get_data_car)

#FOR THE ADMINISTRATOR TO ADD CARS
def add_function_car():
    if brand.get() == "" or year_model.get() == "" or color.get() == "" or plate_no.get() == "" or car_seats.get() == "" or auto_manual.get() == "" or preferred_gas.get() == "" or tinted.get() == "" or prpd.get() == "" or penpd.get() == "":

        messagebox.showerror("Error", "Please fill all the fields")
    else:
        res = messagebox.askquestion("Confirm", "Are you sure you want to add?")
        if res == True:
            conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
            curr = conn.cursor()
            curr.execute("INSERT INTO cartable VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
            id.get, brand.get(), year_model.get(), color.get(), plate_no.get(), car_seats.get(), auto_manual.get(),
            preferred_gas.get(), tinted.get(), prpd.get(), penpd.get()))
            conn.commit()
            conn.close()

            fetch_data_car()
        elif res == False:
            pass
        else:
            pass
        conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "carrental")
        curr = conn.cursor()
        curr.execute("INSERT INTO cartable VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(id.get, brand.get(), year_model.get(), color.get(), plate_no.get(), car_seats.get(),auto_manual.get(), preferred_gas.get(), tinted.get(), prpd.get(), penpd.get()))
        conn.commit()
        conn.close()

        fetch_data_car()

def clear_function_car():
    id.set("")
    brand.set("")
    year_model.set("")
    color.set("")
    plate_no.set("")
    car_seats.set("")
    auto_manual.set("")
    preferred_gas.set("")
    tinted.set("")
    prpd.set("")
    penpd.set("")

#FOR THE ADMINISTRATOR TO UPDATE CAR DETAILS
def update_function_car():
    if brand.get() == "" or year_model.get() == "" or color.get() == "" or plate_no.get() == "" or car_seats.get() == "" or auto_manual.get() == "" or preferred_gas.get() == "" or tinted.get() == "" or prpd.get() == "" or penpd.get() == "":

        messagebox.showerror("Error", "Please fill all the fields")
    else:
        res = messagebox.askquestion("Confirm", "Confirm Update?")
        if res == True:
            conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "carrental")
            curr = conn.cursor()
            curr.execute("update cartable set brand = %s, year_model = %s, color = %s, plate_no = %s, car_seats = %s, auto_manual = %s, preferred_gas = %s, tinted = %s, prpd = %s, penpd = %s where carid = %s",(brand.get(), year_model.get(), color.get(), plate_no.get(), car_seats.get(), auto_manual.get(), preferred_gas.get(), tinted.get(), prpd.get(), penpd.get(), id.get()))
            conn.commit()
            fetch_data_car()
            conn.close()
            fetch_data_car()
        elif res == False:
            pass
        else:
            pass
        conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
        curr = conn.cursor()
        curr.execute(
            "update cartable set brand = %s, year_model = %s, color = %s, plate_no = %s, car_seats = %s, auto_manual = %s, preferred_gas = %s, tinted = %s, prpd = %s, penpd = %s where carid = %s",
            (brand.get(), year_model.get(), color.get(), plate_no.get(), car_seats.get(), auto_manual.get(),
             preferred_gas.get(), tinted.get(), prpd.get(), penpd.get(), id.get()))
        conn.commit()
        fetch_data_car()
        conn.close()
        fetch_data_car()

#FOR THE ADMINISTRATOR TO DELETE CAR DETAILS
def delete_function_car():
    if brand.get() == "" or year_model.get() == "" or color.get() == "" or plate_no.get() == "" or car_seats.get() == "" or auto_manual.get() == "" or preferred_gas.get() == "" or tinted.get() == "" or prpd.get() == "" or penpd.get() == "":

        messagebox.showerror("Error", "Unable to delete. Please fill all the fields.")
    else:
        res = messagebox.askquestion("Confirm", "Are you sure you want to delete?")
        if res == True:
            conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
            curr = conn.cursor()
            curr.execute("DELETE from cartable WHERE plate_no = %s", (plate_no.get()))
            conn.commit()
            fetch_data_car()
            conn.close()
            fetch_data_car()
        elif res == False:
            pass
        else:
            pass
        conn = pymysql.connect(host="localhost", user="root", password="", database="carrental")
        curr = conn.cursor()
        curr.execute("DELETE from cartable WHERE plate_no = %s", (plate_no.get()))
        conn.commit()
        fetch_data_car()
        conn.close()
        fetch_data_car()

def fetch_data_car():
    conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "carrental")
    curr = conn.cursor()
    curr.execute("SELECT * FROM cartable")
    rows = curr.fetchall()
    if len(rows) != 0:
        car_table.delete(*car_table.get_children())
    for row in rows:
        car_table.insert('', tk.END, values = row)
    conn.commit()
    conn.close()

def get_data_car(event):
    cursor_row = car_table.focus()
    content = car_table.item(cursor_row)

    row = content['values']
    id.set(row[0])
    brand.set(row[1])
    year_model.set(row[2])
    color.set(row[3])
    plate_no.set(row[4])
    car_seats.set(row[5])
    auto_manual.set(row[6])
    preferred_gas.set(row[7])
    tinted.set(row[8])
    prpd.set(row[9])
    penpd.set(row[10])

def search_function_car():
    lookup_record = search_entry.get()
    for record in car_table.get_children():
        car_table.delete(record)
    conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "carrental")
    curr = conn.cursor()
    curr.execute("SELECT  * from cartable WHERE brand = %s",(lookup_record))
    rows = curr.fetchall()
    global count
    count = 0
    for record in rows:
        if count % 2 == 0:
            car_table.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10]),
                           tags=('evenrow',))
        else:
            car_table.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10]),
                           tags=('oddrow',))
        count += 1
    conn.commit()
    conn.close()

def showall_function():
    fetch_data_car()

    car_table.heading("ID", text = "ID")
    car_table.heading("Brand", text = "Brand")
    car_table.heading("Year Model", text = "Year Model")
    car_table.heading("Color", text = "Color")
    car_table.heading("Plate No.", text = "Plate No.")
    car_table.heading("Car Seats", text = "Car Seats")
    car_table.heading("Auto / Manual", text = "Auto / Manual")
    car_table.heading("Preferred Gas", text = "Preferred Gas")
    car_table.heading("Tinted", text = "Tinted")
    car_table.heading("Price per Day", text = "Price per Day")
    car_table.heading("Penalty per Day", text = "Penalty per Day")

    car_table['show'] = "headings"
    car_table.column("ID", width = 100)
    car_table.column("Brand", width = 100)
    car_table.column("Year Model", width = 100)
    car_table.column("Color", width = 100)
    car_table.column("Plate No.", width = 100)
    car_table.column("Car Seats", width = 100)
    car_table.column("Auto / Manual", width = 100)
    car_table.column("Preferred Gas", width = 100)
    car_table.column("Tinted", width = 100)
    car_table.column("Price per Day", width = 100)
    car_table.column("Penalty per Day", width = 100)

    car_table.pack(fill = tk.BOTH, expand = True)
    fetch_data_car()
    car_table.bind("<ButtonRelease -1>",get_data_car)

#HAMBURGER MENU - SHOWN AS "OPEN" IN THE SYSTEM
def toggle_window():
    global f1
    f1 = Frame(window, width = 250, height = 250, bg = "#262626")
    f1.place (x = 0, y = 0)

    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_enters(e):
            myButton['background'] = bcolor #ffcc66
            myButton['foreground'] = '#262626' #000d33
        def on_leaves(e):
            myButton['background'] = fcolor
            myButton['foreground'] = '#262626'

        myButton = Button(f1, text = text,
                          width = 32, height = 2, fg = 'white',
                          border = 0, bg = fcolor, activeforeground = 'white',
                          activebackground = bcolor, command = cmd)
        myButton.bind("<Enter>", on_enters)
        myButton.bind("<Leave>", on_leaves)
        myButton.place(x=x, y=y)

    bttn(0, 80, 'REGISTER', 'white', '#262626', registerCustomer)
    bttn(0, 117, 'LOGIN AS CUSTOMER', 'white', '#262626', customer_button_window)
    bttn(0, 154, 'LOGIN AS ADMIN', 'white', '#262626', adminLogin)
    def dele():
        f1.destroy()
    Button(f1, text = "close", command = dele, border = 0, activebackground = '#CDC0B0', bg = '#262626', fg = "white").place(x= 5, y = 10)
Button (window, command = toggle_window, text = "OPEN", border = 0, bg = '#262626', activebackground = '#CDC0B0', fg = "white").place(x=5, y=10)

                                                #FUNCTIONS
def back_rent():
    clear1_window()
    clear_rent_frame()
    toggle_window()
    customer_button_window()

def back_return():
    clear1_window()
    clear_return_frame()
    toggle_window()
    customer_button_window()

def back_register():
    clear_window()
    clear_frontframe()
    front()
    toggle_window()

def back():
    clear_window()
    clear_frontframe()
    front()
    toggle_window()

def back_caradmin():
    clear1_window()
    clear_admin_frame()
    admin_button_window()

def back_customeradmin():
    clear1_window()
    clear_customerinterface_frame()
    admin_button_window()

def back_listofrented():
    clear1_window()
    clear_listofrented_frame()
    admin_button_window()

def back_listofreturned():
    clear1_window()
    clear_listofreturned_frame()
    admin_button_window()

def clear_frontframe():
    for widget in front_frame.winfo_children():
        widget.destroy()

def clear_admin_frame():
    for widget in detail_frame.winfo_children():
        widget.destroy()
    for widget in data_frame.winfo_children():
        widget.destroy()

def clear_return_frame():
    for widget in detail_frame.winfo_children():
        widget.destroy()
    for widget in rentdata_frame.winfo_children():
            widget.destroy()
    for widget in returndata_frame.winfo_children():
            widget.destroy()

def clear_rent_frame():
    for widget in detail_frame.winfo_children():
        widget.destroy()
    for widget in main_frame.winfo_children():
        widget.destroy()
    for widget in customerdata_frame.winfo_children():
        widget.destroy()

def clear_customerinterface_frame():
    for widget in detail_frame.winfo_children():
        widget.destroy()
    for widget in data_frame.winfo_children():
        widget.destroy()

def clear_listofrented_frame():
    for widget in data_frame.winfo_children():
        widget.destroy()

def clear_listofreturned_frame():
    for widget in data_frame.winfo_children():
        widget.destroy()

def main_interface():
    clear_window()

front()
window.mainloop()
