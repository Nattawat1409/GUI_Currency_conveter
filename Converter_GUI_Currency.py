# we need function to create new Path in firebase automate to for intuitive program and access with everyone to deploy it #
# Nattawat Ruensumrit #
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from tkinter import *
from currency_converter import CurrencyConverter
from tkinter import messagebox
from tkinter import ttk
from datetime import date

# GUI colors tone #
deepblue = '#11384A'
sightly_white = '#FAF2EC'
blue_sea = '#2F9CCF'
actual_grey = '#6C858D'
deep_grey = '#2D5060'
sky_light = '#C7DBE3'

# align label entry #
label_width = 15
entry_width = 30

Main_Window = Tk()
Convert_Currency = CurrencyConverter()
cred = credentials.Certificate('input your Json file download from firebase')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'Input your databaseURL from firebase'
})

def Database_Register(user_data_Register , keep_login):
    # pushing data/Create folders into database
    # Register Path #
    ref = db.reference('Users/Register')
    ref.push(user_data_Register)
    # Login Path #
    ref_login = db.reference('Users/Login')
    ref_login.push(keep_login)
def Database_Login(user_data_Login):
    # Pushing data into database
    ref_login = db.reference('Users/Login')

    # Retrieve all login entries
    login_entries = ref_login.get()

    # Check if the user data exists in the database
    found = False
    for key, value in login_entries.items():
        if value['username'] == user_data_Login['username'] and value['password'] == user_data_Login['password']:
            found = True
            print(f"User data '{user_data_Login}' found in database.")
            break
    if not found: # not false = true # Condition
        messagebox.showerror("Warning account" , "Your account doesn't exist in database.Please registration")
    return found


