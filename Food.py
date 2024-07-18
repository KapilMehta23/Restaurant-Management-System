from tkinter import *
from tkinter import ttk
from tkinter.ttk import Panedwindow
from tkinter import Tk, messagebox
import mysql.connector
import PortalRest
myb = mysql.connector.connect(host="localhost", user="root", passwd="Justice", database="Restaurant_Management")

# Object return points there
mycursor = myb.cursor()

def food(k):
    k.destroy()
    root = Tk()
    root.state('zoomed')


    # App Title
    root.title("Restaurant Management ")
    Label(root, text="Food Details").pack()

    # Create Panedwindow
    panedwindow = Panedwindow(root, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)

    # Create Frames
    food = Frame(panedwindow, width=550, height=640, relief=SUNKEN)
    tree = Frame(panedwindow, width=600, height=300, relief=SUNKEN)
    panedwindow.add(food, weight=1)
    panedwindow.add(tree, weight=4)

    food.config(bg="#2b3d4f")
    yellow = Label(food, text="Food Details", bg="#f99406", fg="White", font=('Times New Roman', 30, "bold", "italic"))
    yellow.grid(row=0, column=0, ipady=10, columnspan=10, ipadx=200)

    #  -- food id --
    fid = Label(food, text='Food Id: ', font=('Times New Roman', 20), bg="#2b3d4f", fg="white")
    fid.grid(row=1, column=0, padx=15, pady=15)

    user_input_fid = StringVar()

    user_field_fid = Entry(food, textvariable=user_input_fid, font=('Times New Roman', 18))
    user_field_fid.grid(row=1, column=1, padx=15, pady=15)

    # -- Food Name --
    fname = Label(food, text='Food Name: ', font=('Times New Roman', 20), bg="#2b3d4f", fg="white")
    fname.grid(row=2, column=0, padx=15, pady=15)

    user_input_fname = StringVar()

    user_field_fname = Entry(food, textvariable=user_input_fname, font=('Times New Roman', 18))
    user_field_fname.grid(row=2, column=1, padx=15, pady=15)

    # -- Price --
    fprice = Label(food, text='Price: ', font=('Times New Roman', 20), bg="#2b3d4f", fg="white")
    fprice.grid(row=3, column=0, padx=15, pady=15)

    user_input_fprice = StringVar()

    user_field_fprice = Entry(food, textvariable=user_input_fprice, font=('Times New Roman', 18))
    user_field_fprice.grid(row=3, column=1, padx=15, pady=15)

    # -- Quantity --
    fqty = Label(food, text='Quantity: ', font=('Times New Roman', 20), bg="#2b3d4f", fg="white")
    fqty.grid(row=4, column=0, padx=15, pady=15)

    user_input_fqty = StringVar()

    user_field_fqty = Entry(food, textvariable=user_input_fqty, font=('Times New Roman', 18))
    user_field_fqty.grid(row=4, column=1, padx=15, pady=15)

    # -- cusine id --
    cusineId = Label(food, text='Cusine Id: ', font=('Times New Roman', 20), bg="#2b3d4f", fg="white")
    cusineId.grid(row=5, column=0, padx=15, pady=15)

    user_input_cusineId = StringVar()

    user_field_cusineId = Entry(food, textvariable=user_input_cusineId, font=('Times New Roman', 18))
    user_field_cusineId.grid(row=5, column=1, padx=15, pady=15)

    # -- chef id --
    chefId = Label(food, text='Chef Id: ', font=('Times New Roman', 20), bg="#2b3d4f", fg="white")
    chefId.grid(row=6, column=0, padx=15, pady=15)

    user_input_chefId = StringVar()

    user_field_chefId = Entry(food, textvariable=user_input_chefId, font=('Times New Roman', 18))
    user_field_chefId.grid(row=6, column=1, padx=15, pady=15)


    def verify_food(a, b, c, d, e, f):
        if (len(a) == 0 and len(b) == 0 and len(c) == 0 and len(d) == 0 and len(e) == 0 and len(f) == 0):
            messagebox.showerror("Error", "\nFields can't be empty\nEnter properly!")
            return False

        elif len(a) == 0:
            messagebox.showerror("Error", "Food ID filed is missing")
            return False

        elif len(b) == 0:
            messagebox.showerror("Error", "Food Name filed is missing")
            return False

        elif (b.isalpha() != True):
            messagebox.showerror("Error", "Food Name can't contain Numbers or special characters")
            return False

        elif len(c) == 0:
            messagebox.showerror("Error", "Price filed is missing")
            return False

        elif (c.isdigit() == False):
            messagebox.showerror("Error", "Price should only contain numbers")
            return False

        elif len(d) == 0:
            messagebox.showerror("Error", "Quantity filed is missing")
            return False

        elif (d.isdigit() == False):
            messagebox.showerror("Error", "Quantity should only contain numbers")
            return False

        elif len(e) == 0:
            messagebox.showerror("Error", "Cuisine ID filed is missing")
            return False

        elif len(f) == 0:
            messagebox.showerror("Error", "Chef ID filed is missing")
            return False

        try:
            val = float(c)
            val1 = float(d)
            if (val < 0):
                messagebox.showerror("Error", "Price can't be negative")
                return False

            if (val == 0):
                messagebox.showerror("Error", "Price can't be zero")
                return False

            if (val1 < 0):
                messagebox.showerror("Error", "Quantity can't be negative")
                return False

            if (val1 == 0):
                messagebox.showerror("Error", "Quantity can't be zero")
                return False

        except:
            messagebox.showerror("Error", "Enter only numerical value!")
            return False

        return True


    def ID_primary():
        mycursor.execute("SELECT FOODID FROM FOOD")
        foodl = []

        for x in mycursor:
            s = str(x)[-1:1].strip(',')
            foodl.append(s)

        mycursor.execute("SELECT CHEFID FROM CHEF")
        chef = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            chef.append(s)

        mycursor.execute("SELECT CUISINEID FROM CUISINE")
        cuisine = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            cuisine.append(s)
        f = 0
        cf = 0
        cu = 0
        a = user_field_fid.get().strip()
        b = user_input_chefId.get().strip()
        c = user_field_cusineId.get().strip()

        for i in foodl:
            if a == i:
                print(i)
                messagebox.showerror("Error", "Food ID Already Exist")
                return False
            else:
                f = f + 1

        if f == len(foodl):
            for i in chef:
                if b == i:
                    print(i)
                    for i in cuisine:
                        if c == i:
                            print(i)
                            return True
                        else:
                            cu = cu + 1
                    if cu == len(cuisine):
                        messagebox.showerror("Error", "Cuisine ID Doesn't Exist")
                        return False
                else:
                    cf = cf + 1
            if cf == len(chef):
                messagebox.showerror("Error", "Chef ID Doesn't Exist")
                return False


    def Add_to_food(a, b, c, d, e, f):
        adding = "Insert into food (FOODID,FOODNAME,PRICE,QUANTITY,CUISINEID,CHEFID) values(%s,%s,%s,%s,%s,%s)"
        entry = (a, b, c, d, e, f)
        mycursor.execute(adding, entry)
        myb.commit()
        print(mycursor.rowcount, "record inserted.")


    def Add_food():
        a = user_field_fid.get().strip()
        b = user_input_fname.get().strip()
        c = user_field_fprice.get().strip()
        d = user_field_fqty.get().strip()
        e = user_field_cusineId.get().strip()
        f = user_field_chefId.get().strip()

        if verify_food(a, b, c, d, e, f):
            m = ID_primary()
            if m:
                Add_to_food(a, b, c, d, e, f)
                Clear_food()
                print_treev()


    def ID_primary_food():
        mycursor.execute("SELECT FOODID FROM FOOD")
        food = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            food.append(s)

        mycursor.execute("SELECT CHEFID FROM CHEF")
        chef = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            chef.append(s)

        mycursor.execute("SELECT CUISINEID FROM CUISINE")
        cuisine = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            cuisine.append(s)
        f = 0
        cf = 0
        cu = 0
        a = user_field_fid.get().strip()
        b = user_input_chefId.get().strip()
        c = user_field_cusineId.get().strip()

        for i in food:
            if a == i:
                print(i)
                for i1 in chef:
                    if b == i1:
                        print(i1)
                        for i2 in cuisine:
                            if c == i2:
                                print(i)
                                return True
                            else:
                                cu = cu + 1
                        if cu == len(cuisine):
                            messagebox.showerror("Error", "Cuisine ID Doesn't Exist")
                            return False
                    else:
                        cf = cf + 1
                if cf == len(chef):
                    messagebox.showerror("Error", "Chef ID Doesn't Exist")
                    return False
            else:
                f = f + 1

        if f == len(food):
            messagebox.showerror("Error", "Food ID Doesn't Exist")
            return False


    def update_from_food(a, b, c, d, e, f, a1):
        n1 = "UPDATE food SET foodid = %s ,foodname = %s ,price = %s ,quantity = %s, cuisineid = %s ,chefid = %s where foodid = %s order by foodid;"
        val = (a, b, c, d, e, f, a1)
        mycursor.execute(n1, val)
        myb.commit()


    def Update_food():
        a = user_field_fid.get().strip()
        b = user_input_fname.get().strip()
        c = user_field_fprice.get().strip()
        d = user_field_fqty.get().strip()
        e = user_field_cusineId.get().strip()
        f = user_field_chefId.get().strip()

        if verify_food(a, b, c, d, e, f):
            m = ID_primary_food()
            if m:
                update_from_food(a, b, c, d, e, f, a)
                Clear_food()
                print_treev()


    def delete_from_food(a):
        n = "DELETE FROM FOOD WHERE foodid = " + str(a) + " order by foodid"
        mycursor.execute(n)
        myb.commit()


    def ID_delete_food(a):
        mycursor.execute("SELECT FOODID FROM FOOD")
        food = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            food.append(s)

        f = 0
        for i in food:
            if a == i:
                print(i)
                return True
            else:
                f = f + 1

        if f == len(food):
            messagebox.showerror("Error", "Food ID Doesn't Exist")
            return False


    def Delete_food():
        a = user_field_fid.get()
        m = ID_delete_food(a)
        if m:
            delete_from_food(a)
            Clear_food()
            print_treev()


    def Clear_food():
        for records in treev.get_children():
            treev.delete(records)


    def print_treev():
        mycursor.execute("SELECT * FROM FOOD")
        total = []
        for x in mycursor:
            print(x)
            total.append(x)

        for i in total:
            a, b, c, d, e, f = i
            data = [a, b, c, d, e, f]
            treev.insert('', 'end', values=data)


    Button(food, text='Add', bg="red", fg="white", font=('Times New Roman', 18), command=Add_food).place(x=80, y=500)
    Button(food, text='Update', bg="red", fg="white", font=('Times New Roman', 18), command=Update_food).place(x=180, y=500)
    Button(food, text='Delete', bg="red", fg="white", font=('Times New Roman', 18), command=Delete_food).place(x=310, y=500)
    Button(food, text='Clear', bg="red", fg="white", font=('Times New Roman', 18), command=Clear_food).place(x=430, y=500)
    Button(food, text='<<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.portal(root)).place(x=230, y=600)
    Button(food, text='<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.rest(root)).place(
        x=300, y=600)
    TVList = ['FoodId', 'Food Name', 'Price', 'Quantity', 'Cusine Id', 'Chef Id']

    treev = ttk.Treeview(tree, column=TVList, show='headings', height=5)
    treev['columns'] = ['FoodId', 'Food Name', 'Price', 'Quantity', 'Cusine Id', 'Chef Id']
    # for giving column headings

    for i in TVList:
        treev.column(i, width=100)
        treev.heading(i, text=i.title())
    treev.grid(padx=12, pady=10, ipadx=15, ipady=100)

    # Calling Main()

    root.mainloop()