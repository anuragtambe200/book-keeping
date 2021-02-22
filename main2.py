# ==================================================Importing Packages=================================================
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from math import factorial
import parser
import sqlite3
import time

class DatabaseCustomer:
    def conn(self):
        print("Database : Connection method called")
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        query = "create table if not exists Customer(CustomerA text, CustomerID text, CustomerNI text, GSTNo text, ShipToN text, Contact Text, DefInvoiceType text, DefPaymentTerms text, CreditAcct text, Department text, DefSaleAcct text, DefAcctForReceipts text, CustomerBillingAddress text, CustomerShippingAddress text, MobileNo text, TelephoneNo text, EmailAddress text, FaxNo text, ContactPersonNone text, ContactPersonNtwo text, InvoiceCommentone text, InvoiceCommenttwo text, QuoteCommentone text, QuoteCommenttwo text, DefJob text, BankN text, BranchLocation text, BankAcctN text, BankAcctNo text, BSB text, SwiftCode text, Notes text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : Connection method finished\n")


    def insert(self, CustomerA, CustomerID, CustomerNI, GSTNo, ShipToN, Contact, DefInvoiceType, DefPaymentTerms, CreditAcct, Department, DefSaleAcct, DefAcctForReceipts, CustomerBillingAddress, CustomerShippingAddress, MobileNo, TelephoneNo, EmailAddress, FaxNo, ContactPersonNone, ContactPersonNtwo, InvoiceCommentone, InvoiceCommenttwo, QuoteCommentone, QuoteCommenttwo, DefJob, BankN, BranchLocation, BankAcctN, BankAcctNo, BSB, SwiftCode, Notes):
        print("Database : insert method called xxx")
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        query = "insert into Customer values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, (CustomerA, CustomerID, CustomerNI, GSTNo, ShipToN, Contact, DefInvoiceType, DefPaymentTerms, CreditAcct, Department, DefSaleAcct, DefAcctForReceipts, CustomerBillingAddress, CustomerShippingAddress, MobileNo, TelephoneNo, EmailAddress, FaxNo, ContactPersonNone, ContactPersonNtwo, InvoiceCommentone, InvoiceCommenttwo, QuoteCommentone, QuoteCommenttwo, DefJob, BankN, BranchLocation, BankAcctN, BankAcctNo, BSB, SwiftCode, Notes))
        con.commit()
        con.close()
        print("Database : insert method finished xxxx\n")

    def show(self):
        print("Database : show method called")
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        query = "select * from Customer"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : show method finished\n")
        return rows

    def delete(self, CustomerA):
        print("Database : delete method called", CustomerA)
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        cur.execute("delete from Customer where CustomerA=?", (CustomerA,))
        con.commit()
        con.close()
        print(CustomerA, "Database : delete method finished\n")

    def search(self, CustomerA="", CustomerID="", CustomerNI="", GSTNo="", Contact="", ShipToN="", DefInvoiceType="", DefPaymentTerms="", CreditAcct="", Department="", DefSaleAcct="", DefAcctForReceipts="", CustomerBillingAddress="", CustomerShippingAddress="", MobileNo="", TelephoneNo="", EmailAddress="", FaxNo="", ContactPersonNone="", ContactPersonNtwo="", InvoiceCommentone="", InvoiceCommenttwo="", QuoteCommentone="", QuoteCommenttwo="", DefJob="", BankN="", BranchLocation="", BankAcctN="", BankAcctNo="", BSB="", SwiftCode="", Notes=""):
        print("Database : search method called", CustomerID)
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        cur.execute("select * from Customer where CustomerA=? or CustomerID=?", (CustomerA, CustomerID))
        row = cur.fetchall()
        con.commit()
        con.close()
        print(CustomerID, "Database : search method finished\n")
        return row

    def update(self, CustomerA="", CustomerID="", CustomerNI="", GSTNo="", ShipToN="", DefInvoiceType="", DefPaymentTerms="", CreditAcct="", Department="", DefSaleAcct="", DefAcctForReceipts="", CustomerBillingAddress="", CustomerShippingAddress="", MobileNo="", TelephoneNo="", EmailAddress="", FaxNo="", ContactPersonNone="", ContactPersonNtwo="", InvoiceCommentone="", InvoiceCommenttwo="", QuoteCommentone="", QuoteCommenttwo="", DefJob="", BankN="", BranchLocation="", BankAcctN="", BankAcctNo="", BSB="", SwiftCode="", Notes=""):
        print("Database : update method called")
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        query = "insert into Customer values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute("update Customer set CustomerA=? or CustomerID=? or CustomerNI=? or GSTNo=? or ShipToN=? or Contact=? or DefInvoiceType=? or DefPaymentTermms=? or CreditAcct=? or Department=? or DefSaleAcct=? or DefAcctForReceipts=? or CustomerBillingAddress=? ot CustomerShippingAddress=? or MobileNo=? or TelephoneNo=? or FaxNo=? or ContactPeersonNone=? or ContactPersonNtwo=? or InvoiceCommentone=? or InvoiceCommenttwo=? or QuoteCommentone=? or QuoteCommenttwo=? or DefJob=? or BankN=? or BranchLocation=? or BankAcctN=? or BankAcctNo=? or BSB=? or SwiftCode=? or Notes=?, (CustomerN, CustomerID, CustomerNI, GSTNo, ShipToN, DefInvoiceType, DefPaymentTerms, CreditAcct, Department, DefSaleAcct, DefAcctForReceipts, CustomerBillingAddress, CustomerShippingAddress, MobileNo, TelephoneNo, EmailAddress, FaxNo, ContactPersonNone, ContactPersonNtwo, InvoiceCommentone, InvoiceCommenttwo, QuoteCommenttone, QuoteCommenttwo, DefJob, BankN, BranchLocation, BankAcctN, BankAcctNo, BSB, SwiftCode, Notes)")
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : update method finished\n")

