from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class SaleLineItem:
    def __init__(self, root):
        items = root
        items.title("Add New Sale Line Item")
        items.iconbitmap("./icon.ico")
        items.state('zoomed')

        main_frame = Frame(items)
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

        item = second_frame

        DB = DatabaseSaleItemList()
        DB.conn()

        f1 = ttk.Frame(item, width=600, height=380)
        f1.grid(row=0, column=0)

        f2 = ttk.Frame(item, width=600, height=380)
        f2.grid(row=0, column=1, padx=20)

        f3 = ttk.Frame(item, width=10, height=10)
        f3.grid(row=1, column=0)

        Sale_Account = StringVar()
        Id = StringVar()
        Products_Or_Services = StringVar()
        Line_Description = StringVar()
        Item_Date = StringVar()
        INR_Unit_Price = StringVar()
        INR_Item_Total = StringVar()
        Sale_Tax_Code = StringVar()
        Currency = StringVar()
        Quantity = StringVar()
        Available_Quantity = StringVar()
        INR_Sub_Total = StringVar()
        INR_Tax = StringVar()
        INR_Balance_Due = StringVar()
        Discount_Percent = StringVar()

        def clear():
            print("Sales : Clear method called")
            saleaccount.delete(0, END)
            id.delete(0, END)
            productsorservices.delete(0, END)
            linedescription.delete(0, END)
            itemdate.delete(0, END)
            INR_Unit_Price.delete(0, END)
            inritemtotal.delete(0, END)
            saletaxcode.delete(0, END)
            currency.delete(0, END)
            quantity.delete(0, END)
            availablequantity.delete(0, END)
            inrsubtotal.delete(0, END)
            inrtax.delete(0, END)
            INR_Balance_Due.delete(0, END)
            discountpercent.delete(0, END)
            print("Sales : clear method finished\n")

        def insert():
            print("Sales : Insert method called")
            if Id.get() != 0:
                DB.insert(
                    Sale_Account.get(), Id.get(), Products_Or_Services.get(), Line_Description.get(), Item_Date.get(), INR_Unit_Price.get(),
                    INR_Item_Total.get(), Sale_Tax_Code.get(), Currency.get(), Quantity.get(),
                    Available_Quantity.get(), INR_Sub_Total.get, INR_Tax.get(), INR_Balance_Due.get(), Discount_Percent.get()
                )
                saleItemList.delete(0, END)
                saleItemList.insert(
                    END, Sale_Account.get(), Id.get(), Products_Or_Services.get(), Line_Description.get(), Item_Date.get(), INR_Unit_Price.get(),
                    INR_Item_Total.get(), Sale_Tax_Code.get(), Currency.get(), Quantity.get(),
                    Available_Quantity.get(), INR_Sub_Total.get(), INR_Tax.get(),INR_Balance_Due.get(), Discount_Percent.get()
                )
                showInSaleLineItemList()
                clear()
                print("Sales : Insert method finished\n")
            else:
                messagebox.showerror("Book Keeping", "Enter Supplier ID")

        def showInSaleLineItemList():
            print("Sales : showInSaleLineItemList method called")
            saleItemList.delete(0, END)
            for row in DB.show():
                saleItemList.insert(END, row, str(""))
            print("Sales : showInSaleLineItemList method finished\n")

        def search():
            print("Sales : search method called")
            saleItemList.delete(0,END)
            for row in DB.search(Id.get()):
                saleItemList.insert(END, row, str(""))

            print("Sales : search method finished\n")

        def delete():
            print("Sales :database Delete method called")
            if Id.get() != "":
                DB.delete(pd[1])
                clear()
                showInSaleLineItemList() 
                print("Customer : database Delete method finished\n")
            if Id.get() == "":
                DB.delete(pd[1])
                clear()
                showInSaleLineItemList() 
                print("Customer : database Delete method finished\n")

        def update():
            print("Sale Line Item : Update method called")
            print("pd[1]", pd[1])
            DB.delete(pd[1])
            DB.insert(
                Sale_Account.get(), Id.get(), Products_Or_Services.get(), Line_Description.get(), Item_Date.get(), INR_Unit_Price.get(),
                INR_Item_Total.get(), Sale_Tax_Code.get(), Currency.get(), Quantity.get(),
                Available_Quantity.get(), INR_Sub_Total.get, INR_Tax.get(), INR_Balance_Due.get(), Discount_Percent.get()
            )
            saleItemList.delete(0, END)
            saleItemList.insert(
                END, Sale_Account.get(), Id.get(), Products_Or_Services.get(), Line_Description.get(), Item_Date.get(), INR_Unit_Price.get(),
                INR_Item_Total.get(), Sale_Tax_Code.get(), Currency.get(), Quantity.get(),
                Available_Quantity.get(), INR_Sub_Total.get(), INR_Tax.get(),INR_Balance_Due.get(), Discount_Percent.get()
            )
            showInSaleLineItemList() # called showInCustomerList method after inserting the data record to database table
            clear()
            print("Sale Line Item : Update method finished")

        Label(f1, text="Sale Account").grid(row=0, column=0, padx=int(0.5), pady=int(0.5))
        saleaccount = Entry(f1, font="bold", textvariable=Sale_Account)
        saleaccount.grid(row=0, column=1, padx=int(0.5), pady=int(0.5))

        Label(f1, text="Id").grid(row=0, column=2, padx=int(0.5), pady=int(0.5))
        id = Entry(f1, font="bold", textvariable=Id)
        id.grid(row=0, column=3, padx=int(0.5), pady=int(0.5))

        Label(f1, text="Product OR Services").grid(row=1, column=0, padx=int(0.5), pady=int(0.5))
        productsorservices = Entry(f1, font="bold", textvariable=Products_Or_Services)
        productsorservices.grid(row=1, column=1, padx=int(0.5), pady=int(0.5))

        Label(f1, text="Line Description: ").grid(row=1, column=2, padx=int(2.5), pady=int(2.5))
        linedescription = Entry(f1, font="bold", textvariable=Line_Description)
        linedescription.grid(row=1, column=3, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Item Date: ").grid(row=2, column=0, padx=int(2.5), pady=int(2.5))
        itemdate = Entry(f1, font="bold", textvariable=Item_Date)
        itemdate.grid(row=2, column=1, padx=int(2.5), pady=int(2.5))

        Label(f1, text="INR Unit Price: ").grid(row=2, column=2, padx=int(2.5), pady=int(2.5))
        INR_Unit_Price = Entry(f1, font="bold", textvariable=INR_Unit_Price)
        INR_Unit_Price.grid(row=2, column=3, padx=int(2.5), pady=int(2.5))

        Checkbutton(f1, text="Tax Inclusive: ").grid(row=3, column=0, padx=int(2.5), pady=int(2.5))

        Label(f1, text="INR Item Total: ").grid(row=4, column=0, padx=int(2.5), pady=int(2.5))
        inritemtotal = Entry(f1, font="bold", textvariable=INR_Item_Total)
        inritemtotal.grid(row=4, column=1, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Sale Tax Code: ").grid(row=4, column=2, padx=int(2.5), pady=int(2.5))
        saletaxcode = Entry(f1, font="bold", textvariable=Sale_Tax_Code)
        saletaxcode.grid(row=4, column=3, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Currency: ").grid(row=5, column=0, padx=int(2.5), pady=int(2.5))
        currency = Entry(f1, font="bold", textvariable=Currency)
        currency.grid(row=5, column=1, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Quantity: ").grid(row=6, column=0, padx=int(2.5), pady=int(2.5))
        quantity = Entry(f1, font="bold", textvariable=Quantity)
        quantity.grid(row=6, column=1, padx=int(2.5), pady=int(2.5))

        Checkbutton(f1, text="UOM: ").grid(row=7, column=0, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Available Quantity: ").grid(row=8, column=0, padx=int(2.5), pady=int(2.5))
        availablequantity = Entry(f1, font="bold", textvariable=Available_Quantity)
        availablequantity.grid(row=8, column=1, padx=int(2.5), pady=int(2.5))

        Label(f1, text="INR Sub Total: ").grid(row=8, column=2, padx=int(2.5), pady=int(2.5))
        inrsubtotal = Entry(f1, font="bold", textvariable=INR_Sub_Total)
        inrsubtotal.grid(row=8, column=3, padx=int(2.5), pady=int(2.5))

        Label(f1, text="INR Tax: ").grid(row=9, column=0, padx=int(2.5), pady=int(2.5))
        inrtax = Entry(f1, font="bold", textvariable=INR_Tax)
        inrtax.grid(row=9, column=1, padx=int(2.5), pady=int(2.5))

        Label(f1, text="INR Balance Due: ").grid(row=10, column=0, padx=int(2.5), pady=int(2.5))
        INR_Balance_Due = Entry(f1, font="bold", textvariable=INR_Balance_Due)
        INR_Balance_Due.grid(row=10, column=1, padx=int(2.5), pady=int(2.5))

        Label(f1, text="Discount %: ").grid(row=11, column=0, padx=int(2.5), pady=int(2.5))
        discountpercent = Entry(f1, font="bold", textvariable=Discount_Percent)
        discountpercent.grid(row=11, column=1, padx=int(2.5), pady=int(2.5))

        buttonSaveData = Button(f3, text='Save', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=insert)
        buttonSaveData.grid(row=0, column=0, pady=10)

        buttonShowData = Button(f3, text='Show Data', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=showInSaleLineItemList)
        buttonShowData.grid(row=0, column=1, pady=10, padx=10)

        buttonClearData = Button(f3, text='Reset', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=clear)
        buttonClearData.grid(row=0, column=2, pady=10)

        buttonDeleteData = Button(f3, text='Delete', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=delete)
        buttonDeleteData.grid(row=1, column=0)

        buttonsearchData = Button(f3, text='Search', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=search)
        buttonsearchData.grid(row=1, column=1, padx=10)

        buttonUpdate = Button(f3, text='Update', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=update)
        buttonUpdate.grid(row=1, column=2)

        def SaleLineItemRec(event):
            print("Sales : customerRec method called")
            
            global pd 
            
            searchpd = saleItemList.curselection()[0]
            pd = saleItemList.get(searchpd)
            
            saleaccount.delete(0, END)
            saleaccount.insert(END, pd[0])

            id.delete(0, END)
            id.insert(END, pd[1])
            
            productsorservices.delete(0, END)
            productsorservices.insert(END,pd[2])
            
            linedescription.delete(0, END)
            linedescription.insert(END, pd[3])
            
            itemdate.delete(0, END)
            itemdate.insert(END, pd[4])
            
            INR_Unit_Price.delete(0, END)
            INR_Unit_Price.insert(END, pd[5])
            
            inritemtotal.delete(0, END)
            inritemtotal.insert(END, pd[6])
                
            saletaxcode.delete(0, END)
            saletaxcode.insert(END, pd[7])
            
            currency.delete(0, END)
            currency.insert(END, pd[8])
            
            quantity.delete(0, END)
            quantity.insert(END, pd[9])
            
            availablequantity.delete(0, END)
            availablequantity.insert(END, pd[10])
            
            inrsubtotal.delete(0, END)
            inrsubtotal.insert(END, pd[11])
            
            inrtax.delete(0, END)
            inrtax.insert(END, pd[12])
            
            INR_Balance_Due.delete(0, END)
            INR_Balance_Due.insert(END, pd[13])
            
            discountpercent.delete(0, END)
            discountpercent.insert(END, pd[14])
            
            print("Sales : customerRec method finished\n")

        scroll = Scrollbar(f2)
        scroll.grid(row=1, column=1, sticky='ns')
            
        scroll2 = Scrollbar(f2, orient=HORIZONTAL)
        scroll2.grid(row=2, column=0, sticky='ew')
            
        saleItemList = Listbox(f2, width=60, height=15, font=('arial', 12, 'bold'), yscrollcommand=scroll.set, xscrollcommand=scroll2.set)
        
        saleItemList.bind('<<ListboxSelect>>', SaleLineItemRec)
        saleItemList.grid(row=1, column=0)
            
        scroll.config(command=saleItemList.yview)
        scroll2.config(command=saleItemList.xview)

        items.mainloop()

class DatabaseSaleItemList:
    def conn(self):
        print("Database : Connection method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "create table if not exists SaleItemList(Sale_Account text, Id text, Products_Or_Services text, Line_Description text, Item_Date text, INR_Unit_Price text, INR_Item_Total text, Sale_Tax_Code text, Currency text, Quantity text, Available_Quantity text, INR_Sub_Total text, INR_Tax text, INR_Balance_Due text, Discount_Percent text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : Connection method finished\n")

    def insert(self, Sale_Account, Id, Products_Or_Services, Line_Description, Item_Date, INR_Unit_Price, INR_Item_Total, Sale_Tax_Code, Currency, Quantity, Available_Quantity, INR_Sub_Total, INR_Tax, INR_Balance_Due, Discount_Percent):
        print("Database : Insert method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "insert into SaleItemList values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, (Sale_Account, Id, Products_Or_Services, Line_Description, Item_Date, INR_Unit_Price, INR_Item_Total, Sale_Tax_Code, Currency, Quantity, Available_Quantity, INR_Sub_Total, INR_Tax, INR_Balance_Due, Discount_Percent))
        con.commit()
        con.close()
        print("Database : Insert method finished\n")

    def show(self):
        print("Database : Show method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "select * from SaleItemList"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : Show method finished\n")
        return rows

    def delete(self, Id):
        print("Database : Delete method called",)
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("delete from SaleItemList where Id=?", (Id,))
        con.commit()
        con.close()
        print("Database : Delete method finished\n")

    def search(self, Id=""):
        print("Database : Sales search method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("select * from SaleItemList where Id=?", (Id))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Sales search method finished\n")
        return row

    def update(self, ID=""):
        print("Database : Update method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("update Customer set ID=?", (ID))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Update method finished\n")
