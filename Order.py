from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Panedwindow, Treeview
import mysql.connector
import PortalRest
myb = mysql.connector.connect(host="localhost", user="root", passwd="Justice", database="Restaurant_Management")

# Object return points there
mycursor = myb.cursor()

def order(k):
    k.destroy()
    root = Tk()
    # App Title
    root.title("Python GUI Application ")
    root.state('zoomed')
    ttk.Label(root, text="Separating widget").pack()
    # Create Panedwindow
    panedwindow = Panedwindow(root, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)
    # Create Frams
    order = Frame(panedwindow, width=100, height=300, relief=SUNKEN)
    order.config(background="#2b3d4f")


    def Add_To_order(a, b, c, d, e):
        t = "Restaurant_Management.Order"
        print(t)
        adding = "Insert into " + t.lower() + " (ORDID,TOTALCOST,FOODID,DRINKID,DELID) values(%s,%s,%s,%s,%s)"
        entry = (a, b, c, d, e)
        mycursor.execute(adding, entry)
        myb.commit()
        print(mycursor.rowcount, "record inserted.")


    yellow = Label(order, text="Order details", bg="#f99406", fg="White", font=('Times New Roman', 30, "bold", "italic"))
    yellow.grid(row=0, column=0, ipady=10, columnspan=10, ipadx=250)

    #  -- Order id --
    oid = Label(order, text='Order Id: ', font=('Times New Roman', 24), bg="#2b3d4f", fg="white")
    oid.grid(row=1, column=0, padx=15, pady=15)

    user_input_oid = StringVar()

    user_field_fid = Entry(order, textvariable=user_input_oid, font=('Times New Roman', 18))
    user_field_fid.grid(row=1, column=1, padx=15, pady=15)

    # -- Total Cost --
    totcost = Label(order, text='Total Cost: ', font=('Times New Roman', 24), bg="#2b3d4f", fg="white")
    totcost.grid(row=2, column=0, padx=15, pady=15)

    user_input_totcost = StringVar()

    user_field_totcost = Entry(order, textvariable=user_input_totcost, font=('Times New Roman', 18))
    user_field_totcost.grid(row=2, column=1, padx=15, pady=15)

    # -- Food id --
    fid = Label(order, text='Food Id: ', font=('Times New Roman', 24), bg="#2b3d4f", fg="white")
    fid.grid(row=3, column=0, padx=15, pady=15)

    user_input_fid = StringVar()

    user_field_fid = Entry(order, textvariable=user_input_fid, font=('Times New Roman', 18))
    user_field_fid.grid(row=3, column=1, padx=15, pady=15)

    # -- Drink Id --
    did = Label(order, text='Drink Id: ', font=('Times New Roman', 24), bg="#2b3d4f", fg="white")
    did.grid(row=4, column=0, padx=15, pady=15)

    user_input_did = StringVar()

    user_field_did = Entry(order, textvariable=user_input_did, font=('Times New Roman', 18))
    user_field_did.grid(row=4, column=1, padx=15, pady=15)

    # -- delivery id --
    delid = Label(order, text='Delivery Id: ', font=('Times New Roman', 24), bg="#2b3d4f", fg="white")
    delid.grid(row=5, column=0, padx=15, pady=15)

    user_input_delid = StringVar()

    user_field_delid = Entry(order, textvariable=user_input_delid, font=('Times New Roman', 18))
    user_field_delid.grid(row=5, column=1, padx=15, pady=15)


    def verify_details(a, b, c, d, e):
        if (len(a) == 0 and len(b) == 0 and len(c) == 0 and len(d) == 0 and len(e) == 0):
            messagebox.showerror("Error", "\tFields can't be empty\nEnter properly!")
            return False

        elif len(a) == 0:
            messagebox.showerror("Error", "ORDER ID field is missing")
            return False

        elif len(b) == 0:
            messagebox.showerror("Error", "TOTAL COST field is missing")
            return False

        elif len(c) == 0:  #stuti foreign key Restaurant_Management.ORDER TABLE
            messagebox.showerror("Error", "Restaurant_Management.ORDER Id field is missing")
            return False

        elif len(d) == 0:
            messagebox.showerror("Error", "DRINK ID field is missing")
            return False

        elif len(e) == 0:
            messagebox.showerror("Error", "Delivery ID field is missing")
            return False
        try:
            val = float(b)
            if (val < 0):
                messagebox.showerror("Error", "CTOTAL COST can't be negative")
                return False

            if (val == 0):
                messagebox.showerror("Error", "TOTAL COST can't be zero")
                return False

        except:
            messagebox.showerror("Error", "Enter only numerical value!")
            return False


        return True

    def Add_to_order(a, b, c, d, e):
        adding = "Insert into Restaurant_Management.ORDER (ORDID,TOTALCOST,FOODID,DRINKID,DELID) values(%s,%s,%s,%s,%s)"
        entry = (a, b, c, d, e)
        mycursor.execute(adding, entry)
        myb.commit()
        print(mycursor.rowcount, "record inserted.")

    def Add_order():
        a = user_input_oid.get().strip()
        b = user_input_totcost.get().strip()
        c = user_input_fid.get().strip()
        d = user_input_did.get().strip()
        e = user_input_delid.get().strip()

        if verify_details(a, b, c, d, e):
            m = ID_primary(a)
            if m:
                Add_to_order(a, b, c, d, e)
                Clear_order()
                print_treev()

    def ID_primary(a):
        mycursor.execute("SELECT ORDID FROM Restaurant_Management.ORDER")
        order = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            order.append(s)


        mycursor.execute("SELECT FOODID FROM FOOD")
        food = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            food.append(s)

        mycursor.execute("SELECT DRINKID FROM DRINKS")
        drink = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            drink.append(s)


        mycursor.execute("SELECT DELID FROM DELIVERY")
        delivery = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            delivery.append(s)

        o = 0
        f = 0
        dr = 0
        de = 0

        a = user_input_oid.get().strip()
        b = user_input_fid.get().strip()
        c = user_input_did.get().strip()
        d = user_input_delid.get().strip()

        print(order)
        for i in order:
            if a == i:
                print(i)
                messagebox.showerror("Error", "ORDER ID Already Exist")
                return False
            else:
                f = f + 1

        if b not in food:
            messagebox.showerror("Error", "Food ID Doesn't Exist")
            return False

        if c not in drink:
            messagebox.showerror("Error", "Drink ID Doesn't Exist")
            return False

        if d not in delivery:
            messagebox.showerror("Error", "Delivery ID Doesn't Exist")
            return False

        return True

        # if f == len(order):
        #     for i in order:
        #         if a == i:
        #             print(i)
        #             for i in food:
        #                 if b == i:
        #                     print(i)
        #                     for i in drink:
        #                         if c == i:
        #                             print(i)
        #                             for i in delivery:
        #                                 if d == i:
        #                                     print(i)
        #                                     return True
        #                                 else:
        #                                     de = de + 1
        #                             if de == len(delivery):
        #                                 messagebox.showerror("Error", "Delivery ID Doesn't Exist")
        #                                 return False
        #                         else:
        #                             dr = dr + 1
        #                     if dr == len(drink):
        #                         messagebox.showerror("Error", "Drink ID Doesn't Exist")
        #                         return False
        #                 else:
        #                     f = f + 1
        #             if f == len(food):
        #                 messagebox.showerror("Error", "Food ID Doesn't Exist")
        #                 return False
        #         else:
        #             o = o + 1

        #     if o == len(order):
        #         # messagebox.showerror("Error", "Order ID Doesn't Exist")
        #         return True


    def ID_primary_order(a):
        mycursor.execute("SELECT ORDID FROM Restaurant_Management.ORDER")
        order = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            order.append(s)

        mycursor.execute("SELECT FOODID FROM FOOD")
        food = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            food.append(s)

        mycursor.execute("SELECT DRINKID FROM DRINKS")
        drink = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            drink.append(s)


        mycursor.execute("SELECT DELID FROM DELIVERY")
        delivery = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            delivery.append(s)

        o = 0
        f = 0
        dr = 0
        de = 0

        a = user_input_oid.get().strip()
        b = user_input_fid.get().strip()
        c = user_input_did.get().strip()
        d = user_input_delid.get().strip()

        for i in order:
            if a == i:
                print(i)
                for i in food:
                    if b == i:
                        print(i)
                        for i in drink:
                            if c == i:
                                print(i)
                                for i in delivery:
                                    if d == i:
                                        print(i)
                                        return True
                                    else:
                                        de = de + 1
                                if de == len(delivery):
                                    messagebox.showerror("Error", "Delivery ID Doesn't Exist")
                                    return False
                            else:
                                dr = dr + 1
                        if dr == len(drink):
                            messagebox.showerror("Error", "Drink ID Doesn't Exist")
                            return False
                    else:
                        f = f + 1
                if f == len(food):
                    messagebox.showerror("Error", "Food ID Doesn't Exist")
                    return False
            else:
                o = o + 1
        if o == len(order):
            messagebox.showerror("Error", "Order ID Doesn't Exist")
            return False

    def update_from_order(a, b, c, d, e, a1):
        n1 = "UPDATE Restaurant_Management.ORDER SET ordid = %s ,totalcost = %s ,foodid = %s ,drinkid = %s, delid = %s where ordid = %s order by ordid;"
        val = (a, b, c, d, e, a1)
        mycursor.execute(n1, val)
        myb.commit()

    def Update_order():
        a = user_input_oid.get().strip()
        b = user_input_totcost.get().strip()
        c = user_input_fid.get().strip()
        d = user_input_did.get().strip()
        e = user_input_delid.get().strip()

        if verify_details(a, b, c, d, e):
            m = ID_primary_order(a)
            if m:
                update_from_order(a, b, c, d, e, a)
                Clear_order()
                print_treev()

    def delete_from_order(a):
        n = "DELETE FROM Restaurant_Management.ORDER WHERE ORDID = " + str(a) + " order by ORDID"
        mycursor.execute(n)
        myb.commit()

    def ID_delete_order(a):
        mycursor.execute("SELECT ORDID FROM Restaurant_Management.ORDER")
        ord = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            ord.append(s)

        f=0
        for i in ord:
            if a == i:
                print(i)
                return True
            else:
                f = f + 1

        if f == len(ord):
            messagebox.showerror("Error", "Order ID Doesn't Exist")
            return False

    def Delete_order():
        a = user_input_oid.get()
        m = ID_delete_order(a)
        if m:
            delete_from_order(a)
            Clear_order()
            print_treev()


    def Clear_order():
        for records in treev.get_children():
            treev.delete(records)

    def print_treev():
        mycursor.execute("SELECT * FROM Restaurant_Management.ORDER")
        total = []
        for x in mycursor:
            print(x)
            total.append(x)

        for i in total:
            a, b, c, d, e= i
            data = [a, b, c, d, e]
            treev.insert('', 'end', values=data)



    Button(order, text='Add', bg="red", fg="white", font=('Times New Roman', 18),command=Add_order).place(x=100, y=480)
    Button(order, text='Update', bg="red", fg="white", font=('Times New Roman', 18),command=Update_order).place(x=200, y=480)
    Button(order, text='Delete', bg="red", fg="white", font=('Times New Roman', 18),command=Delete_order).place(x=330, y=480)
    Button(order, text='Clear', bg="red", fg="white", font=('Times New Roman', 18),command=Clear_order).place(x=450, y=480)
    Button(order, text='<<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.portal(root)).place(x=230, y=600)
    Button(order, text='<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.rest(root)).place(
        x=300, y=600)
    tree = ttk.Frame(panedwindow, width=400, height=400, relief=SUNKEN)
    panedwindow.add(order, weight=1)
    panedwindow.add(tree, weight=4)

    TVList = ['Order ID', 'Total Cost', 'Food ID', 'Drink ID', 'Delivery Id']
    treev = Treeview(tree, column=TVList, show='headings')

    # for giving column headings

    for i in TVList:
        treev.column(i, width=160)
        treev.heading(i, text=i.title())
    treev.grid(ipadx=0, padx=20)
    root.mainloop()
