from tkinter import *
from tkinter import ttk
from tkinter.ttk import Panedwindow
from tkinter import Tk, messagebox
import mysql.connector
import PortalRest

myb = mysql.connector.connect(host="localhost", user="root", passwd="Justice", database="Restaurant_Management")

# Object return points there
mycursor = myb.cursor()

def cuisine(k):
    k.destroy()
    root = Tk()
    root.state('zoomed')


    # App Title
    root.title("Restaurant Management ")
    Label(root, text="Cusine Details").pack()

    # Create Panedwindow
    panedwindow = Panedwindow(root, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)

    # Create Frames
    cuisine = Frame(panedwindow, width=550, height=640, relief=SUNKEN)
    tree = Frame(panedwindow, width=600, height=300, relief=SUNKEN)

    panedwindow.add(cuisine, weight=1)
    panedwindow.add(tree, weight=4)

    cuisine.config(bg="#2b3d4f")

    yellow = Label(cuisine, text="Cuisine Details", bg="#f99406", fg="White",
                   font=('Times New Roman', 30, "bold", "italic"))
    yellow.grid(row=0, column=0, ipady=10, columnspan=10, ipadx=190, padx=0)

    extra = Label(cuisine, text="   ", bg="#2b3d4f")
    extra.grid(row=1, pady=10)

    #  -- cuisine id --
    cuisineId = Label(cuisine, text='Cuisine Id: ', font=('Times New Roman', 20), bg="#2b3d4f", fg="white")
    cuisineId.grid(row=2, column=0, padx=15, pady=65)

    user_input_cuisineId = StringVar()

    user_field_cuisineId = Entry(cuisine, textvariable=user_input_cuisineId, font=('Times New Roman', 18))
    user_field_cuisineId.grid(row=2, column=1, padx=15, pady=15)

    # -- cuisine Name --
    cname = Label(cuisine, text='Cuisine Name: ', font=('Times New Roman', 20), bg="#2b3d4f", fg="white")
    cname.grid(row=3, column=0, padx=15, pady=15)

    user_input_cname = StringVar()

    user_field_cname = Entry(cuisine, textvariable=user_input_cname, font=('Times New Roman', 18))
    user_field_cname.grid(row=3, column=1, padx=15, pady=15)


    def verify_cuisine(a, b):
        if len(b) == 0 and len(a) == 0:
            messagebox.showerror("Error", "\tFields can't be empty\nEnter ID and Name properly!")
            return False

        elif (len(a) == 0):
            messagebox.showerror("Error", "Cuisine ID filed is missing")
            return False

        elif (len(b) == 0):
            messagebox.showerror("Error", "Cuisine Name filed is missing")
            return False

        elif (b.isalpha() != True):
            messagebox.showerror("Error", "Cuisine Name can't contain Numbers or special characters")
            return False

        return True


    def ID_primary(a):
        mycursor.execute("SELECT CUISINEID FROM CUISINE")
        datab = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            datab.append(s)

        c = 0
        for i in datab:
            if a == i:
                print(i)
                messagebox.showerror("Error", "Cuisine ID Already Exist")
                return False
            else:
                c = c + 1

        if c == len(datab):
            return True


    def Add_to_cuisine(a, b):
        adding = "Insert into cuisine (CUISINEID,CUISINENAME) values(%s,%s)"
        entry = (a, b)
        mycursor.execute(adding, entry)
        myb.commit()
        print(mycursor.rowcount, "record inserted.")


    def Add_cuisine():
        a = user_input_cuisineId.get()
        b = user_input_cname.get().strip()

        if verify_cuisine(a, b):
            m = ID_primary(a)
            if m:
                Add_to_cuisine(a, b)
                Clear_cuisine()
                print_treev()


    def Update_cuisine():
        a = user_input_cuisineId.get()
        b = user_input_cname.get().strip()
        if verify_cuisine(a, b):
            m = ID_primary_cuisine(a)
            if m:
                update_from_cuisine(a, b, a)
                Clear_cuisine()
                print_treev()


    def ID_primary_cuisine(a):
        mycursor.execute("SELECT CUISINEID FROM CUISINE")
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
            messagebox.showerror("Error", "Cuisine ID Doesn't Exist")
            return False


    def update_from_cuisine(a, b, a1):
        n1 = "UPDATE cuisine SET cuisineid = %s ,cuisinename = %s where cuisineid = %s order by cuisineid;"
        val = (a, b, a1)
        mycursor.execute(n1, val)
        myb.commit()

    def delete_from_cuisine(a):
        n = "DELETE FROM CUISINE WHERE cuisineid = " + str(a) + " order by cuisineid"
        mycursor.execute(n)
        myb.commit()

    def Delete_cuisine():
        a = user_input_cuisineId.get()
        m = ID_primary_cuisine(a)
        if m:
            delete_from_cuisine(a)
            Clear_cuisine()
            print_treev()


    def Clear_cuisine():
        for records in treev.get_children():
            treev.delete(records)


    def print_treev():
        mycursor.execute("SELECT * FROM CUISINE")
        total = []
        for x in mycursor:
            print(x)
            total.append(x)

        for i in total:
            x, y = i
            data = [x, y]
            treev.insert('', 'end', values=data)


    Button(cuisine, text='Add', bg="red", fg="white", font=('Times New Roman', 18), command=Add_cuisine).place(x=80, y=400)
    Button(cuisine, text='Update', bg="red", fg="white", font=('Times New Roman', 18), command=Update_cuisine).place(x=180,
                                                                                                                     y=400)
    Button(cuisine, text='Delete', bg="red", fg="white", font=('Times New Roman', 18), command=Delete_cuisine).place(x=310,
                                                                                                                     y=400)
    Button(cuisine, text='Clear', bg="red", fg="white", font=('Times New Roman', 18), command=Clear_cuisine).place(x=430,
                                                                                                                   y=400)
    Button(cuisine, text='<<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.portal(root)).place(x=230, y=500)
    Button(cuisine, text='<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.rest(root)).place(
        x=300, y=500)
    TVList = ['Cuisine Id', 'Cuisine Name']

    treev = ttk.Treeview(tree, column=TVList, show='headings', height=5)
    treev['columns'] = ['Cuisine Id', 'Cuisine Name']
    # for giving column headings

    for i in TVList:
        treev.column(i, width=250)
        treev.heading(i, text=i.title())
    treev.grid(padx=60, pady=20, ipady=100)

    # Calling Main()

    root.mainloop()
