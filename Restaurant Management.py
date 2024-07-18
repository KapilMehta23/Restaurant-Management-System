from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import Customer
import Payment
import Delivery
import Cuisine
import Food
import Order
import Drinks
import Employee
import Chef


myb = mysql.connector.connect(host="localhost", user="root", passwd="Justice", database="Restaurant_Management")

# Object return points there
mycursor = myb.cursor()

def customer(temp):
    #temp.destroy()
    Customer.customer(temp)

def cuisine(temp):
    #temp.destroy()
    Cuisine.cuisine(temp)

def food(temp):
    #temp.destroy()
    Food.food(temp)

def employee(temp):
    #temp.destroy()
    Employee.employee(temp)

def chef(temp):
    #temp.destroy()
    Chef.chef(temp)

def payment(temp):
    #temp.destroy()
    Payment.payment(temp)

def order(temp):
    #temp.destroy()
    Order.order(temp)

def delivery(temp):
    #temp.destroy()
    Delivery.delivery(temp)

def drinks(temp):
    #temp.destroy()
    Drinks.drinks(temp)

def rest(temp):
    temp.destroy()

    master = Tk()
    master.title("GK_SCIENCE_ODD")
    master.geometry("600x500")
    master.maxsize(600, 500)

    img = ImageTk.PhotoImage(Image.open(r"quiz.jpg").resize((600, 500), Image.ANTIALIAS))
    Label(image=img).place(x=0, y=0)

    Label(master, text="SELECT YOUR PROFESSION", font=("Calibri 30 bold", 18), fg='white', bg='#0d0e13').pack(pady=15)

    Button(master, height=2, width=13, text="EMPLOYEE", fg='white', bg='#051564',
           command=lambda: employee(master)).pack(pady=2)
    Button(master, height=2, width=13, text="CHEF", fg='white', bg='#051564', command=lambda: chef(master)).pack(pady=2)
    Button(master, height=2, width=13, text="DELIVERY", fg='white', bg='#051564',
           command=lambda: delivery(master)).pack(pady=2)
    Button(master, height=2, width=13, text="PAYMENT", fg='white', bg='#051564', command=lambda: payment(master)).pack(
        pady=2)
    Button(master, height=2, width=13, text="FOOD", fg='white', bg='#051564', command=lambda: food(master)).pack(pady=2)
    Button(master, height=2, width=13, text="DRINKS", fg='white', bg='#051564', command=lambda: drinks(master)).pack(
        pady=2)
    Button(master, height=2, width=13, text="CUISINE", fg='white', bg='#051564', command=lambda: cuisine(master)).pack(
        pady=2)
    Button(master, height=2, width=13, text="ORDER", fg='white', bg='#051564', command=lambda: order(master)).pack(
        pady=2)
    master.mainloop()

def portal(temp):
    temp.destroy()

    root = Tk()
    root.geometry("700x500")
    #root.config(background="white")
    Label(root, text="CHOOSE ANY OF THE FOLLOWING", font=("Times", "24", "bold"), bg="white").pack(pady=5)

    img = ImageTk.PhotoImage(Image.open(r"computer.jpg").resize((500, 400), Image.ANTIALIAS))
    Label(image=img, bg="white").place(x=100, y=50)

    Button(root, text="RESTAURANT", font=("Calibri 10 bold"), height=3, width=12, bg="#e06919",
           command=lambda: rest(root)).place(x=190, y=450)
    Button(root, text="CUSTOMER", font=("Calibri 10 bold"), height=3, width=12, bg="#e06919",
           command=lambda: customer(root)).place(x=470, y=450)
    root.mainloop()

def login(temp):
    temp.destroy()
    GUI = Tk()
    GUI.title("Login")
    GUI.geometry('650x430')
    table_name = "hello"

    def loginPage():

        # -----UserName----
        GUI.config(background="#2b3d4f")
        yellow = Label(GUI, text="Login", bg="#f99406", fg="White", font=('Times New Roman', 30, "bold", "italic"))
        yellow.grid(row=0, column=0, columnspan=10, ipady=10, ipadx=280)

        user = Label(GUI, text='Username: ', font=('Times New Roman', 18), bg="#2b3d4f", fg="white")
        user.grid(row=3, column=2, padx=10, pady=45)

        Label(GUI, text='Password: ', font=('Times New Roman', 18), bg="#2b3d4f", fg="white").grid(row=4, column=2,
                                                                           padx=10, pady=45)

        a = StringVar()
        Entry(GUI, textvariable=a, font=('Times New Roman', 18)).grid(row=3, column=3, padx=10, pady=45)
        b = StringVar()
        Entry(GUI, show='*', textvariable=b, font=('Times New Roman', 18)).grid(row=4, column=3, padx=10, pady=45)

        user = ["Kapil"]
        passw = "1234"

        def logIn(GUI):
            username = a.get().strip()
            password = b.get().strip()

            if (len(username) == 0):
                messagebox.showerror("Error", "Username field empty")
                return False
            elif (len(password) == 0):
                messagebox.showerror("Error", "Password field empty")
                return False

            elif username not in user:
                messagebox.showerror("Error", "Username does not exist")
                return False

            elif password != passw:
                messagebox.showerror("Error", "Password does not exist")
                return False

            portal(GUI)

        login = Button(GUI, text='Login', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
                       command=lambda: logIn(GUI))
        login.grid(row=5, column=2, padx=100, pady=10, ipadx=40, ipady=5)

    loginPage()

    GUI.mainloop()

root = Tk()
root.title("DBMS_INNOVATIVE_ASSIGNMENT")
root.geometry("700x500")
root.maxsize(700,500)
img = ImageTk.PhotoImage(Image.open("C:\\Users\\Kapil Mehta\\Desktop\\4th SEM\\DBMS-ref\\Restaurant_Management_System\\restaurant.jpg").resize((700, 500), Image.ANTIALIAS))
Label(image = img).place(x=0,y=0)

Label(root, text ="Restaurant management",font = ("Times", "24", "bold italic"),bg = "#8f8830").pack(pady=5)
Button(root,text = "Proceed",height=2,width=7,bg = "#F0970D",command=lambda:login(root)).place(x=305,y=50)
root.mainloop()