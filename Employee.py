# Create app using with separating widget
from tkinter import *
from tkinter.ttk import Panedwindow
from tkinter import ttk
from tkinter import Tk, messagebox
import PortalRest
import mysql.connector

myb = mysql.connector.connect(host="localhost", user="root", passwd="Justice", database="Restaurant_Management")

# Object return points there
mycursor = myb.cursor()

def employee(k):
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
    tree = Frame(panedwindow, width=600, height=640, relief=SUNKEN)
    panedwindow.add(window, weight=1)
    panedwindow.add(tree, weight=6)
    window.config(background="#2b3d4f")

    Label(window, text="EMPLOYEE", bg="#f99406", fg="White", font=('Times New Roman', 30, "bold")).grid(row=0, column=0,
                                                                                                        columnspan=10,
                                                                                                        ipady=7, ipadx=250)
    Label(window, text='First Name:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=5, column=2)
    Label(window, text='Last Name:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=6, column=2)
    Label(window, text='Emp Id:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=7, column=2)
    Label(window, text='Email Id:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=8, column=2)
    Label(window, text='Address :', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=9, column=2)
    Label(window, text='Gender:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=10, column=2)
    Label(window, text='Phone No:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=11, column=2)
    Label(window, text='Salary:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=12, column=2)

    fname = StringVar()
    user_field = Entry(window, textvariable=fname, font=('Times New Roman', 18)).grid(row=5, column=4)
    lname = StringVar()
    user_field1 = Entry(window, textvariable=lname, font=('Times New Roman', 18)).grid(row=6, column=4)
    empid = StringVar()
    user_field2 = Entry(window, textvariable=empid, font=('Times New Roman', 18)).grid(row=7, column=4)
    email = StringVar()
    user_field3 = Entry(window, textvariable=email, font=('Times New Roman', 18)).grid(row=8, column=4)
    address = StringVar()
    user_field4 = Entry(window, textvariable=address, font=('Times New Roman', 18)).grid(row=9, column=4)
    gender = StringVar()
    user_field5 = Entry(window, textvariable=gender, font=('Times New Roman', 18)).grid(row=10, column=4)
    phone = StringVar()
    user_field6 = Entry(window, textvariable=phone, font=('Times New Roman', 18)).grid(row=11, column=4)
    salary = StringVar()
    user_field7 = Entry(window, textvariable=salary, font=('Times New Roman', 18)).grid(row=12, column=4)


    def verify_details(a, b, c, d, e, f, g, h):
        if (len(a) == 0 and len(b) == 0 and len(c) == 0 and len(d) == 0 and len(e) == 0 and len(f) == 0 and len(
                g) == 0 and len(h) == 0):
            messagebox.showerror("Error", "\tFields can't be empty\nEnter properly!")
            return False

        elif len(b) == 0:
            messagebox.showerror("Error", "First Name filed is missing")
            return False

        elif (b.isalpha() != True):
            messagebox.showerror("Error", "First Name can't contain Numbers or special characters")
            return False

        elif len(c) == 0:
            messagebox.showerror("Error", "Last Name filed is missing")
            return False

        elif (c.isalpha() != True):
            messagebox.showerror("Error", "Last Name can't contain Numbers or special characters")
            return False

        elif len(a) == 0:
            messagebox.showerror("Error", "Employee ID filed is missing")
            return False

        elif len(d) == 0:
            messagebox.showerror("Error", "Email filed is missing")
            return False

        elif (str(d).count('@') != 1 or str(d).count('.com') != 1):
            messagebox.showerror("Error", "Email ID must contain @ and .com only once")
            return False

        elif len(e) == 0:
            messagebox.showerror("Error", "Address filed is missing")
            return False

        elif len(g) == 0:
            messagebox.showerror("Error", "Gender filed is missing")
            return False

        elif not (g == 'F' or g == 'f' or g == 'M' or g == 'm' or g == 'O' or g == 'o'):
            messagebox.showerror("Error", "Gender filed must be F or M or O")
            return False

        elif len(f) == 0:
            messagebox.showerror("Error", "Phone Number filed is missing")
            return False

        elif len(f) != 10:
            messagebox.showerror("Error", "Phone Number length must be 10")
            return False

        elif f.isdigit() == False:
            messagebox.showerror("Error", "Phone Number should only contain numbers")
            return False

        elif len(h) == 0:
            messagebox.showerror("Error", "Salary filed is missing")
            return False

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
        mycursor.execute("SELECT EMPID FROM EMPLOYEE")
        datab = []

        for x in mycursor:
            s = str(x)[1:5].strip(',')
            datab.append(s)
        c = 0
        a = empid.get().strip()

        for i in datab:
            if a == i:
                print(i)
                messagebox.showerror("Error", "Employee ID Already Exist")
                return False
            else:
                c = c + 1

        if c == len(datab):
            return True


    def Add_to_employee(a, b, c, d, e, f, g, h):
        adding = "Insert into employee  (EMPID,FNAME,LNAME,EMAILID,ADDRESS,PHONENO,GENDER,SALARY) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        entry = (a, b, c, d, e, f, g, h)
        mycursor.execute(adding, entry)
        myb.commit()
        print(mycursor.rowcount, "record inserted.")


    def Add_emp():
        a = empid.get().strip()
        b = fname.get().strip()
        c = lname.get().strip()
        d = email.get().strip()
        e = address.get().strip()
        f = phone.get().strip()
        g = gender.get().strip()
        h = salary.get().strip()

        if verify_details(a, b, c, d, e, f, g, h):
            m = ID_primary()
            if m:
                Add_to_employee(a, b, c, d, e, f, g, h)
                Clear_emp()
                print_treev()


    def print_treev():
        mycursor.execute("SELECT * FROM EMPLOYEE")
        total = []
        for x in mycursor:
            print(x)
            total.append(x)

        for i in total:
            a, b, c, d, e, f, g, h = i
            data = [a, b, c, d, e, f, g, h]
            treev.insert('', 'end', values=data)


    def ID_primary_emp(a):
        mycursor.execute("SELECT EMPID FROM EMPLOYEE")
        employee = []

        for x in mycursor:
            s = str(x)[1:5].strip(',')
            employee.append(s)

        c = 0
        for i in employee:
            if a == i:
                print(i)
                return True
            else:
                c = c + 1

        if c == len(employee):
            messagebox.showerror("Error", "Employee ID Doesn't Exist")
            return False


    def update_from_emp(a, b, c, d, e, f, g, h, a1):
        n1 = "UPDATE employee SET empid = %s ,fname = %s ,lname = %s ,emailid = %s, address = %s ,phoneno = %s ,gender = %s ,salary = %s  where empid = %s order by empid;"
        val = (a, b, c, d, e, f, g, h, a1)
        mycursor.execute(n1, val)
        myb.commit()


    def Update_emp():
        a = empid.get().strip()
        b = fname.get().strip()
        c = lname.get().strip()
        d = email.get().strip()
        e = address.get().strip()
        f = phone.get().strip()
        g = gender.get().strip()
        h = salary.get().strip()
        if verify_details(a, b, c, d, e, f, g, h):
            m = ID_primary_emp(a)
            if m:
                update_from_emp(a, b, c, d, e, f, g, h, a)
                Clear_emp()
                print_treev()

    def delete_from_emp(a):
        n = "DELETE FROM EMPLOYEE WHERE empid = " + str(a) + " order by empid"
        mycursor.execute(n)
        myb.commit()

    def Delete_emp():
        a = empid.get()
        m = ID_primary_emp(a)
        if m:
            delete_from_emp(a)
            Clear_emp()
            print_treev()


    def Clear_emp():
        for records in treev.get_children():
            treev.delete(records)


    Button(window, text='Add', bg="red", fg="white", font=('Times New Roman', 18), command=Add_emp).place(x=100, y=380)
    Button(window, text='Update', bg="red", fg="white", font=('Times New Roman', 18), command=Update_emp).place(x=200,
                                                                                                                y=380)
    Button(window, text='Delete', bg="red", fg="white", font=('Times New Roman', 18), command=Delete_emp).place(x=330,
                                                                                                                y=380)
    Button(window, text='Clear', bg="red", fg="white", font=('Times New Roman', 18), command=Clear_emp).place(x=450, y=380)
    Button(window, text='<<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.portal(root)).place(x=230, y=500)
    Button(window, text='<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.rest(root)).place(
        x=300, y=500)
    TVList = ['First Name', 'Last Name', 'Emp Id', 'Email Id', 'Address', 'Gender', 'Phone No', 'Salary']
    treev = ttk.Treeview(tree, column=TVList, show='headings')
    treev['columns'] = ['First Name', 'Last Name', 'Emp Id', 'Email Id', 'Address', 'Gender', 'Phone No', 'Salary']
    # for giving column headings

    for i in TVList:
        treev.column(i, width=80)
        treev.heading(i, text=i.title())
    treev.grid(ipadx=40, padx=30)
    # Calling Main()
    root.mainloop()