#  class for Front end UI ( User Interface)
class Customers:
    def __init__(self, root):
        # ============================create object referance instance of DataBase class as p=============================
        DB = DatabaseCustomer()
        DB.conn()

        self.root = root
        self.root.title("Warehouse Inventry Sales Purchase Management System")
        self.root.geometry("1350x690+0+0")

        css = self.root
        
        f2 = ttk.LabelFrame(css, width=100, height=100)
        f2.grid(row=0, column=0, rowspan=24)

        f1 = ttk.LabelFrame(css, width=600, height=380)
        f1.grid(row=0, column=1)

        CustomerA = StringVar()
        CustomerID = StringVar()
        CustomerNI = StringVar()
        GSTNo = StringVar()
        ShipToN = StringVar()
        Contact = StringVar()
        DefInvoiceType = StringVar()
        DefPaymentTerms = StringVar()
        CreditAcct = StringVar()
        Department = StringVar()
        DefSaleAcct = StringVar()
        DefAcctForReceipts = StringVar()
        CustomerBillingAddress = StringVar()
        CustomerShippingAddress = StringVar()
        MobileNo = StringVar()
        TelephoneNo = StringVar()
        EmailAddress = StringVar()
        FaxNo = StringVar()
        ContactPersonN1 = StringVar()
        ContactPersonN2 = StringVar()
        InvoiceComment1 = StringVar()
        InvoiceComment2 = StringVar()
        QuoteComment1 = StringVar()
        QuoteComment2 = StringVar()
        DefJob = StringVar()
        BankN = StringVar()
        BranchLocation = StringVar()
        BankAcctN = StringVar()
        BankAcctNo = StringVar()
        BSB = StringVar()
        SwiftCode = StringVar()
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

            print("Customer : clear method finished\n")        

        def delete():
            print("Customer :database Delete method called")
            if CustomerA.get() != "":
                DB.delete(pd[0])
                clear()
                showInCustomerList() 
                print("Customer : database Delete method finished\n")
            if CustomerA.get() == "":
                DB.delete(pd[0])
                clear()
                showInCustomerList() 
                print("Customer : database Delete method finished\n")
        
        def close():
            close = messagebox.askokcancel("Book Keeping", "Are You Sure you want to exit?")
            if close > 0:
                css.destroy()
                return
        
        def search():
            print("Customer : search method called")
            CustomerList.delete(0,END)
            for row in DB.search(CustomerA.get(), CustomerID.get(), CustomerNI.get(), GSTNo.get(), ShipToN.get(), Contact.get(), DefInvoiceType.get(), DefPaymentTerms.get(), CreditAcct.get(), Department.get(), DefSaleAcct.get(), DefAcctForReceipts.get(), CustomerBillingAddress.get(), CustomerShippingAddress.get(), MobileNo.get(), TelephoneNo.get(), EmailAddress.get(), FaxNo.get(), ContactPersonN1.get(), ContactPersonN2.get(), InvoiceComment1.get(), InvoiceComment2.get(), QuoteComment1.get(), QuoteComment2.get(), DefJob.get(), BankN.get(), BranchLocation.get(), BankAcctN.get(), BankAcctNo.get(), BSB.get(), SwiftCode.get(), Notes.get()):
                CustomerList.insert(END, row, str(""))

            print("Customer : search method finished\n")

        def insert():
            print("Customer : Insert method called")
            if CustomerID.get() != 0:
                DB.insert(
                    CustomerA.get(), CustomerID.get(), CustomerNI.get(), GSTNo.get(), ShipToN.get(), 
                    Contact.get(), DefInvoiceType.get(), DefPaymentTerms.get(), CreditAcct.get(),
                    Department.get(), DefSaleAcct.get(), DefAcctForReceipts.get(), CustomerBillingAddress.get(),
                    CustomerShippingAddress.get(), MobileNo.get(), TelephoneNo.get(), EmailAddress.get(), FaxNo.get(), 
                    ContactPersonN1.get(), ContactPersonN2.get(), InvoiceComment1.get(), InvoiceComment2.get(), 
                    QuoteComment1.get(), QuoteComment2.get(), DefJob.get(), BankN.get(), BranchLocation.get(), 
                    BankAcctN.get(), BankAcctNo.get(), BSB.get(), SwiftCode.get(), Notes.get()
                    )

                CustomerList.delete(0, END)

                CustomerList.insert(
                    END, CustomerA.get(), CustomerID.get(), CustomerNI.get(), GSTNo.get(), ShipToN.get(), 
                    Contact.get(), DefInvoiceType.get(), DefPaymentTerms.get(), CreditAcct.get(), DefPaymentTerms.get(), 
                    Department.get(), DefSaleAcct.get(), DefAcctForReceipts.get(), CustomerBillingAddress.get(), 
                    CustomerShippingAddress.get(), MobileNo.get(), TelephoneNo.get(), EmailAddress.get(), FaxNo.get(), 
                    ContactPersonN1.get(), ContactPersonN2.get(), InvoiceComment1.get(), InvoiceComment2.get(), 
                    QuoteComment1.get(), QuoteComment2.get(), DefJob.get(), BankN.get(), BranchLocation.get(), 
                    BankAcctN.get(), BankAcctNo.get(), BSB.get(), SwiftCode.get(), Notes.get()
                    )

                showInCustomerList() # called showInCustomerList method after inserting the data record to database table
                clear()
                print("Customer : Insert method finished\n")
            else:
                messagebox.showerror("Book Keeping", "Enter Customer ID")

        def showInCustomerList():
            print("Customer : showInCustomerList method called")
            CustomerList.delete(0, END)
            for row in DB.show():
                CustomerList.insert(END, row, str(""))
            print("Customer : showInCustomerList method finished\n")


        Label(f2, text="Customer Name: ").grid(row=0, column=2)
        customername = Entry(f2, textvariable=CustomerA, font="bold")
        customername.grid(row=0, column=3)

        Label(f2, text="Customer ID: ").grid(row=0, column=4)
        customerid = Entry(f2, font="bold", textvariable=CustomerID)
        customerid.grid(row=0, column=5)

        Label(f2, text="Customer Name(For Invoices/Quotes): ").grid(row=1, column=2)
        customernameforinvoices_quotes = Entry(f2, font="bold", textvariable=CustomerNI)
        customernameforinvoices_quotes.grid(row=1, column=3)

        Label(f2, text="GST Number: ").grid(row=1, column=4)
        gstnumber = Entry(f2, font="bold", textvariable=GSTNo)
        gstnumber.grid(row=1, column=5)

        Checkbutton(f2, text="Reports Receipts: ").grid(row=2, column=2)

        Label(f2, text="Ship to Name: ").grid(row=3, column=2)
        shiptoname = Entry(f2, font="bold", textvariable=ShipToN)
        shiptoname.grid(row=3, column=3)

        Label(f2, text="Contact Number: ").grid(row=3, column=4)
        contactnumber = Entry(f2, font="bold", textvariable=Contact)
        contactnumber.grid(row=3, column=5)

        Label(f2, text="Default Invoice Type: ").grid(row=4, column=2)
        defaultinvoicetype = Entry(f2, font="bold", textvariable=DefInvoiceType)
        defaultinvoicetype.grid(row=4, column=3)

        Label(f2, text="Default Payment Terms: ").grid(row=5, column=2)
        defaultpaymentterms = Entry(f2, textvariable=DefPaymentTerms, font="bold")
        defaultpaymentterms.grid(row=5, column=3)

        Label(f2, text="Credit Account: ").grid(row=6, column=2)
        creditaccount = Entry(f2, font="bold", textvariable=CreditAcct)
        creditaccount.grid(row=6, column=3)

        Label(f2, text="Departmenet: ").grid(row=6, column=4)
        department = Entry(f2, font="bold", textvariable=Department)
        department.grid(row=6, column=5)

        Label(f2, text="Default Sale Account: ").grid(row=7, column=2)
        defaultsaleaccount = Entry(f2, font="bold", textvariable=DefSaleAcct)
        defaultsaleaccount.grid(row=7, column=3)

        Label(f2, text="Default Account For Receipts: ").grid(row=8, column=2)
        defaultaccountforreceipts = Entry(f2, font="bold", textvariable=DefAcctForReceipts)
        defaultaccountforreceipts.grid(row=8, column=3)

        Label(f2, text="Customer Billing Address: ").grid(row=9, column=2)
        customerbillingaddress = Entry(f2, font="bold", textvariable=CustomerBillingAddress)
        customerbillingaddress.grid(row=9, column=3)

        Label(f2, text="Customer Shipping Address: ").grid(row=9, column=4)
        customershippingaddress = Entry(f2, font="bold", textvariable=CustomerShippingAddress)
        customershippingaddress.grid(row=9, column=5)

        Label(f2, text="Cell / Mobile Number: ").grid(row=10, column=2)
        mobilenumber = Entry(f2, font="bold", textvariable=MobileNo)
        mobilenumber.grid(row=10, column=3)

        Label(f2, text="Telephone Number: ").grid(row=10, column=4)
        telephonenumber = Entry(f2, font="bold", textvariable=TelephoneNo)
        telephonenumber.grid(row=10, column=5)

        Label(f2, text="Email Address: ").grid(row=11, column=2)
        emailaddress = Entry(f2, font="bold", textvariable=EmailAddress)
        emailaddress.grid(row=11, column=3)

        Label(f2, text="Fax Number: ").grid(row=11, column=4)
        faxnumber = Entry(f2, font="bold", textvariable=FaxNo)
        faxnumber.grid(row=11, column=5)

        Label(f2, text="Contact Person Name 1: ").grid(row=12, column=2)
        contactpersonname1 = Entry(f2, font="bold", textvariable=ContactPersonN1)
        contactpersonname1.grid(row=12, column=3)

        Label(f2, text="Contact Person Name 2: ").grid(row=12, column=4)
        contactpersonname2 = Entry(f2, font="bold", textvariable=ContactPersonN2)
        contactpersonname2.grid(row=12, column=5)

        Label(f2, text="Invoice Comment 1: ").grid(row=13, column=2)
        invoicecomment1 = Entry(f2, font="bold", textvariable=InvoiceComment1)
        invoicecomment1.grid(row=13, column=3)

        Label(f2, text="Invoice Comment 2: ").grid(row=14, column=2)
        invoicecomment2 = Entry(f2, font="bold", textvariable=InvoiceComment2)
        invoicecomment2.grid(row=14, column=3)

        Label(f2, text="Quote Comment 1: ").grid(row=15, column=2)
        quotcomment1 = Entry(f2, font="bold", textvariable=QuoteComment1)
        quotcomment1.grid(row=15, column=3)

        Label(f2, text="Quote Comment 2: ").grid(row=16, column=2)
        quotcomment2 = Entry(f2, font="bold", textvariable=QuoteComment2)
        quotcomment2.grid(row=16, column=3)

        Label(f2, text="Default Job: ").grid(row=17, column=2)
        defaultjob = Entry(f2, font="bold", textvariable=DefJob)
        defaultjob.grid(row=17, column=3)

        Checkbutton(f2, text="Inactive Customer ", justify=LEFT).grid(row=18, column=2)

        Label(f2, text="Bank Name: ").grid(row=19, column=2)
        bankname = Entry(f2, font="bold", textvariable=BankN)
        bankname.grid(row=19, column=3)

        Label(f2, text="Branch Location: ").grid(row=19, column=4)
        branchlocation = Entry(f2, font="bold", textvariable=BranchLocation)
        branchlocation.grid(row=19, column=5)

        Label(f2, text="Bank Account Name: ").grid(row=20, column=2)
        bankaccountname = Entry(f2, font="bold", textvariable=BankAcctN)
        bankaccountname.grid(row=20, column=3)

        Label(f2, text="Bank Account Number: ").grid(row=20, column=4)
        bankaccountnumber = Entry(f2, font="bold", textvariable=BankAcctNo)
        bankaccountnumber.grid(row=20, column=5)

        Label(f2, text="BSB: ").grid(row=21, column=2)
        bsb = Entry(f2, font="bold", textvariable=BSB)
        bsb.grid(row=21, column=3)

        Label(f2, text="Swift Code: ").grid(row=21, column=4)
        swiftcode = Entry(f2, font="bold", textvariable=SwiftCode)
        swiftcode.grid(row=21, column=5)

        Label(f2, text="Notes: ").grid(row=22, column=2)
        notes = Entry(f2, font="bold", textvariable=Notes)
        notes.grid(row=22, column=3)

        # ============ADD BUTTON TO OPERATION FRAME=====================================================================
        buttonSaveData = Button(f2, text='Save', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=insert)
        buttonSaveData.grid(row=23, column=2)

        buttonShowData = Button(f2, text='Show Data', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=showInCustomerList)
        buttonShowData.grid(row=23, column=3)

        buttonClearData = Button(f2, text='Reset', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=clear)
        buttonClearData.grid(row=23, column=4)

        buttonDeleteData = Button(f2, text='Delete', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=delete)
        buttonDeleteData.grid(row=23, column=5)

        buttonsearchData = Button(f2, text='Search', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=search)
        buttonsearchData.grid(row=23, column=6)

        buttonClose = Button(f2, text='Close', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=close)
        buttonClose.grid(row=23, column=7)

        # add to scroll bar

        def customerRec(event):
            print("Customer : customerRec method called")
            
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
            
            print("Customer : customerRec method finished\n")

        scroll = ttk.Scrollbar(f1)
        scroll.grid(row=0, column=1, sticky='ns')

        scroll2 = ttk.Scrollbar(f1, orient=HORIZONTAL)
        scroll2.grid(row=1, column=0, sticky='ew')

        CustomerList = Listbox(f1, width=40, height=26, font=('arial', 12, 'bold'), xscrollcommand=scroll2.set, yscrollcommand=scroll.set)
        CustomerList.bind('<<ListboxSelect>>', customerRec)
        CustomerList.grid(row=0, column=0)

        scroll.config(command=CustomerList.yview)
        scroll2.config(command=CustomerList.xview)


        css.mainloop()



