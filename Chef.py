# Create app using with separating widget
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Panedwindow
from tkinter import Tk, messagebox
import mysql.connector
import PortalRest
myb = mysql.connector.connect(host="localhost", user="root", passwd="Justice", database="Restaurant_Management")

# Object return points there
mycursor = myb.cursor()
    # from tkinter import ttk

def chef(k):
    k.destroy()
    root = Tk()
    # App Title
    root.title("Python GUI Application ")
    root.state('zoomed')
    root.config(background='#abdbe3')
    Label(root, text="RESTAURANT DATABASE SYSTEM", font=('Times New Roman', 24, "bold"), bg='#abdbe3').pack(pady=10)
    # Create Panedwindow
    panedwindow = Panedwindow(root, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)
    # Create Frams
    window = Frame(panedwindow, width=500, height=640)
    tree = Frame(panedwindow, width=600, height=600, relief=SUNKEN)
    panedwindow.add(window, weight=1)
    panedwindow.add(tree, weight=6)

    window.config(background="#2b3d4f")

    Label(window, text="CHEF", bg="#f99406", fg="White", font=('Times New Roman', 30, "bold")).grid(row=0, column=0,
                                                                                                    columnspan=10, ipady=7,
                                                                                                    ipadx=300)
    Label(window, text='Chef Name:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=5, column=2)
    Label(window, text='Chef Id:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=6, column=2)
    Label(window, text='Emp Id:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=7, column=2)
    Label(window, text='Email Id:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=8, column=2)
    Label(window, text='Address :', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=9, column=2)
    Label(window, text='Spec:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=10, column=2)
    Label(window, text='Phone No:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=11, column=2)
    Label(window, text='Salary:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=12, column=2)

    chefname = StringVar()
    user_field = Entry(window, textvariable=chefname, font=('Times New Roman', 18)).grid(row=5, column=4)
    chefid = StringVar()
    user_field = Entry(window, textvariable=chefid, font=('Times New Roman', 18)).grid(row=6, column=4)
    empid = StringVar()
    user_field = Entry(window, textvariable=empid, font=('Times New Roman', 18)).grid(row=7, column=4)
    email = StringVar()
    user_field = Entry(window, textvariable=email, font=('Times New Roman', 18)).grid(row=8, column=4)
    address = StringVar()
    user_field = Entry(window, textvariable=address, font=('Times New Roman', 18)).grid(row=9, column=4)
    spec = StringVar()
    user_field = Entry(window, textvariable=spec, font=('Times New Roman', 18)).grid(row=10, column=4)
    phone = StringVar()
    user_field = Entry(window, textvariable=phone, font=('Times New Roman', 18)).grid(row=11, column=4)
    salary = StringVar()
    user_field = Entry(window, textvariable=salary, font=('Times New Roman', 18)).grid(row=12, column=4)


    def Add_chef():
        a = chefid.get().strip()
        b = chefname.get().strip()
        c = address.get().strip()
        d = phone.get().strip()
        e = spec.get().strip()
        f = empid.get().strip()
        g = email.get().strip()
        h = salary.get().strip()

        if verify_chef(a, b, c, d, e, f, g, h):
            m = ID_primary()
            if m:
                Add_to_chef(a, b, c, d, e, f, g, h)
                Clear_chef()
                print_treev()


    def verify_chef(a, b, c, d, e, f, g, h):
        if (len(a) == 0 and len(b) == 0 and len(c) == 0 and len(d) == 0 and len(e) == 0 and len(f) == 0 and len(
                g) == 0 and len(h) == 0):
            messagebox.showerror("Error", "\nFields can't be empty\nEnter properly!")
            return False

        elif len(b) == 0:
            messagebox.showerror("Error", "Chef Name filed is missing")
            return False

        elif (b.isalpha() != True):
            messagebox.showerror("Error", "Chef Name can't contain Numbers or special characters")
            return False

        elif len(a) == 0:
            messagebox.showerror("Error", "Chef ID filed is missing")
            return False

        elif len(f) == 0:
            messagebox.showerror("Error", "Employee ID filed is missing")
            return False

        elif len(g) == 0:
            messagebox.showerror("Error", "Email ID filed is missing")
            return False

        elif (str(g).count('@') != 1 or str(g).count('.com') != 1):
            messagebox.showerror("Error", "Email ID must contain @ and .com only once")
            return False

        elif len(c) == 0:
            messagebox.showerror("Error", "Address filed is missing")
            return False

        elif len(e) == 0:
            messagebox.showerror("Error", "Speciality filed is missing")
            return False

        elif len(d) == 0:
            messagebox.showerror("Error", "Phone Number filed is missing")
            return False

        elif len(d) != 10:
            messagebox.showerror("Error", "Phone Number length must be 10")
            return False

        elif (d.isdigit() == False):
            messagebox.showerror("Error", "Phone Number should only contain numbers")
            return False

        elif len(h) == 0:
            messagebox.showerror("Error", "Salary filed is missing")
            return False

        val = 0
        try:
            val = float(h)
            if (val < 0):
                messagebox.showerror("Error", "Salary can't be negative")
                return False

            if (val == 0):
                messagebox.showerror("Error", "Salary can't be zero")
                return False

        except:
            messagebox.showerror("Error", "Enter only numerical value!")
            return False

        return True


    def ID_primary():
        mycursor.execute("SELECT CHEFID FROM CHEF")
        chef = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            chef.append(s)

        mycursor.execute("SELECT EMPID FROM EMPLOYEE")
        employee = []

        for x in mycursor:
            s = str(x)[1:5].strip(',')
            employee.append(s)

        mycursor.execute("SELECT CUISINEID FROM CUISINE")
        cuisine = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            cuisine.append(s)
        cf = 0
        e = 0
        cu = 0
        a = chefid.get().strip()
        b = empid.get().strip()
        c = spec.get().strip()
        for i in chef:
            if a == i:
                print(i)
                messagebox.showerror("Error", "Chef ID Already Exist")
                return False
            else:
                cf = cf + 1

        if cf == len(chef):
            for i in employee:
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
                    e = e + 1
            if e == len(employee):
                messagebox.showerror("Error", "Employee ID Doesn't Exist")
                return False


    def Add_to_chef(a, b, c, d, e, f, g, h):
        adding = "Insert into chef (CHEFID,CHEFNAME,ADDRESS,PHONENO,SPEC,EMPID,EMAILID,SALARY) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        entry = (a, b, c, d, e, f, g, h)
        mycursor.execute(adding, entry)
        myb.commit()
        print(mycursor.rowcount, "record inserted.")


    def Update_chef():
        a = chefid.get().strip()
        b = chefname.get().strip()
        c = address.get().strip()
        d = phone.get().strip()
        e = spec.get().strip()
        f = empid.get().strip()
        g = email.get().strip()
        h = salary.get().strip()
        if verify_chef(a, b, c, d, e, f, g, h):
            m = ID_primary_chef(a)
            if m:
                update_from_chef(a, b, c, d, e, f, g, h, a)
                # treev.insert('', 'end', values='')
                Clear_chef()
                print_treev()


    def update_from_chef(a, b, c, d, e, f, g, h, a1):
        n1 = "UPDATE chef SET chefid = %s ,chefname = %s ,address = %s ,phoneno = %s, spec = %s ,empid = %s ,emailid = %s ,salary = %s  where chefid = %s order by chefid;"
        val = (a, b, c, d, e, f, g, h, a1)
        mycursor.execute(n1, val)
        myb.commit()


    def ID_primary_chef(a):
        mycursor.execute("SELECT CHEFID FROM CHEF")
        chef = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            chef.append(s)

        mycursor.execute("SELECT EMPID FROM EMPLOYEE")
        employee = []

        for x in mycursor:
            s = str(x)[1:5].strip(',')
            employee.append(s)

        mycursor.execute("SELECT CUISINEID FROM CUISINE")
        cuisine = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            cuisine.append(s)

        cf = 0
        e = 0
        cu = 0
        a = chefid.get().strip()
        b = empid.get().strip()
        c = spec.get().strip()

        for i in chef:
            if a == i:
                print(i)
                for i in employee:
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
                        e = e + 1
                if e == len(employee):
                    messagebox.showerror("Error", "Employee ID Doesn't Exist")
                    return False
            else:
                cf = cf + 1

        if cf == len(chef):
            messagebox.showerror("Error", "Chef ID Doesn't Exist")
            return False

    def ID_delete_chef(a):
        mycursor.execute("SELECT CHEFID FROM CHEF")
        chef = []

        for x in mycursor:
            s = str(x)[1:3].strip(',')
            chef.append(s)

        c=0
        for i in chef:
            if a == i:
                print(i)
                return True
            else:
                c = c + 1

        if c == len(chef):
            messagebox.showerror("Error", "Chef ID Doesn't Exist")
            return False

    def Delete_chef():
        a = chefid.get()
        m = ID_delete_chef(a)
        if m:
            delete_from_chef(a)
            Clear_chef()
            print_treev()


    def delete_from_chef(a):
        n = "DELETE FROM CHEF WHERE chefid = " + str(a) + " order by chefid"
        mycursor.execute(n)
        myb.commit()


    def print_treev():
        mycursor.execute("SELECT * FROM CHEF")
        total = []
        for x in mycursor:
            print(x)
            total.append(x)

        for i in total:
            a, b, c, d, e, f, g, h = i
            data = [a, b, c, d, e, f, g, h]
            treev.insert('', 'end', values=data)


    def Clear_chef():
        for records in treev.get_children():
            treev.delete(records)


    Button(window, text='Add', bg="red", fg="white", font=('Times New Roman', 18), command=Add_chef).place(x=100, y=380)
    Button(window, text='Update', bg="red", fg="white", font=('Times New Roman', 18), command=Update_chef).place(x=200,
                                                                                                                 y=380)
    Button(window, text='Delete', bg="red", fg="white", font=('Times New Roman', 18), command=Delete_chef).place(x=330,
                                                                                                                 y=380)
    Button(window, text='Clear', bg="red", fg="white", font=('Times New Roman', 18), command=Clear_chef).place(x=450, y=380)
    Button(window, text='<<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.portal(root)).place(x=230, y=500)
    Button(window, text='<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.rest(root)).place(
        x=300, y=500)
    # Button(window, text='<<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
    #        command=lambda: PortalRest.portal(root)).place(x=230, y=600)
    # Button(window, text='<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18), command=lambda: PortalRest.rest(root)).place(
    #     x=300, y=600)
    TVList = ['CHEFID', 'CHEFNAME', 'ADDRESS', 'PHONENO', 'SPEC', 'EMPID', 'EMAILID', 'SALARY']

    treev = ttk.Treeview(tree, column=TVList, show='headings')
    treev['columns'] = ['CHEFID', 'CHEFNAME', 'ADDRESS', 'PHONENO', 'SPEC', 'EMPID', 'EMAILID', 'SALARY']
    # for giving column headings


    for i in TVList:
        treev.column(i, width=80)
        treev.heading(i, text=i.title())
    treev.grid(ipadx=50, padx=30)
    # Calling Main()
    root.mainloop()
