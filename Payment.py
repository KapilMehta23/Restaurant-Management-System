#Create app using with separating widget
from tkinter import *
from tkinter.ttk import Panedwindow
from tkinter import messagebox, ttk
import mysql.connector
import PortalRest
myb = mysql.connector.connect(host="localhost", user="root", passwd="Justice", database="Restaurant_Management")

# Object return points there
mycursor = myb.cursor()

def payment(k):
    k.destroy()
    root=Tk()
    #App Title
    root.title("Python GUI Application ")
    root.state('zoomed')
    root.config(background='#abdbe3')

    Label(root, text="RESTAURANT DATABASE SYSTEM",font=('Times New Roman',24,"bold"),bg='#abdbe3').pack(pady=10)

    #Create Panedwindow
    panedwindow=Panedwindow(root, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)
    #Create Frams


    window = Frame(panedwindow,width=480,height=640)
    tree= Frame(panedwindow,width=600,height=640, relief=SUNKEN)
    panedwindow.add(window, weight=1)
    panedwindow.add(tree, weight=6)
    window.config(background="#2b3d4f")


    Label(window, text="PAYMENT", bg="#f99406",fg="White",font=('Times New Roman',30,"bold")).grid(row=0, column=0,columnspan=10,ipady=7,ipadx=220)
    Label(window, text='PID:', font=('Times New Roman', 18), bg="#2b3d4f",fg="white").grid(row= 6, column=2,pady = 8)
    Label(window, text='PAY METHOD:', font=('Times New Roman', 18), bg="#2b3d4f",fg="white").grid(row=7, column=2,pady = 8)
    Label(window, text='CUST ID:', font=('Times New Roman', 18), bg="#2b3d4f",fg="white").grid(row=8, column=2,pady=8)
    Label(window, text='ORD ID:', font=('Times New Roman', 18), bg="#2b3d4f",fg="white").grid(row=9, column=2,pady = 8)

    user_input_pid = StringVar()
    user_input_paymethod = StringVar()
    user_input_custid = StringVar()
    user_input_ordid = StringVar()

    user_field = Entry(window, textvariable=user_input_pid, font=('Times New Roman', 18)).grid(row=6, column=4,pady = 8)
    user_field = Entry(window, textvariable=user_input_paymethod, font=('Times New Roman', 18)).grid(row=7, column=4,pady = 8)
    user_field = Entry(window, textvariable=user_input_custid, font=('Times New Roman', 18)).grid(row=8, column=4,pady = 8)
    user_field = Entry(window, textvariable=user_input_ordid, font=('Times New Roman', 18)).grid(row=9, column=4, pady = 8)


    def verify_details(a, b, c, d):
        if (len(a) == 0 and len(b) == 0 and len(c) == 0 and len(d) == 0):
            messagebox.showerror("Error", "\tFields can't be empty\nEnter properly!")
            return False

        elif len(a) == 0:
            messagebox.showerror("Error", "PAYMENT ID is missing")
            return False

        elif len(a) > 20:
            messagebox.showerror("Error", "PAYMENT ID LENGTH OVERFLOW")
            return False


        elif len(b) == 0:
            messagebox.showerror("Error", "PAYMENT METHOD is missing")
            return False

        elif len(c) == 0:
            messagebox.showerror("Error", "Customer Id field is missing")
            return False
        elif c.isdigit() != True:
            messagebox.showerror("Error", "Customer Id field add only integral values")
            return False

        elif len(d) == 0:
            messagebox.showerror("Error", "ORDER ID field is missing")
            return False
        elif d.isdigit() != True:
            messagebox.showerror("Error", "Order Id conatins only integral values")
            return False

        return True

    def ID_primary():
        mycursor.execute("SELECT PID FROM PAYMENT")
        pay = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            pay.append(s)

        mycursor.execute("SELECT ORDID FROM Restaurant_Management.ORDER")
        order = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            order.append(s)

        mycursor.execute("SELECT CUSTID FROM CUSTOMER")
        cust = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            cust.append(s)
        p = 0
        ord = 0
        cs = 0
        a = user_input_pid.get().strip()
        b = user_input_ordid.get().strip()
        c = user_input_custid.get().strip()

        for i in pay:
            if a == i:
                print(i)
                messagebox.showerror("Error", "Payment ID Already Exist")
                return False
            else:
                p = p + 1

        if p == len(pay):
            for i in order:
                if b == i:
                    print(i)
                    for i in cust:
                        if c == i:
                            print(i)
                            return True
                        else:
                            cs = cs + 1
                    if cs == len(cust):
                        messagebox.showerror("Error", "Customer ID Doesn't Exist")
                        return False
                else:
                    ord = ord + 1
            if ord == len(order):
                messagebox.showerror("Error", "Order ID Doesn't Exist")
                return False


    def Add_to_payment(a, b, c, d):
        adding = "Insert into payment (PID,PAYMETHOD,CUSTID,ORDID) values(%s,%s,%s,%s)"
        entry = (a, b, c, d)
        mycursor.execute(adding, entry)
        myb.commit()
        print(mycursor.rowcount, "record inserted.")

    def Add_payment():
        a = user_input_pid.get().strip()
        b = user_input_paymethod.get().strip()
        c = user_input_custid.get().strip()
        d = user_input_ordid.get().strip()

        if verify_details(a, b, c, d):
            m = ID_primary()
            if m:
                Add_to_payment(a, b, c, d)
                Clear_payment()
                print_treev()


    def ID_primary_payment():
        mycursor.execute("SELECT PID FROM PAYMENT")
        payment = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            payment.append(s)

        mycursor.execute("SELECT ORDID FROM Restaurant_Management.ORDER")
        order = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            order.append(s)

        mycursor.execute("SELECT CUSTID FROM CUSTOMER")
        cust = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            cust.append(s)
        p = 0
        ord = 0
        cs = 0
        a = user_input_pid.get().strip()
        b = user_input_ordid.get().strip()
        c = user_input_custid.get().strip()

        for i in payment:
            if a == i:
                print(i)
                for i1 in order:
                    if b == i1:
                        print(i1)
                        for i2 in cust:
                            if c == i2:
                                print(i)
                                return True
                            else:
                                cs = cs + 1
                        if cs == len(cust):
                            messagebox.showerror("Error", "Customer ID Doesn't Exist")
                            return False
                    else:
                        ord = ord + 1
                if ord == len(order):
                    messagebox.showerror("Error", "Order ID Doesn't Exist")
                    return False
            else:
                p = p + 1

        if p == len(payment):
            messagebox.showerror("Error", "PAYMENT ID Doesn't Exist")
            return False

    def update_from_payment(a, b, c, d, a1):
        n1 = "UPDATE payment SET PID = %s ,PAYMETHOD = %s ,CUSTID = %s ,ORDID = %s where PID = %s order by PID;"
        val = (a, b, c, d, a1)
        mycursor.execute(n1, val)
        myb.commit()

    def Update_payment():
        a = user_input_pid.get().strip()
        b = user_input_paymethod.get().strip()
        c = user_input_custid.get().strip()
        d = user_input_ordid.get().strip()



        if verify_details(a, b, c, d):
            m = ID_primary_payment()
            if m:
                update_from_payment(a, b, c, d, a)
                Clear_payment()
                print_treev()

    def delete_from_payment(a):
        n = "DELETE FROM PAYMENT WHERE PID = " + str(a) + " order by PID"
        mycursor.execute(n)
        myb.commit()

    def ID_delete_payment(a):
        mycursor.execute("SELECT PID FROM PAYMENT")
        payment = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            payment.append(s)

        p=0
        for i in payment:
            if a == i:
                print(i)
                return True
            else:
                p = p + 1

        if p == len(payment):
            messagebox.showerror("Error", "PAYMENT ID Doesn't Exist")
            return False

    def Delete_payment():
        a = user_input_pid.get()
        m = ID_delete_payment(a)
        if m:
            delete_from_payment(a)
            Clear_payment()
            print_treev()

    def Clear_payment():
        for records in treev.get_children():
            treev.delete(records)

    def print_treev():
        mycursor.execute("SELECT * FROM PAYMENT")
        total = []
        for x in mycursor:
            print(x)
            total.append(x)

        for i in total:
            a, b, c, d= i
            data = [a, b, c, d]
            treev.insert('', 'end', values=data)

    Button(window, text='Add',bg="red",fg="white",font=('Times New Roman', 18), command=Add_payment).place(x=100,y=380)
    Button(window, text='Update',bg="red",fg="white",font=('Times New Roman', 18), command=Update_payment).place(x=200,y=380)
    Button(window, text='Delete', bg="red", fg="white", font=('Times New Roman', 18), command=Delete_payment).place(x=330, y=380)
    Button(window, text='Clear',bg="red",fg="white",font=('Times New Roman', 18), command=Clear_payment).place(x=450,y=380)
    Button(window, text='<<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.portal(root)).place(x=230, y=500)
    Button(window, text='<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.rest(root)).place(
        x=300, y=500)
    TVList = ['PID', 'PAY METHOD','CUST ID','ORD ID']
    treev = ttk.Treeview(tree, column=TVList, show='headings')

    # for giving column headings

    for i in TVList:
        treev.column(i,width=120)
        treev.heading(i, text=i.title())
    treev.grid(ipadx=40,padx=30,pady=30)
    #Calling Main()
    root.mainloop()