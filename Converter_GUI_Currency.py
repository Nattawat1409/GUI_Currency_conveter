import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from tkinter import *
from currency_converter import CurrencyConverter

Main_Window = Tk()
Convert_Currency = CurrencyConverter()

cred = credentials.Certificate('helloworldfirebase-69c9d-firebase-adminsdk-3l74r-1a3724fca5.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://helloworldfirebase-69c9d-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

def Database_Register(user_data_Register):
    # pushing data into database
    ref = db.reference('Users/Register')
    ref.push(user_data_Register)

def Database_Login(user_data_Login):
    # pushing data into database
    ref = db.reference('Users/Login')
    ref.push(user_data_Login)

def converter_Screen():
    Menu_Name.configure(text="Convert from Currency1 to Currency2", width=30)

    Amount_Label = Label(Main_Window, text="Prices", foreground="black", width=label_width, font=('Helvetica', 20), anchor=E)
    Amount_Label.grid(column=0, row=2, pady=2, sticky=E)
    Price_input = Entry(Main_Window, font=("Helvetica", 20), width=entry_width)
    Price_input.grid(column=1, row=2, pady=2, padx=1, sticky=W)

    Currency1_Label = Label(Main_Window, text="Currency 1", foreground="black", width=label_width, font=('Helvetica', 20), anchor=E)
    Currency1_Label.grid(column=0, row=3, pady=2, sticky=E)
    Currency1_input = Entry(Main_Window, font=("Helvetica", 20), width=entry_width)
    Currency1_input.grid(column=1, row=3, pady=2, padx=1, sticky=W)

    Currency2_Label = Label(Main_Window, text="Currency 2", foreground="black", width=label_width, font=('Helvetica', 20), anchor=E)
    Currency2_Label.grid(column=0, row=4, pady=2, sticky=E)
    Currency2_input = Entry(Main_Window, font=("Helvetica", 20), width=entry_width)
    Currency2_input.grid(column=1, row=4, pady=2, padx=1, sticky=W)

    Convert_Button = Button(Main_Window, text="Convert", foreground="white", bg="orange", width=20, font=('Helvetica', 20))
    Convert_Button.grid(column=0, row=5, columnspan=2, pady=10)

    Result_after_converted = Label(Main_Window, text="Result", font=('Helvetica', 20), width=entry_width, activeforeground="Black", activebackground="white")
    Result_after_converted.grid(column=0, row=6, columnspan=2, pady=10)

    def Process_Convert(event):
        amount = float(Price_input.get())
        current1 = Currency1_input.get().upper()
        current2 = Currency2_input.get().upper()
        final_result = Convert_Currency.convert(amount, current1, current2)
        Format_float = "{:.5f}".format(final_result)
        Include_Unit = Format_float + " " + current2
        Result_after_converted.configure(text=Include_Unit)

    Convert_Button.bind('<Button-1>', Process_Convert)

def After_ClickLogin(event):
    # After click login
    Login_button.destroy()
    Register_button.destroy()

    User_label = Label(Main_Window, text="Username", foreground="black", width=10, font=('Helvetica', 20), anchor=E)
    User_label.grid(column=0, row=2, pady=2, sticky=E)
    User_Data = Entry(Main_Window, font=("Helvetica", 20), width=20)
    User_Data.grid(column=1, row=2, pady=2, sticky=W)

    Password_label = Label(Main_Window, text="Password", foreground="black", width=10, font=('Helvetica', 20), anchor=E)
    Password_label.grid(column=0, row=3, pady=2, sticky=E)
    Password_Data = Entry(Main_Window, font=("Helvetica", 20), width=20, show='*')
    Password_Data.grid(column=1, row=3, pady=2, sticky=W)

    ConfirmLog_Button = Button(Main_Window, text="Login", foreground="white", bg="orange", width=20, font=('Helvetica', 20))
    ConfirmLog_Button.grid(column=0, row=4, columnspan=2, pady=10)
    def Store_user_data_login(event):
        user_login_data = {
            'username': User_Data.get(),
            'password': Password_Data.get(),
        }
        Database_Login(user_login_data)
        # Clear the fields after storing data
        User_Data.delete(0, END)
        Password_Data.delete(0, END)

        User_label.destroy(),
        User_Data.destroy(),
        Password_label.destroy(),
        Password_Data.destroy(),
        ConfirmLog_Button.destroy(),
        converter_Screen()

    ConfirmLog_Button.bind('<Button-1>', Store_user_data_login)



def After_ClickRegister(event):
    # After click Register
    Login_button.destroy()
    Register_button.destroy()

    User_label = Label(Main_Window, text="Username", foreground="black", width=15, font=('Helvetica', 20), anchor=E)
    User_label.grid(column=0, row=2, pady=2, sticky=E)
    User_Data = Entry(Main_Window, font=("Helvetica", 20), width=30)
    User_Data.grid(column=1, row=2, pady=2, sticky=W)

    Password_label = Label(Main_Window, text="Password", foreground="black", width=15, font=('Helvetica', 20), anchor=E)
    Password_label.grid(column=0, row=3, pady=2, sticky=E)
    Password_Data = Entry(Main_Window, font=("Helvetica", 20), width=30, show='*')
    Password_Data.grid(column=1, row=3, pady=2, sticky=W)

    Gmail_label = Label(Main_Window, text="Gmail", foreground="black", width=15, font=('Helvetica', 20), anchor=E)
    Gmail_label.grid(column=0, row=4, pady=2, sticky=E)
    Gmail_Data = Entry(Main_Window, font=("Helvetica", 20), width=30)
    Gmail_Data.grid(column=1, row=4, pady=2, sticky=W)

    Confirm_Gmail = Label(Main_Window, text="Confirm Gmail", foreground="black", width=15, font=('Helvetica', 20), anchor=E)
    Confirm_Gmail.grid(column=0, row=5, pady=2, sticky=E)
    Confirm_Gmail_Data = Entry(Main_Window, font=("Helvetica", 20), width=30)
    Confirm_Gmail_Data.grid(column=1, row=5, pady=2, sticky=W)


    def Store_user_data(event):
        user_register_data = {
            'username': User_Data.get(),
            'password': Password_Data.get(),
            'gmail': Gmail_Data.get(),
            'confirm_gmail': Confirm_Gmail_Data.get()
        }
        Database_Register(user_register_data)
        # Clear the fields after storing data
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

    CreateAccount_Button = Button(Main_Window, text="Create Account", foreground="white", bg="orange", width=20, font=('Helvetica', 20))
    CreateAccount_Button.grid(column=0, row=6, columnspan=2, pady=10)
    CreateAccount_Button.bind('<Button-1>', Store_user_data)



                                # Main Window
Main_Window.iconbitmap('money-clipart-transparent-background-free-png.ico')
Main_Window.title('Currency Converter')
Main_Window.configure(bg='azure2')

label_width = 15
entry_width = 30

Menu_Name = Label(Main_Window, text="Currency Converter Program", foreground="#458B74", bg="#CDC8B1", font=("Helvetica", 30, 'bold'))
Menu_Name.grid(column=0, row=0, columnspan=2, pady=10)

# to register and login
Register_button = Button(Main_Window, text="Register", foreground="white", bg="green", width=10, font=('Helvetica', 20))
Register_button.grid(column=0, row=1, columnspan=2, pady=10)
Register_button.bind('<Button-1>', After_ClickRegister)

Login_button = Button(Main_Window, text="Login", foreground="white", bg="green", width=10, font=('Helvetica', 20))
Login_button.grid(column=0, row=2, columnspan=2, pady=10)
Login_button.bind('<Button-1>', After_ClickLogin)

Main_Window.mainloop()