if __name__ == "__main__":
    root = Tk()
    application = Customers(root)
    root.mainloop()

    # root = Tk()
    # root.title("Book Keeping - Customer / sales")
    # root.geometry("1350x690+0+0")

    # ttk.Button(root, text="Customers", command=customerform).grid(row=0, column=0)
    # ttk.Button(root, text="Sales").grid(row=0, column=1)

    # root.mainloop()
        
accounting = Tk()
accounting.title("Book Keeping")
accounting.geometry("1350x690+0+0")
accounting.resizable(height=False, width=False)
# accounting.iconbitmap(r"C:\\Users\\Mahaveer\Desktop\\Photos")

acc = Frame(accounting)
acc.grid()

def cus():
    import Customers

# ==================================================Defining Commands==================================


# Command for Help and About this app

def help_about():
    ha = Tk()
    ha.title("Book Keeping - About / Help")
    ha.resizable(height=False, width=False)
    ha.geometry("1265x725+0+0")
    ha.iconbitmap(r'C:\\Users\\Mahaveer\Desktop\\Photos')


    def about():
        abouts = Tk()
        abouts.title("Book Keeping - About / Help - About")
        abouts.resizable(height=False, width=False)
        abouts.geometry("1265x725+0+0")
        abouts.iconbitmap(r'C:\\Users\\Mahaveer\Desktop\\Photos')

        Label(abouts, text='''Book Keeping \n Version 1.0 \n Creator - Anurag Tambe \n Date Created - XX XX 2020''', font=20, justify=CENTER).grid(row=0, column=0)

        abouts.mainloop()
        
    def helps():
        root1 = Tk()
        root1.title("Book Keeping - About / Help - Help")
        root1.resizable(height=False, width=False)
        root1.geometry("1265x725+0+0")
        root1.iconbitmap(r'C:\\Users\\Mahaveer\Desktop\\Photos')

        Labe1l = Label(root1, text='''You are on Right Platform Now''', font=20, justify=LEFT).grid(row=0, column=0)

        root1.mainloop()

    Button(ha, height=1, width=17, padx=16, bd=8, font=('arial', 15, 'bold'), text="Help", command=helps
            ).grid(row=0, column=0, pady=10, padx=10)

    Button(ha, height=1, width=17, padx=16, bd=8, font=('arial', 15, 'bold'), text="About",
            command=about).grid(row=0, column=1, pady=10, padx=10)

    ha.mainloop()

    # Command to Define Customers Form
    
                
