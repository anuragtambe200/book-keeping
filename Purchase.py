from tkinter import *
import sqlite3
from string import ascii_uppercase
from itertools import chain
from tkinter import messagebox
from tkinter import ttk
from Products import Products
from Products import DatabaseProducts
from Suppliers import Supplier
from Suppliers import DatabaseSupplier

class Purchase:
    def __init__(self, root):
        DB = DatabasePurchase()
        DB.conn()

        self.root = root
        self.root.title("Bok Keeping - Purchase")
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

        Supplier_Name = StringVar()
        Order_Number = StringVar()
        Order_Type = StringVar()
        Purchase_Date = StringVar()
        Due_Date = StringVar()
        Purchase_Description = StringVar()
        Withdrawal_Account = StringVar()
        INR_Total = StringVar()
        INR_Balance_Due = StringVar()
        Ex_Tax = StringVar()
        Supplier_Address = StringVar()
        Ship_To_Address = StringVar()
        Supplier_Reference = StringVar()
        Ship_To_Name = StringVar()
        Received_Date = StringVar()
        Notes = StringVar()
        Purchaser = StringVar()
        Department = StringVar()
        
        def clear():
            print("Purchase : Clear method called")
            suppliername.delete(0, END)
            orderno.delete(0, END)
            ordertype.delete(0, END)
            purchasedate.delete(0, END)
            duedate.delete(0, END)
            purchasedescription.delete(0, END)
            withdrawalaccount.delete(0, END)
            inrtotal.delete(0, END)
            inrbalancedue.delete(0, END)
            extax.delete(0, END)
            supplieraddress.delete(0, END)
            shiptoaddress.delete(0, END)
            supplierreference.delete(0, END)
            shiptoname.delete(0, END)
            receiveddate.delete(0, END)
            notes.delete(0, END)
            purchaser.delete(0, END)
            department.delete(0, END)
            print("Purchase : Clear method finished\n")

        def delete():
            print("Purchase : Delete method called")
            DB.delete(pd[1])
            clear()
            showInPurchaseList() 
            print("Purchase : Delete method finished\n")
        
        def search():
            print("Purchase : search method called")
            purchaseList.delete(0,END)
            for row in DB.search(Order_Number.get()):
                purchaseList.insert(END, row, str(""))
            print("Purchase : search method finished\n")

        def insert():
            print("Purchase : Insert method called")
            DB.insert(
                suppliername.get(), Order_Number.get(), Order_Type.get(), Purchase_Date.get(), Due_Date.get(),
                Purchase_Description.get(), Withdrawal_Account.get(), INR_Total.get(), INR_Balance_Due.get(),
                Ex_Tax.get(), Supplier_Address.get(), Ship_To_Address.get(), Supplier_Reference.get(), Ship_To_Name.get(), Received_Date.get(), Notes.get(), Purchaser.get(), Department.get()
            )
            purchaseList.delete(0, END)
            purchaseList.insert(
                END, suppliername.get(), Order_Number.get(), Order_Type.get(), Purchase_Date.get(), Due_Date.get(),
                Purchase_Description.get(), Withdrawal_Account.get(), INR_Total.get(), INR_Balance_Due.get(),
                Ex_Tax.get(), Supplier_Address.get(), Ship_To_Address.get(), Supplier_Reference.get(), Ship_To_Name.get(), Received_Date.get(), Notes.get(), Purchaser.get(), Department.get()
            )
            showInPurchaseList()
            clear()
            print("Purchase : Insert method finished\n")

        def showInPurchaseList():
            print("Purchase : ShowInPurchaseList method called")
            purchaseList.delete(0, END)
            for row in DB.show():
                purchaseList.insert(END, row, str(""))
            print("Purchase : ShowInPurchaseList method finished\n")

        def update():
            print("Purchase : Update method called")
            print("pd[1]", pd[1])
            DB.delete(pd[1])
            DB.insert(
                suppliername.get(), Order_Number.get(), Order_Type.get(), Purchase_Date.get(), Due_Date.get(),
                Purchase_Description.get(), Withdrawal_Account.get(), INR_Total.get(), INR_Balance_Due.get(),
                Ex_Tax.get(), Supplier_Address.get(), Ship_To_Address.get(), Supplier_Reference.get(), Ship_To_Name.get(), Received_Date.get(), Notes.get(), Purchaser.get(), Department.get()
            )
            purchaseList.delete(0, END)
            purchaseList.insert(
                END, suppliername.get(), Order_Number.get(), Order_Type.get(), Purchase_Date.get(), Due_Date.get(),
                Purchase_Description.get(), Withdrawal_Account.get(), INR_Total.get(), INR_Balance_Due.get(),
                    Ex_Tax.get(), Supplier_Address.get(), Ship_To_Address.get(), Supplier_Reference.get(), Ship_To_Name.get(), Received_Date.get(), Notes.get(), Purchaser.get(), Department.get()
            )
            showInPurchaseList() # called showInProductList method after inserting the data record to database table
            clear()
            print("Purchase : Update method finished\n")

        def products():
            root = Toplevel()
            application = Products(root)
            root.mainloop()

        def suppliers():
            root = Toplevel()
            app = Supplier(root)
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

        for row in DB.suppliername(Supplier_Name):
            test_list.append(row)

        test_list = list(flattern(test_list))

        suppliername = Entry(f1)
        suppliername.grid(row=0, column=1)
        suppliername.bind('<KeyPress>', on_keypress)

        def on_select(event):
            print('(event) previous:', event.widget.get('active'))
            print('(event)  current:', event.widget.get(event.widget.curselection()))
            print('---')
            searchpds = listbox.curselection()[0]
            pds = listbox.get(searchpds)
            suppliername.delete(0, END)
            suppliername.insert(END, pds)

        listbox = Listbox(f1, height=5)
        listbox.grid(row=0, column=2)
        listbox.bind('<<ListboxSelect>>', on_select)
        listbox_update(test_list)

        Label(f1, text="Supplier Name").grid(row=0, column=0, padx=int(0.5), pady=int(0.5))

        ttk.Button(f1, text="+", command=suppliers).grid(row=0, column=3)

        Label(f1, text="Order Number").grid(row=1, column=0, padx=int(0.5), pady=int(0.5))
        orderno = Entry(f1, font="bold", textvariable=Order_Number)
        orderno.grid(row=1, column=1, padx=int(0.5), pady=int(0.5))
            
        Label(f1, text="Order Type: ").grid(row=1, column=2, padx=int(2.5), pady=int(2.5))
        ordertype = Entry(f1, font="bold", textvariable=Order_Type)
        ordertype.grid(row=1, column=3, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Purchase Date: ").grid(row=2, column=0, padx=int(2.5), pady=int(2.5))
        purchasedate = Entry(f1, font="bold", textvariable=Purchase_Date)
        purchasedate.grid(row=2, column=1, padx=int(2.5), pady=int(2.5))
            
        Label(f1, text="Due Date: ").grid(row=2, column=2, padx=int(2.5), pady=int(2.5))
        duedate = Entry(f1, font="bold", textvariable=Due_Date)
        duedate.grid(row=2, column=3, padx=int(2.5), pady=int(2.5))

        Checkbutton(f1, text="Is RFQ ").grid(row=3, column=0, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Purchase Description: ").grid(row=4, column=0, padx=int(2.5), pady=int(2.5))
        purchasedescription = Entry(f1, font="bold", textvariable=Purchase_Description)
        purchasedescription.grid(row=4, column=1, padx=int(2.5), pady=int(2.5))
            
        Label(f1, text="Withdrawal Account: ").grid(row=5, column=0, padx=int(2.5), pady=int(2.5))
        withdrawalaccount = Entry(f1, font="bold", textvariable=Withdrawal_Account)
        withdrawalaccount.grid(row=5, column=1, padx=int(2.5), pady=int(2.5))
            
        Label(f1, text="INR Total: ").grid(row=5, column=2, padx=int(2.5), pady=int(2.5))
        inrtotal = Entry(f1, font="bold", textvariable=INR_Total)
        inrtotal.grid(row=5, column=3, padx=int(2.5), pady=int(2.5))

        Label(f1, text="INR Balance Due: ").grid(row=6, column=0, padx=int(2.5), pady=int(2.5))
        inrbalancedue = Entry(f1, font="bold", textvariable=INR_Balance_Due)
        inrbalancedue.grid(row=6, column=1, padx=int(2.5), pady=int(2.5))

        Label(f1, text="INR Total (ex tax): ").grid(row=7, column=0, padx=int(2.5), pady=int(2.5))
        extax = Entry(f1, font="bold", textvariable=Ex_Tax)
        extax.grid(row=7, column=1, padx=int(2.5), pady=int(2.5))

        Checkbutton(f1, text="Recurring Purchase: ").grid(row=8, column=0, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Supplier Address: ").grid(row=9, column=0, padx=int(2.5), pady=int(2.5))
        supplieraddress = Entry(f1, font="bold", textvariable=Supplier_Address)
        supplieraddress.grid(row=9, column=1, padx=int(2.5), pady=int(2.5))
            
        Label(f1, text="Ship To Address: ").grid(row=9, column=2, padx=int(2.5), pady=int(2.5))
        shiptoaddress = Entry(f1, font="bold", textvariable=Ship_To_Address)
        shiptoaddress.grid(row=9, column=3, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Supplier Reference: ").grid(row=10, column=0, padx=int(2.5), pady=int(2.5))
        supplierreference = Entry(f1, font="bold", textvariable=Supplier_Reference)
        supplierreference.grid(row=10, column=1, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Ship To Name: ").grid(row=11, column=0, padx=int(2.5), pady=int(2.5))
        shiptoname = Entry(f1, font="bold", textvariable=Ship_To_Name)
        shiptoname.grid(row=11, column=1, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Received Date: ").grid(row=11, column=2, padx=int(2.5), pady=int(2.5))
        receiveddate = Entry(f1, font="bold", textvariable=Received_Date)
        receiveddate.grid(row=11, column=3, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Notes: ").grid(row=12, column=0, padx=int(2.5), pady=int(2.5))
        notes = Entry(f1, font="bold", textvariable=Notes)
        notes.grid(row=12, column=1, padx=int(2.5), pady=int(2.5))
            
        Label(f1, text="Purchaser: ").grid(row=12, column=2, padx=int(2.5), pady=int(2.5))
        purchaser = Entry(f1, font="bold", textvariable=Purchaser)
        purchaser.grid(row=12, column=3, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Department: ").grid(row=13, column=0, padx=int(2.5), pady=int(2.5))
        department = Entry(f1, font="bold", textvariable=Department)
        department.grid(row=13, column=1, padx=int(2.5), pady=int(2.5))

        ttk.Button(f1, text="Add Item", command=products).grid(row=14, column=0, padx=int(2.5), pady=int(2.5), columnspan=4)

        buttonSaveData = Button(f3, text='Save', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=insert)
        buttonSaveData.grid(row=0, column=0, pady=20)

        buttonShowData = Button(f3, text='Show Data', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=showInPurchaseList)
        buttonShowData.grid(row=0, column=1, pady=20, padx=10)

        buttonClearData = Button(f3, text='Reset', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=clear)
        buttonClearData.grid(row=0, column=2, pady=20)

        buttonDeleteData = Button(f3, text='Delete', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=delete)
        buttonDeleteData.grid(row=1, column=0)

        buttonsearchData = Button(f3, text='Search', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=search)
        buttonsearchData.grid(row=1, column=1, padx=10)

        buttonUpdate = Button(f3, text='Update', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=update)
        buttonUpdate.grid(row=1, column=2)

        def purchaseRec(event):
            print("Purchase : PurchaseRec method called")
            global pd 
            searchPd = purchaseList.curselection()[0]
            pd = purchaseList.get(searchPd)
            suppliername.delete(0, END)
            suppliername.insert(END, pd[0])
            orderno.delete(0, END)
            orderno.insert(END, pd[1])
            ordertype.delete(0, END)
            ordertype.insert(END, pd[2])
            purchasedate.delete(0, END)
            purchasedate.insert(END, pd[3])
            duedate.delete(0, END)
            duedate.insert(END, pd[4])
            purchasedescription.delete(0, END)
            purchasedescription.insert(END, pd[5])
            withdrawalaccount.delete(0, END)
            withdrawalaccount.insert(END, pd[6])
            inrtotal.delete(0, END)
            inrtotal.insert(END, pd[7])
            inrbalancedue.delete(0, END)
            inrbalancedue.insert(END, pd[8])
            extax.delete(0, END)
            extax.insert(END, pd[9])
            supplieraddress.delete(0, END)
            supplieraddress.insert(END, pd[10])
            shiptoaddress.delete(0, END)
            shiptoaddress.insert(END, pd[11])
            supplierreference.delete(0, END)
            supplierreference.insert(END, pd[12])
            shiptoname.delete(0, END)
            shiptoname.insert(END, pd[13])
            receiveddate.delete(0, END)
            receiveddate.insert(END, pd[14])
            notes.delete(0, END)
            notes.insert(END, pd[15])
            purchaser.delete(0, END)
            purchaser.insert(END, pd[16])
            department.delete(0, END)
            department.insert(END, pd[17])
            print("Purchase : supplierRec method finished\n")

        scroll = Scrollbar(f2)
        scroll.grid(row=15, column=5, sticky='ns')
        
        scroll2 = Scrollbar(f2, orient=HORIZONTAL)
        scroll2.grid(row=16, column=0, sticky='ew', columnspan=4)
        
        purchaseList = Listbox(f2, width=60, height=22, font=('arial', 12, 'bold'), yscrollcommand=scroll.set, xscrollcommand=scroll2.set)

        purchaseList.bind('<<ListboxSelect>>', purchaseRec)
        purchaseList.grid(row=15, column=0, columnspan=4)
        scroll.config(command=purchaseList.yview)
        scroll2.config(command=purchaseList.xview)


class DatabasePurchase:
    def conn(self):
        print("Database : Connection method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "create table if not exists Purchase(Supplier_Name text, Order_Number text, Order_Type text, Purchase_Date text, Due_Date text, Purchase_Description text, Withdrawal_Account text, INR_Total text, INR_Balance_Due text, Ex_Tax text, Supplier_Address text, Ship_To_Address text, Supplier_Reference text, Ship_To_Name text, Received_Date text, Notes text, Purchaser text, Department text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : Connection method finished\n")

    def insert(self, Supplier_Name, Order_Number, Order_Type, Purchase_Date, Due_Date, Purchase_Description, Withdrawal_Account, INR_Total, INR_Balance_Due, Ex_Tax, Supplier_Address, Ship_To_Address, Supplier_Reference, Ship_To_Name, Received_Date, Notes, Purchaser, Department):
        print("Database : Insert method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "insert into Purchase values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, (Supplier_Name, Order_Number, Order_Type, Purchase_Date, Due_Date, Purchase_Description, Withdrawal_Account, INR_Total, INR_Balance_Due, Ex_Tax, Supplier_Address, Ship_To_Address, Supplier_Reference, Ship_To_Name, Received_Date, Notes, Purchaser, Department))
        con.commit()
        con.close()
        print("Database : Insert method finished\n")

    def show(self):
        print("Database : show method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "select * from Purchase"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : show method finished\n")
        return rows

    def delete(self, Order_Number):
        print("Database : delete method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("delete from Purchase where Order_Number=?", (Order_Number,))
        con.commit()
        con.close()
        print("Database : delete method finished\n")

    def search(self, Order_Number=""):
        print("Database : Search method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("select * from Purchase where Order_Number=?", (Order_Number))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Search method finished\n")
        return row

    def update(self, Order_Number=""):
        print("Database : Update method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("update Purchase set Order_Number=?", (Order_Number))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Update method finished\n")

    def suppliername(self, Supplier_Name):
        print("Database : Suppliername method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("select Supplier_Name from Supplier")
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Suppliername method finished\n")
        return row
