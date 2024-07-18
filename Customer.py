from tkinter import *
from tkinter import ttk
from tkinter.ttk import Panedwindow
from tkinter import Tk, messagebox
import mysql.connector
import PortalRest

myb = mysql.connector.connect(host="localhost", user="root", passwd="Justice", database="Restaurant_Management")

# Object return points there
mycursor = myb.cursor()


flagcity = 1
flagallergy = 1

def customer(k):
    k.destroy()
    root = Tk()
    root.state('zoomed')
    #App Title
    root.title("Restaurant Management ")
    Label(root, text="Customer Details").pack()

    #Create Panedwindow
    panedwindow=Panedwindow(root, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)

    #Create Frames
    customer = Frame(panedwindow, width=550, height=640, relief=SUNKEN)
    tree = Frame(panedwindow, width=600, height=300, relief=SUNKEN)

    panedwindow.add(customer, weight=1)
    panedwindow.add(tree, weight=4)

    customer.config(bg="#2b3d4f")
    yellow = Label(customer, text="Customer Details", bg="#f99406",fg="White",font=('Times New Roman',30,"bold","italic"))
    yellow.grid(row=0, column=0, ipady=10,columnspan=10, ipadx=200)



    # -- Customer First Name --
    fname = Label(customer, text='First Name: ', font=('Times New Roman', 20), bg="#2b3d4f",fg="white")
    fname.grid(row=2, column=0)

    user_input_fname = StringVar()

    user_field_fname = Entry(customer, textvariable=user_input_fname, font=('Times New Roman', 18))
    user_field_fname.grid(row=2, column=1)

    # -- Customer last Name --
    lname = Label(customer, text='Last Name: ', font=('Times New Roman', 20), bg="#2b3d4f",fg="white")
    lname.grid(row=3, column=0)

    user_input_lname = StringVar()

    user_field_lname = Entry(customer, textvariable=user_input_lname, font=('Times New Roman', 18))
    user_field_lname.grid(row=3, column=1)


    #  -- customer id --
    fid = Label(customer, text='Customer Id: ', font=('Times New Roman', 20), bg="#2b3d4f",fg="white")
    fid.grid(row=4, column=0)


    user_input_cid = StringVar()

    user_field_fid = Entry(customer, textvariable=user_input_cid, font=('Times New Roman', 18))
    user_field_fid.grid(row=4, column=1)

    # --email-id
    Label(customer, text='Email Id:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=5, column=0)

    user_input_email = StringVar()
    user_field = Entry(customer, textvariable=user_input_email, font=('Times New Roman', 18)).grid(row=5, column=1)


    Label(customer, text='City:', font=('Times New Roman', 20), bg="#2b3d4f",fg="white").grid(row=6, column=0)
    Label(customer, text='Street:', font=('Times New Roman', 20), bg="#2b3d4f",fg="white").grid(row=7, column=0)
    Label(customer, text='Pincode:', font=('Times New Roman', 20), bg="#2b3d4f",fg="white").grid(row=8, column=0)
    Label(customer, text='Gender:', font=('Times New Roman', 20), bg="#2b3d4f",fg="white").grid(row=9, column=0)
    Label(customer, text='Phone No:', font=('Times New Roman', 20), bg="#2b3d4f",fg="white").grid(row=10, column=0)
    Label(customer, text='Allergy:', font=('Times New Roman', 20), bg="#2b3d4f", fg="white").grid(row=11, column=0)

    user_input_city = StringVar()
    user_field = Entry(customer, textvariable=user_input_city, font=('Times New Roman', 18)).grid(row=6, column=1)

    user_input_street = StringVar()
    user_field = Entry(customer, textvariable=user_input_street, font=('Times New Roman', 18)).grid(row=7, column=1)

    user_input_pincode = StringVar()
    user_field = Entry(customer, textvariable=user_input_pincode, font=('Times New Roman', 18)).grid(row=8, column=1)

    user_input_gender = StringVar()
    user_field = Entry(customer, textvariable=user_input_gender, font=('Times New Roman', 18)).grid(row=9, column=1)

    user_input_phoneNo = StringVar()
    user_field = Entry(customer, textvariable=user_input_phoneNo, font=('Times New Roman', 18)).grid(row=10, column=1)

    user_input_allergy = StringVar()
    user_field = Entry(customer,show = 'null', textvariable=user_input_allergy, font=('Times New Roman', 18)).grid(row=11, column=1)



    def verify_customer(a, b, c, d, e, f, g, h, i, j):
        if (len(a) == 0 and len(b) == 0 and len(c) == 0 and len(d) == 0 and len(e) == 0 and len(f) == 0):
            messagebox.showerror("Error", "\nFields can't be empty\nEnter properly!")
            return False

        elif len(a) == 0:
            messagebox.showerror("Error", "First Name is missing")
            return False

        elif (a.isalpha() != True):
            messagebox.showerror("Error", "First Name can't contain Numbers or special characters")
            return False
        elif (len(a) > 25):
            messagebox.showerror("Error", "Enter only first 25 letter of your name")
            return False


        elif len(b) == 0:
            messagebox.showerror("Error", "Last Name is missing")
            return False

        elif (b.isalpha() != True):
            messagebox.showerror("Error", "Last Name can't contain Numbers or special characters")
            return False
        elif (len(b) > 20):
            messagebox.showerror("Error", "Enter only first 20 letter of your last name")
            return False


        elif len(c) == 0:
            messagebox.showerror("Error", "Customer Id is missing")
            return False

        elif (c.isalpha() == True):
            messagebox.showerror("Error", "Customer Id should contain only numbers")
            return False

        elif (str(d).count('@') != 1 or str(d).count('.com') != 1):
            messagebox.showerror("Error", "Email ID must contain @ and .com only once")
            return False

        elif (len(d) > 30):
            messagebox.showerror("Error", "Email id length exceeded")
            return False

        elif len(f) == 0:
            messagebox.showerror("Error", "Street is missing")
            return False
        elif (len(f) > 20):
            messagebox.showerror("Error", "Email id length exceeded")
            return False

        elif len(g) == 0:
            messagebox.showerror("Error", "Pincode is missing")
            return False

        elif (g.isdigit() == False):
            messagebox.showerror("Error", "Pincode should only contain numbers")
            return False

        elif (len(g) < 6):
            messagebox.showerror("Error", "Pincode should be atleast 6 digits")
            return False

        elif (len(g) > 7):
            messagebox.showerror("Error", "Pincode should be not more than 6 digits")
            return False


        elif len(h) == 0:
            messagebox.showerror("Error", "Gender is missing")
            return False

        elif (h.upper() != 'F' and h.upper() != 'M' and h.upper() != 'O'):
            messagebox.showerror("Error", "Gender should be only F, M, O")
            return False

        elif len(i) == 0:
            messagebox.showerror("Error", "Phoneno is missing")
            return False

        elif len(i) != 10:
            messagebox.showerror("Error", "Phoneno should of 10 digits only")
            return False

        global flagcity
        global flagallergy
        if len(e) == 0:
            flagcity = 0
        if len(j) == 0:
            flagallergy =0

        return True

    def ID_primary():
        mycursor.execute("SELECT CUSTID FROM CUSTOMER")
        cust = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            cust.append(s)
        a = user_input_cid.get().strip()

        for i in cust:
            if a == i:
                # print(i)

                messagebox.showerror("Error", "Customer ID Already Exist")
                return False



        return True

    def Add_to_customer(a, b, c, d, e, f, g, h, i, j):
        adding = "Insert into customer (Fname,lname,custid,emailid,city,street,pincode,gender,phoneno,allergy) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        if flagcity == 0:
            e = "Ahmedabad"

        if flagallergy == 0:
            j = "Null"

        entry = (a, b, c, d, e, f,g, h, i, j)
        mycursor.execute(adding, entry)
        myb.commit()
        print(mycursor.rowcount, "record inserted.")

    def Add_customer():

        a = user_input_fname.get().strip()
        b = user_input_lname.get().strip()
        c = user_input_cid.get().strip()
        d = user_input_email.get().strip()
        e = user_input_city.get().strip()
        f = user_input_street.get().strip()
        g = user_input_pincode.get().strip()
        h = user_input_gender.get().strip()
        i = user_input_phoneNo.get().strip()
        j = user_input_allergy.get().strip()

        if verify_customer(a, b, c, d, e, f, g, h, i, j):
            m = ID_primary()
            if m:
                Add_to_customer(a, b, c, d, e, f, g, h, i, j)
                Clear_customer()
                print_treev()

    def print_treev():
        mycursor.execute("SELECT * FROM Customer")
        total = []
        for x in mycursor:
            # print(x)
            total.append(x)

        for i in total:
            a, b, c, d, e, f, g, h, i, j = i
            data = [a, b, c, d, e, f, g, h, i, j]
            treev.insert('', 'end', values=data)



    def Delete_customer():
        pass

    def update_from_customer(a, b, c, d, e, f, g, h, i, j, a1):
        # (Fname,lname,custid,emailid,city,street,pincode,gender,phoneno,allergy
        n1 = "UPDATE customer SET fname = %s ,lname = %s , custid = %s , emailid = %s , city = %s ,street = %s, pincode = %s, gender = %s , phoneno = %s , allergy = %s where custid = %s order by custid;"
        val = (a, b, c, d, e, f, g, h, i, j, a1)
        mycursor.execute(n1, val)
        myb.commit()

    def ID_primary_customer(a):
        mycursor.execute("SELECT CUSTID FROM Customer")
        cus = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            cus.append(s)

        c = 0
        for i in cus:
            if a == i:
                print(i)
                return True
            else:
                c = c + 1

        if c == len(cus):
            messagebox.showerror("Error", "Customer ID doesn't exist")
            return False


    def Update_customer():

        a = user_input_fname.get().strip()
        b = user_input_lname.get().strip()
        c = user_input_cid.get().strip()
        d = user_input_email.get().strip()
        e = user_input_city.get().strip()
        f = user_input_street.get().strip()
        g = user_input_pincode.get().strip()
        h = user_input_gender.get().strip()
        i = user_input_phoneNo.get().strip()
        j = user_input_allergy.get().strip()

        if verify_customer(a, b, c, d, e, f, g, h, i, j):
            m = ID_primary_customer(c)
            if m:
                update_from_customer(a, b, c, d, e, f, g, h, i, j, c)
                Clear_customer()
                print_treev()

    def delete_from_customer(a):
        n = "DELETE FROM CUSTOMER WHERE CUSTID = " + str(a) + " order by CUSTID"
        mycursor.execute(n)
        myb.commit()

    def ID_delete_customer(a):
        mycursor.execute("SELECT CUSTID FROM CUSTOMER")
        customer = []

        for x in mycursor:
            s = str(x)[1:-1].strip(',')
            customer.append(s)

        for i in customer:
            if a == i:
                print(i)
                return True


        messagebox.showerror("Error", "Customer ID Doesn't Exist")
        return False

    def Delete_customer():
        a = user_input_cid.get()
        m = ID_delete_customer(a)
        if m:
            delete_from_customer(a)
            Clear_customer()
            print_treev()

    def Clear_customer():
        for records in treev.get_children():
            treev.delete(records)


    Button(customer, text='Add',bg="red",fg="white",font=('Times New Roman', 18), command=Add_customer).place(x=80,y=500)
    Button(customer, text='Update',bg="red",fg="white",font=('Times New Roman', 18), command=Update_customer).place(x=180,y=500)
    Button(customer, text='Delete',bg="red",fg="white",font=('Times New Roman', 18), command=Delete_customer).place(x=310,y=500)
    Button(customer, text='Clear', bg="red", fg="white", font=('Times New Roman', 18), command=Clear_customer).place(x=430, y=500)
    Button(customer, text='<<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18),
           command=lambda: PortalRest.portal(root)).place(x=230, y=500)
    Button(customer, text='<', bg="#1bb6fe", fg="white", font=('Times New Roman', 18), command=lambda: PortalRest.rest(root)).place(
        x=300, y=500)
    TVList = ['Fname', 'lname', 'custid', 'emailid', 'city', 'street', 'pincode', 'gender', 'phoneno', 'allergy']


    treev = ttk.Treeview(tree, column=TVList, show='headings', height=5)
    treev['columns']= ['Fname', 'lname', 'custid', 'emailid', 'city', 'street', 'pincode', 'gender', 'phoneno', 'allergy']
    # for giving column headings

    for i in TVList:
        treev.column(i,width=100)
        treev.heading(i, text=i.title())
    treev.grid(padx=12, pady=10,ipadx=15, ipady=100)




    root.mainloop()