# ==================================================Command for Menu Bar===============================

menu = Menu(accounting)

menu.add_cascade(label="Products")
menu.add_cascade(label="Customers")
menu.add_cascade(label="Suppliers / Purchase")
menu.add_cascade(label="Reports")
menu.add_cascade(label="Backup")
menu.add_cascade(label="Verify Books")
menu.add_cascade(label="Calculator")
menu.add_cascade(label="Alerts")
menu.add_cascade(label="Book Details")
menu.add_cascade(label="Log Out")
menu.add_cascade(label="App Settings")
menu.add_cascade(label="Book Settings")
menu.add_cascade(label="Help / About")
menu.add_cascade(label="Exit", command=accounting.destroy)

accounting.config(menu=menu)

# ======================= Command for Buttons =================================

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Products / Services").grid(row=3, column=0, pady=10)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Suppliers / Purchase").grid(row=4, column=0)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Employees").grid(row=2, column=1)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Administration") \
#     .grid(row=0, column=1, padx=10)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="General Journal").grid(row=3,
#                                                                                             column=2)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Accounts").grid(row=0, column=2)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Reports").grid(row=2, column=4)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Lager Entries").grid(row=4,
#                                                                                             column=2)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Current P & L").grid(row=1,
#                                                                                             column=1)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Alerts").grid(row=0, column=3,
#                                                                                     padx=10)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="General Help").grid(row=1, column=4
#                                                                                             )

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="About / Help") \
#     .grid(row=0, column=4)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Customer / Sales").grid(row=1, column=0, pady=10)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Banking").grid(row=1, column=2)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Share Portfolio").grid(row=4,
#                                                                                             column=1)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Data Processing").grid(row=1,
#                                                                                             column=3)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Jobs").grid(row=3, column=1)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Book Details").grid(row=0, column=0
#                                                                                             )

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Expense / Budget").grid(row=2,
#                                                                                                 column=2)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Current / Balance").grid(row=2,
#                                                                                                 column=0)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Drop Box").grid(row=2, column=3)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Sync").grid(row=3, column=3)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Search").grid(row=4, column=3)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Rate This App").grid(row=3,
#                                                                                             column=4)

# Button(accounting, height=1, width=15, padx=16, bd=8, font=15, text="Change Account Settings").grid(row=4, column=4)

# ========================End of this app================================================================

accounting.mainloop()
#========================= Add Backend database for Customer ============================================================
