from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk

class Supplier:
    def __init__(self, root):
        DB = DatabaseSupplier()
        DB.conn()

        self.root = root
        self.root.title("Book Keeping - Suppliers")
        self.root.state('zoomed')
        self.root.iconbitmap("./icon.ico")

        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scroll = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scroll.pack(side=RIGHT, fill=Y)

        my_scroll2 = Scrollbar(my_canvas, orient=HORIZONTAL, command=my_canvas.xview)
        my_scroll2.pack(side=BOTTOM, anchor=S, fill=X)

        my_canvas.configure(xscrollcommand=my_scroll2.set, yscrollcommand=my_scroll.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        second_frame = Frame(my_canvas)
        
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        def OnMouseWheel(event):
            my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        def _bound_to_mousewheel(event):
            my_canvas.bind_all("<MouseWheel>", OnMouseWheel)

        def _unbound_to_mousewheel(event):
            my_canvas.unbind_all("<MouseWheel>")
        
        my_canvas.bind_all("<MouseWheel>", OnMouseWheel)

        my_canvas.bind('<Enter>', _bound_to_mousewheel)
        
        my_canvas.bind('<Leave>', _unbound_to_mousewheel)

        def _OnMouseWheel(event):
            my_canvas.xview_scroll(int(-1*(event.delta/120)), "units")

        def __bound_to_mousewheel(event):
            my_canvas.bind_all("<MouseWheel>", OnMouseWheel)

        def __unbound_to_mousewheel(event):
            my_canvas.unbind_all("<MouseWheel>")
        
        my_canvas.bind_all("<Shift-MouseWheel>", _OnMouseWheel)

        my_canvas.bind('<Enter>', __bound_to_mousewheel)
        
        my_canvas.bind('<Leave>', __unbound_to_mousewheel)
        
        home = second_frame

        f1 = ttk.Frame(home, width=600, height=380)
        f1.grid(row=0, column=0)

        f2 = ttk.Frame(home, width=600, height=380)
        f2.grid(row=0, column=1, padx=20)

        f3 = ttk.Frame(home, width=10, height=10)
        f3.grid(row=1, column=0)

        SupplierName = StringVar()
        Supplier_Id = StringVar()
        Supplier_Name_For_Orders = StringVar()
        GST_Number = StringVar()
        Ship_To_Name = StringVar()
        Contact_Number = StringVar()
        Default_Order_Type = StringVar()
        Default_Payment_Terms = StringVar()
        Credit_Account = StringVar()
        Department = StringVar()
        Default_Purchase_Account = StringVar()
        Default_Account_For_Payments = StringVar()
        Supplier_Billing_Address = StringVar()
        Our_Shipping_Address = StringVar()
        Mobile_Number = StringVar()
        Telephone_Number = StringVar()
        Email_Address = StringVar()
        Fax_Number = StringVar()
        Contact_Person_Name_1 = StringVar()
        Contact_Person_Name_2 = StringVar()
        Order_Comment_1 = StringVar()
        Order_Comment_2 = StringVar()
        Quote_Comment_1 = StringVar()
        Quote_Comment_2 = StringVar()
        Default_Job = StringVar()
        Bank_Name = StringVar()
        Branch_Location = StringVar()
        Bank_Account_Name = StringVar()
        Bank_Account_Number = StringVar()
        BSB = StringVar()
        Swift_Code  = StringVar()
        Notes = StringVar()

        def clear():
            print("Supplier : Clear method called")
            suppliername.delete(0, END)
            supplierid.delete(0, END)
            suppliernamefororders.delete(0, END)
            gstnumber.delete(0, END)
            shiptoname.delete(0, END)
            contactnumber.delete(0, END)
            defaultordertype.delete(0, END)        
            defaultpaymentterms.delete(0, END)        
            creditaccount.delete(0, END)        
            department.delete(0, END)        
            defaultpurchaseaccount.delete(0, END)
            defaultaccountforpayments.delete(0, END)        
            supplierbillingaddress.delete(0, END)        
            ourshippingaddress.delete(0, END)       
            mobilenumber.delete(0, END)        
            telephonenumber.delete(0, END)
            emailaddress.delete(0, END)
            faxnumber.delete(0, END)
            contactpersonname1.delete(0, END)
            contactpersonname2.delete(0, END)
            ordercomment1.delete(0, END)
            ordercomment2.delete(0, END)
            quotcomment1.delete(0, END)
            quotcomment2.delete(0, END)
            defaultjob.delete(0, END)
            bankname.delete(0, END)
            branchlocation.delete(0, END)
            bankaccountname.delete(0, END)
            bankaccountnumber.delete(0, END)        
            bsb.delete(0, END)
            swiftcode.delete(0, END)
            notes.delete(0, END)
            
            print("Supplier : clear method finished\n")

        def delete():
            print("Supplier :database Delete method called")
            if Supplier_Id.get() != "":
                DB.delete(pd[0])
                clear()
                showInsupplierList() 
                print("Supplier : database Delete method finished\n")
            if Supplier_Id.get() == "":
                DB.delete(pd[1])
                clear()
                showInsupplierList() 
                print("Supplier : database Delete method finished\n")

        
        def search():
            print("Supplier : search method called")
            supplierList.delete(0,END)
            for row in DB.search(Supplier_Id.get()):
                supplierList.insert(END, row, str(""))
            print("Supplier : search method finished\n")

        def insert():
            print("Supplier : Insert method called")
            if Supplier_Id.get() != 0:
                DB.insert(
                    SupplierName.get(), Supplier_Id.get(), Supplier_Name_For_Orders.get(), GST_Number.get(), Ship_To_Name.get(),
                    Contact_Number.get(), Default_Order_Type.get(), Default_Payment_Terms.get(), Credit_Account.get(),
                    Department.get(), Default_Purchase_Account.get(), Default_Account_For_Payments.get(), Supplier_Billing_Address.get(),
                    Our_Shipping_Address.get(), Mobile_Number.get(), Telephone_Number.get(), Email_Address.get(), Fax_Number.get(), 
                    Contact_Person_Name_1.get(), Contact_Person_Name_2.get(), Order_Comment_1.get(), Order_Comment_2.get(), 
                    Quote_Comment_1.get(), Quote_Comment_2.get(), Default_Job.get(), Bank_Name.get(), Branch_Location.get(), 
                    Bank_Account_Name.get(), Bank_Account_Number.get(), BSB.get(), Swift_Code.get(), Notes.get()
                    )
                supplierList.delete(0, END)
                supplierList.insert(
                    END, SupplierName.get(), Supplier_Id.get(), Supplier_Name_For_Orders.get(), GST_Number.get(), Ship_To_Name.get(),
                    Contact_Number.get(), Default_Order_Type.get(), Default_Payment_Terms.get(), Credit_Account.get(),
                    Department.get(), Default_Purchase_Account.get(), Default_Account_For_Payments.get(), Supplier_Billing_Address.get(),
                    Our_Shipping_Address.get(), Mobile_Number.get(), Telephone_Number.get(), Email_Address.get(), Fax_Number.get(), 
                    Contact_Person_Name_1.get(), Contact_Person_Name_2.get(), Order_Comment_1.get(), Order_Comment_2.get(), 
                    Quote_Comment_1.get(), Quote_Comment_2.get(), Default_Job.get(), Bank_Name.get(), Branch_Location.get(), 
                    Bank_Account_Name.get(), Bank_Account_Number.get(), BSB.get(), Swift_Code.get(), Notes.get()
                    )
                showInsupplierList() # called showInCustomerList method after inserting the data record to database table
                clear()        
                print("Supplier : Insert method finished\n")
            else:
                messagebox.showerror("Book Keeping", "Enter Supplier ID")
        
        def showInsupplierList():
            print("Supplier : showInProductList method called")
            supplierList.delete(0, END)
            for row in DB.show():
                supplierList.insert(END, row, str(""))
            print("Supplier : showInProductList method finished\n")

        def update():
            print("Suppliers : Update method called")
            print("pd[1]", pd[1])
            DB.delete(pd[1])
            DB.insert(
                SupplierName.get(), Supplier_Id.get(), Supplier_Name_For_Orders.get(), GST_Number.get(), Ship_To_Name.get(),
                Contact_Number.get(), Default_Order_Type.get(), Default_Payment_Terms.get(), Credit_Account.get(),
                Department.get(), Default_Purchase_Account.get(), Default_Account_For_Payments.get(), Supplier_Billing_Address.get(),
                Our_Shipping_Address.get(), Mobile_Number.get(), Telephone_Number.get(), Email_Address.get(), Fax_Number.get(), 
                Contact_Person_Name_1.get(), Contact_Person_Name_2.get(), Order_Comment_1.get(), Order_Comment_2.get(), 
                Quote_Comment_1.get(), Quote_Comment_2.get(), Default_Job.get(), Bank_Name.get(), Branch_Location.get(), 
                Bank_Account_Name.get(), Bank_Account_Number.get(), BSB.get(), Swift_Code.get(), Notes.get()
            )

            supplierList.delete(0, END)

            supplierList.insert(
                END, SupplierName.get(), Supplier_Id.get(), Supplier_Name_For_Orders.get(), GST_Number.get(), Ship_To_Name.get(),
                Contact_Number.get(), Default_Order_Type.get(), Default_Payment_Terms.get(), Credit_Account.get(),
                Department.get(), Default_Purchase_Account.get(), Default_Account_For_Payments.get(), Supplier_Billing_Address.get(),
                Our_Shipping_Address.get(), Mobile_Number.get(), Telephone_Number.get(), Email_Address.get(), Fax_Number.get(), 
                Contact_Person_Name_1.get(), Contact_Person_Name_2.get(), Order_Comment_1.get(), Order_Comment_2.get(), 
                Quote_Comment_1.get(), Quote_Comment_2.get(), Default_Job.get(), Bank_Name.get(), Branch_Location.get(), 
                Bank_Account_Name.get(), Bank_Account_Number.get(), BSB.get(), Swift_Code.get(), Notes.get()
            )

            showInsupplierList() # called showInCustomerList method after inserting the data record to database table
            clear()
            print("Suppliers : Update method finished")

        Label(f1, text="Supplier Name: ").grid(row=0, column=0)
        suppliername = Entry(f1, font="bold", textvariable=SupplierName)
        suppliername.grid(row=0, column=1)
            
        Label(f1, text="Supplier ID: ").grid(row=0, column=2)
        supplierid = Entry(f1, font="bold", textvariable=Supplier_Id)
        supplierid.grid(row=0, column=3)

        Label(f1, text="Supplier Name (For Orders): ").grid(row=1, column=0)
        suppliernamefororders = Entry(f1, font="bold", textvariable=Supplier_Name_For_Orders)
        suppliernamefororders.grid(row=1, column=1)
            
        Label(f1, text="GST Number: ").grid(row=1, column=2)
        gstnumber = Entry(f1, font="bold", textvariable=GST_Number)
        gstnumber.grid(row=1, column=3)

        Checkbutton(f1, text="Reports Receipts ").grid(row=2, column=0)

        Label(f1, text="Ship to Name: ").grid(row=3, column=0)
        shiptoname = Entry(f1, font="bold", textvariable=Ship_To_Name)
        shiptoname.grid(row=3, column=1)
        
        Label(f1, text="Contact Number: ").grid(row=3, column=2)
        contactnumber = Entry(f1, font="bold", textvariable=Contact_Number)
        contactnumber.grid(row=3, column=3)

        Label(f1, text="Default Order Type: ").grid(row=4, column=0)
        defaultordertype = Entry(f1, font="bold", textvariable=Default_Order_Type)
        defaultordertype.grid(row=4, column=1)

        Label(f1, text="Default Payment Terms: ").grid(row=5, column=0)
        defaultpaymentterms = Entry(f1, font="bold", textvariable=Default_Payment_Terms)
        defaultpaymentterms.grid(row=5, column=1)

        Label(f1, text="Credit Account: ").grid(row=6, column=0)
        creditaccount = Entry(f1, font="bold", textvariable=Credit_Account)
        creditaccount.grid(row=6, column=1)
            
        Label(f1, text="Departmenet: ").grid(row=6, column=2)
        department = Entry(f1, font="bold", textvariable=Department)
        department.grid(row=6, column=3)

        Label(f1, text="Default Purchase Account: ").grid(row=7, column=0)
        defaultpurchaseaccount = Entry(f1, font="bold", textvariable=Default_Purchase_Account)
        defaultpurchaseaccount.grid(row=7, column=1)

        Label(f1, text="Default Account For Payments: ").grid(row=8, column=0)
        defaultaccountforpayments = Entry(f1, font="bold", textvariable=Default_Account_For_Payments)
        defaultaccountforpayments.grid(row=8, column=1)

        Label(f1, text="Supplier Billing Address: ").grid(row=9, column=0)
        supplierbillingaddress = Entry(f1, font="bold", textvariable=Supplier_Billing_Address)
        supplierbillingaddress.grid(row=9, column=1)
        
        Label(f1, text="Our Shipping Address: ").grid(row=9, column=2)
        ourshippingaddress = Entry(f1, font="bold", textvariable=Our_Shipping_Address)
        ourshippingaddress.grid(row=9, column=3)

        Label(f1, text="Cell / Mobile Number: ").grid(row=10, column=0)
        mobilenumber = Entry(f1, font="bold", textvariable=Mobile_Number)
        mobilenumber.grid(row=10, column=1)
        
        Label(f1, text="Telephone Number: ").grid(row=10, column=2)
        telephonenumber = Entry(f1, font="bold", textvariable=Telephone_Number)
        telephonenumber.grid(row=10, column=3)

        Label(f1, text="Email Address: ").grid(row=11, column=0)
        emailaddress = Entry(f1, font="bold", textvariable=Email_Address)
        emailaddress.grid(row=11, column=1)
        
        Label(f1, text="Fax Number: ").grid(row=11, column=2)
        faxnumber = Entry(f1, font="bold", textvariable=Fax_Number)
        faxnumber.grid(row=11, column=3)

        Label(f1, text="Contact Person Name 1: ").grid(row=12, column=0)
        contactpersonname1 = Entry(f1, font="bold", textvariable=Contact_Person_Name_1)
        contactpersonname1.grid(row=12, column=1)
        
        Label(f1, text="Contact Person Name 2: ").grid(row=12, column=2)
        contactpersonname2 = Entry(f1, font="bold", textvariable=Contact_Person_Name_2)
        contactpersonname2.grid(row=12, column=3)

        Label(f1, text="Order Comment 1: ").grid(row=13, column=0)
        ordercomment1 = Entry(f1, font="bold", textvariable=Order_Comment_1)
        ordercomment1.grid(row=13, column=1)

        Label(f1, text="Order Comment 2: ").grid(row=14, column=0)
        ordercomment2 = Entry(f1, font="bold", textvariable=Order_Comment_2)
        ordercomment2.grid(row=14, column=1)

        Label(f1, text="Quote Comment 1: ").grid(row=15, column=0)
        quotcomment1 = Entry(f1, font="bold", textvariable=Quote_Comment_1)
        quotcomment1.grid(row=15, column=1)

        Label(f1, text="Quote Comment 2: ").grid(row=16, column=0)
        quotcomment2 = Entry(f1, font="bold", textvariable=Quote_Comment_2)
        quotcomment2.grid(row=16, column=1)

        Label(f1, text="Default Job: ").grid(row=17, column=0)
        defaultjob = Entry(f1, font="bold", textvariable=Default_Job)
        defaultjob.grid(row=17, column=1)

        Checkbutton(f1, text="Inactive Supplier ").grid(row=18, column=0)

        Label(f1, text="Bank Name: ").grid(row=19, column=0)
        bankname = Entry(f1, font="bold", textvariable=Bank_Name)
        bankname.grid(row=19, column=1)
        
        Label(f1, text="Branch Location: ").grid(row=19, column=2)
        branchlocation = Entry(f1, font="bold", textvariable=Branch_Location)
        branchlocation.grid(row=19, column=3)
            
        Label(f1, text="Bank Account Name: ").grid(row=20, column=0)
        bankaccountname = Entry(f1, font="bold", textvariable=Bank_Account_Name)
        bankaccountname.grid(row=20, column=1)
        
        Label(f1, text="Bank Account Number: ").grid(row=20, column=2)
        bankaccountnumber = Entry(f1, font="bold", textvariable=Bank_Account_Number)
        bankaccountnumber.grid(row=20, column=3)

        Label(f1, text="BSB: ").grid(row=21, column=0)
        bsb = Entry(f1, font="bold", textvariable=BSB)
        bsb.grid(row=21, column=1)
        
        Label(f1, text="Swift Code: ").grid(row=21, column=2)
        swiftcode = Entry(f1, font="bold", textvariable=Swift_Code)
        swiftcode.grid(row=21, column=3)

        Label(f1, text="Notes: ").grid(row=22, column=0)
        notes = Entry(f1, font="bold", textvariable=Notes)
        notes.grid(row=22, column=1)

        buttonSaveData = Button(f3, text='Save', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=insert)
        buttonSaveData.grid(row=0, column=0, pady=10)

        buttonShowData = Button(f3, text='Show Data', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=showInsupplierList)
        buttonShowData.grid(row=0, column=1, pady=10, padx=10)

        buttonClearData = Button(f3, text='Reset', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=clear)
        buttonClearData.grid(row=0, column=2, pady=10)

        buttonDeleteData = Button(f3, text='Delete', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=delete)
        buttonDeleteData.grid(row=1, column=0)

        buttonsearchData = Button(f3, text='Search', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=search)
        buttonsearchData.grid(row=1, column=1, padx=10)

        buttonUpdate = Button(f3, text='Update', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=update)
        buttonUpdate.grid(row=1, column=2)

        def supplierRec(event):
            print("Supplier : customerRec method called")
            global pd 
            searchpd = supplierList.curselection()[0]
            pd = supplierList.get(searchpd)
            suppliername.delete(0, END)
            suppliername.insert(END, pd[0])
            supplierid.delete(0, END)
            supplierid.insert(END,pd[1])
            suppliernamefororders.delete(0, END)
            suppliernamefororders.insert(END, pd[2])
            gstnumber.delete(0, END)
            gstnumber.insert(END, pd[3])
            shiptoname.delete(0, END)
            shiptoname.insert(END, pd[4])
            contactnumber.delete(0, END)
            contactnumber.insert(END, pd[5])
            defaultordertype.delete(0, END)
            defaultordertype.insert(END, pd[6])
            defaultpaymentterms.delete(0, END)
            defaultpaymentterms.insert(END, pd[7])
            creditaccount.delete(0, END)
            creditaccount.insert(END, pd[8])
            department.delete(0, END)
            department.insert(END, pd[9])
            defaultpurchaseaccount.delete(0, END)
            defaultpurchaseaccount.insert(END, pd[10])
            defaultaccountforpayments.delete(0, END)
            defaultaccountforpayments.insert(END, pd[11])
            supplierbillingaddress.delete(0, END)
            supplierbillingaddress.insert(END, pd[12])
            ourshippingaddress.delete(0, END)
            ourshippingaddress.insert(END, pd[13])
            mobilenumber.delete(0, END)
            mobilenumber.insert(END, pd[14])
            telephonenumber.delete(0, END)
            telephonenumber.insert(END, pd[15])
            emailaddress.delete(0, END)
            emailaddress.insert(END, pd[16])
            faxnumber.delete(0, END)
            faxnumber.insert(END, pd[17])
            contactpersonname1.delete(0, END)
            contactpersonname1.insert(END, pd[18])
            contactpersonname2.delete(0, END)
            contactpersonname2.insert(END, pd[19])
            ordercomment1.delete(0, END)
            ordercomment1.insert(END, pd[20])
            ordercomment2.delete(0, END)
            ordercomment2.insert(END, pd[21])
            quotcomment1.delete(0, END)
            quotcomment1.insert(END, pd[22])
            quotcomment2.delete(0, END)
            quotcomment2.insert(END, pd[23])
            defaultjob.delete(0, END)
            defaultjob.insert(END, pd[24])
            bankname.delete(0, END)
            bankname.insert(END, pd[25])
            branchlocation.delete(0, END)
            branchlocation.insert(END, pd[26])
            bankaccountname.delete(0, END)
            bankaccountname.insert(END, pd[27])
            bankaccountnumber.delete(0, END)
            bankaccountnumber.insert(END, pd[28])
            bsb.delete(0, END)
            bsb.insert(END, pd[29])
            swiftcode.delete(0, END)
            swiftcode.insert(END, pd[30])
            notes.delete(0, END)
            notes.insert(END, pd[31])
            print("Supplier : customerRec method finished\n")

        scroll = Scrollbar(f2)
        scroll.grid(row=1, column=1, sticky='ns')
            
        scroll2 = Scrollbar(f2, orient=HORIZONTAL)
        scroll2.grid(row=2, column=0, sticky='ew')
            
        supplierList = Listbox(f2, width=60, height=28, font=('arial', 12, 'bold'), yscrollcommand=scroll.set, xscrollcommand=scroll2.set)
        
        supplierList.bind('<<ListboxSelect>>', supplierRec)
        supplierList.grid(row=1, column=0, padx=8)
            
        scroll.config(command=supplierList.yview)
        scroll2.config(command=supplierList.xview)


class DatabaseSupplier:
    def conn(self):
        print("Database : Connection method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "create table if not exists Supplier(Supplier_Name text, Supplier_Id text, Supplier_Name_For_Orders text, GST_Number text, Ship_To_Name text, Contact_Number text, Default_Order_Type text, Default_Payment_Terms text, Credit_Account text, Department text, Default_Purchase_Account text, Default_Account_For_Payments text, Supplier_Billing_Address text, Our_Shipping_Address text, Mobile_Number text, Telephone_Number text, Email_Address text, Fax_Number text, Contact_Person_Name_1 text, Contact_Person_Name_2 text, Order_Comment_1 text, Order_Comment_2 text, Quote_Comment_1 text, Quote_Comment_2 text, Default_Job text, Bank_Name text, Branch_Location text, Bank_Account_Name text, Bank_Account_Number text, BSB text, Swift_Code text, Notes text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : Connection method finished\n")
        
    def insert(self, SupplierName, Supplier_Id, Supplier_Name_For_Orders, GST_Number, Ship_To_Name, Contact_Number, Default_Order_Type, Default_Payment_Terms, Credit_Account, Department, Default_Purchase_Account, Default_Account_For_Payments, Supplier_Billing_Address, Our_Shipping_Address, Mobile_Number, Telephone_Number, Email_Address, Fax_Number, Contact_Person_Name_1, Contact_Person_Name_2, Order_Comment_1, Order_Comment_2, Quote_Comment_1, Quote_Comment_2, Default_Job, Bank_Name, Branch_Location, Bank_Account_Name, Bank_Account_Number, BSB, Swift_Code, Notes):
        print("Database : Insert method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "insert into Supplier values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, (SupplierName, Supplier_Id, Supplier_Name_For_Orders, GST_Number, Ship_To_Name, Contact_Number, Default_Order_Type, Default_Payment_Terms, Credit_Account, Department, Default_Purchase_Account, Default_Account_For_Payments, Supplier_Billing_Address, Our_Shipping_Address, Mobile_Number, Telephone_Number, Email_Address, Fax_Number, Contact_Person_Name_1, Contact_Person_Name_2, Order_Comment_1, Order_Comment_2, Quote_Comment_1, Quote_Comment_2, Default_Job, Bank_Name, Branch_Location, Bank_Account_Name, Bank_Account_Number, BSB, Swift_Code, Notes))
        con.commit()
        con.close()
        print("Database : Insert method finished\n")

    def show(self):
        print("Database : Show method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "select * from Supplier"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : Show method finished\n")
        return rows

    def delete(self, Supplier_Id):
        print("Database : Delete method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("delete from Supplier where Supplier_Id=?", (Supplier_Id,))
        con.commit()
        con.close()
        print("Database : Delete method finished\n")

    def search(self, Supplier_Id):
        print("Database : Search method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("select * from Supplier where Supplier_Id=?", (Supplier_Id))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Search method finished\n")
        return row

    def update(self, Supplier_Id=""):
        print("Database : Update method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("update Supplier set SupplierId=?", (Supplier_Id))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Update method finished\n")
