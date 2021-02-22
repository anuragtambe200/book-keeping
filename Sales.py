from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from itertools import chain
from Sale_Line_Item import SaleLineItem
from Sale_Line_Item import DatabaseSaleItemList
from Products import Products
from Products import DatabaseProducts
from Customers import Customer
from Customers import DatabaseCustomer

class Sales:
    def __init__(self, root):
        DB = DatabaseSales()
        DB.conn()

        self.root = root
        self.root.title("Book Keeping - Customer / Sales - Sales")
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
        
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        Customer_Name = StringVar()
        Invoice_Number = StringVar()
        Invoice_Type = StringVar()
        Sale_Date = StringVar()
        Due_Date = StringVar()
        Sale_Description = StringVar()
        INR_Total = StringVar()
        INR_Balance_Due = StringVar()
        Ex_Tax = StringVar()
        Bill_To_Address = StringVar()
        Ship_To_Address = StringVar()
        Invoice_Comments = StringVar()
        Customer_Reference = StringVar()
        Ship_To_Name = StringVar()
        Shipment_Date = StringVar()
        Notes = StringVar()
        Salesperson = StringVar()
        Department = StringVar()

        f2 = ttk.Frame(home, width=100, height=100)
        f2.grid(row=0, column=0, padx=0)

        f1 = ttk.Frame(home, width=600, height=380)
        f1.grid(row=0, column=1, padx=20)

        f3 = ttk.Frame(home, width=10, height=10)
        f3.grid(row=1, column=0)

        def clear():
            print("Sales : Clear method called")
            customername.delete(0, END)
            invoicenumber.delete(0, END)
            invoicetype.delete(0, END)
            saledate.delete(0, END)
            duedate.delete(0, END)
            saledescription.delete(0, END)
            inrtotal.delete(0, END)
            inrbalancedue.delete(0, END)
            extax.delete(0, END)
            billtoaddress.delete(0, END)
            shiptoaddress.delete(0, END)
            invoicecomments.delete(0, END)
            customerreference.delete(0, END)
            shiptoname.delete(0, END)
            shipmentdate.delete(0, END)
            notes.delete(0, END)
            salesperson.delete(0, END)
            department.delete(0, END)
            print("Sales : clear method finished\n")

        def insert():
            print("Sales : Insert method called")
            if Invoice_Number.get() != 0:
                DB.insert(
                    customername.get(), Invoice_Number.get(), Invoice_Type.get(), Sale_Date.get(), Due_Date.get(),
                    Sale_Description.get(), INR_Total.get(), INR_Balance_Due.get(), Ex_Tax.get(),
                    Bill_To_Address.get(), Ship_To_Address.get(), Invoice_Comments.get(), Customer_Reference.get(),
                    Ship_To_Name.get(), Shipment_Date.get(), Notes.get(), Salesperson.get(), Department.get()
                )
    
                saleItemList.delete(0, END)
    
                saleItemList.insert(
                    END, customername.get(), Invoice_Number.get(), Invoice_Type.get(), Sale_Date.get(), Due_Date.get(),
                    Sale_Description.get(), INR_Total.get(), INR_Balance_Due.get(), Ex_Tax.get(),
                    Bill_To_Address.get(), Ship_To_Address.get(), Invoice_Comments.get(), Customer_Reference.get(),
                    Ship_To_Name.get(), Shipment_Date.get(), Notes.get(), Salesperson.get(), Department.get()
                )
        
                showInsalesList()
                clear()
                print("Sales : Insert method finished\n")
            else:
                messagebox.showerror("Book Keeping", "Enter Supplier ID")

        def showInsalesList():
            print("Sales : showInsalesList method called")
            saleItemList.delete(0, END)
            for row in DB.show():
                saleItemList.insert(END, row, str(""))
            print("Sales : showInsalesList method finished\n")
        
        def search():
            print("Sales : search method called")
            saleItemList.delete(0,END)
            for row in DB.search(Invoice_Number.get()):
                saleItemList.insert(END, row, str(""))

            print("Sales : search method finished\n")
        
        def delete():
            print("Sales :database Delete method called")
            if Invoice_Number.get() != "":
                DB.delete(pd[1])
                clear()
                showInsalesList() 
                print("Customer : database Delete method finished\n")
            if Invoice_Number.get() == "":
                DB.delete(pd[1])
                clear()
                showInsalesList() 
                print("Customer : database Delete method finished\n")

        def update():
            print("Sales : Update method called")
            print("pd[1]", pd[1])
            DB.delete(pd[1])
            DB.insert(
                customername.get(), Invoice_Number.get(), Invoice_Type.get(), Sale_Date.get(), Due_Date.get(),
                Sale_Description.get(), INR_Total.get(), INR_Balance_Due.get(), Ex_Tax.get(),
                Bill_To_Address.get(), Ship_To_Address.get(), Invoice_Comments.get(), Customer_Reference.get(),
                Ship_To_Name.get(), Shipment_Date.get(), Notes.get(), Salesperson.get(), Department.get()
            )
            saleItemList.delete(0, END)
            saleItemList.insert(
                END, customername.get(), Invoice_Number.get(), Invoice_Type.get(), Sale_Date.get(), Due_Date.get(),
                Sale_Description.get(), INR_Total.get(), INR_Balance_Due.get(), Ex_Tax.get(),
                Bill_To_Address.get(), Ship_To_Address.get(), Invoice_Comments.get(), Customer_Reference.get(),
                Ship_To_Name.get(), Shipment_Date.get(), Notes.get(), Salesperson.get(), Department.get()
            )
            showInsalesList()
            clear()
            print("Sales : Update method finished")
        
        def add_new_sale_line_item():
            root = Toplevel()
            app = SaleLineItem(root)
            root.mainloop()

        def products():
            root = Toplevel()
            application = Products(root)
            root.mainloop()

        def customer():
            root = Toplevel()
            app = Customer(root)
            root.mainloop()

        def on_keypress(event):
            print(event)
            print(event.state & 4)
            print(event.keysym == 'a')
            if event.keysym == 'BackSpace':
                value = event.widget.get()[:-1]
            elif (event.state & 4):
                value = event.widget.get()
            else:
                value = event.widget.get() + event.char
            value = value.strip().lower()
            if value == '':
                data = test_list
            else:
                data = []
                for item in test_list:
                    if value in item.lower():
                        data.append(item)
            listbox_update(data)

        def listbox_update(data):
            listbox.delete(0, 'end')
            data = sorted(data, key=str.lower)
            for item in data:
                listbox.insert('end', item)

        test_list = []

        def flattern(listOfLists):
            return chain.from_iterable(listOfLists)

        for row in DB.customername(Customer_Name):
            test_list.append(row)

        test_list = list(flattern(test_list))

        customername = Entry(f2)
        customername.grid(row=0, column=1)
        customername.bind('<KeyPress>', on_keypress)

        def on_select(event):
            # display element selected on list
            print('(event) previous:', event.widget.get('active'))
            print('(event)  current:', event.widget.get(event.widget.curselection()))
            print('---')
            searchpds = listbox.curselection()[0]
            pds = listbox.get(searchpds)
            customername.delete(0, END)
            customername.insert(END, pds)

        listbox = Listbox(f2, height=5)
        listbox.grid(row=0, column=2)
        listbox.bind('<<ListboxSelect>>', on_select)
        listbox_update(test_list)

        Label(f2, text="Customer Name: ").grid(row=0, column=0)

        ttk.Button(f2, text='+', command=customer).grid(row=0, column=3)

        Label(f2, text="Invoice Number: ").grid(row=1, column=0, padx=int(0.5), pady=int(0.5))
        invoicenumber = Entry(f2, font="bold", textvariable=Invoice_Number)
        invoicenumber.grid(row=1, column=1, padx=int(0.5), pady=int(0.5))

        Label(f2, text="Invoice Type: ").grid(row=1, column=2, padx=int(2.5), pady=int(2.5))
        invoicetype = Entry(f2, font="bold", textvariable=Invoice_Type)
        invoicetype.grid(row=1, column=3, padx=int(2.5), pady=int(2.5))

        Label(f2, text="Sale Date: ").grid(row=2, column=0, padx=int(2.5), pady=int(2.5))
        saledate = Entry(f2, font="bold", textvariable=Sale_Date)
        saledate.grid(row=2, column=1, padx=int(2.5), pady=int(2.5))
        
        Label(f2, text="Due Date: ").grid(row=2, column=2, padx=int(2.5), pady=int(2.5))
        duedate = Entry(f2, font="bold", textvariable=Due_Date)
        duedate.grid(row=2, column=3, padx=int(2.5), pady=int(2.5))

        Checkbutton(f2, text="Is Quote: ").grid(row=3, column=0, padx=int(2.5), pady=int(2.5))

        Label(f2, text="Sale Description: ").grid(row=4, column=0, padx=int(2.5), pady=int(2.5))
        saledescription = Entry(f2, font="bold", textvariable=Sale_Description)
        saledescription.grid(row=4, column=1, padx=int(2.5), pady=int(2.5))
        
        Label(f2, text="INR Total: ").grid(row=4, column=2, padx=int(2.5), pady=int(2.5))
        inrtotal = Entry(f2, font="bold", textvariable=INR_Total)
        inrtotal.grid(row=4, column=3, padx=int(2.5), pady=int(2.5))

        Label(f2, text="INR Balance Due: ").grid(row=5, column=0, padx=int(2.5), pady=int(2.5))
        inrbalancedue = Entry(f2, font="bold", textvariable=INR_Balance_Due)
        inrbalancedue.grid(row=5, column=1, padx=int(2.5), pady=int(2.5))

        Label(f2, text="INR Total (ex tax): ").grid(row=6, column=0, padx=int(2.5), pady=int(2.5))
        extax = Entry(f2, font="bold", textvariable=Ex_Tax)
        extax.grid(row=6, column=1, padx=int(2.5), pady=int(2.5))

        Checkbutton(f2, text="Recurring Sale: ").grid(row=7, column=0, padx=int(2.5), pady=int(2.5))

        Label(f2, text="Bill To Address: ").grid(row=8, column=0, padx=int(2.5), pady=int(2.5))
        billtoaddress = Entry(f2, font="bold", textvariable=Bill_To_Address)
        billtoaddress.grid(row=8, column=1, padx=int(2.5), pady=int(2.5))
        
        Label(f2, text="Ship To Address: ").grid(row=8, column=2, padx=int(2.5), pady=int(2.5))
        shiptoaddress = Entry(f2, font="bold", textvariable=Ship_To_Address)
        shiptoaddress.grid(row=8, column=3, padx=int(2.5), pady=int(2.5))

        Label(f2, text="Invoice Comments: ").grid(row=9, column=0, padx=int(2.5), pady=int(2.5))
        invoicecomments = Entry(f2, font="bold", textvariable=Invoice_Comments)
        invoicecomments.grid(row=9, column=1, padx=int(2.5), pady=int(2.5))

        Label(f2, text="Customer Reference: ").grid(row=10, column=0, padx=int(2.5), pady=int(2.5))
        customerreference = Entry(f2, font="bold", textvariable=Customer_Reference)
        customerreference.grid(row=10, column=1, padx=int(2.5), pady=int(2.5))

        Label(f2, text="Ship To  Name: ").grid(row=11, column=0, padx=int(2.5), pady=int(2.5))
        shiptoname = Entry(f2, font="bold", textvariable=Ship_To_Name)
        shiptoname.grid(row=11, column=1, padx=int(2.5), pady=int(2.5))
        
        Label(f2, text="Shipment Date: ").grid(row=11, column=2, padx=int(2.5), pady=int(2.5))
        shipmentdate = Entry(f2, font="bold", textvariable=Shipment_Date)
        shipmentdate.grid(row=11, column=3, padx=int(2.5), pady=int(2.5))

        Label(f2, text="Notes: ").grid(row=12, column=0, padx=int(2.5), pady=int(2.5))
        notes = Entry(f2, font="bold", textvariable=Notes)
        notes.grid(row=12, column=1, padx=int(2.5), pady=int(2.5))
        
        Label(f2, text="Salesperson: ").grid(row=12, column=2, padx=int(2.5), pady=int(2.5))
        salesperson = Entry(f2, font="bold", textvariable=Salesperson)
        salesperson.grid(row=12, column=3, padx=int(2.5), pady=int(2.5))

        Label(f2, text="Department: ").grid(row=13, column=0, padx=int(2.5), pady=int(2.5))
        department = Entry(f2, font="bold", textvariable=Department)
        department.grid(row=13, column=1, padx=int(2.5), pady=int(2.5))

        Button(f2, text="Add Item", fg='green', command=products).grid(row=14, column=2, columnspan=2, padx=int(2.5), pady=int(2.5))

        def saleRec(event):
            print("Sales : customerRec method called")
            global pd 
            searchpd = saleItemList.curselection()[0]
            pd = saleItemList.get(searchpd)
            customername.delete(0, END)
            customername.insert(END, pd[0])
            invoicenumber.delete(0, END)
            invoicenumber.insert(END,pd[1])
            invoicetype.delete(0, END)
            invoicetype.insert(END, pd[2])
            saledate.delete(0, END)
            saledate.insert(END, pd[3])
            duedate.delete(0, END)
            duedate.insert(END, pd[4])
            saledescription.delete(0, END)
            saledescription.insert(END, pd[5])
            inrtotal.delete(0, END)
            inrtotal.insert(END, pd[6])
            inrbalancedue.delete(0, END)
            inrbalancedue.insert(END, pd[7])
            extax.delete(0, END)
            extax.insert(END, pd[8])
            billtoaddress.delete(0, END)
            billtoaddress.insert(END, pd[9])
            shiptoaddress.delete(0, END)
            shiptoaddress.insert(END, pd[10])
            invoicecomments.delete(0, END)
            invoicecomments.insert(END, pd[11])
            customerreference.delete(0, END)
            customerreference.insert(END, pd[12])
            shiptoname.delete(0, END)
            shiptoname.insert(END, pd[13])
            shipmentdate.delete(0, END)
            shipmentdate.insert(END, pd[14])
            notes.delete(0, END)
            notes.insert(END, pd[15])
            salesperson.delete(0, END)
            salesperson.insert(END, pd[16])
            department.delete(0, END)
            department.insert(END, pd[17])
            print("Sales : customerRec method finished\n")

        scroll = Scrollbar(f1)
        scroll.grid(row=15, column=5, sticky='ns')
        
        scroll2 = Scrollbar(f1, orient=HORIZONTAL)
        scroll2.grid(row=16, column=0, sticky='ew', columnspan=4)
        
        saleItemList = Listbox(f1, width=55, height=22, font=('arial', 12, 'bold'), yscrollcommand=scroll.set, xscrollcommand=scroll2.set)

        saleItemList.bind('<<ListboxSelect>>', saleRec)
        saleItemList.grid(row=15, column=0, columnspan=4)
        
        scroll.config(command=saleItemList.yview)
        scroll2.config(command=saleItemList.xview)

        Button(f2, text="+ Add New Sale Line Item", command=add_new_sale_line_item, fg='green').grid(row=17, column=0, columnspan=2, padx=int(2.5), pady=int(2.5))

        buttonSaveData = Button(f3, text='Save', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=insert)
        buttonSaveData.grid(row=0, column=0, pady=10)

        buttonShowData = Button(f3, text='Show Data', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command= showInsalesList)
        buttonShowData.grid(row=0, column=1, padx=10, pady=10)

        buttonClearData = Button(f3, text='Reset', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=clear)
        buttonClearData.grid(row=0, column=2, pady=10)

        buttonDeleteData = Button(f3, text='Delete', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=delete)
        buttonDeleteData.grid(row=1, column=0)

        buttonsearchData = Button(f3, text='Search', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=search)
        buttonsearchData.grid(row=1, column=1, padx=10)

        buttonUpdate = Button(f3, text='Update', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=update)
        buttonUpdate.grid(row=1, column=2)

        home.mainloop()


