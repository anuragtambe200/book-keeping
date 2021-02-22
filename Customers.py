from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3


class Customer:
    def __init__(self, root):
        DB = DatabaseCustomer()
        DB.conn()

        self.root = root
        self.root.title("Book Keeping - Customer")
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

        css = second_frame
        
        f2 = ttk.Frame(css, width=100, height=100)
        f2.grid(row=0, column=0)

        f1 = ttk.Frame(css, width=600, height=380)
        f1.grid(row=0, column=1, padx=20)

        f3 = ttk.Frame(css, width=10, height=10)
        f3.grid(row=1, column=0)

        Customer_Name = StringVar()
        Customer_Id = StringVar()
        Customer_Name_For_Invoices_Quotes = StringVar()
        GST_Number = StringVar()
        Ship_To_Name = StringVar()
        Contact = StringVar()
        Default_Invoice_Type = StringVar()
        Default_Payment_Terms = StringVar()
        Credit_Account = StringVar()
        Department = StringVar()
        Default_Sale_Account = StringVar()
        Default_Account_For_Receipts = StringVar()
        Customer_Billing_Address = StringVar()
        Customer_Shipping_Address = StringVar()
        Mobile_Number = StringVar()
        Telephone_Number = StringVar()
        Email_Address = StringVar()
        Fax_Number = StringVar()
        Contact_Person_Name_1 = StringVar()
        Contact_Person_Name_2 = StringVar()
        Invoice_Comment_1 = StringVar()
        Invoice_Comment_2 = StringVar()
        Quote_Comment_1 = StringVar()
        Quote_Comment_2 = StringVar()
        Default_Job = StringVar()
        Bank_Name = StringVar()
        Branch_Location = StringVar()
        Bank_Account_Name = StringVar()
        Bank_Account_Number = StringVar()
        BSB = StringVar()
        Swift_Code = StringVar()
        Notes = StringVar()

        def clear():
            print("Customer : Clear method called")
            customername.delete(0, END)
            customerid.delete(0, END)
            customernameforinvoices_quotes.delete(0, END)
            gstnumber.delete(0, END)
            shiptoname.delete(0, END)
            contactnumber.delete(0, END)
            defaultinvoicetype.delete(0, END)
            defaultpaymentterms.delete(0, END)
            creditaccount.delete(0, END)
            department.delete(0, END)
            defaultsaleaccount.delete(0, END)
            defaultaccountforreceipts.delete(0, END)
            customerbillingaddress.delete(0, END)
            customershippingaddress.delete(0, END)
            mobilenumber.delete(0, END)
            telephonenumber.delete(0, END)
            emailaddress.delete(0, END)
            faxnumber.delete(0, END)
            contactpersonname1.delete(0, END)
            contactpersonname2.delete(0, END)
            invoicecomment1.delete(0, END)
            invoicecomment2.delete(0, END)
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
            print("Customer : Clear method finished\n")        

        def delete():
            print("Customer : Delete method called")
            DB.delete(pd[1])
            clear()
            showInCustomerList() 
            print("Customer : Delete method finished\n")
            
        def search():
            print("Customer : Search method called")
            CustomerList.delete(0,END)
            for row in DB.search(Customer_Id.get()):
                CustomerList.insert(END, row, str(""))
            print("Customer : Search method finished\n")

        def insert():
            print("Customer : Insert method called")
            if Customer_Id.get() != 0:
                DB.insert(
                    Customer_Name.get(), Customer_Id.get(), Customer_Name_For_Invoices_Quotes.get(), GST_Number.get(), Ship_To_Name.get(), 
                    Contact.get(), Default_Invoice_Type.get(), Default_Payment_Terms.get(), Credit_Account.get(),
                    Department.get(), Default_Sale_Account.get(), Default_Account_For_Receipts.get(), Customer_Billing_Address.get(),
                    Customer_Shipping_Address.get(), Mobile_Number.get(), Telephone_Number.get(), Email_Address.get(), Fax_Number.get(), 
                    Contact_Person_Name_1.get(), Contact_Person_Name_2.get(), Invoice_Comment_1.get(), Invoice_Comment_2.get(), 
                    Quote_Comment_1.get(), Quote_Comment_2.get(), Default_Job.get(), Bank_Name.get(), Branch_Location.get(), 
                    Bank_Account_Name.get(), Bank_Account_Number.get(), BSB.get(), Swift_Code.get(), Notes.get()
                )
                CustomerList.delete(0, END)
                CustomerList.insert(
                    END, Customer_Name.get(), Customer_Id.get(), Customer_Name_For_Invoices_Quotes.get(), GST_Number.get(), Ship_To_Name.get(), 
                    Contact.get(), Default_Invoice_Type.get(), Default_Payment_Terms.get(), Credit_Account.get(), Default_Payment_Terms.get(), 
                    Department.get(), Default_Sale_Account.get(), Default_Account_For_Receipts.get(), Customer_Billing_Address.get(), 
                    Customer_Shipping_Address.get(), Mobile_Number.get(), Telephone_Number.get(), Email_Address.get(), Fax_Number.get(), 
                    Contact_Person_Name_1.get(), Contact_Person_Name_2.get(), Invoice_Comment_1.get(), Invoice_Comment_2.get(), 
                    Quote_Comment_1.get(), Quote_Comment_2.get(), Default_Job.get(), Bank_Name.get(), Branch_Location.get(), 
                    Bank_Account_Name.get(), Bank_Account_Number.get(), BSB.get(), Swift_Code.get(), Notes.get()
                )
                showInCustomerList() # called showInCustomerList method after inserting the data record to database table
                clear()
                print("Customer : Insert method finished\n")
            else:
                messagebox.showerror("Book Keeping", "Enter Customer ID")

        def showInCustomerList():
            print("Customer : ShowInCustomerList method called")
            CustomerList.delete(0, END)
            for row in DB.show():
                CustomerList.insert(END, row, str(""))
            print("Customer : ShowInCustomerList method finished\n")

        def update():
            print("Customer : Update method called")
            print("pd[1]", pd[1])
            DB.delete(pd[1])
            DB.insert(
                Customer_Name.get(), Customer_Id.get(), Customer_Name_For_Invoices_Quotes.get(), GST_Number.get(), Ship_To_Name.get(), 
                Contact.get(), Default_Invoice_Type.get(), Default_Payment_Terms.get(), Credit_Account.get(),
                Department.get(), Default_Sale_Account.get(), Default_Account_For_Receipts.get(), Customer_Billing_Address.get(),
                Customer_Shipping_Address.get(), Mobile_Number.get(), Telephone_Number.get(), Email_Address.get(), Fax_Number.get(), 
                Contact_Person_Name_1.get(), Contact_Person_Name_2.get(), Invoice_Comment_1.get(), Invoice_Comment_2.get(), 
                Quote_Comment_1.get(), Quote_Comment_2.get(), Default_Job.get(), Bank_Name.get(), Branch_Location.get(), 
                Bank_Account_Name.get(), Bank_Account_Number.get(), BSB.get(), Swift_Code.get(), Notes.get()
            )
            CustomerList.delete(0, END)
            CustomerList.insert(
                END, (Customer_Name.get(), Customer_Id.get(), Customer_Name_For_Invoices_Quotes.get(), GST_Number.get(), Ship_To_Name.get(), 
                Contact.get(), Default_Invoice_Type.get(), Default_Payment_Terms.get(), Credit_Account.get(), Default_Payment_Terms.get(), 
                Department.get(), Default_Sale_Account.get(), Default_Account_For_Receipts.get(), Customer_Billing_Address.get(), 
                Customer_Shipping_Address.get(), Mobile_Number.get(), Telephone_Number.get(), Email_Address.get(), Fax_Number.get(), 
                Contact_Person_Name_1.get(), Contact_Person_Name_2.get(), Invoice_Comment_1.get(), Invoice_Comment_2.get(), 
                Quote_Comment_1.get(), Quote_Comment_2.get(), Default_Job.get(), Bank_Name.get(), Branch_Location.get(), 
                Bank_Account_Name.get(), Bank_Account_Number.get(), BSB.get(), Swift_Code.get(), Notes.get())
            )
            showInCustomerList()
            clear()
            print("Customer : Update method finished")

        Label(f2, text="Customer Name: ").grid(row=0, column=2)
        customername = Entry(f2, textvariable=Customer_Name, font="bold")
        customername.grid(row=0, column=3)

        Label(f2, text="Customer ID: ").grid(row=0, column=4)
        customerid = Entry(f2, font="bold", textvariable=Customer_Id)
        customerid.grid(row=0, column=5)

        Label(f2, text="Customer Name(For Invoices/Quotes): ").grid(row=1, column=2)
        customernameforinvoices_quotes = Entry(f2, font="bold", textvariable=Customer_Name_For_Invoices_Quotes)
        customernameforinvoices_quotes.grid(row=1, column=3)

        Label(f2, text="GST Number: ").grid(row=1, column=4)
        gstnumber = Entry(f2, font="bold", textvariable=GST_Number)
        gstnumber.grid(row=1, column=5)

        Checkbutton(f2, text="Reports Receipts: ").grid(row=2, column=2)

        Label(f2, text="Ship to Name: ").grid(row=3, column=2)
        shiptoname = Entry(f2, font="bold", textvariable=Ship_To_Name)
        shiptoname.grid(row=3, column=3)

        Label(f2, text="Contact Number: ").grid(row=3, column=4)
        contactnumber = Entry(f2, font="bold", textvariable=Contact)
        contactnumber.grid(row=3, column=5)

        Label(f2, text="Default Invoice Type: ").grid(row=4, column=2)
        defaultinvoicetype = Entry(f2, font="bold", textvariable=Default_Invoice_Type)
        defaultinvoicetype.grid(row=4, column=3)

        Label(f2, text="Default Payment Terms: ").grid(row=5, column=2)
        defaultpaymentterms = Entry(f2, textvariable=Default_Payment_Terms, font="bold")
        defaultpaymentterms.grid(row=5, column=3)

        Label(f2, text="Credit Account: ").grid(row=6, column=2)
        creditaccount = Entry(f2, font="bold", textvariable=Credit_Account)
        creditaccount.grid(row=6, column=3)

        Label(f2, text="Departmenet: ").grid(row=6, column=4)
        department = Entry(f2, font="bold", textvariable=Department)
        department.grid(row=6, column=5)

        Label(f2, text="Default Sale Account: ").grid(row=7, column=2)
        defaultsaleaccount = Entry(f2, font="bold", textvariable=Default_Sale_Account)
        defaultsaleaccount.grid(row=7, column=3)

        Label(f2, text="Default Account For Receipts: ").grid(row=8, column=2)
        defaultaccountforreceipts = Entry(f2, font="bold", textvariable=Default_Account_For_Receipts)
        defaultaccountforreceipts.grid(row=8, column=3)

        Label(f2, text="Customer Billing Address: ").grid(row=9, column=2)
        customerbillingaddress = Entry(f2, font="bold", textvariable=Customer_Billing_Address)
        customerbillingaddress.grid(row=9, column=3)

        Label(f2, text="Customer Shipping Address: ").grid(row=9, column=4)
        customershippingaddress = Entry(f2, font="bold", textvariable=Customer_Shipping_Address)
        customershippingaddress.grid(row=9, column=5)

        Label(f2, text="Cell / Mobile Number: ").grid(row=10, column=2)
        mobilenumber = Entry(f2, font="bold", textvariable=Mobile_Number)
        mobilenumber.grid(row=10, column=3)

        Label(f2, text="Telephone Number: ").grid(row=10, column=4)
        telephonenumber = Entry(f2, font="bold", textvariable=Telephone_Number)
        telephonenumber.grid(row=10, column=5)

        Label(f2, text="Email Address: ").grid(row=11, column=2)
        emailaddress = Entry(f2, font="bold", textvariable=Email_Address)
        emailaddress.grid(row=11, column=3)

        Label(f2, text="Fax Number: ").grid(row=11, column=4)
        faxnumber = Entry(f2, font="bold", textvariable=Fax_Number)
        faxnumber.grid(row=11, column=5)

        Label(f2, text="Contact Person Name 1: ").grid(row=12, column=2)
        contactpersonname1 = Entry(f2, font="bold", textvariable=Contact_Person_Name_1)
        contactpersonname1.grid(row=12, column=3)

        Label(f2, text="Contact Person Name 2: ").grid(row=12, column=4)
        contactpersonname2 = Entry(f2, font="bold", textvariable=Contact_Person_Name_2)
        contactpersonname2.grid(row=12, column=5)

        Label(f2, text="Invoice Comment 1: ").grid(row=13, column=2)
        invoicecomment1 = Entry(f2, font="bold", textvariable=Invoice_Comment_1)
        invoicecomment1.grid(row=13, column=3)

        Label(f2, text="Invoice Comment 2: ").grid(row=14, column=2)
        invoicecomment2 = Entry(f2, font="bold", textvariable=Invoice_Comment_2)
        invoicecomment2.grid(row=14, column=3)

        Label(f2, text="Quote Comment 1: ").grid(row=15, column=2)
        quotcomment1 = Entry(f2, font="bold", textvariable=Quote_Comment_1)
        quotcomment1.grid(row=15, column=3)

        Label(f2, text="Quote Comment 2: ").grid(row=16, column=2)
        quotcomment2 = Entry(f2, font="bold", textvariable=Quote_Comment_2)
        quotcomment2.grid(row=16, column=3)

        Label(f2, text="Default Job: ").grid(row=17, column=2)
        defaultjob = Entry(f2, font="bold", textvariable=Default_Job)
        defaultjob.grid(row=17, column=3)

        Checkbutton(f2, text="Inactive Customer ", justify=LEFT).grid(row=18, column=2)

        Label(f2, text="Bank Name: ").grid(row=19, column=2)
        bankname = Entry(f2, font="bold", textvariable=Bank_Name)
        bankname.grid(row=19, column=3)

        Label(f2, text="Branch Location: ").grid(row=19, column=4)
        branchlocation = Entry(f2, font="bold", textvariable=Branch_Location)
        branchlocation.grid(row=19, column=5)

        Label(f2, text="Bank Account Name: ").grid(row=20, column=2)
        bankaccountname = Entry(f2, font="bold", textvariable=Bank_Account_Name)
        bankaccountname.grid(row=20, column=3)

        Label(f2, text="Bank Account Number: ").grid(row=20, column=4)
        bankaccountnumber = Entry(f2, font="bold", textvariable=Bank_Account_Number)
        bankaccountnumber.grid(row=20, column=5)

        Label(f2, text="BSB: ").grid(row=21, column=2)
        bsb = Entry(f2, font="bold", textvariable=BSB)
        bsb.grid(row=21, column=3)

        Label(f2, text="Swift Code: ").grid(row=21, column=4)
        swiftcode = Entry(f2, font="bold", textvariable=Swift_Code)
        swiftcode.grid(row=21, column=5)

        Label(f2, text="Notes: ").grid(row=22, column=2)
        notes = Entry(f2, font="bold", textvariable=Notes)
        notes.grid(row=22, column=3)

        buttonSaveData = Button(f3, text='Save', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=insert)
        buttonSaveData.grid(row=0, column=0, pady=10)

        buttonShowData = Button(f3, text='Show Data', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=showInCustomerList)
        buttonShowData.grid(row=0, column=1, padx=10, pady=10)

        buttonClearData = Button(f3, text='Reset', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=clear)
        buttonClearData.grid(row=0, column=2, pady=10)

        buttonDeleteData = Button(f3, text='Delete', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=delete)
        buttonDeleteData.grid(row=1, column=0)

        buttonsearchData = Button(f3, text='Search', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=search)
        buttonsearchData.grid(row=1, column=1, padx=10)

        buttonUpdate = Button(f3, text='Update', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=update)
        buttonUpdate.grid(row=1, column=2)

        def customerRec(event):
            print("Customer : CustomerRec method called")
            global pd
            searchpd = CustomerList.curselection()[0]
            pd = CustomerList.get(searchpd)
            customername.delete(0, END)
            customername.insert(END, pd[0])
            customerid.delete(0, END)
            customerid.insert(END,pd[1])
            customernameforinvoices_quotes.delete(0, END)
            customernameforinvoices_quotes.insert(END, pd[2])
            gstnumber.delete(0, END)
            gstnumber.insert(END, pd[3])
            shiptoname.delete(0, END)
            shiptoname.insert(END, pd[4])
            contactnumber.delete(0, END)
            contactnumber.insert(END, pd[5])
            defaultinvoicetype.delete(0, END)
            defaultinvoicetype.insert(END, pd[6])
            defaultpaymentterms.delete(0, END)
            defaultpaymentterms.insert(END, pd[7])
            creditaccount.delete(0, END)
            creditaccount.insert(END, pd[8])
            department.delete(0, END)
            department.insert(END, pd[9])
            defaultsaleaccount.delete(0, END)
            defaultsaleaccount.insert(END, pd[10])
            defaultaccountforreceipts.delete(0, END)
            defaultaccountforreceipts.insert(END, pd[11])
            customerbillingaddress.delete(0, END)
            customerbillingaddress.insert(END, pd[12])
            customershippingaddress.delete(0, END)
            customershippingaddress.insert(END, pd[13])
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
            invoicecomment1.delete(0, END)
            invoicecomment1.insert(END, pd[20])
            invoicecomment2.delete(0, END)
            invoicecomment2.insert(END, pd[21])
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
            print("Customer : CustomerRec method finished\n")

        scroll = Scrollbar(f1)
        scroll.grid(row=0, column=1, sticky='ns')

        scroll2 = Scrollbar(f1, orient=HORIZONTAL)
        scroll2.grid(row=1, column=0, sticky='ew')

        CustomerList = Listbox(f1, width=60, height=26, font=('arial', 12, 'bold'), xscrollcommand=scroll2.set, yscrollcommand=scroll.set)
        CustomerList.bind('<<ListboxSelect>>', customerRec)
        CustomerList.grid(row=0, column=0)

        scroll.config(command=CustomerList.yview)
        scroll2.config(command=CustomerList.xview)

        css.mainloop()


