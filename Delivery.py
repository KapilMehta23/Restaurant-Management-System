from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Panedwindow, Style
from tkcalendar.dateentry import DateEntry
import mysql.connector
import PortalRest

myb = mysql.connector.connect(host="localhost", user="root", passwd="Justice", database="Restaurant_Management")

# Object return points there
mycursor = myb.cursor()

def delivery(k):
    k.destroy()
    root = Tk()
    root.state('zoomed')

    #App Title
    root.title("Restaurant Management ")
    Label(root, text="Delievry Details").pack()

    #Create Panedwindow
    panedwindow=Panedwindow(root, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)

    #Create Frames
    delivery=Frame(panedwindow,width=550,height=640, relief=SUNKEN)
    tree=Frame(panedwindow,width=600,height=300, relief=SUNKEN)
    panedwindow.add(delivery, weight=1)
    panedwindow.add(tree, weight=4)

    delivery.config(bg="#2b3d4f")

    yellow = Label(delivery, text="Delivery Details", bg="#f99406",fg="White",font=('Times New Roman',30,"bold","italic"))
    yellow.grid(row=0, column=0, ipady=10, columnspan=10, ipadx=190,padx=0)


    extra = Label(delivery, text="   ", bg="#2b3d4f")
    extra.grid(row=1,pady=10)

    #  -- delivery id --
    deliveryId = Label(delivery, text='Delivery Id: ', font=('Times New Roman', 20), bg="#2b3d4f",fg="white")
    deliveryId.grid(row=2, column=0, padx=15, pady=15)


    user_input_deliveryId = StringVar()

    user_field_deliveryId = Entry(delivery, textvariable=user_input_deliveryId, font=('Times New Roman', 18))
    user_field_deliveryId.grid(row=2, column=1, padx=15, pady=15)


    # -- delivery Name --
    dname = Label(delivery, text='Delivery Name: ', font=('Times New Roman', 20), bg="#2b3d4f",fg="white")
    dname.grid(row=3, column=0, padx=15, pady=15)

    user_input_dname = StringVar()

    user_field_dname = Entry(delivery, textvariable=user_input_dname, font=('Times New Roman', 18))
    user_field_dname.grid(row=3, column=1, padx=15, pady=15)



    # ---Customer id---
    custId = Label(delivery, text='Customer Id: ', font=('Times New Roman', 20), bg="#2b3d4f",fg="white")
    custId.grid(row=4, column=0, padx=15, pady=15)

    user_input_custId = StringVar()

    user_field_custId = Entry(delivery, textvariable=user_input_custId, font=('Times New Roman', 18))
    user_field_custId.grid(row=4, column=1, padx=15, pady=15)

    #  --Employee Id---
    empId = Label(delivery, text='Employee Id: ', font=('Times New Roman', 20), bg="#2b3d4f",fg="white")
    empId.grid(row=5, column=0, padx=15, pady=15)

    user_input_empId = StringVar()

    user_field_empId = Entry(delivery, textvariable=user_input_empId, font=('Times New Roman', 18))
    user_field_empId.grid(row=5, column=1, padx=15, pady=15)


    # -- delievery charge --
    delCharge = Label(delivery, text='Delivery Charge: ', font=('Times New Roman', 20), bg="#2b3d4f",fg="white")
    delCharge.grid(row=6, column=0, padx=15, pady=15)

    user_input_delCharge = StringVar()

    user_field_delCharge = Entry(delivery, textvariable=user_input_delCharge, font=('Times New Roman', 18))
    user_field_delCharge.grid(row=6, column=1, padx=15, pady=15)


    # -- delievery date --
    delDate = Label(delivery, text='Delivery Date: ', font=('Times New Roman', 20), bg="#2b3d4f",fg="white")
    delDate.grid(row=1, column=0, padx=15, pady=15)

    # user_field_delDate = StringVar()

    user_field_delDate = DateEntry(delivery, width=18, date_pattern='YYYY/MM/DD', font=('Times New Roman', 18))
    user_field_delDate.grid(row=1, column=1, padx=15, pady=15)

    # --Add--
    def verify_details(a, b, c, d, e, f):
        if (len(a) == 0 and len(b) == 0 and len(c) == 0 and len(d) == 0 and len(e) == 0 and len(f) == 0):
            messagebox.showerror("Error", "\tFields can't be empty\nEnter properly!")
            return False

        elif len(a) == 0:
            messagebox.showerror("Error", "Delivery ID field is missing")
            return False

        elif len(b) == 0:
            messagebox.showerror("Error", "Delivery Name field is missing")
            return False

        elif (b.isalpha() != True):
            messagebox.showerror("Error", "Delivery Name can't contain Numbers or special characters")
            return False

        elif len(c) == 0:  #stuti foreign key   CUSTOMER TABLE
            messagebox.showerror("Error", "Customer Id field is missing")
            return False

        elif len(d) == 0: #stuti foreign key   Employee TABLE
            messagebox.showerror("Error", "Employee ID field is missing")
            return False

        elif len(e) == 0:
            messagebox.showerror("Error", "Delivery Charge field is missing")
            return False

        try:
            val = float(e)
            if (val < 0):
                messagebox.showerror("Error", "Charge can't be negative")
                return False

            if (val == 0):
                messagebox.showerror("Error", "Charge can't be zero")
                return False

        except:
            messagebox.showerror("Error", "Enter only numerical value!")
            return False


        return True

    def ID_primary():
        mycursor.execute("SELECT DELID FROM DELIVERY")
        delv = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            delv.append(s)

        mycursor.execute("SELECT CUSTID FROM CUSTOMER")
        cust = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            cust.append(s)

        mycursor.execute("SELECT EMPID FROM EMPLOYEE")
        emp = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            emp.append(s)
        d = 0
        cu = 0
        e = 0
        a = user_input_deliveryId.get().strip()
        b = user_input_custId.get().strip()
        c = user_input_empId.get().strip()

        for i in delv:
            if a == i:
                print(i)
                messagebox.showerror("Error", "DELIVERY ID Already Exist")
                return False
            else:
                d = d + 1

        if d == len(delv):
            for i in cust:
                if b == i:
                    print(i)
                    for i in emp:
                        if c == i:
                            print(i)
                            return True
                        else:
                            e = e + 1
                    if e == len(emp):
                        messagebox.showerror("Error", "Employee ID Doesn't Exist")
                        return False
                else:
                    cu = cu + 1
            if cu == len(cust):
                messagebox.showerror("Error", "Customer ID Doesn't Exist")
                return False

    # DELID PRIMARY KEY


    def Add_to_delivery(a, b, c, d, e, f):
        adding = "Insert into DELIVERY (DELID, DELNAME, CUSTID, EMPID, DELCHARGE, DELDATE)  values(%s,%s,%s,%s,%s,%s)"
        entry = (a, b, c, d, e, f)
        mycursor.execute(adding, entry)
        myb.commit()
        print(mycursor.rowcount, "record inserted.")

    def Add_delivery():
        a = user_input_deliveryId.get().strip()
        b = user_input_dname.get().strip()
        c = user_input_custId.get().strip()
        d = user_input_empId.get().strip()
        e = user_input_delCharge.get().strip()
        f = user_field_delDate.get()

        if verify_details(a, b, c, d, e, f):
            m = ID_primary()
            if m:
                Add_to_delivery(a, b, c, d, e, f)
                Clear_delivery()
                print_treev()


    def ID_primary_delivery():
        mycursor.execute("SELECT DELID FROM DELIVERY")
        delv = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            delv.append(s)

        mycursor.execute("SELECT CUSTID FROM CUSTOMER")
        cust = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            cust.append(s)

        mycursor.execute("SELECT EMPID FROM EMPLOYEE")
        emp = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            emp.append(s)
        d = 0
        cu = 0
        e = 0
        a = user_input_deliveryId.get().strip()
        b = user_input_custId.get().strip()
        c = user_input_empId.get().strip()

        for i in delv:
            if a == i:
                print(i)
                for i1 in cust:
                    if b == i1:
                        print(i1)
                        for i2 in emp:
                            if c == i2:
                                print(i)
                                return True
                            else:
                                e = e + 1
                        if e == len(emp):
                            messagebox.showerror("Error", "Employee Id Doesn't Exist")
                            return False
                    else:
                        cu = cu + 1
                if cu == len(cust):
                    messagebox.showerror("Error", "Customer Id Doesn't Exist")
                    return False
            else:
                d = d + 1

        if d == len(delv):
            messagebox.showerror("Error", "Delivery Id Doesn't Exist")
            return False

    def Clear_delivery():
        for records in treev.get_children():
            treev.delete(records)

    def print_treev():
        mycursor.execute("SELECT * FROM DELIVERY")
        total = []
        for x in mycursor:
            print(x)
            total.append(x)

        for i in total:
            a, b, c, d, e, f= i
            data = [a, b, c, d, e, f]
            treev.insert('', 'end', values=data)

    # ['DeliveryId', 'Delivery Name', 'Customer Id', 'Employee Id','Delivery Charge', 'Delivery Date']
    def update_from_delivery(a, b, c, d, e, f, a1):
        n1 = "UPDATE delivery SET DELID = %s ,delname = %s ,custid = %s ,empid = %s, delcharge = %s ,deldate = %s where DELID = %s order by DELID;"
        val = (a, b, c, d, e, f, a1)
        mycursor.execute(n1, val)
        myb.commit()

    def Update_delivery():
        a = user_input_deliveryId.get().strip()
        b = user_input_dname.get().strip()
        c = user_input_custId.get().strip()
        d = user_input_empId.get().strip()
        e = user_input_delCharge.get().strip()
        f = user_field_delDate.get()

        if verify_details(a, b, c, d, e, f):
            m = ID_primary_delivery()
            if m:
                update_from_delivery(a, b, c, d, e, f, a)
                Clear_delivery()
                print_treev()

    def delete_from_delivery(a):
        n = "DELETE FROM DELIVERY WHERE DELID = " + str(a) + " order by DELID"
        mycursor.execute(n)
        myb.commit()

    def ID_delete_delivery(a):
        mycursor.execute("SELECT DELID FROM DELIVERY")
        delv = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            delv.append(s)

        for i in delv:
            if a == i:
                print(i)
                return True

        messagebox.showerror("Error", "DELIVERY ID Doesn't Exist")
        return False

    def Delete_delivery():
        a = user_input_deliveryId.get()
        m = ID_delete_delivery(a)
        if m:
            delete_from_delivery(a)
            Clear_delivery()
            print_treev()


    Button(delivery, text='Add',bg="red",fg="white",font=('Times New Roman', 18),command=Add_delivery).place(x=80,y=500)
    Button(delivery, text='Update',bg="red",fg="white",font=('Times New Roman', 18),command=Update_delivery).place(x=180,y=500)
    Button(delivery, text='Delete',bg="red",fg="white",font=('Times New Roman', 18),command=Delete_delivery).place(x=310,y=500)
    Button(delivery, text='Clear', bg="red", fg="white", font=('Times New Roman', 18),command=Clear_delivery).place(x=430, y=500)
    Button(delivery, text='<<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.portal(root)).place(x=230, y=600)
    Button(delivery, text='<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.rest(root)).place(
        x=300, y=600)
    TVList = ['DeliveryId', 'Delivery Name', 'Customer Id', 'Employee Id','Delivery Charge', 'Delivery Date']

    treev = ttk.Treeview(tree, column=TVList, show='headings', height=5)
    treev['columns']= ['DeliveryId', 'Delivery Name', 'Customer Id', 'Employee Id','Delivery Charge', 'Delivery Date']
    # for giving column headings

    for i in TVList:
        treev.column(i,width=100)
        treev.heading(i, text=i.title())
    treev.grid(padx=10, pady=10, ipady=100)


    #Calling Main()

    root.mainloop()