class DatabaseSales:
    def conn(self):
        print("Database : Connection method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "create table if not exists Sales(Customer_Name text, Invoice_Number text, Invoice_Type text, Sale_Date text, Due_Date text, Sale_Description text, INR_Total text, INR_Balance_Due text, Ex_Tax text, Bill_To_Address text, Ship_To_Address text, Invoice_Comments text, Customer_Reference text, Ship_To_Name text, Shipment_Date text, Notes text, Salesperson text, Department text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : Connection method finished\n")

    def insert(self, Customer_Name, Invoice_Number, Invoice_Type, Sale_Date, Due_Date, Sale_Description, INR_Total, INR_Balance_Due, Ex_Tax, Bill_To_Address, Ship_To_Address, Invoice_Comments, Customer_Reference, Ship_To_Name, Shipment_Date, Notes, Salesperson, Department):
        print("Database : Insert method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "insert into Sales values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, (Customer_Name, Invoice_Number, Invoice_Type, Sale_Date, Due_Date, Sale_Description, INR_Total, INR_Balance_Due, Ex_Tax, Bill_To_Address, Ship_To_Address, Invoice_Comments, Customer_Reference, Ship_To_Name, Shipment_Date, Notes, Salesperson, Department))
        con.commit()
        con.close()
        print("Database : Insert method finished\n")

    def show(self):
        print("Database : Show method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "select * from Sales"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : Show method finished\n")
        return rows

    def delete(self, Invoice_Number):
        print("Database : Delete method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("delete from Sales where Invoice_Number=?", (Invoice_Number,))
        con.commit()
        con.close()
        print("Database : Delete method finished\n")

    def search(self, Invoice_Number=""):
        print("Database : Search method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("select * from Sales where Invoice_Number=?", (Invoice_Number))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Search method finished\n")
        return row

    def update(self, Invoice_Number=""):
        print("Database : Update method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("update Customer set Invoice_Number=?", (Invoice_Number))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Update method finished\n")

    def customername(self, Supplier_Name):
        print("Database : Customername method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("select Customer_Name from Customer")
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Customername method finished\n")
        return row