class DatabaseCustomer:
    def conn(self):
        print("Database : Connection method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "create table if not exists Customer(Customer_Name text, Customer_Id text, Customer_Name_For_Invoices_Quotes text, GST_Number text, Ship_To_Name text, Contact Text, Default_Invoice_Type text, Default_Payment_Terms text, Credit_Account text, Department text, Default_Sale_Account text, Default_Account_For_Receipts text, Customer_Billing_Address text, Customer_Shipping_Address text, Mobile_Number text, Telephone_Number text, Email_Address text, Fax_Number text, Contact_Person_Name_1 text, Contact_Person_Name_2 text, Invoice_Comment_1 text, Invoice_Comment_2 text, Quote_Comment_1 text, Quote_Comment_2 text, Default_Job text, Bank_Name text, Branch_Location text, Bank_Account_Name text, Bank_Account_Number text, BSB text, Swift_Code text, Notes text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : Connection method finished\n")

    def insert(self, Customer_Name, Customer_Id, Customer_Name_For_Invoices_Quotes, GST_Number, Ship_To_Name, Contact, Default_Invoice_Type, Default_Payment_Terms, Credit_Account, Department, Default_Sale_Account, Default_Account_For_Receipts, Customer_Billing_Address, Customer_Shipping_Address, Mobile_Number, Telephone_Number, Email_Address, Fax_Number, Contact_Person_Name_1, Contact_Person_Name_2, Invoice_Comment_1, Invoice_Comment_2, Quote_Comment_1, Quote_Comment_2, Default_Job, Bank_Name, Branch_Location, Bank_Account_Name, Bank_Account_Number, BSB, Swift_Code, Notes):
        print("Database : Insert method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "insert into Customer values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, (Customer_Name, Customer_Id, Customer_Name_For_Invoices_Quotes, GST_Number, Ship_To_Name, Contact, Default_Invoice_Type, Default_Payment_Terms, Credit_Account, Department, Default_Sale_Account, Default_Account_For_Receipts, Customer_Billing_Address, Customer_Shipping_Address, Mobile_Number, Telephone_Number, Email_Address, Fax_Number, Contact_Person_Name_1, Contact_Person_Name_2, Invoice_Comment_1, Invoice_Comment_2, Quote_Comment_1, Quote_Comment_2, Default_Job, Bank_Name, Branch_Location, Bank_Account_Name, Bank_Account_Number, BSB, Swift_Code, Notes))
        con.commit()
        con.close()
        print("Database : Insert method finished\n")

    def show(self):
        print("Database : Show method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "select * from Customer"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : Show method finished\n")
        return rows

    def delete(self, Customer_Id):
        print("Database : Delete method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("delete from Customer where Customer_Id=?", (Customer_Id,))
        con.commit()
        con.close()
        print("Database : Delete method finished\n")

    def search(self, Customer_Id=""):
        print("Database : Search method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("select * from Customer where Customer_Id=?", (Customer_Id))
        row = cur.fetchall()
        con.commit()
        con.close()
        print(Customer_Id, "Database : Search method finished\n")
        return row

    def update(self, Customer_Id=""):
        print("Database : Update method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("update Customer set Customer_Id=?", (Customer_Id))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Update method finished\n")
