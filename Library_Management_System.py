import tkinter
from tkinter import messagebox
from tkinter import ttk
import tkinter.font
import mysql.connector
from datetime import datetime, timedelta, date

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nazi1990",
    database="library_system"
)
mycursor = mydb.cursor()

window = tkinter.Tk()
window.title("Library Management System")
window.state('zoomed')
bg = tkinter.PhotoImage(
    file="D:\C Data\Documents\ECUST Class Related Documents (IMPORTANT)\Y3\S1\Database Principles\Final Project\lib.png")
bg_img = tkinter.Label(window, image=bg)
bg_img.place(relwidth=1, relheight=1)
label_font = tkinter.font.Font(
    family="Monotype Corsiva", size=30, weight="bold")
normal_font = tkinter.font.Font(
    family="Simplified Arabic", size=16, weight='bold')
s = ttk.Style()
s.configure('Zain.Treeview', background='#333333', foreground='#FFFFFF')
user_image = tkinter.PhotoImage(
    file=r"D:\C Data\Documents\ECUST Class Related Documents (IMPORTANT)\Y3\S1\Database Principles\Final Project\user_img.png")


def login_page():
    global customer_login
    customer_login = tkinter.Frame(
        window, bg='#333333', highlightbackground='cyan', highlightthickness=2)
    # Creating widgets
    cus_login_label = tkinter.Label(
        customer_login, text="Customer Login", bg='#333333', fg="#FF3399", font=label_font)
    cus_username_label = tkinter.Label(
        customer_login, text="ID", bg='#333333', fg="#FFFFFF", font=normal_font)

    def cus_login():
        global cus_username_login
        cus_username_login = cus_username_entry.get()
        username_check = 0
        password_check = 0

        cus_login_query = "SELECT customer_id FROM customers"
        mycursor.execute(cus_login_query)
        rows = mycursor.fetchall()
        for row in rows:
            for col in row:
                converted_col = str(col)
                if cus_username_login == converted_col:
                    username_check = 1
                    break

        mycursor.execute(
            "SELECT password FROM passwords WHERE customer_id = (%s)", (cus_username_login,))
        passes = mycursor.fetchall()
        for row in passes:
            for col in row:
                if cus_password_entry.get() == col:
                    password_check = 1

        if username_check == 1 and password_check == 1:
            messagebox.showinfo(title="Login Success",
                                message="You successfully logged in.")
            cus_menu()
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    cus_username_entry = tkinter.Entry(customer_login, font=normal_font)
    cus_password_entry = tkinter.Entry(
        customer_login, show="*", font=normal_font)

    cus_password_label = tkinter.Label(
        customer_login, text="Password", bg='#333333', fg="#FFFFFF", font=normal_font)
    cus_login_button = tkinter.Button(
        customer_login, text="Login", bg="#FF3399", fg="#FFFFFF", font=normal_font, command=cus_login)

    # Placing widgets on the screen
    cus_login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    cus_username_label.grid(row=1, column=0)
    cus_username_entry.grid(row=1, column=1, pady=20)
    cus_password_label.grid(row=2, column=0)
    cus_password_entry.grid(row=2, column=1, pady=20)
    cus_login_button.grid(row=3, column=0, columnspan=2, pady=30)

    customer_login.place(relx=0.1, rely=0.25, relwidth=0.25, relheight=0.5)

    # -----------------------Employee Login---------------------------------------

    global employee_login
    employee_login = tkinter.Frame(
        window, bg='#333333', highlightbackground='cyan', highlightthickness=2)
    # Creating widgets
    em_login_label = tkinter.Label(
        employee_login, text="Employee Login", bg='#333333', fg="#FF3399", font=label_font)
    em_username_label = tkinter.Label(
        employee_login, text="ID", bg='#333333', fg="#FFFFFF", font=normal_font)

    def em_login():
        global em_username_login
        em_username_login = em_username_entry.get()
        username_check = 0
        password_check = 0

        em_login_query = "SELECT staff_id FROM staff"
        mycursor.execute(em_login_query)
        rows = mycursor.fetchall()
        for row in rows:
            for col in row:
                converted_col = str(col)
                if em_username_login == converted_col:
                    username_check = 1
                    break

        mycursor.execute(
            "SELECT password FROM em_password WHERE staff_id = (%s)", (em_username_login,))
        passes = mycursor.fetchall()
        for row in passes:
            for col in row:
                if em_password_entry.get() == col:
                    password_check = 1

        if username_check == 1 and password_check == 1:
            messagebox.showinfo(title="Login Success",
                                message="You successfully logged in.")
            em_menu()
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    em_username_entry = tkinter.Entry(employee_login, font=normal_font)
    em_password_entry = tkinter.Entry(
        employee_login, show="*", font=normal_font)

    em_password_label = tkinter.Label(
        employee_login, text="Password", bg='#333333', fg="#FFFFFF", font=normal_font)
    em_login_button = tkinter.Button(
        employee_login, text="Login", bg="#FF3399", fg="#FFFFFF", font=normal_font, command=em_login)

    # Placing widgets on the screen
    em_login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    em_username_label.grid(row=1, column=0)
    em_username_entry.grid(row=1, column=1, pady=20)
    em_password_label.grid(row=2, column=0)
    em_password_entry.grid(row=2, column=1, pady=20)
    em_login_button.grid(row=3, column=0, columnspan=2, pady=30)

    employee_login.place(relx=0.4, rely=0.25, relwidth=0.25, relheight=0.5)

    # ----------------------Admin Login-----------------
    global admin_login
    admin_login = tkinter.Frame(
        window, bg='#333333', highlightbackground='cyan', highlightthickness=2)
    # Creating widgets
    ad_login_label = tkinter.Label(
        admin_login, text="Admin Login", bg='#333333', fg="#FF3399", font=label_font)
    ad_username_label = tkinter.Label(
        admin_login, text="ID", bg='#333333', fg="#FFFFFF", font=normal_font)

    def ad_login():
        username = "admin"
        password = "1234"
        if ad_username_entry.get() == username and ad_password_entry.get() == password:
            messagebox.showinfo(title="Login Success",
                                message="You successfully logged in.")
            admin_menu()
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    ad_username_entry = tkinter.Entry(admin_login, font=normal_font)
    ad_password_entry = tkinter.Entry(admin_login, show="*", font=normal_font)

    ad_password_label = tkinter.Label(
        admin_login, text="Password", bg='#333333', fg='#FFFFFF', font=normal_font)
    ad_login_button = tkinter.Button(
        admin_login, text="Login", bg="#FF3399", fg='#FFFFFF', font=normal_font, command=ad_login)

    # Placing widgets on the screen
    ad_login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    ad_username_label.grid(row=1, column=0)
    ad_username_entry.grid(row=1, column=1, pady=20)
    ad_password_label.grid(row=2, column=0)
    ad_password_entry.grid(row=2, column=1, pady=20)
    ad_login_button.grid(row=3, column=0, columnspan=2, pady=30)

    admin_login.place(relx=0.7, rely=0.25, relwidth=0.25, relheight=0.5)

    # --------------Register Button-----------------
    global register_btn
    register_btn = tkinter.Button(
        window, text="Register", bg="#FF3399", fg="#FFFFFF", font=normal_font, command=register_cus)
    register_btn.place(relx=0.45, rely=0.8, relwidth=0.1, relheight=0.1)


def register_cus():
    register_window = tkinter.Toplevel(bg='#333333')
    register_window.geometry('500x500')

    title_label = tkinter.Label(
        register_window, text="Registration", bg='#333333', fg="#FF3399", font=label_font)
    warning_label = tkinter.Label(
        register_window, text="Warning: Please format correctly", bg='#333333', fg="#c40606", font=normal_font)
    name_label = tkinter.Label(
        register_window, text="Enter your Name:", font=normal_font, bg='#333333', fg="#FF3399")
    address_label = tkinter.Label(
        register_window, text="Enter your Address:", font=normal_font, bg='#333333', fg="#FF3399")
    email_label = tkinter.Label(
        register_window, text="Enter your Email:", font=normal_font, bg='#333333', fg="#FF3399")
    gender_label = tkinter.Label(
        register_window, text="Enter your Gender:", font=normal_font, bg='#333333', fg="#FF3399")

    name_entry = tkinter.Entry(register_window)
    address_entry = tkinter.Entry(register_window)
    email_entry = tkinter.Entry(register_window)
    gender_entry = tkinter.Entry(register_window)

    def take_details():
        insert_data = [(name_entry.get(), address_entry.get(),
                        email_entry.get(), gender_entry.get())]
        insert_query = "INSERT INTO customers(customer_name, customer_address, customer_email, customer_gender) VALUES (%s,%s,%s,%s)"
        mycursor.executemany(insert_query, insert_data)
        mydb.commit()

        password_window = tkinter.Toplevel(bg='#333333')
        password_window.geometry('500x250')
        register_window.destroy()
        id_label = tkinter.Label(
            password_window, text="Login ID:", font=normal_font, bg='#333333', fg="#FF3399")
        pass_label = tkinter.Label(
            password_window, text="Enter your Password:", font=normal_font, bg='#333333', fg="#FF3399")

        new_id = tkinter.StringVar()
        id_entry = tkinter.Entry(
            password_window, textvariable=new_id, state=tkinter.DISABLED)
        pass_entry = tkinter.Entry(password_window)

        def back_to_login():
            pass_data = [(id_entry.get(), pass_entry.get())]
            pass_query = "INSERT INTO passwords(customer_id, password) VALUES(%s,%s)"
            mycursor.executemany(pass_query, pass_data)
            mydb.commit()

            messagebox.showinfo(title="Successful",
                                message="Registration was Successful")
            password_window.destroy()

        setpass_btn = tkinter.Button(password_window, text="Register",
                                     bg="#FF3399", fg="#FFFFFF", font=normal_font, command=back_to_login)

        checkid_query = "SELECT MAX(customer_id) FROM customers"
        mycursor.execute(checkid_query)
        rows = mycursor.fetchall()
        for row in rows:
            for col in row:
                converted_col = str(col)
                new_id.set(converted_col)

        id_label.grid(row=0, column=0)
        id_entry.grid(row=0, column=1)
        pass_label.grid(row=1, column=0)
        pass_entry.grid(row=1, column=1)
        setpass_btn.grid(row=2, column=0, columnspan=2)

    complete_btn = tkinter.Button(register_window, text="Register",
                                  bg="#FF3399", fg="#FFFFFF", font=normal_font, command=take_details)

    # --------------Placing Widgets-----------------
    title_label.grid(row=0, column=0, columnspan=2)
    warning_label.grid(row=1, column=0, columnspan=2)

    name_label.grid(row=2, column=0)
    name_entry.grid(row=2, column=1)

    address_label.grid(row=3, column=0)
    address_entry.grid(row=3, column=1)

    email_label.grid(row=4, column=0)
    email_entry.grid(row=4, column=1)

    gender_label.grid(row=5, column=0)
    gender_entry.grid(row=5, column=1)

    complete_btn.grid(row=6, column=0, columnspan=2)


def admin_menu():
    # -------Ambience-------
    welcome_label = tkinter.Label(
        window, text="Welcome to the Library", font=label_font, background='#333333', foreground='#FF3399')
    welcome_label.place(x=0, y=0, relwidth=1, height=40)

    # --------------------Frame Setup----------------
    register_btn.destroy()
    employee_login.destroy()
    customer_login.destroy()
    admin_login.destroy()

    # -------------------Welcome Screen---------------
    welcome_frame = tkinter.Frame(window, background='#333333')
    welcome_frame.place(relx=0.15, rely=0.1, relwidth=0.75, relheight=0.4)

    greeting_label = tkinter.Label(welcome_frame, text="Welcome to the Library Management System!",
                                   font=label_font, background='#333333', foreground='#FF3399')
    name_welcome = tkinter.Label(welcome_frame, text="Hello, Admin",
                                 font=label_font, background='#333333', foreground='#FF3399')

    greeting_label.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.15)
    name_welcome.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.15)

    # ---------------Menu Panel----------------
    menu_panel = tkinter.Frame(window, bd=2, relief='ridge', bg='#333333')
    menu_panel.place(x=0, y=100, width=200, height=300)

    menu_label = tkinter.Label(menu_panel, text="Menu")
    menu_label.pack(side='top', fill='x')

    btn_books = tkinter.Button(menu_panel, text="Books", command=lambda: switch_tables(
        0, 0), compound='left', bg='white', cursor='hand2')
    btn_books.pack(side='top', fill='x')

    btn_staff = tkinter.Button(menu_panel, text="Staff", command=lambda: switch_tables(
        0, 1), compound='left', bg='white', cursor='hand2')
    btn_staff.pack(side='top', fill='x')

    btn_customers = tkinter.Button(menu_panel, text="Customers", command=lambda: switch_tables(
        0, 2), compound='left', bg='white', cursor='hand2')
    btn_customers.pack(side='top', fill='x')

    btn_borrower = tkinter.Button(menu_panel, text="Borrower", command=lambda: switch_tables(
        0, 3), compound='left', bg='white', cursor='hand2')
    btn_borrower.pack(side='top', fill='x')

    btn_branch = tkinter.Button(menu_panel, text="Branch", command=lambda: switch_tables(
        0, 4), compound='left', bg='white', cursor='hand2')
    btn_branch.pack(side='top', fill='x')

    btn_cuspasw = tkinter.Button(menu_panel, text="Customer Password", command=lambda: switch_tables(
        0, 5), compound='left', bg='white', cursor='hand2')
    btn_cuspasw.pack(side='top', fill='x')

    btn_empasw = tkinter.Button(menu_panel, text="Staff Password", command=lambda: switch_tables(
        0, 6), compound='left', bg='white', cursor='hand2')
    btn_empasw.pack(side='top', fill='x')


