from tkinter import *
from PIL import Image, ImageTk
import Customer
import Payment
import Delivery
import Cuisine
import Food
import Order
import Drinks
import Employee
import Chef


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
           command=lambda: Customer.customer(root)).place(x=470, y=450)
    root.mainloop()

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
           command=lambda: Employee.employee(master)).pack(pady=2)
    Button(master, height=2, width=13, text="CHEF", fg='white', bg='#051564', command=lambda: Chef.chef(master)).pack(pady=2)
    Button(master, height=2, width=13, text="DELIVERY", fg='white', bg='#051564',
           command=lambda: Delivery.delivery(master)).pack(pady=2)
    Button(master, height=2, width=13, text="PAYMENT", fg='white', bg='#051564', command=lambda: Payment.payment(master)).pack(
        pady=2)
    Button(master, height=2, width=13, text="FOOD", fg='white', bg='#051564', command=lambda: Food.food(master)).pack(pady=2)
    Button(master, height=2, width=13, text="DRINKS", fg='white', bg='#051564', command=lambda: Drinks.drinks(master)).pack(
        pady=2)
    Button(master, height=2, width=13, text="CUISINE", fg='white', bg='#051564', command=lambda: Cuisine.cuisine(master)).pack(
        pady=2)
    Button(master, height=2, width=13, text="ORDER", fg='white', bg='#051564', command=lambda: Order.order(master)).pack(
        pady=2)
    master.mainloop()