def converter_Screen():
    Menu_Name.configure(text="Convert from Currency1 to Currency2", width=30)

    Amount_Label = Label(Main_Window, text="Prices",
                         fg=sightly_white, bg=blue_sea,
                         width=label_width,
                         font=('Helvetica', 20),
                         anchor=E)
    Amount_Label.grid(column=0, row=2, pady=2, sticky=E)
    Price_input = Entry(Main_Window, font=("Helvetica", 20), width=entry_width)
    Price_input.grid(column=1, row=2, pady=2, padx=1, sticky=W)

    # current1 #
    Currency1_Label = Label(Main_Window, text="Current1",
                            fg=sightly_white, bg=blue_sea,
                            width=label_width,
                            font=('Helvetica', 20), anchor=E)
    Currency1_Label.grid(column=0, row=3, pady=2, sticky=E)

    # make a list to keep all currencys #
    currency_list = ['DKK' ,'TRY', 'ILS', 'MTL', 'BGN', 'MYR', 'SIT', 'GBP', 'HUF', 'IDR', 'CHF', 'CAD', 'NZD',
                     'RUB', 'LVL', 'HRK', 'RON', 'BRL', 'SEK', 'CYP', 'HKD', 'AUD', 'JPY', 'PLN', 'CZK', 'USD',
                     'ISK', 'KRW', 'TRL', 'EEK', 'THB', 'SKK', 'NOK', 'MXN', 'ZAR', 'EUR', 'INR', 'LTL', 'SGD',
                     'CNY', 'ROL', 'PHP', 'THB']
    Currency1_input = ttk.Combobox(Main_Window, values=currency_list, font=("Helvetica", 20), width=entry_width)
    Currency1_input.grid(column=1, row=3, pady=2, padx=1, sticky=W)

    # current2 #
    Currency2_Label = Label(Main_Window, text="Current2",
                            fg=sightly_white, bg=blue_sea,
                            width=label_width,
                            font=('Helvetica', 20), anchor=E)
    Currency2_Label.grid(column=0, row=4, pady=2, sticky=E)
    Currency2_input = ttk.Combobox(Main_Window, values=currency_list, font=("Helvetica", 20), width=entry_width)
    Currency2_input.grid(column=1, row=4, pady=2, padx=1, sticky=W)
    ## ADD DATE BUTTON ##
    Convert_Button = Button(Main_Window, text="Convert", fg=sightly_white,
                            bg=actual_grey, width=20,
                            font=('Arial', 20 , 'bold'))
    Convert_Button.grid(column=0, row=8, columnspan=2, pady=10)
    Result_after_converted = Label(Main_Window, text="Result", font=('Arial', 20 , 'bold'), width=entry_width,
                                   activeforeground="Black", activebackground="white")
    Result_after_converted.grid(column=0, row=9, columnspan=2, pady=10)

    # Calculate and convert current function #
    def Process_Convert(event):
        try:
            amount = float(Price_input.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid amount.")
            return

        current1 = Currency1_input.get().upper()
        current2 = Currency2_input.get().upper()

        try:  # formula to calculate currency conversion #
            final_result = Convert_Currency.convert(amount, current1, current2)
            Format_float = "{:.5f}".format(final_result)
            Include_Unit = Format_float + " " + current2
            Result_after_converted.configure(text=Include_Unit)
        except Exception as e:
            messagebox.showerror("Conversion Error", str(e))  # occur exception from system #

    Convert_Button.bind('<Button-1>', Process_Convert)

    # After click login
def After_ClickLogin(event):
    Login_button.destroy()
    Register_button.destroy()

    User_label = Label(Main_Window, text="Username", fg=sightly_white, bg  = blue_sea,  width=10, font=('Helvetica', 20), anchor=E)
    User_label.grid(column=0, row=2, pady=2, sticky=E)
    User_Data = Entry(Main_Window, font=("Helvetica", 20), width=20)
    User_Data.grid(column=1, row=2, pady=2, sticky=W)

    Password_label = Label(Main_Window, text="Password", fg=sightly_white, bg = blue_sea,width=10, font=('Helvetica', 20), anchor=E)
    Password_label.grid(column=0, row=3, pady=2, sticky=E)
    Password_Data = Entry(Main_Window, font=("Helvetica", 20), width=20, show='*')
    Password_Data.grid(column=1, row=3, pady=2, sticky=W)

    ConfirmLog_Button = Button(Main_Window, text="Login", foreground=sightly_white, bg=actual_grey , width=20, font=('Arial', 20 , 'bold'))
    ConfirmLog_Button.grid(column=0, row=4, columnspan=2, pady=10)
    def Store_user_data_login(event):

        user_login_data = {
            'username': User_Data.get(),
            'password': Password_Data.get(),
        }

        if Database_Login(user_login_data) == True:
            def Delete_afterInput():
                User_Data.delete(0, END)
                Password_Data.delete(0, END)
                User_label.destroy(),
                User_Data.destroy(),
                Password_label.destroy(),
                Password_Data.destroy(),
                ConfirmLog_Button.destroy(),
                converter_Screen()

            Delete_afterInput()

        # if false anything won't change on GUI #
    ConfirmLog_Button.bind('<Button-1>', Store_user_data_login)

def After_ClickRegister(event):
    # After click Register
    Login_button.destroy()
    Register_button.destroy()
    Menu_Name.configure(width=30)
    User_label = Label(Main_Window, text="Username", foreground="black", width=15,
                       fg = sightly_white,
                       bg = blue_sea,
                       font=('Helvetica', 20),
                       anchor=E)
    User_label.grid(column=0, row=2, pady=2, sticky=E)
    User_Data = Entry(Main_Window, font=("Helvetica", 20), width=30)
    User_Data.grid(column=1, row=2, pady=2, sticky=W)

    Password_label = Label(Main_Window, text="Password", foreground="black",
                           fg = sightly_white, bg = blue_sea ,
                           width=15, font=('Helvetica', 20),anchor=E)
    Password_label.grid(column=0, row=3, pady=2, sticky=E)
    Password_Data = Entry(Main_Window, font=("Helvetica", 20), width=30, show='*')
    Password_Data.grid(column=1, row=3, pady=2, sticky=W)

    Gmail_label = Label(Main_Window, text="Gmail", foreground="black",fg = sightly_white,
                        bg = blue_sea, width=15,
                        font=('Helvetica', 20), anchor=E)
    Gmail_label.grid(column=0, row=4, pady=2, sticky=E)
    Gmail_Data = Entry(Main_Window, font=("Helvetica", 20), width=30)
    Gmail_Data.grid(column=1, row=4, pady=2, sticky=W)

    Confirm_Gmail = Label(Main_Window, text="Confirm Gmail", foreground="black",
                          fg = sightly_white, bg = blue_sea,
                          width=15, font=('Helvetica', 20), anchor=E)
    Confirm_Gmail.grid(column=0, row=5, pady=2, sticky=E)
    Confirm_Gmail_Data = Entry(Main_Window, font=("Helvetica", 20), width=30)
    Confirm_Gmail_Data.grid(column=1, row=5, pady=2, sticky=W)

    def Store_user_data(event):
        if  Gmail_Data.get() == Confirm_Gmail_Data.get():
            user_register_data = {
                'username': User_Data.get(),
                'password': Password_Data.get(),
                'gmail': Gmail_Data.get(),
                'confirm_gmail': Confirm_Gmail_Data.get()
            }
            store_in_login = {
                'username': user_register_data['username'] ,
                'password' : user_register_data['password']
            }
            Database_Register(user_register_data , store_in_login)
            User_Data.delete(0, END)
            Password_Data.delete(0, END)
            Gmail_Data.delete(0, END)
            Confirm_Gmail_Data.delete(0, END)

            converter_Screen()
            # Destroy labels and entry fields after processing
            User_label.destroy()
            User_Data.destroy()
            Password_label.destroy()
            Password_Data.destroy()
            Gmail_label.destroy()
            Gmail_Data.destroy()
            Confirm_Gmail.destroy()
            Confirm_Gmail_Data.destroy()
            CreateAccount_Button.destroy()

        elif Gmail_Data.get() != Confirm_Gmail_Data.get():
            messagebox.showerror("your email are not corresponding",
                                 "Oops, please recheck your Email again which are related")
        # Clear the fields after storing data


    CreateAccount_Button = Button(Main_Window, text="Create Account" ,fg = sightly_white,
                                  bg = actual_grey, width=20, font=('Arial', 20 , 'bold'))
    CreateAccount_Button.grid(column=0, row=6, columnspan=2, pady=10)
    CreateAccount_Button.bind('<Button-1>', Store_user_data)


    # Main Window #
Main_Window.iconbitmap('money-clipart-transparent-background-free-png.ico') # add icon for symbol of program #
Main_Window.title('Currency Converter')
Main_Window.configure(bg=sightly_white)

Menu_Name = Label(Main_Window, text="Currency Converter Program", foreground=blue_sea, bg= deepblue , fg = sightly_white,width = 35 , font=("Helvetica", 30, 'bold'))
Menu_Name.grid(column=0, row=0, columnspan=2, pady=10)

# to register and login #
Register_button = Button(Main_Window, text="Register", foreground= sightly_white, bg=blue_sea, width=10, font=('Arial', 20 , 'bold'))
Register_button.grid(column=0, row=1, columnspan=2, pady=10)
Register_button.bind('<Button-1>', After_ClickRegister)
Login_button = Button(Main_Window, text="Login", foreground=sightly_white, bg=blue_sea, width=10, font=('Arial', 20 , 'bold'))
Login_button.grid(column=0, row=2, columnspan=2, pady=10)
Login_button.bind('<Button-1>', After_ClickLogin)

Main_Window.mainloop()