def em_menu():
    # -------Ambience-------
    welcome_label = tkinter.Label(
        window, text="Welcome to the Library", font=label_font, background='#333333', foreground='#FF3399')
    welcome_label.place(x=0, y=0, relwidth=1, height=40)

    # ------------User Button----------------
    def user_menu():
        user_window = tkinter.Toplevel(bg='#333333')
        user_window.geometry('500x500')

        id_field = tkinter.Label(
            user_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
        name_field = tkinter.Label(
            user_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
        position_field = tkinter.Label(
            user_window, text='Position', font=normal_font, bg='#333333', fg='cyan')
        branch_field = tkinter.Label(
            user_window, text='Branch ID', font=normal_font, bg='#333333', fg='cyan')
        gender_field = tkinter.Label(
            user_window, text='Gender', font=normal_font, bg='#333333', fg='cyan')

        idstr = tkinter.StringVar()
        namestr = tkinter.StringVar()
        posstr = tkinter.StringVar()
        brstr = tkinter.StringVar()
        genstr = tkinter.StringVar()
        paswstr = tkinter.StringVar()

        id_entry = tkinter.Entry(user_window, textvariable=idstr,
                                 font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        name_entry = tkinter.Entry(
            user_window, textvariable=namestr, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        position_entry = tkinter.Entry(
            user_window, textvariable=posstr, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        branch_entry = tkinter.Entry(
            user_window, textvariable=brstr, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        gender_entry = tkinter.Entry(
            user_window, textvariable=genstr, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        gender_entry = tkinter.Entry(
            user_window, textvariable=paswstr, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

        idstr.set(em_username_login)

        mycursor.execute(
            "SELECT staff_name FROM staff WHERE staff_id = %s", (em_username_login,))
        name_result = mycursor.fetchall()
        for row in name_result:
            for col in row:
                namestr.set(col)

        mycursor.execute(
            "SELECT staff_position FROM staff WHERE staff_id = %s", (em_username_login,))
        position_result = mycursor.fetchall()
        for row in position_result:
            for col in row:
                posstr.set(col)

        mycursor.execute(
            "SELECT branch_id FROM staff WHERE staff_id = %s", (em_username_login,))
        branch_result = mycursor.fetchall()
        for row in branch_result:
            for col in row:
                brstr.set(col)

        mycursor.execute(
            "SELECT staff_gender FROM staff WHERE staff_id = %s", (em_username_login,))
        gender_result = mycursor.fetchall()
        for row in gender_result:
            for col in row:
                genstr.set(col)

        mycursor.execute(
            "SELECT password FROM em_password WHERE staff_id = %s", (em_username_login,))
        pasw_result = mycursor.fetchall()
        for row in pasw_result:
            for col in row:
                paswstr.set(col)

        id_field.grid(row=0, column=0)
        name_field.grid(row=1, column=0)
        position_field.grid(row=2, column=0)
        branch_field.grid(row=3, column=0)
        gender_field.grid(row=4, column=0)

        id_entry.grid(row=0, column=1)
        name_entry.grid(row=1, column=1)
        position_entry.grid(row=2, column=1)
        branch_entry.grid(row=3, column=1)
        gender_entry.grid(row=4, column=1)

    user_button = tkinter.Button(
        window, image=user_image, borderwidth=0, command=user_menu)
    user_button.place(relx=1, rely=0, x=0, y=0,
                      width=75, height=75, anchor='ne')

    # --------------------Frame Setup----------------
    register_btn.destroy()
    employee_login.destroy()
    customer_login.destroy()
    admin_login.destroy()

    # -------------------Welcome Screen---------------
    welcome_frame = tkinter.Frame(window, background='#333333')
    welcome_frame.place(relx=0.15, rely=0.1, relwidth=0.75, relheight=0.4)

    greeting_label = tkinter.Label(welcome_frame, text="Welcome to the Library Management System!",
                                   font=label_font, background='#333333', foreground='#FF3399')

    mycursor.execute(
        "SELECT staff_name FROM staff WHERE staff_id = %s", (em_username_login,))
    result = mycursor.fetchall()
    for row in result:
        for col in row:
            greeting_name = "Hello, " + col

    name_welcome = tkinter.Label(welcome_frame, text=greeting_name,
                                 font=label_font, background='#333333', foreground='#FF3399')

    greeting_label.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.15)
    name_welcome.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.15)

    # ---------------Menu Panel----------------
    menu_panel = tkinter.Frame(window, bd=2, relief='ridge', bg='#333333')
    menu_panel.place(x=0, y=100, width=200, height=300)

    menu_label = tkinter.Label(menu_panel, text="Menu")
    menu_label.pack(side='top', fill='x')

    btn_books = tkinter.Button(menu_panel, text="Books", command=lambda: switch_tables(
        1, 0), compound='left', bg='white', cursor='hand2')
    btn_books.pack(side='top', fill='x')

    btn_staff = tkinter.Button(menu_panel, text="Staff", command=lambda: switch_tables(
        1, 1), compound='left', bg='white', cursor='hand2')
    btn_staff.pack(side='top', fill='x')

    btn_customers = tkinter.Button(menu_panel, text="Customers", command=lambda: switch_tables(
        1, 2), compound='left', bg='white', cursor='hand2')
    btn_customers.pack(side='top', fill='x')

    btn_borrower = tkinter.Button(menu_panel, text="Borrower", command=lambda: switch_tables(
        1, 3), compound='left', bg='white', cursor='hand2')
    btn_borrower.pack(side='top', fill='x')

    btn_branch = tkinter.Button(menu_panel, text="Branch", command=lambda: switch_tables(
        1, 4), compound='left', bg='white', cursor='hand2')
    btn_branch.pack(side='top', fill='x')


def cus_menu():
    # -------Ambience-------
    welcome_label = tkinter.Label(
        window, text="Welcome to the Library", font=label_font, background='#333333', foreground='#FF3399')
    welcome_label.place(x=0, y=0, relwidth=1, height=40)

    # ------------User Button----------------
    def user_menu():
        user_window = tkinter.Toplevel(bg='#333333')
        user_window.geometry('500x500')

        id_field = tkinter.Label(
            user_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
        name_field = tkinter.Label(
            user_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
        address_field = tkinter.Label(
            user_window, text='Address', font=normal_font, bg='#333333', fg='cyan')
        email_field = tkinter.Label(
            user_window, text='Email', font=normal_font, bg='#333333', fg='cyan')
        gender_field = tkinter.Label(
            user_window, text='Gender', font=normal_font, bg='#333333', fg='cyan')
        pass_field = tkinter.Label(
            user_window, text='Password', font=normal_font, bg='#333333', fg='cyan')

        idstr = tkinter.StringVar()
        namestr = tkinter.StringVar()
        addstr = tkinter.StringVar()
        malstr = tkinter.StringVar()
        genstr = tkinter.StringVar()
        paswstr = tkinter.StringVar()

        id_entry = tkinter.Entry(user_window, textvariable=idstr,
                                 font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        name_entry = tkinter.Entry(
            user_window, textvariable=namestr, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        address_entry = tkinter.Entry(
            user_window, textvariable=addstr, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        email_entry = tkinter.Entry(
            user_window, textvariable=malstr, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        gender_entry = tkinter.Entry(
            user_window, textvariable=genstr, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        pass_entry = tkinter.Entry(
            user_window, textvariable=paswstr, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

        idstr.set(cus_username_login)

        mycursor.reset()

        mycursor.execute(
            "SELECT customer_name FROM customers WHERE customer_id = %s", (cus_username_login,))
        name_result = mycursor.fetchall()
        for row in name_result:
            for col in row:
                namestr.set(col)

        mycursor.execute(
            "SELECT customer_address FROM customers WHERE customer_id = %s", (cus_username_login,))
        address_result = mycursor.fetchall()
        for row in address_result:
            for col in row:
                addstr.set(col)

        mycursor.execute(
            "SELECT customer_email FROM customers WHERE customer_id = %s", (cus_username_login,))
        email_result = mycursor.fetchall()
        for row in email_result:
            for col in row:
                malstr.set(col)

        mycursor.execute(
            "SELECT customer_gender FROM customers WHERE customer_id = %s", (cus_username_login,))
        gender_result = mycursor.fetchall()
        for row in gender_result:
            for col in row:
                genstr.set(col)

        mycursor.execute(
            "SELECT password FROM passwords WHERE customer_id = %s", (cus_username_login,))
        pasw_result = mycursor.fetchall()
        for row in pasw_result:
            for col in row:
                paswstr.set(col)

        id_field.grid(row=0, column=0)
        name_field.grid(row=1, column=0)
        address_field.grid(row=2, column=0)
        email_field.grid(row=3, column=0)
        gender_field.grid(row=4, column=0)
        pass_field.grid(row=5, column=0)

        id_entry.grid(row=0, column=1)
        name_entry.grid(row=1, column=1)
        address_entry.grid(row=2, column=1)
        email_entry.grid(row=3, column=1)
        gender_entry.grid(row=4, column=1)
        pass_entry.grid(row=5, column=1)

        mycursor.execute(
            "SELECT * FROM borrower WHERE customer_id = (%s)", (cus_username_login,))
        if mycursor.fetchone():
            mycursor.execute(
                "SELECT expiry_date FROM borrower WHERE customer_id = (%s)", (cus_username_login,))
            expiry_date = mycursor.fetchall()
            for row in expiry_date:
                for col in row:
                    if col < date.today():
                        borrow_text = 'You have a overdue book. Ask an employee for assistance'
                        text_color = '#a60202'
                    elif col == date.today():
                        borrow_text = 'You have a book due today. Ask an employee for assistance'
                        text_color = '#a60202'
                    else:
                        borrow_text = 'You have borrowed book to return by: ' + \
                            col.strftime("%Y/%m/%d")
                        text_color = '#029c09'
            borrow_field = tkinter.Label(
                user_window, text=borrow_text, font=normal_font, bg=text_color, fg='#FFFFFF')
            borrow_field.grid(row=6, column=0, columnspan=2)

    user_button = tkinter.Button(
        window, image=user_image, borderwidth=0, command=user_menu)
    user_button.place(relx=1, rely=0, x=0, y=0,
                      width=75, height=75, anchor='ne')

    # --------------------Frame Setup----------------
    register_btn.destroy()
    employee_login.destroy()
    customer_login.destroy()
    admin_login.destroy()

    # -------------------Welcome Screen--------------------
    welcome_frame = tkinter.Frame(window, background='#333333')
    welcome_frame.place(relx=0.15, rely=0.1, relwidth=0.75, relheight=0.4)

    greeting_label = tkinter.Label(welcome_frame, text="Welcome to the Library Management System!",
                                   font=label_font, background='#333333', foreground='#FF3399')

    mycursor.execute(
        "SELECT customer_name FROM customers WHERE customer_id = %s", (cus_username_login,))
    result = mycursor.fetchall()
    for row in result:
        for col in row:
            greeting_name = "Hello, " + col

    name_welcome = tkinter.Label(welcome_frame, text=greeting_name,
                                 font=label_font, background='#333333', foreground='#FF3399')

    greeting_label.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.15)
    name_welcome.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.15)

    # -------------Button for books table-------------
    continue_to_books = tkinter.Button(welcome_frame, text="Continue to Books Table",
                                       bg="#FF3399", fg="#FFFFFF", font=normal_font, command=lambda: switch_tables(2, 0))
    continue_to_books.place(
        relx=0, rely=1, relheight=0.15, relwidth=1, anchor='sw')


def switch_tables(utype, table_choice):
    print('Switching...')

    if table_choice == 0:
        books_table(utype)
    elif table_choice == 1:
        employees_table(utype)
    elif table_choice == 2:
        customers_table(utype)
    elif table_choice == 3:
        borrower_table(utype)
    elif table_choice == 4:
        branch_table(utype)
    elif table_choice == 5:
        cuspasw_table(utype)
    elif table_choice == 6:
        empasw_table(utype)


def books_table(user_type):
    print('Books Table')
    # --------------Frame Setup------------
    book_frame = tkinter.Frame(window)
    bk_table_frame = tkinter.Frame(book_frame, bg='#333333')
    bk_display_frame = tkinter.Frame(book_frame, bg='#333333')

    # -----------Label Setup-------------
    label1 = tkinter.Label(
        bk_table_frame, text='Search Library Books', font=label_font, bg='#333333', fg='#FF3399')
    field_select = tkinter.Label(
        bk_table_frame, text='Select a Field', font=normal_font, bg='#333333', fg='#FF3399')
    keyword_enter = tkinter.Label(
        bk_table_frame, text='Enter your Keyword', font=normal_font, bg='#333333', fg='#FF3399')

    # ------------Search Button-----------------
    def search_from_table():
        current_choice = query_choice.get()

        for i in tree.get_children():
            tree.delete(i)

        if current_choice == "ID":
            search_query = "SELECT * FROM books WHERE book_id LIKE %s"
        elif current_choice == "Name":
            search_query = "SELECT * FROM books WHERE book_name LIKE %s"
        elif current_choice == "Author":
            search_query = "SELECT * FROM books WHERE book_author LIKE %s"
        elif current_choice == "Genre":
            search_query = "SELECT * FROM books WHERE book_genre LIKE %s"
        elif current_choice == "ISBN":
            search_query = "SELECT * FROM books WHERE book_ISBN LIKE %s"
        else:
            search_query = "SELECT * FROM books"

        data = (keyword.get(),)
        mycursor.execute(search_query, data)
        search_lst = mycursor.fetchall()
        for contact in search_lst:
            tree.insert('', tkinter.END, values=contact)

    search_btn = tkinter.Button(
        bk_table_frame, text='Search', command=search_from_table)

    keyword = tkinter.Entry(bk_table_frame)

    # ------Setting Up the Table------
    book_display_query = "SELECT * FROM books"
    mycursor.execute(book_display_query)
    bk_lst = mycursor.fetchall()
    mycursor.reset()

    headers = ('id', 'name', 'author', 'genre', 'ISBN', 'copies')

    tree = ttk.Treeview(bk_display_frame, columns=headers,
                        show='headings', selectmode='browse', style='Zain.Treeview')

    tree.column('id', anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
    tree.heading('id', text='ID')

    tree.column('name', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('name', text='Name')

    tree.column('author', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('author', text='Author')

    tree.column('genre', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('genre', text='Genre')

    tree.column('ISBN', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('ISBN', text='ISBN')

    tree.column('copies', anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
    tree.heading('copies', text='Copies')

    for contact in bk_lst:
        tree.insert('', tkinter.END, values=contact)

    # ------Scrollbar for the Table-----------
    scrollbar = ttk.Scrollbar(
        bk_display_frame, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    # ------Querying-----
    choice = tkinter.StringVar()
    query_choice = ttk.Combobox(bk_table_frame, textvariable=choice)

    query_choice['values'] = ("ID", "Name", "Author", "Genre", "ISBN")
    query_choice['state'] = 'readonly'

    # -------------Only for Admin and Employee---------------
    if user_type == 0 or user_type == 1:
        select_frame = tkinter.Frame(
            bk_table_frame, bg='#333333', highlightbackground='cyan', highlightthickness=1)

        id_var = tkinter.StringVar()
        name_var = tkinter.StringVar()
        author_var = tkinter.StringVar()
        genre_var = tkinter.StringVar()
        isbn_var = tkinter.StringVar()
        copies_var = tkinter.StringVar()

        first_label = tkinter.Entry(
            select_frame, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        second_label = tkinter.Entry(
            select_frame, text=name_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        third_label = tkinter.Entry(
            select_frame, text=author_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        fourth_label = tkinter.Entry(
            select_frame, text=genre_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        fifth_label = tkinter.Entry(
            select_frame, text=isbn_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        sixth_label = tkinter.Entry(
            select_frame, text=copies_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

        # ------Printing the Selected Item-----
        def displaySelectedItem(a):
            selectedItem = tree.selection()[0]

            id_var.set(tree.item(selectedItem)['values'][0])
            name_var.set(tree.item(selectedItem)['values'][1])
            author_var.set(tree.item(selectedItem)['values'][2])
            genre_var.set(tree.item(selectedItem)['values'][3])
            isbn_var.set(tree.item(selectedItem)['values'][4])
            copies_var.set(tree.item(selectedItem)['values'][5])

        tree.bind("<<TreeviewSelect>>", displaySelectedItem)

        def update_entry():
            bk_update_window = tkinter.Toplevel(bg='#333333')
            bk_update_window.geometry('500x500')
            bk_update_window.title("Update Book")

            first_entry = tkinter.Entry(
                bk_update_window, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            second_entry = tkinter.Entry(
                bk_update_window, font=normal_font, bg='#333333', fg='cyan')
            third_entry = tkinter.Entry(
                bk_update_window, font=normal_font, bg='#333333', fg='cyan')
            fourth_entry = tkinter.Entry(
                bk_update_window, font=normal_font, bg='#333333', fg='cyan')
            fifth_entry = tkinter.Entry(
                bk_update_window, font=normal_font, bg='#333333', fg='cyan')
            sixth_entry = tkinter.Entry(
                bk_update_window, font=normal_font, bg='#333333', fg='cyan')

            second_entry.insert(0, second_label.get())
            third_entry.insert(0, third_label.get())
            fourth_entry.insert(0, fourth_label.get())
            fifth_entry.insert(0, fifth_label.get())
            sixth_entry.insert(0, sixth_label.get())

            id_field = tkinter.Label(
                bk_update_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
            name_field = tkinter.Label(
                bk_update_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
            author_field = tkinter.Label(
                bk_update_window, text='Author', font=normal_font, bg='#333333', fg='cyan')
            genre_field = tkinter.Label(
                bk_update_window, text='Genre', font=normal_font, bg='#333333', fg='cyan')
            isbn_field = tkinter.Label(
                bk_update_window, text='ISBN', font=normal_font, bg='#333333', fg='cyan')
            copies_field = tkinter.Label(
                bk_update_window, text='Copies', font=normal_font, bg='#333333', fg='cyan')

            def execute_update():
                update_id = first_entry.get()
                new_name = second_entry.get()
                new_author = third_entry.get()
                new_genre = fourth_entry.get()
                new_isbn = fifth_entry.get()
                new_copies = sixth_entry.get()

                update_values = [
                    (new_name, new_author, new_genre, new_isbn, new_copies, update_id)]
                update_query = "UPDATE books SET book_name = (%s), book_author = (%s), book_genre = (%s), book_ISBN = (%s), book_copies = (%s) WHERE book_id = (%s)"
                mycursor.executemany(update_query, update_values)
                mydb.commit()

                bk_table_frame.destroy()
                bk_display_frame.destroy()
                bk_update_window.destroy()
                books_table(user_type)

            confirm_update_btn = tkinter.Button(
                bk_update_window, text="Confirm", font=normal_font, bg='#FFF700', fg='black', command=execute_update)

            id_field.grid(row=0, column=0)
            name_field.grid(row=1, column=0)
            author_field.grid(row=2, column=0)
            genre_field.grid(row=3, column=0)
            isbn_field.grid(row=4, column=0)
            copies_field.grid(row=5, column=0)
            confirm_update_btn.grid(row=6, column=0)

            first_entry.grid(row=0, column=1)
            second_entry.grid(row=1, column=1)
            third_entry.grid(row=2, column=1)
            fourth_entry.grid(row=3, column=1)
            fifth_entry.grid(row=4, column=1)
            sixth_entry.grid(row=5, column=1)

        def delete_entry():
            bk_delete_window = tkinter.Toplevel(bg='#333333')
            bk_delete_window.geometry('500x500')
            bk_delete_window.title("Delete Book")

            first_entry = tkinter.Entry(
                bk_delete_window, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            second_entry = tkinter.Entry(
                bk_delete_window, text=name_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            third_entry = tkinter.Entry(bk_delete_window, text=author_var,
                                        font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            fourth_entry = tkinter.Entry(
                bk_delete_window, text=genre_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            fifth_entry = tkinter.Entry(
                bk_delete_window, text=isbn_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            sixth_entry = tkinter.Entry(bk_delete_window, text=copies_var,
                                        font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

            id_field = tkinter.Label(
                bk_delete_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
            name_field = tkinter.Label(
                bk_delete_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
            author_field = tkinter.Label(
                bk_delete_window, text='Author', font=normal_font, bg='#333333', fg='cyan')
            genre_field = tkinter.Label(
                bk_delete_window, text='Genre', font=normal_font, bg='#333333', fg='cyan')
            isbn_field = tkinter.Label(
                bk_delete_window, text='ISBN', font=normal_font, bg='#333333', fg='cyan')
            copies_field = tkinter.Label(
                bk_delete_window, text='Copies', font=normal_font, bg='#333333', fg='cyan')

            def execute_delete():
                delete_id = [(first_entry.get(),)]
                update_query = "DELETE FROM books WHERE book_id = (%s)"
                mycursor.executemany(update_query, delete_id)
                mydb.commit()

                bk_table_frame.destroy()
                bk_display_frame.destroy()
                bk_delete_window.destroy()
                books_table(user_type)

            confirm_delete_btn = tkinter.Button(
                bk_delete_window, text="Confirm Delete", font=normal_font, bg='#730105', fg='#FFFFFF', command=execute_delete)

            id_field.grid(row=0, column=0)
            name_field.grid(row=1, column=0)
            author_field.grid(row=2, column=0)
            genre_field.grid(row=3, column=0)
            isbn_field.grid(row=4, column=0)
            copies_field.grid(row=5, column=0)
            confirm_delete_btn.grid(row=6, column=0)

            first_entry.grid(row=0, column=1)
            second_entry.grid(row=1, column=1)
            third_entry.grid(row=2, column=1)
            fourth_entry.grid(row=3, column=1)
            fifth_entry.grid(row=4, column=1)
            sixth_entry.grid(row=5, column=1)

        def insert_entry():
            bk_insert_window = tkinter.Toplevel(bg='#333333')
            bk_insert_window.geometry('500x500')
            bk_insert_window.title("Insert Book")

            second_entry = tkinter.Entry(
                bk_insert_window, font=normal_font, bg='#333333', fg='cyan')
            third_entry = tkinter.Entry(
                bk_insert_window, font=normal_font, bg='#333333', fg='cyan')
            fourth_entry = tkinter.Entry(
                bk_insert_window, font=normal_font, bg='#333333', fg='cyan')
            fifth_entry = tkinter.Entry(
                bk_insert_window, font=normal_font, bg='#333333', fg='cyan')
            sixth_entry = tkinter.Entry(
                bk_insert_window, font=normal_font, bg='#333333', fg='cyan')

            name_field = tkinter.Label(
                bk_insert_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
            author_field = tkinter.Label(
                bk_insert_window, text='Author', font=normal_font, bg='#333333', fg='cyan')
            genre_field = tkinter.Label(
                bk_insert_window, text='Genre', font=normal_font, bg='#333333', fg='cyan')
            isbn_field = tkinter.Label(
                bk_insert_window, text='ISBN', font=normal_font, bg='#333333', fg='cyan')
            copies_field = tkinter.Label(
                bk_insert_window, text='Copies', font=normal_font, bg='#333333', fg='cyan')

            def execute_insert():
                new_name = second_entry.get()
                new_author = third_entry.get()
                new_genre = fourth_entry.get()
                new_isbn = fifth_entry.get()
                new_copies = sixth_entry.get()

                insert_values = [
                    (new_name, new_author, new_genre, new_isbn, new_copies), ]
                insert_query = "INSERT INTO books(book_name, book_author, book_genre, book_ISBN, book_copies) VALUES (%s,%s,%s,%s,%s)"
                mycursor.executemany(insert_query, insert_values)
                mydb.commit()

                bk_table_frame.destroy()
                bk_display_frame.destroy()
                bk_insert_window.destroy()
                books_table(user_type)

            confirm_update_btn = tkinter.Button(
                bk_insert_window, text="Confirm", font=normal_font, bg='#03FF0F', fg='black', command=execute_insert)

            name_field.grid(row=0, column=0)
            author_field.grid(row=1, column=0)
            genre_field.grid(row=2, column=0)
            isbn_field.grid(row=3, column=0)
            copies_field.grid(row=4, column=0)
            confirm_update_btn.grid(row=5, column=0)

            second_entry.grid(row=0, column=1)
            third_entry.grid(row=1, column=1)
            fourth_entry.grid(row=2, column=1)
            fifth_entry.grid(row=3, column=1)
            sixth_entry.grid(row=4, column=1)

        update_btn = tkinter.Button(
            select_frame, text='Edit', bg='#FFF700', fg='#000300', command=update_entry)
        delete_btn = tkinter.Button(
            select_frame, text='Delete', bg='#730105', fg='#FFFFFF', command=delete_entry)
        insert_btn = tkinter.Button(
            select_frame, text='Insert', bg='#03FF0F', fg='#000300', command=insert_entry)

        # ------------------Grid------------------------------------
        first_label.grid(row=0, column=0)
        second_label.grid(row=1, column=0)
        third_label.grid(row=2, column=0)
        fourth_label.grid(row=3, column=0)
        fifth_label.grid(row=4, column=0)
        sixth_label.grid(row=5, column=0)
        update_btn.grid(row=6, column=0, columnspan=2)
        delete_btn.grid(row=7, column=0, columnspan=2)
        insert_btn.grid(row=8, column=0, columnspan=2)

        select_frame.place(relx=1, rely=0, x=0, y=0, anchor='ne')

    borrow_query = 'SELECT book_name FROM books WHERE book_id = (SELECT * FROM most_borrowed)'
    mycursor.execute(borrow_query)
    rows = mycursor.fetchall()
    for row in rows:
        for col in row:
            stats_text = "The most borrowed book right now is " + col

    borrowed_stats = tkinter.Label(
        bk_table_frame, text=stats_text, font=normal_font, bg='#333333', fg='#FF3399')

    # ----------------Grid----------------------

    label1.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)

    field_select.grid(row=1, column=0)
    query_choice.grid(row=1, column=1, pady=20)

    keyword_enter.grid(row=1, column=2)
    keyword.grid(row=1, column=3, pady=20, padx=10)

    search_btn.grid(row=1, column=4, columnspan=2, pady=20)

    borrowed_stats.grid(row=2, column=0, columnspan=2, sticky='news', pady=40)

    bk_table_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    # -----------------------------------------------------------

    tree.grid(row=3, column=0, columnspan=4)
    scrollbar.grid(row=3, column=4, sticky='ns')

    bk_display_frame.place(relx=0, rely=1, anchor='sw')

    book_frame.place(relx=0.15, rely=0.1, relwidth=0.75, relheight=0.75)


def employees_table(user_type):
    print('Employees Table')
    # --------------Frame Setup------------
    employee_frame = tkinter.Frame(window)
    em_table_frame = tkinter.Frame(employee_frame, bg='#333333')
    em_display_frame = tkinter.Frame(employee_frame, bg='#333333')

    # -----------Label Setup-------------
    label1 = tkinter.Label(
        em_table_frame, text='Search Employees', font=label_font, bg='#333333', fg='#FF3399')
    field_select = tkinter.Label(
        em_table_frame, text='Select a Field', font=normal_font, bg='#333333', fg='#FF3399')
    keyword_enter = tkinter.Label(
        em_table_frame, text='Enter your Keyword', font=normal_font, bg='#333333', fg='#FF3399')

    # ------------Search Button-----------------
    def search_from_table():
        current_choice = query_choice.get()

        for i in tree.get_children():
            tree.delete(i)

        if current_choice == "ID":
            search_query = "SELECT * FROM staff WHERE staff_id LIKE (%s)"
        elif current_choice == "Name":
            search_query = "SELECT * FROM staff WHERE staff_name LIKE (%s)"
        elif current_choice == "Position":
            search_query = "SELECT * FROM staff WHERE staff_position LIKE (%s)"
        elif current_choice == "Branch ID":
            search_query = "SELECT * FROM staff WHERE branch_id LIKE (%s)"
        elif current_choice == "Gender":
            search_query = "SELECT * FROM staff WHERE staff_gender LIKE (%s)"
        else:
            search_query = "SELECT * FROM staff"

        data = (keyword.get(),)
        mycursor.execute(search_query, data)
        search_lst = mycursor.fetchall()
        for contact in search_lst:
            tree.insert('', tkinter.END, values=contact)

    search_btn = tkinter.Button(
        em_table_frame, text='Search', command=search_from_table)
    keyword = tkinter.Entry(em_table_frame)

    # ------Setting Up the Table------
    em_display_query = "SELECT * FROM staff"
    mycursor.execute(em_display_query)
    em_lst = mycursor.fetchall()

    headers = ('id', 'name', 'gender', 'branch_id')

    tree = ttk.Treeview(em_display_frame, columns=headers,
                        show='headings', selectmode='browse', style='Zain.Treeview')

    tree.column('id', anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
    tree.heading('id', text='ID')

    tree.column('name', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('name', text='Name')

    tree.column('gender', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('gender', text='Gender')

    tree.column('branch_id', anchor=tkinter.CENTER,
                stretch=tkinter.NO, width=100)
    tree.heading('branch_id', text='Branch ID')

    for contact in em_lst:
        tree.insert('', tkinter.END, values=contact)

    # ------Scrollbar for the Table-----------
    scrollbar = ttk.Scrollbar(
        em_display_frame, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    # ------Querying-----
    choice = tkinter.StringVar()
    query_choice = ttk.Combobox(em_table_frame, textvariable=choice)

    query_choice['values'] = ("ID", "Name", "Position", "Branch ID", "Gender")
    query_choice['state'] = 'readonly'

    # -------------Only for Admin---------------
    if user_type == 0:
        select_frame = tkinter.Frame(
            em_table_frame, bg='#333333', highlightbackground='cyan', highlightthickness=1)

        id_var = tkinter.StringVar()
        name_var = tkinter.StringVar()
        position_var = tkinter.StringVar()
        branchid_var = tkinter.StringVar()
        gender_var = tkinter.StringVar()

        first_label = tkinter.Entry(
            select_frame, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        second_label = tkinter.Entry(
            select_frame, text=name_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        third_label = tkinter.Entry(select_frame, text=position_var,
                                    font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        fourth_label = tkinter.Entry(select_frame, text=branchid_var,
                                     font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        fifth_label = tkinter.Entry(
            select_frame, text=gender_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

        # ------Printing the Selected Item-----
        def printSelectedItem(a):
            selectedItem = tree.selection()[0]

            id_var.set(tree.item(selectedItem)['values'][0])
            name_var.set(tree.item(selectedItem)['values'][1])
            position_var.set(tree.item(selectedItem)['values'][2])
            branchid_var.set(tree.item(selectedItem)['values'][3])
            gender_var.set(tree.item(selectedItem)['values'][4])

        tree.bind("<<TreeviewSelect>>", printSelectedItem)

        def update_entry():
            em_update_window = tkinter.Toplevel(bg='#333333')
            em_update_window.geometry('500x500')
            em_update_window.title("Update Employee")

            first_entry = tkinter.Entry(
                em_update_window, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            second_entry = tkinter.Entry(
                em_update_window, font=normal_font, bg='#333333', fg='cyan')
            third_entry = tkinter.Entry(
                em_update_window, font=normal_font, bg='#333333', fg='cyan')
            fourth_entry = tkinter.Entry(
                em_update_window, font=normal_font, bg='#333333', fg='cyan')
            fifth_entry = tkinter.Entry(
                em_update_window, font=normal_font, bg='#333333', fg='cyan')

            second_entry.insert(0, second_label.get())
            third_entry.insert(0, third_label.get())
            fourth_entry.insert(0, fourth_label.get())
            fifth_entry.insert(0, fifth_label.get())

            id_field = tkinter.Label(
                em_update_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
            name_field = tkinter.Label(
                em_update_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
            position_field = tkinter.Label(
                em_update_window, text='Position', font=normal_font, bg='#333333', fg='cyan')
            branchid_field = tkinter.Label(
                em_update_window, text='Branch ID', font=normal_font, bg='#333333', fg='cyan')
            gender_field = tkinter.Label(
                em_update_window, text='Gender', font=normal_font, bg='#333333', fg='cyan')

            def execute_update():
                update_id = first_entry.get()
                new_name = second_entry.get()
                new_position = third_entry.get()
                new_branchid = fourth_entry.get()
                new_gender = fifth_entry.get()

                update_values = [
                    (new_name, new_position, new_branchid, new_gender, update_id)]
                update_query = "UPDATE staff SET staff_name = (%s), staff_position = (%s), branch_id = (%s), staff_gender = (%s) WHERE staff_id = (%s)"
                mycursor.executemany(update_query, update_values)
                mydb.commit()

                em_table_frame.destroy()
                em_display_frame.destroy()
                em_update_window.destroy()
                employees_table(user_type)

            confirm_update_btn = tkinter.Button(
                em_update_window, text="Confirm", font=normal_font, bg='#FFF700', fg='black', command=execute_update)

            id_field.grid(row=0, column=0)
            name_field.grid(row=1, column=0)
            position_field.grid(row=2, column=0)
            branchid_field.grid(row=3, column=0)
            gender_field.grid(row=4, column=0)
            confirm_update_btn.grid(row=5, column=0)

            first_entry.grid(row=0, column=1)
            second_entry.grid(row=1, column=1)
            third_entry.grid(row=2, column=1)
            fourth_entry.grid(row=3, column=1)
            fifth_entry.grid(row=4, column=1)

        def check_delete():
            if id_var == '1':
                messagebox.showerror(
                    title="Error", message="Cannot delete Admin")
            else:
                delete_entry()

        def delete_entry():
            em_delete_window = tkinter.Toplevel(bg='#333333')
            em_delete_window.geometry('500x500')
            em_delete_window.title("Delete Employee")

            first_entry = tkinter.Entry(
                em_delete_window, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            second_entry = tkinter.Entry(
                em_delete_window, text=name_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            third_entry = tkinter.Entry(em_delete_window, text=position_var,
                                        font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            fourth_entry = tkinter.Entry(em_delete_window, text=branchid_var,
                                         font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            fifth_entry = tkinter.Entry(em_delete_window, text=gender_var,
                                        font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

            id_field = tkinter.Label(
                em_delete_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
            name_field = tkinter.Label(
                em_delete_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
            position_field = tkinter.Label(
                em_delete_window, text='Position', font=normal_font, bg='#333333', fg='cyan')
            branchid_field = tkinter.Label(
                em_delete_window, text='Branch ID', font=normal_font, bg='#333333', fg='cyan')
            gender_field = tkinter.Label(
                em_delete_window, text='Gender', font=normal_font, bg='#333333', fg='cyan')

            def execute_delete():
                delete_id = [(first_entry.get(),)]
                update_query = "DELETE FROM staff WHERE staff_id = (%s)"
                mycursor.executemany(update_query, delete_id)
                mydb.commit()

                em_table_frame.destroy()
                em_display_frame.destroy()
                em_delete_window.destroy()
                employees_table(user_type)

            confirm_delete_btn = tkinter.Button(
                em_delete_window, text="Confirm Delete", font=normal_font, bg='#730105', fg='#FFFFFF', command=execute_delete)

            id_field.grid(row=0, column=0)
            name_field.grid(row=1, column=0)
            position_field.grid(row=2, column=0)
            branchid_field.grid(row=3, column=0)
            gender_field.grid(row=4, column=0)
            confirm_delete_btn.grid(row=6, column=0)

            first_entry.grid(row=0, column=1)
            second_entry.grid(row=1, column=1)
            third_entry.grid(row=2, column=1)
            fourth_entry.grid(row=3, column=1)
            fifth_entry.grid(row=4, column=1)

        def insert_entry():
            em_insert_window = tkinter.Toplevel(bg='#333333')
            em_insert_window.geometry('500x500')
            em_insert_window.title("Insert Employee")

            first_entry = tkinter.Entry(
                em_insert_window, font=normal_font, bg='#333333', fg='cyan')
            second_entry = tkinter.Entry(
                em_insert_window, font=normal_font, bg='#333333', fg='cyan')
            third_entry = tkinter.Entry(
                em_insert_window, font=normal_font, bg='#333333', fg='cyan')
            fourth_entry = tkinter.Entry(
                em_insert_window, font=normal_font, bg='#333333', fg='cyan')
            fifth_entry = tkinter.Entry(
                em_insert_window, font=normal_font, bg='#333333', fg='cyan')

            id_field = tkinter.Label(
                em_insert_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
            name_field = tkinter.Label(
                em_insert_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
            position_field = tkinter.Label(
                em_insert_window, text='Position', font=normal_font, bg='#333333', fg='cyan')
            branchid_field = tkinter.Label(
                em_insert_window, text='Branch ID', font=normal_font, bg='#333333', fg='cyan')
            gender_field = tkinter.Label(
                em_insert_window, text='Gender', font=normal_font, bg='#333333', fg='cyan')

            def execute_insert():
                new_id = first_entry.get()
                new_name = second_entry.get()
                new_author = third_entry.get()
                new_genre = fourth_entry.get()
                new_isbn = fifth_entry.get()

                insert_values = [
                    (new_id, new_name, new_author, new_genre, new_isbn), ]
                insert_query = "INSERT INTO staff(staff_id, staff_name, staff_position, branch_id, staff_gender) VALUES (%s,%s,%s,%s,%s)"
                mycursor.executemany(insert_query, insert_values)
                mydb.commit()

                em_table_frame.destroy()
                em_display_frame.destroy()
                em_insert_window.destroy()
                employees_table(user_type)

            confirm_update_btn = tkinter.Button(
                em_insert_window, text="Confirm", font=normal_font, bg='#03FF0F', fg='cyan', command=execute_insert)

            id_field.grid(row=0, column=0)
            name_field.grid(row=1, column=0)
            position_field.grid(row=2, column=0)
            branchid_field.grid(row=3, column=0)
            gender_field.grid(row=4, column=0)
            confirm_update_btn.grid(row=5, column=0)

            first_entry.grid(row=0, column=1)
            second_entry.grid(row=1, column=1)
            third_entry.grid(row=2, column=1)
            fourth_entry.grid(row=3, column=1)
            fifth_entry.grid(row=4, column=1)

        update_btn = tkinter.Button(
            select_frame, text='Edit', bg='#FFF700', fg='#000300', command=update_entry)
        delete_btn = tkinter.Button(
            select_frame, text='Delete', bg='#730105', fg='#FFFFFF', command=check_delete)
        insert_btn = tkinter.Button(
            select_frame, text='Insert', bg='#03FF0F', fg='#000300', command=insert_entry)

        # ------------------Grid------------------------------------
        first_label.grid(row=0, column=0)
        second_label.grid(row=1, column=0)
        third_label.grid(row=2, column=0)
        fourth_label.grid(row=3, column=0)
        update_btn.grid(row=6, column=0)
        delete_btn.grid(row=7, column=0)
        insert_btn.grid(row=8, column=0)

        select_frame.place(relx=1, rely=0, x=0, y=0, anchor='ne')

    # ----------------Grid----------------------

    label1.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)

    field_select.grid(row=1, column=0)
    query_choice.grid(row=1, column=1, pady=20)

    keyword_enter.grid(row=1, column=2)
    keyword.grid(row=1, column=3, pady=20)

    search_btn.grid(row=1, column=4, columnspan=2, pady=20)

    em_table_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    # -----------------------------------------------------------

    tree.grid(row=3, column=0, columnspan=4)
    scrollbar.grid(row=3, column=4, sticky='ns')

    em_display_frame.place(relx=0, rely=1, relwidth=1, anchor='sw')

    employee_frame.place(relx=0.15, rely=0.1, relwidth=0.75, relheight=0.75)


def customers_table(user_type):
    print('Customers Table')
    # --------------Frame Setup------------
    customers_frame = tkinter.Frame(window)
    cus_table_frame = tkinter.Frame(customers_frame, bg='#333333')
    cus_display_frame = tkinter.Frame(customers_frame, bg='#333333')

    # -----------Label Setup-------------
    label1 = tkinter.Label(
        cus_table_frame, text='Search Customers', font=label_font, bg='#333333', fg='#FF3399')
    field_select = tkinter.Label(
        cus_table_frame, text='Select a Field', font=normal_font, bg='#333333', fg='#FF3399')
    keyword_enter = tkinter.Label(
        cus_table_frame, text='Enter your Keyword', font=normal_font, bg='#333333', fg='#FF3399')

    # ------------Search Button-----------------
    def search_from_table():
        current_choice = query_choice.get()

        for i in tree.get_children():
            tree.delete(i)

        if current_choice == "ID":
            search_query = "SELECT * FROM customers WHERE customer_id LIKE (%s)"
        elif current_choice == "Name":
            search_query = "SELECT * FROM customers WHERE customer_name LIKE (%s)"
        elif current_choice == "Address":
            search_query = "SELECT * FROM customers WHERE customer_address LIKE (%s)"
        elif current_choice == "Email":
            search_query = "SELECT * FROM customers WHERE customer_email LIKE (%s)"
        elif current_choice == "Gender":
            search_query = "SELECT * FROM customers WHERE customer_gender LIKE (%s)"
        else:
            search_query = "SELECT * FROM customers"

        data = (keyword.get(),)
        mycursor.execute(search_query, data)
        search_lst = mycursor.fetchall()
        for contact in search_lst:
            tree.insert('', tkinter.END, values=contact)

    search_btn = tkinter.Button(
        cus_table_frame, text='Search', command=search_from_table)
    keyword = tkinter.Entry(cus_table_frame)

    # ------Setting Up the Table------
    cus_display_query = "SELECT * FROM customers"
    mycursor.execute(cus_display_query)
    cus_lst = mycursor.fetchall()

    headers = ('id', 'name', 'address', 'email', 'gender')

    tree = ttk.Treeview(cus_display_frame, columns=headers,
                        show='headings', selectmode='browse', style='Zain.Treeview')

    tree.column('id', anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
    tree.heading('id', text='ID')

    tree.column('name', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('name', text='Name')

    tree.column('address', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('address', text='Address')

    tree.column('email', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('email', text='Email')

    tree.column('gender', anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
    tree.heading('gender', text='Gender')

    for contact in cus_lst:
        tree.insert('', tkinter.END, values=contact)

    # ------Scrollbar for the Table-----------
    scrollbar = ttk.Scrollbar(
        cus_display_frame, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    # ------Querying-----
    choice = tkinter.StringVar()
    query_choice = ttk.Combobox(cus_table_frame, textvariable=choice)

    query_choice['values'] = ("ID", "Name", "Address", "Email", "Gender")
    query_choice['state'] = 'readonly'

    # -------------Only for Admin/Employees---------------
    select_frame = tkinter.Frame(
        cus_table_frame, bg='#333333', highlightbackground='cyan', highlightthickness=1)

    id_var = tkinter.StringVar()
    name_var = tkinter.StringVar()
    address_var = tkinter.StringVar()
    email_var = tkinter.StringVar()
    gender_var = tkinter.StringVar()

    first_label = tkinter.Entry(select_frame, text=id_var, font=normal_font,
                                bg='#333333', fg='cyan', state=tkinter.DISABLED)
    second_label = tkinter.Entry(
        select_frame, text=name_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
    third_label = tkinter.Entry(select_frame, text=address_var,
                                font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
    fourth_label = tkinter.Entry(select_frame, text=email_var,
                                 font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
    fifth_label = tkinter.Entry(select_frame, text=gender_var,
                                font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

    # ------Printing the Selected Item-----
    def printSelectedItem(a):
        selectedItem = tree.selection()[0]

        id_var.set(tree.item(selectedItem)['values'][0])
        name_var.set(tree.item(selectedItem)['values'][1])
        address_var.set(tree.item(selectedItem)['values'][2])
        email_var.set(tree.item(selectedItem)['values'][3])
        gender_var.set(tree.item(selectedItem)['values'][4])

    tree.bind("<<TreeviewSelect>>", printSelectedItem)

    def update_entry():
        cus_update_window = tkinter.Toplevel(bg='#333333')
        cus_update_window.geometry('500x500')
        cus_update_window.title("Update Customer")

        first_entry = tkinter.Entry(cus_update_window, text=id_var,
                                    font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        second_entry = tkinter.Entry(
            cus_update_window, font=normal_font, bg='#333333', fg='cyan')
        third_entry = tkinter.Entry(
            cus_update_window, font=normal_font, bg='#333333', fg='cyan')
        fourth_entry = tkinter.Entry(
            cus_update_window, font=normal_font, bg='#333333', fg='cyan')
        fifth_entry = tkinter.Entry(
            cus_update_window, font=normal_font, bg='#333333', fg='cyan')

        second_entry.insert(0, second_label.get())
        third_entry.insert(0, third_label.get())
        fourth_entry.insert(0, fourth_label.get())
        fifth_entry.insert(0, fifth_label.get())

        id_field = tkinter.Label(
            cus_update_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
        name_field = tkinter.Label(
            cus_update_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
        address_field = tkinter.Label(
            cus_update_window, text='Address', font=normal_font, bg='#333333', fg='cyan')
        email_field = tkinter.Label(
            cus_update_window, text='Email', font=normal_font, bg='#333333', fg='cyan')
        gender_field = tkinter.Label(
            cus_update_window, text='Gender', font=normal_font, bg='#333333', fg='cyan')

        def execute_update():
            update_id = first_entry.get()
            new_name = second_entry.get()
            new_address = third_entry.get()
            new_email = fourth_entry.get()
            new_gender = fifth_entry.get()

            update_values = [
                (new_name, new_address, new_email, new_gender, update_id)]
            update_query = "UPDATE customers SET customer_name = (%s), customer_address = (%s), customer_email = (%s), customer_gender = (%s) WHERE customer_id = (%s)"
            mycursor.executemany(update_query, update_values)
            mydb.commit()

            cus_table_frame.destroy()
            cus_display_frame.destroy()
            cus_update_window.destroy()
            customers_table(user_type)

        confirm_update_btn = tkinter.Button(
            cus_update_window, text="Confirm", font=normal_font, bg='#FFF700', fg='black', command=execute_update)

        id_field.grid(row=0, column=0)
        name_field.grid(row=1, column=0)
        address_field.grid(row=2, column=0)
        email_field.grid(row=3, column=0)
        gender_field.grid(row=4, column=0)
        confirm_update_btn.grid(row=5, column=0)

        first_entry.grid(row=0, column=1)
        second_entry.grid(row=1, column=1)
        third_entry.grid(row=2, column=1)
        fourth_entry.grid(row=3, column=1)
        fifth_entry.grid(row=4, column=1)

    def delete_entry():
        cus_delete_window = tkinter.Toplevel(bg='#333333')
        cus_delete_window.geometry('500x500')
        cus_delete_window.title("Delete Customer")

        first_entry = tkinter.Entry(cus_delete_window, text=id_var,
                                    font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        second_entry = tkinter.Entry(cus_delete_window, text=name_var,
                                     font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        third_entry = tkinter.Entry(cus_delete_window, text=address_var,
                                    font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        fourth_entry = tkinter.Entry(cus_delete_window, text=email_var,
                                     font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        fifth_entry = tkinter.Entry(cus_delete_window, text=gender_var,
                                    font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

        id_field = tkinter.Label(
            cus_delete_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
        name_field = tkinter.Label(
            cus_delete_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
        address_field = tkinter.Label(
            cus_delete_window, text='Address', font=normal_font, bg='#333333', fg='cyan')
        email_field = tkinter.Label(
            cus_delete_window, text='Email', font=normal_font, bg='#333333', fg='cyan')
        gender_field = tkinter.Label(
            cus_delete_window, text='Gender', font=normal_font, bg='#333333', fg='cyan')

        def execute_delete():
            delete_id = [(first_entry.get(),)]
            update_query = "DELETE FROM customers WHERE customer_id = (%s)"
            mycursor.executemany(update_query, delete_id)
            mydb.commit()

            cus_table_frame.destroy()
            cus_display_frame.destroy()
            cus_delete_window.destroy()
            customers_table(user_type)

        confirm_delete_btn = tkinter.Button(
            cus_delete_window, text="Confirm Delete", font=normal_font, bg='#730105', fg='#FFFFFF', command=execute_delete)

        id_field.grid(row=0, column=0)
        name_field.grid(row=1, column=0)
        address_field.grid(row=2, column=0)
        email_field.grid(row=3, column=0)
        gender_field.grid(row=4, column=0)
        confirm_delete_btn.grid(row=6, column=0)

        first_entry.grid(row=0, column=1)
        second_entry.grid(row=1, column=1)
        third_entry.grid(row=2, column=1)
        fourth_entry.grid(row=3, column=1)
        fifth_entry.grid(row=4, column=1)

    def insert_entry():
        cus_insert_window = tkinter.Toplevel(bg='#333333')
        cus_insert_window.geometry('500x500')
        cus_insert_window.title("Insert Customer")

        second_entry = tkinter.Entry(
            cus_insert_window, font=normal_font, bg='#333333', fg='cyan')
        third_entry = tkinter.Entry(
            cus_insert_window, font=normal_font, bg='#333333', fg='cyan')
        fourth_entry = tkinter.Entry(
            cus_insert_window, font=normal_font, bg='#333333', fg='cyan')
        fifth_entry = tkinter.Entry(
            cus_insert_window, font=normal_font, bg='#333333', fg='cyan')

        name_field = tkinter.Label(
            cus_insert_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
        address_field = tkinter.Label(
            cus_insert_window, text='Address', font=normal_font, bg='#333333', fg='cyan')
        email_field = tkinter.Label(
            cus_insert_window, text='Email', font=normal_font, bg='#333333', fg='cyan')
        gender_field = tkinter.Label(
            cus_insert_window, text='Gender', font=normal_font, bg='#333333', fg='cyan')

        def execute_insert():
            new_name = second_entry.get()
            new_author = third_entry.get()
            new_genre = fourth_entry.get()
            new_isbn = fifth_entry.get()

            insert_values = [(new_name, new_author, new_genre, new_isbn), ]
            insert_query = "INSERT INTO customers(customer_name, customer_address, customer_email, customer_gender) VALUES (%s,%s,%s,%s)"
            mycursor.executemany(insert_query, insert_values)
            mydb.commit()

            cus_table_frame.destroy()
            cus_display_frame.destroy()
            cus_insert_window.destroy()
            customers_table(user_type)

        confirm_update_btn = tkinter.Button(
            cus_insert_window, text="Confirm", font=normal_font, bg='#03FF0F', fg='black', command=execute_insert)

        name_field.grid(row=0, column=0)
        address_field.grid(row=1, column=0)
        email_field.grid(row=2, column=0)
        gender_field.grid(row=3, column=0)
        confirm_update_btn.grid(row=5, column=0)

        second_entry.grid(row=0, column=1)
        third_entry.grid(row=1, column=1)
        fourth_entry.grid(row=2, column=1)
        fifth_entry.grid(row=3, column=1)

    update_btn = tkinter.Button(
        select_frame, text='Edit', bg='#FFF700', fg='#000300', command=update_entry)
    delete_btn = tkinter.Button(
        select_frame, text='Delete', bg='#730105', fg='#FFFFFF', command=delete_entry)
    insert_btn = tkinter.Button(
        select_frame, text='Insert', bg='#03FF0F', fg='#000300', command=insert_entry)

    # ------------------Grid------------------------------------
    first_label.grid(row=0, column=0)
    second_label.grid(row=1, column=0)
    third_label.grid(row=2, column=0)
    fourth_label.grid(row=3, column=0)
    update_btn.grid(row=6, column=0)
    delete_btn.grid(row=7, column=0)
    insert_btn.grid(row=8, column=0)

    select_frame.place(relx=1, rely=0, x=0, y=0, anchor='ne')

    # ----------------Grid----------------------

    label1.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)

    field_select.grid(row=1, column=0)
    query_choice.grid(row=1, column=1, pady=20)

    keyword_enter.grid(row=1, column=2)
    keyword.grid(row=1, column=3, pady=20)

    search_btn.grid(row=1, column=4, columnspan=2, pady=20)

    cus_table_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    # -----------------------------------------------------------

    tree.grid(row=3, column=0, columnspan=4)
    scrollbar.grid(row=3, column=4, sticky='ns')

    cus_display_frame.place(relx=0, rely=1, relwidth=1, anchor='sw')

    customers_frame.place(relx=0.15, rely=0.1, relwidth=0.75, relheight=0.75)


def borrower_table(user_type):
    print("Borrower Table")
    # --------------Frame Setup------------
    borrower_frame = tkinter.Frame(window)
    bor_table_frame = tkinter.Frame(borrower_frame, bg='#333333')
    bor_display_frame = tkinter.Frame(borrower_frame, bg='#333333')

    # -----------Label Setup-------------
    label1 = tkinter.Label(
        bor_table_frame, text='Search Borrowers', font=label_font, bg='#333333', fg='#FF3399')
    field_select = tkinter.Label(
        bor_table_frame, text='Select a Field', font=normal_font, bg='#333333', fg='#FF3399')
    keyword_enter = tkinter.Label(
        bor_table_frame, text='Enter your Keyword', font=normal_font, bg='#333333', fg='#FF3399')

    # ------------Search Button-----------------
    def search_from_table():
        current_choice = query_choice.get()

        for i in tree.get_children():
            tree.delete(i)

        if current_choice == "Borrow ID":
            search_query = "SELECT * FROM borrower WHERE borrower_id LIKE (%s)"
        elif current_choice == "Borrow Date":
            search_query = "SELECT * FROM borrower WHERE borrow_date LIKE (%s)"
        elif current_choice == "Expiry Date":
            search_query = "SELECT * FROM borrower WHERE expiry_date LIKE (%s)"
        elif current_choice == "Customer ID":
            search_query = "SELECT * FROM borrower WHERE customer_id LIKE (%s)"
        elif current_choice == "Book ID":
            search_query = "SELECT * FROM borrower WHERE book_id LIKE (%s)"
        elif current_choice == "Staff ID":
            search_query = "SELECT * FROM borrower WHERE staff_id LIKE (%s)"
        else:
            search_query = "SELECT * FROM borrower"

        data = (keyword.get(),)
        mycursor.execute(search_query, data)
        search_lst = mycursor.fetchall()
        for contact in search_lst:
            tree.insert('', tkinter.END, values=contact)

    search_btn = tkinter.Button(
        bor_table_frame, text='Search', command=search_from_table)
    keyword = tkinter.Entry(bor_table_frame)

    # ------Setting Up the Table------
    cus_display_query = "SELECT * FROM borrower"
    mycursor.execute(cus_display_query)
    cus_lst = mycursor.fetchall()

    headers = ('borrow_id', 'borrow_date', 'expiry_date',
               'customer_id', 'book_id', 'staff_id')

    tree = ttk.Treeview(bor_display_frame, columns=headers,
                        show='headings', selectmode='browse', style='Zain.Treeview')

    tree.column('borrow_id', anchor=tkinter.CENTER,
                stretch=tkinter.NO, width=100)
    tree.heading('borrow_id', text='Borrow ID')

    tree.column('borrow_date', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('borrow_date', text='Borrow Date')

    tree.column('expiry_date', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('expiry_date', text='Expiry Date')

    tree.column('customer_id', anchor=tkinter.CENTER,
                stretch=tkinter.NO, width=100)
    tree.heading('customer_id', text='Customer ID')

    tree.column('book_id', anchor=tkinter.CENTER,
                stretch=tkinter.NO, width=100)
    tree.heading('book_id', text='Book ID')

    tree.column('staff_id', anchor=tkinter.CENTER,
                stretch=tkinter.NO, width=100)
    tree.heading('staff_id', text='Staff ID')

    for contact in cus_lst:
        tree.insert('', tkinter.END, values=contact)

    # ------Scrollbar for the Table-----------
    scrollbar = ttk.Scrollbar(
        bor_display_frame, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    # ------Querying-----
    choice = tkinter.StringVar()
    query_choice = ttk.Combobox(bor_table_frame, textvariable=choice)

    query_choice['values'] = ("Borrow ID", "Borrow Date",
                              "Expiry Date", "Customer ID", "Book ID", "Staff ID")
    query_choice['state'] = 'readonly'

    # -------------Only for Admin/Employee---------------
    if user_type == 0 or user_type == 1:
        select_frame = tkinter.Frame(
            bor_table_frame, bg='#333333', highlightbackground='cyan', highlightthickness=1)

        id_var = tkinter.StringVar()
        bordate_var = tkinter.StringVar()
        expirydate_var = tkinter.StringVar()
        cusid_var = tkinter.StringVar()
        bkid_var = tkinter.StringVar()
        emid_var = tkinter.StringVar()

        first_label = tkinter.Entry(
            select_frame, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        second_label = tkinter.Entry(
            select_frame, text=bordate_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        third_label = tkinter.Entry(select_frame, text=expirydate_var,
                                    font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        fourth_label = tkinter.Entry(
            select_frame, text=cusid_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        fifth_label = tkinter.Entry(
            select_frame, text=bkid_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        sixth_label = tkinter.Entry(
            select_frame, text=emid_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

        # ------Printing the Selected Item-----
        def displaySelectedItem(a):
            selectedItem = tree.selection()[0]

            id_var.set(tree.item(selectedItem)['values'][0])
            bordate_var.set(tree.item(selectedItem)['values'][1])
            expirydate_var.set(tree.item(selectedItem)['values'][2])
            cusid_var.set(tree.item(selectedItem)['values'][3])
            bkid_var.set(tree.item(selectedItem)['values'][4])
            emid_var.set(tree.item(selectedItem)['values'][5])

        tree.bind("<<TreeviewSelect>>", displaySelectedItem)

        def update_entry():
            bor_update_window = tkinter.Toplevel(bg='#333333')
            bor_update_window.geometry('500x500')
            bor_update_window.title("Update Borrower")

            first_entry = tkinter.Entry(
                bor_update_window, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            second_entry = tkinter.Entry(
                bor_update_window, font=normal_font, bg='#333333', fg='cyan')
            third_entry = tkinter.Entry(
                bor_update_window, font=normal_font, bg='#333333', fg='cyan')
            fourth_entry = tkinter.Entry(
                bor_update_window, font=normal_font, bg='#333333', fg='cyan')
            fifth_entry = tkinter.Entry(
                bor_update_window, font=normal_font, bg='#333333', fg='cyan')
            sixth_entry = tkinter.Entry(
                bor_update_window, font=normal_font, bg='#333333', fg='cyan')

            second_entry.insert(0, second_label.get())
            third_entry.insert(0, third_label.get())
            fourth_entry.insert(0, fourth_label.get())
            fifth_entry.insert(0, fifth_label.get())
            sixth_entry.insert(0, sixth_label.get())

            id_field = tkinter.Label(
                bor_update_window, text='Borrower ID', font=normal_font, bg='#333333', fg='cyan')
            bordate_field = tkinter.Label(
                bor_update_window, text='Borrow Date', font=normal_font, bg='#333333', fg='cyan')
            expdate_field = tkinter.Label(
                bor_update_window, text='Expiry Date', font=normal_font, bg='#333333', fg='cyan')
            cusid_field = tkinter.Label(
                bor_update_window, text='Customer ID', font=normal_font, bg='#333333', fg='cyan')
            bkid_field = tkinter.Label(
                bor_update_window, text='Book ID', font=normal_font, bg='#333333', fg='cyan')
            emid_field = tkinter.Label(
                bor_update_window, text='Staff ID', font=normal_font, bg='#333333', fg='cyan')

            def execute_update():
                update_id = first_entry.get()
                new_bordate = second_entry.get()
                new_expdate = third_entry.get()
                new_cusid = fourth_entry.get()
                new_bkid = fifth_entry.get()
                new_emid = sixth_entry.get()

                update_values = [
                    (new_bordate, new_expdate, new_cusid, new_bkid, new_emid, update_id)]
                update_query = "UPDATE borrower SET borrow_date = (%s), expiry_date = (%s), customer_id = (%s), book_id = (%s), staff_id = (%s) WHERE borrower_id = (%s)"
                mycursor.executemany(update_query, update_values)
                mydb.commit()

                bor_table_frame.destroy()
                bor_display_frame.destroy()
                bor_update_window.destroy()
                borrower_table(user_type)

            confirm_update_btn = tkinter.Button(
                bor_update_window, text="Confirm", font=normal_font, bg='#FFF700', fg='black', command=execute_update)

            id_field.grid(row=0, column=0)
            bordate_field.grid(row=1, column=0)
            expdate_field.grid(row=2, column=0)
            cusid_field.grid(row=3, column=0)
            bkid_field.grid(row=4, column=0)
            emid_field.grid(row=5, column=0)
            confirm_update_btn.grid(row=6, column=0)

            first_entry.grid(row=0, column=1)
            second_entry.grid(row=1, column=1)
            third_entry.grid(row=2, column=1)
            fourth_entry.grid(row=3, column=1)
            fifth_entry.grid(row=4, column=1)
            sixth_entry.grid(row=5, column=1)

        def delete_entry():
            bor_delete_window = tkinter.Toplevel(bg='#333333')
            bor_delete_window.geometry('500x500')
            bor_delete_window.title("Delete Borrower")

            first_entry = tkinter.Entry(
                bor_delete_window, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            second_entry = tkinter.Entry(bor_delete_window, text=bordate_var,
                                         font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            third_entry = tkinter.Entry(bor_delete_window, text=expirydate_var,
                                        font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            fourth_entry = tkinter.Entry(
                bor_delete_window, text=cusid_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            fifth_entry = tkinter.Entry(
                bor_delete_window, text=bkid_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            sixth_entry = tkinter.Entry(
                bor_delete_window, text=emid_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

            id_field = tkinter.Label(
                bor_delete_window, text='Borrow ID', font=normal_font, bg='#333333', fg='cyan')
            bordate_field = tkinter.Label(
                bor_delete_window, text='Borrow Date', font=normal_font, bg='#333333', fg='cyan')
            expdate_field = tkinter.Label(
                bor_delete_window, text='Expiry Date', font=normal_font, bg='#333333', fg='cyan')
            cusid_field = tkinter.Label(
                bor_delete_window, text='Customer ID', font=normal_font, bg='#333333', fg='cyan')
            bkid_field = tkinter.Label(
                bor_delete_window, text='Book ID', font=normal_font, bg='#333333', fg='cyan')
            emid_field = tkinter.Label(
                bor_delete_window, text='Staff ID', font=normal_font, bg='#333333', fg='cyan')

            def execute_delete():
                delete_id = [(first_entry.get(),)]
                update_query = "DELETE FROM borrowers WHERE borrower_id = (%s)"
                mycursor.executemany(update_query, delete_id)
                mydb.commit()

                bor_table_frame.destroy()
                bor_display_frame.destroy()
                bor_delete_window.destroy()
                books_table(user_type)

            confirm_delete_btn = tkinter.Button(
                bor_delete_window, text="Confirm Delete", font=normal_font, bg='#730105', fg='#FFFFFF', command=execute_delete)

            id_field.grid(row=0, column=0)
            bordate_field.grid(row=1, column=0)
            expdate_field.grid(row=2, column=0)
            cusid_field.grid(row=3, column=0)
            bkid_field.grid(row=4, column=0)
            emid_field.grid(row=5, column=0)
            confirm_delete_btn.grid(row=6, column=0)

            first_entry.grid(row=0, column=1)
            second_entry.grid(row=1, column=1)
            third_entry.grid(row=2, column=1)
            fourth_entry.grid(row=3, column=1)
            fifth_entry.grid(row=4, column=1)
            sixth_entry.grid(row=5, column=1)

        def insert_entry():
            bor_insert_window = tkinter.Toplevel(bg='#333333')
            bor_insert_window.geometry('500x500')
            bor_insert_window.title("Insert Borrower")

            now = datetime.now()
            date_now = now.strftime('%Y-%m-%d')
            exp_now = now + timedelta(days=14)
            exp_date = exp_now.strftime('%Y-%m-%d')
            fourth_entry = tkinter.Entry(
                bor_insert_window, font=normal_font, bg='#333333', fg='cyan')
            fifth_entry = tkinter.Entry(
                bor_insert_window, font=normal_font, bg='#333333', fg='cyan')
            sixth_entry = tkinter.Entry(
                bor_insert_window, font=normal_font, bg='#333333', fg='cyan')

            cusid_field = tkinter.Label(
                bor_insert_window, text='Customer ID', font=normal_font, bg='#333333', fg='cyan')
            bkid_field = tkinter.Label(
                bor_insert_window, text='Book ID', font=normal_font, bg='#333333', fg='cyan')
            emid_field = tkinter.Label(
                bor_insert_window, text='Staff ID', font=normal_font, bg='#333333', fg='cyan')

            def execute_insert():
                new_bordate = date_now
                new_expdate = exp_date
                new_cusid = fourth_entry.get()
                new_bkid = fifth_entry.get()
                new_emid = sixth_entry.get()

                insert_values = [
                    (new_bordate, new_expdate, new_cusid, new_bkid, new_emid), ]
                insert_query = "INSERT INTO borrower(borrow_date, expiry_date, customer_id, book_id, staff_id) VALUES (%s,%s,%s,%s,%s)"
                mycursor.executemany(insert_query, insert_values)
                mydb.commit()

                bor_table_frame.destroy()
                bor_display_frame.destroy()
                bor_insert_window.destroy()
                borrower_table(user_type)

            confirm_update_btn = tkinter.Button(
                bor_insert_window, text="Confirm", font=normal_font, bg='#03FF0F', fg='black', command=execute_insert)

            cusid_field.grid(row=0, column=0)
            bkid_field.grid(row=1, column=0)
            emid_field.grid(row=2, column=0)
            confirm_update_btn.grid(row=3, column=0)

            fourth_entry.grid(row=0, column=1)
            fifth_entry.grid(row=1, column=1)
            sixth_entry.grid(row=2, column=1)

        update_btn = tkinter.Button(
            select_frame, text='Edit', bg='#FFF700', fg='#000300', command=update_entry)
        delete_btn = tkinter.Button(
            select_frame, text='Delete', bg='#730105', fg='#FFFFFF', command=delete_entry)
        insert_btn = tkinter.Button(
            select_frame, text='Insert', bg='#03FF0F', fg='#000300', command=insert_entry)

        # ------------------Grid------------------------------------
        first_label.grid(row=0, column=0)
        second_label.grid(row=1, column=0)
        third_label.grid(row=2, column=0)
        fourth_label.grid(row=3, column=0)
        fifth_label.grid(row=4, column=0)
        sixth_label.grid(row=5, column=0)
        update_btn.grid(row=6, column=0, columnspan=2)
        delete_btn.grid(row=7, column=0, columnspan=2)
        insert_btn.grid(row=8, column=0, columnspan=2)

        select_frame.place(relx=1, rely=0, x=0, y=0, anchor='ne')

    # ----------------Grid----------------------

    label1.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)

    field_select.grid(row=1, column=0)
    query_choice.grid(row=1, column=1, pady=20)

    keyword_enter.grid(row=1, column=2)
    keyword.grid(row=1, column=3, pady=20)

    search_btn.grid(row=1, column=4, columnspan=2, pady=20)

    bor_table_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    # -----------------------------------------------------------

    tree.grid(row=3, column=0, columnspan=4)
    scrollbar.grid(row=3, column=4, sticky='ns')

    bor_display_frame.place(relx=0, rely=1, relwidth=1, anchor='sw')

    borrower_frame.place(relx=0.15, rely=0.1, relwidth=0.75, relheight=0.75)


def branch_table(user_type):
    print("Branch Table")
    # --------------Frame Setup------------
    branch_frame = tkinter.Frame(window)
    branch_table_frame = tkinter.Frame(branch_frame, bg='#333333')
    branch_display_frame = tkinter.Frame(branch_frame, bg='#333333')

    # -----------Label Setup-------------
    label1 = tkinter.Label(
        branch_table_frame, text='Search Branch', font=label_font, bg='#333333', fg='#FF3399')
    field_select = tkinter.Label(
        branch_table_frame, text='Select a Field', font=normal_font, bg='#333333', fg='#FF3399')
    keyword_enter = tkinter.Label(
        branch_table_frame, text='Enter your Keyword', font=normal_font, bg='#333333', fg='#FF3399')

    # ------------Search Button-----------------
    def search_from_table():
        current_choice = query_choice.get()

        for i in tree.get_children():
            tree.delete(i)

        if current_choice == "ID":
            search_query = "SELECT * FROM branch WHERE branch_id LIKE (%s)"
        elif current_choice == "Name":
            search_query = "SELECT * FROM branch WHERE branch_name LIKE (%s)"
        elif current_choice == "Address":
            search_query = "SELECT * FROM branch WHERE branch_address LIKE (%s)"
        else:
            search_query = "SELECT * FROM branch"

        data = (keyword.get(),)
        mycursor.execute(search_query, data)
        search_lst = mycursor.fetchall()
        for contact in search_lst:
            tree.insert('', tkinter.END, values=contact)

    search_btn = tkinter.Button(
        branch_table_frame, text='Search', command=search_from_table)
    keyword = tkinter.Entry(branch_table_frame)

    # ------Setting Up the Table------
    branch_display_query = "SELECT * FROM branch"
    mycursor.execute(branch_display_query)
    cus_lst = mycursor.fetchall()

    headers = ('id', 'name', 'address')

    tree = ttk.Treeview(branch_display_frame, columns=headers,
                        show='headings', selectmode='browse', style='Zain.Treeview')

    tree.column('id', anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
    tree.heading('id', text='ID')

    tree.column('name', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('name', text='Name')

    tree.column('address', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('address', text='Address')

    for contact in cus_lst:
        tree.insert('', tkinter.END, values=contact)

    # ------------Scrollbar for the Table-----------
    scrollbar = ttk.Scrollbar(
        branch_display_frame, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    # ------Querying-----
    choice = tkinter.StringVar()
    query_choice = ttk.Combobox(branch_table_frame, textvariable=choice)

    query_choice['values'] = ("ID", "Name", "Address")
    query_choice['state'] = 'readonly'

    # -------------Only for Admin---------------
    if user_type == 0:
        select_frame = tkinter.Frame(
            branch_table_frame, bg='#333333', highlightbackground='cyan', highlightthickness=1)

        id_var = tkinter.StringVar()
        name_var = tkinter.StringVar()
        address_var = tkinter.StringVar()

        first_label = tkinter.Entry(
            select_frame, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        second_label = tkinter.Entry(
            select_frame, text=name_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        third_label = tkinter.Entry(select_frame, text=address_var,
                                    font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

        # ------Printing the Selected Item-----
        def printSelectedItem(a):
            selectedItem = tree.selection()[0]

            id_var.set(tree.item(selectedItem)['values'][0])
            name_var.set(tree.item(selectedItem)['values'][1])
            address_var.set(tree.item(selectedItem)['values'][2])

        tree.bind("<<TreeviewSelect>>", printSelectedItem)

        def update_entry():
            br_update_window = tkinter.Toplevel(bg='#333333')
            br_update_window.geometry('500x500')
            br_update_window.title("Update Branch")

            first_entry = tkinter.Entry(
                br_update_window, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            second_entry = tkinter.Entry(
                br_update_window, font=normal_font, bg='#333333', fg='cyan')
            third_entry = tkinter.Entry(
                br_update_window, font=normal_font, bg='#333333', fg='cyan')

            second_entry.insert(0, second_label.get())
            third_entry.insert(0, third_label.get())

            id_field = tkinter.Label(
                br_update_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
            name_field = tkinter.Label(
                br_update_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
            address_field = tkinter.Label(
                br_update_window, text='Address', font=normal_font, bg='#333333', fg='cyan')

            def execute_update():
                update_id = first_entry.get()
                new_name = second_entry.get()
                new_address = third_entry.get()

                update_values = [(new_name, new_address, update_id)]
                update_query = "UPDATE branch SET branch_name = (%s), branch_address = (%s) WHERE branch_id = (%s)"
                mycursor.executemany(update_query, update_values)
                mydb.commit()

                branch_table_frame.destroy()
                branch_display_frame.destroy()
                br_update_window.destroy()
                branch_table(user_type)

            confirm_update_btn = tkinter.Button(
                br_update_window, text="Confirm", font=normal_font, bg='#FFF700', fg='black', command=execute_update)

            id_field.grid(row=0, column=0)
            name_field.grid(row=1, column=0)
            address_field.grid(row=2, column=0)
            confirm_update_btn.grid(row=3, column=0)

            first_entry.grid(row=0, column=1)
            second_entry.grid(row=1, column=1)
            third_entry.grid(row=2, column=1)

        def check_delete():
            if id_var == '1':
                messagebox.showerror(
                    title="Error", message="Cannot delete Headquarters")
            else:
                delete_entry()

        def delete_entry():
            br_delete_window = tkinter.Toplevel(bg='#333333')
            br_delete_window.geometry('500x500')
            br_delete_window.title("Delete Branch")

            first_entry = tkinter.Entry(
                br_delete_window, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            second_entry = tkinter.Entry(
                br_delete_window, text=name_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            third_entry = tkinter.Entry(br_delete_window, text=address_var,
                                        font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

            id_field = tkinter.Label(
                br_delete_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
            name_field = tkinter.Label(
                br_delete_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
            address_field = tkinter.Label(
                br_delete_window, text='Address', font=normal_font, bg='#333333', fg='cyan')

            def execute_delete():
                delete_id = [(first_entry.get(),)]
                update_query = "DELETE FROM branch WHERE branch_id = (%s)"
                mycursor.executemany(update_query, delete_id)
                mydb.commit()

                branch_table_frame.destroy()
                branch_display_frame.destroy()
                br_delete_window.destroy()
                branch_table(user_type)

            confirm_delete_btn = tkinter.Button(
                br_delete_window, text="Confirm Delete", font=normal_font, bg='#730105', fg='#FFFFFF', command=execute_delete)

            id_field.grid(row=0, column=0)
            name_field.grid(row=1, column=0)
            address_field.grid(row=2, column=0)
            confirm_delete_btn.grid(row=3, column=0)

            first_entry.grid(row=0, column=1)
            second_entry.grid(row=1, column=1)
            third_entry.grid(row=2, column=1)

        def insert_entry():
            br_insert_window = tkinter.Toplevel(bg='#333333')
            br_insert_window.geometry('500x500')
            br_insert_window.title("Insert Branch")

            first_entry = tkinter.Entry(
                br_insert_window, font=normal_font, bg='#333333', fg='cyan')
            second_entry = tkinter.Entry(
                br_insert_window, font=normal_font, bg='#333333', fg='cyan')
            third_entry = tkinter.Entry(
                br_insert_window, font=normal_font, bg='#333333', fg='cyan')

            id_field = tkinter.Label(
                br_insert_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
            name_field = tkinter.Label(
                br_insert_window, text='Name', font=normal_font, bg='#333333', fg='cyan')
            address_field = tkinter.Label(
                br_insert_window, text='Address', font=normal_font, bg='#333333', fg='cyan')

            def execute_insert():
                new_id = first_entry.get()
                new_name = second_entry.get()
                new_address = third_entry.get()

                insert_values = [(new_id, new_name, new_address), ]
                insert_query = "INSERT INTO branch(branch_id, branch_name, branch_address) VALUES (%s,%s,%s)"
                mycursor.executemany(insert_query, insert_values)
                mydb.commit()

                branch_table_frame.destroy()
                branch_display_frame.destroy()
                br_insert_window.destroy()
                branch_table(user_type)

            confirm_update_btn = tkinter.Button(
                br_insert_window, text="Confirm", font=normal_font, bg='#03FF0F', fg='black', command=execute_insert)

            id_field.grid(row=0, column=0)
            name_field.grid(row=1, column=0)
            address_field.grid(row=2, column=0)
            confirm_update_btn.grid(row=3, column=0)

            first_entry.grid(row=0, column=1)
            second_entry.grid(row=1, column=1)
            third_entry.grid(row=2, column=1)

        update_btn = tkinter.Button(
            select_frame, text='Edit', bg='#FFF700', fg='#000300', command=update_entry)
        delete_btn = tkinter.Button(
            select_frame, text='Delete', bg='#730105', fg='#FFFFFF', command=check_delete)
        insert_btn = tkinter.Button(
            select_frame, text='Insert', bg='#03FF0F', fg='#000300', command=insert_entry)

        # ------------------Grid------------------------------------
        first_label.grid(row=0, column=0)
        second_label.grid(row=1, column=0)
        third_label.grid(row=2, column=0)
        update_btn.grid(row=3, column=0)
        delete_btn.grid(row=4, column=0)
        insert_btn.grid(row=5, column=0)

        select_frame.place(relx=1, rely=0, x=0, y=0, anchor='ne')

    # ----------------Grid----------------------

    label1.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)

    field_select.grid(row=1, column=0)
    query_choice.grid(row=1, column=1, pady=20)

    keyword_enter.grid(row=1, column=2)
    keyword.grid(row=1, column=3, pady=20)

    search_btn.grid(row=1, column=4, columnspan=2, pady=20)

    branch_table_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    # -----------------------------------------------------------

    tree.grid(row=3, column=0, columnspan=4)
    scrollbar.grid(row=3, column=4, sticky='ns')

    branch_display_frame.place(relx=0, rely=1, relwidth=1, anchor='sw')

    branch_frame.place(relx=0.15, rely=0.1, relwidth=0.75, relheight=0.75)


def cuspasw_table(user_type):
    print("Customer Password Table")
    # --------------Frame Setup------------
    cuspw_frame = tkinter.Frame(window)
    cuspw_table_frame = tkinter.Frame(cuspw_frame, bg='#333333')
    cuspw_display_frame = tkinter.Frame(cuspw_frame, bg='#333333')

    # -----------Label Setup-------------
    label1 = tkinter.Label(
        cuspw_table_frame, text='Search Customer Password', font=label_font, bg='#333333', fg='#FF3399')
    field_select = tkinter.Label(
        cuspw_table_frame, text='Select a Field', font=normal_font, bg='#333333', fg='#FF3399')
    keyword_enter = tkinter.Label(
        cuspw_table_frame, text='Enter your Keyword', font=normal_font, bg='#333333', fg='#FF3399')

    # ------------Search Button-----------------
    def search_from_table():
        current_choice = query_choice.get()

        for i in tree.get_children():
            tree.delete(i)

        if current_choice == "ID":
            search_query = "SELECT * FROM passwords WHERE customer_id LIKE (%s)"
        elif current_choice == "Password":
            search_query = "SELECT * FROM passwords WHERE password LIKE (%s)"
        else:
            search_query = "SELECT * FROM passwords"

        data = (keyword.get(),)
        mycursor.execute(search_query, data)
        search_lst = mycursor.fetchall()
        for contact in search_lst:
            tree.insert('', tkinter.END, values=contact)

    search_btn = tkinter.Button(
        cuspw_table_frame, text='Search', command=search_from_table)
    keyword = tkinter.Entry(cuspw_table_frame)

    # ------Setting Up the Table------
    branch_display_query = "SELECT * FROM passwords"
    mycursor.execute(branch_display_query)
    cus_lst = mycursor.fetchall()

    headers = ('id', 'password')

    tree = ttk.Treeview(cuspw_display_frame, columns=headers,
                        show='headings', selectmode='browse', style='Zain.Treeview')

    tree.column('id', anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
    tree.heading('id', text='ID')

    tree.column('password', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('password', text='Password')

    for contact in cus_lst:
        tree.insert('', tkinter.END, values=contact)

    # ------------Scrollbar for the Table-----------
    scrollbar = ttk.Scrollbar(
        cuspw_display_frame, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    # ------Querying-----
    choice = tkinter.StringVar()
    query_choice = ttk.Combobox(cuspw_table_frame, textvariable=choice)

    query_choice['values'] = ("ID", "Password")
    query_choice['state'] = 'readonly'

    # -------------Only for Admin---------------
    if user_type == 0:
        select_frame = tkinter.Frame(
            cuspw_table_frame, bg='#333333', highlightbackground='cyan', highlightthickness=1)

        id_var = tkinter.StringVar()
        pasw_var = tkinter.StringVar()

        first_label = tkinter.Entry(
            select_frame, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        second_label = tkinter.Entry(
            select_frame, text=pasw_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

        # ------Printing the Selected Item-----
        def printSelectedItem(a):
            selectedItem = tree.selection()[0]

            id_var.set(tree.item(selectedItem)['values'][0])
            pasw_var.set(tree.item(selectedItem)['values'][1])

        tree.bind("<<TreeviewSelect>>", printSelectedItem)

        def update_entry():
            cuspasw_update_window = tkinter.Toplevel(bg='#333333')
            cuspasw_update_window.geometry('500x500')
            cuspasw_update_window.title("Update Branch")

            first_entry = tkinter.Entry(
                cuspasw_update_window, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            second_entry = tkinter.Entry(
                cuspasw_update_window, font=normal_font, bg='#333333', fg='cyan')

            second_entry.insert(0, second_label.get())

            id_field = tkinter.Label(
                cuspasw_update_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
            pasw_field = tkinter.Label(
                cuspasw_update_window, text='Password', font=normal_font, bg='#333333', fg='cyan')

            def execute_update():
                update_id = first_entry.get()
                new_pass = second_entry.get()

                update_values = [(new_pass, update_id)]
                update_query = "UPDATE passwords SET password = (%s) WHERE customer_id = (%s)"
                mycursor.executemany(update_query, update_values)
                mydb.commit()

                cuspw_table_frame.destroy()
                cuspw_display_frame.destroy()
                cuspasw_update_window.destroy()
                cuspasw_table(user_type)

            confirm_update_btn = tkinter.Button(
                cuspasw_update_window, text="Confirm", font=normal_font, bg='#FFF700', fg='black', command=execute_update)

            id_field.grid(row=0, column=0)
            pasw_field.grid(row=1, column=0)
            confirm_update_btn.grid(row=2, column=0)

            first_entry.grid(row=0, column=1)
            second_entry.grid(row=1, column=1)

        update_btn = tkinter.Button(
            select_frame, text='Edit', bg='#FFF700', fg='#000300', command=update_entry)

        # ------------------Grid------------------------------------
        first_label.grid(row=0, column=0)
        second_label.grid(row=1, column=0)
        update_btn.grid(row=2, column=0)

        select_frame.place(relx=1, rely=0, x=0, y=0, anchor='ne')

    # ----------------Grid----------------------

    label1.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)

    field_select.grid(row=1, column=0)
    query_choice.grid(row=1, column=1, pady=20)

    keyword_enter.grid(row=1, column=2)
    keyword.grid(row=1, column=3, pady=20)

    search_btn.grid(row=1, column=4, columnspan=2, pady=20)

    cuspw_table_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    # -----------------------------------------------------------

    tree.grid(row=3, column=0, columnspan=4)
    scrollbar.grid(row=3, column=4, sticky='ns')

    cuspw_display_frame.place(relx=0, rely=1, relwidth=1, anchor='sw')

    cuspw_frame.place(relx=0.15, rely=0.1, relwidth=0.75, relheight=0.75)


def empasw_table(user_type):
    print("Employee Password Table")
    # --------------Frame Setup------------
    empw_frame = tkinter.Frame(window)
    empw_table_frame = tkinter.Frame(empw_frame, bg='#333333')
    empw_display_frame = tkinter.Frame(empw_frame, bg='#333333')

    # -----------Label Setup-------------
    label1 = tkinter.Label(
        empw_table_frame, text='Search Employee Password', font=label_font, bg='#333333', fg='#FF3399')
    field_select = tkinter.Label(
        empw_table_frame, text='Select a Field', font=normal_font, bg='#333333', fg='#FF3399')
    keyword_enter = tkinter.Label(
        empw_table_frame, text='Enter your Keyword', font=normal_font, bg='#333333', fg='#FF3399')

    # ------------Search Button-----------------
    def search_from_table():
        current_choice = query_choice.get()

        for i in tree.get_children():
            tree.delete(i)

        if current_choice == "ID":
            search_query = "SELECT * FROM em_password WHERE staff_id LIKE (%s)"
        elif current_choice == "Password":
            search_query = "SELECT * FROM em_password WHERE password LIKE (%s)"
        else:
            search_query = "SELECT * FROM em_password"

        data = (keyword.get(),)
        mycursor.execute(search_query, data)
        search_lst = mycursor.fetchall()
        for contact in search_lst:
            tree.insert('', tkinter.END, values=contact)

    search_btn = tkinter.Button(
        empw_table_frame, text='Search', command=search_from_table)
    keyword = tkinter.Entry(empw_table_frame)

    # ------Setting Up the Table------
    branch_display_query = "SELECT * FROM em_password"
    mycursor.execute(branch_display_query)
    em_lst = mycursor.fetchall()

    headers = ('id', 'password')

    tree = ttk.Treeview(empw_display_frame, columns=headers,
                        show='headings', selectmode='browse', style='Zain.Treeview')

    tree.column('id', anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
    tree.heading('id', text='ID')

    tree.column('password', anchor=tkinter.CENTER, stretch=tkinter.NO)
    tree.heading('password', text='Password')

    for contact in em_lst:
        tree.insert('', tkinter.END, values=contact)

    # ------------Scrollbar for the Table-----------
    scrollbar = ttk.Scrollbar(
        empw_display_frame, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    # ------Querying-----
    choice = tkinter.StringVar()
    query_choice = ttk.Combobox(empw_table_frame, textvariable=choice)

    query_choice['values'] = ("ID", "Password")
    query_choice['state'] = 'readonly'

    # -------------Only for Admin---------------
    if user_type == 0:
        select_frame = tkinter.Frame(
            empw_table_frame, bg='#333333', highlightbackground='cyan', highlightthickness=1)

        id_var = tkinter.StringVar()
        pasw_var = tkinter.StringVar()

        first_label = tkinter.Entry(
            select_frame, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
        second_label = tkinter.Entry(
            select_frame, text=pasw_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)

        # ------Printing the Selected Item-----
        def printSelectedItem(a):
            selectedItem = tree.selection()[0]

            id_var.set(tree.item(selectedItem)['values'][0])
            pasw_var.set(tree.item(selectedItem)['values'][1])

        tree.bind("<<TreeviewSelect>>", printSelectedItem)

        def update_entry():
            empasw_update_window = tkinter.Toplevel(bg='#333333')
            empasw_update_window.geometry('500x500')
            empasw_update_window.title("Update Employee Password")

            first_entry = tkinter.Entry(
                empasw_update_window, text=id_var, font=normal_font, bg='#333333', fg='cyan', state=tkinter.DISABLED)
            second_entry = tkinter.Entry(
                empasw_update_window, font=normal_font, bg='#333333', fg='cyan')

            second_entry.insert(0, second_label.get())

            id_field = tkinter.Label(
                empasw_update_window, text='ID', font=normal_font, bg='#333333', fg='cyan')
            pasw_field = tkinter.Label(
                empasw_update_window, text='Password', font=normal_font, bg='#333333', fg='cyan')

            def execute_update():
                update_id = first_entry.get()
                new_pass = second_entry.get()

                update_values = [(new_pass, update_id)]
                update_query = "UPDATE em_password SET password = (%s) WHERE staff_id = (%s)"
                mycursor.executemany(update_query, update_values)
                mydb.commit()

                empw_table_frame.destroy()
                empw_display_frame.destroy()
                empasw_update_window.destroy()
                empasw_table(user_type)

            confirm_update_btn = tkinter.Button(
                empasw_update_window, text="Confirm", font=normal_font, bg='#FFF700', fg='black', command=execute_update)

            id_field.grid(row=0, column=0)
            pasw_field.grid(row=1, column=0)
            confirm_update_btn.grid(row=2, column=0)

            first_entry.grid(row=0, column=1)
            second_entry.grid(row=1, column=1)

        update_btn = tkinter.Button(
            select_frame, text='Edit', bg='#FFF700', fg='#000300', command=update_entry)

        # ------------------Grid------------------------------------
        first_label.grid(row=0, column=0)
        second_label.grid(row=1, column=0)
        update_btn.grid(row=2, column=0)

        select_frame.place(relx=1, rely=0, x=0, y=0, anchor='ne')

    # ----------------Grid----------------------

    label1.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)

    field_select.grid(row=1, column=0)
    query_choice.grid(row=1, column=1, pady=20)

    keyword_enter.grid(row=1, column=2)
    keyword.grid(row=1, column=3, pady=20)

    search_btn.grid(row=1, column=4, columnspan=2, pady=20)

    empw_table_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    # -----------------------------------------------------------

    tree.grid(row=3, column=0, columnspan=4)
    scrollbar.grid(row=3, column=4, sticky='ns')

    empw_display_frame.place(relx=0, rely=1, relwidth=1, anchor='sw')

    empw_frame.place(relx=0.15, rely=0.1, relwidth=0.75, relheight=0.75)


login_page()
window.mainloop()
