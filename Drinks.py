from tkinter import *
from tkinter import ttk
from tkinter.ttk import Panedwindow
from tkinter import Tk, messagebox
import mysql.connector
import PortalRest
myb = mysql.connector.connect(host="localhost", user="root", passwd="Justice", database="Restaurant_Management")

# Object return points there
mycursor = myb.cursor()

def drinks(k):
    k.destroy()
    root = Tk()
    root.state('zoomed')

    # App Title
    root.title("Restaurant Management ")
    Label(root, text="Drinks Details").pack()

    # Create Panedwindow
    panedwindow = Panedwindow(root, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)

    # Create Frames
    drinks = Frame(panedwindow, width=550, height=640, relief=SUNKEN)
    tree = Frame(panedwindow, width=600, height=300, relief=SUNKEN)

    panedwindow.add(drinks, weight=1)
    panedwindow.add(tree, weight=4)

    drinks.config(bg="#2b3d4f")
    yellow = Label(drinks, text="Drinks Details", bg="#f99406", fg="White", font=('Times New Roman', 30, "bold", "italic"))
    yellow.grid(row=0, column=0, ipady=10, columnspan=10, ipadx=240)

    extra = Label(drinks, text="   ", bg="#2b3d4f")
    extra.grid(row=1, pady=10)

    #  -- drinks id --
    dId = Label(drinks, text='Drink Id: ', font=('Times New Roman', 24), bg="#2b3d4f", fg="white")
    dId.grid(row=2, column=0, padx=15, pady=15)

    user_input_dId = StringVar()

    user_field_dId = Entry(drinks, textvariable=user_input_dId, font=('Times New Roman', 18))
    user_field_dId.grid(row=2, column=1, padx=15, pady=15)

    # -- drinks Name --
    dname = Label(drinks, text='Drink Name: ', font=('Times New Roman', 24), bg="#2b3d4f", fg="white")
    dname.grid(row=3, column=0, padx=15, pady=15)

    user_input_dname = StringVar()

    user_field_dname = Entry(drinks, textvariable=user_input_dname, font=('Times New Roman', 18))
    user_field_dname.grid(row=3, column=1, padx=15, pady=15)

    # -- Price --
    dprice = Label(drinks, text='Price: ', font=('Times New Roman', 24), bg="#2b3d4f", fg="white")
    dprice.grid(row=4, column=0, padx=15, pady=15)

    user_input_dprice = StringVar()

    user_field_dprice = Entry(drinks, textvariable=user_input_dprice, font=('Times New Roman', 18))
    user_field_dprice.grid(row=4, column=1, padx=15, pady=15)

    # -- Size --
    dsize = Label(drinks, text='Size: ', font=('Times New Roman', 24), bg="#2b3d4f", fg="white")
    dsize.grid(row=5, column=0, padx=15, pady=15)

    # drop down
    user_input_dsize = StringVar(drinks)
    option = ["Small", "Medium", "Large"]
    drop = OptionMenu(drinks, user_input_dsize, *option)
    drop.config(width=18, font=('Times New Roman', 16), bg="#1bb6fe", fg="white")
    user_input_dsize.set("Select one")
    drop.grid(row=5, column=1, padx=15, pady=15)


    def ID_primary():
        mycursor.execute("SELECT DRINKID FROM DRINKS")
        datab = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            datab.append(s)

        c = 0
        a = user_input_dId.get().strip()

        for i in datab:
            if a == i:
                print(i)
                messagebox.showerror("Error", "Drink ID Already Exist")
                return False
            else:
                c = c + 1

        if c == len(datab):
            return True


    def verify_drinks(a, b, c, d):
        if len(b) == 0 and len(c) == 0 and len(a) == 0 and len(d) == "Select one":
            messagebox.showerror("Error", "\tFields can't be empty\nAdd ID, Name,Size or Price properly!")
            return False

        elif (len(a) == 0):
            messagebox.showerror("Error", "Drink ID filed is missing")
            return False

        elif (len(b) == 0):
            messagebox.showerror("Error", "Drink Name filed is missing")
            return False

        elif (b.isalpha() != True):
            messagebox.showerror("Error", "Drink Name can't contain Numbers or special characters")
            return False

        elif (len(c) == 0):
            messagebox.showerror("Error", "Drink Price filed is missing")
            return False

        elif (d == "Select one"):
            messagebox.showerror("Error", "Drink Size is missing")
            return False

        val = 0
        try:
            val = float(c)
            if val < 0:
                messagebox.showerror("Error", "Price can't be negative")
                return False

        except:
            messagebox.showerror("Error", "Enter only numerical value!")
            return False

        return True


    def Add_drinks():
        a = user_input_dId.get()
        b = user_input_dname.get().strip()
        c = user_input_dprice.get().strip()
        d = user_input_dsize.get().strip()

        if verify_drinks(a, b, c, d):
            m = ID_primary()
            if m:
                Add_to_drinks(a, b, c, d)
                clear_from_drinks()
                print_treev()


    def Add_to_drinks(dId, dname, dprice, dsize):
        adding = "Insert into drinks (DRINKID,DNAME,PRICE,SIZE) values(%s,%s,%s,%s)"
        entry = (dId, dname, dprice, dsize)
        mycursor.execute(adding, entry)
        myb.commit()
        print(mycursor.rowcount, "record inserted.")


    # --Add--
    def ID_primary_drink(a):
        mycursor.execute("SELECT DRINKID FROM DRINKS")
        datab = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            datab.append(s)

        c = 0
        for i in datab:
            if a == i:
                print(i)
                return True
            else:
                c = c + 1

        if c == len(datab):
            messagebox.showerror("Error", "Drink ID Doesn't Exist")
            return False


    def update_from_drinks(a, b, c, d, a1):
        n1 = "UPDATE drinks SET drinkid = %s ,dname = %s ,price = %s ,size = %s  where drinkid = %s order by drinkid;"
        val = (a, b, c, d, a1)
        mycursor.execute(n1, val)
        myb.commit()


    def update_drinks():
        a = user_input_dId.get()
        b = user_input_dname.get().strip()
        c = user_input_dprice.get().strip()
        d = user_input_dsize.get().strip()
        if verify_drinks(a, b, c, d):
            m = ID_primary_drink(a)
            if m:
                update_from_drinks(a, b, c, d, a)
                clear_from_drinks()
                print_treev()



    def delete_from_drinks(a):
        n = "DELETE FROM DRINKS WHERE drinkid = " + str(a) + " order by drinkid"
        mycursor.execute(n)
        myb.commit()


    def delete_drinks():
        a = user_input_dId.get()
        # if verify_drinks():
        m = ID_primary_drink(a)
        if m:
            delete_from_drinks(a)
            clear_from_drinks()
            print_treev()


    def print_treev():
        mycursor.execute("SELECT * FROM DRINKS")
        total = []
        for x in mycursor:
            print(x)
            total.append(x)

        for i in total:
            x, y, z, m = i
            data = [x, y, z, m]
            treev.insert('', 'end', values=data)


    def clear_from_drinks():
        for records in treev.get_children():
            treev.delete(records)


    Button(drinks, text='Add', bg="red", fg="white", font=('Times New Roman', 18), command=Add_drinks).place(x=80, y=450)
    Button(drinks, text='Update', bg="red", fg="white", font=('Times New Roman', 18), command=update_drinks).place(x=180,
                                                                                                                   y=450)
    Button(drinks, text='Delete', bg="red", fg="white", font=('Times New Roman', 18), command=delete_drinks).place(x=310,
                                                                                                                   y=450)
    Button(drinks, text='Clear', bg="red", fg="white", font=('Times New Roman', 18), command=clear_from_drinks).place(x=430,
                                                                                                                      y=450)
    Button(drinks, text='<<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.portal(root)).place(x=230, y=550)
    Button(drinks, text='<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.rest(root)).place(
        x=300, y=550)
    TVList = ['DrinkId', 'Drink Name', 'Price', 'Size']

    treev = ttk.Treeview(tree, column=TVList, show='headings', height=5)
    treev['columns'] = ['DrinkId', 'Drink Name', 'Price', 'Size']
    # for giving column headings

    for i in TVList:
        treev.column(i, width=120)
        treev.heading(i, text=i.title())

    treev.grid(padx=12, pady=10, ipadx=20, ipady=100)

    # Calling Main()
    root.mainloop()
