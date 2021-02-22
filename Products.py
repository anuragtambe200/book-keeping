from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk


class Products:
    def __init__(self, root):
        DB = DatabaseProducts()
        DB.conn()

        self.root = root
        self.root.title("Book Keeping - Products / Services - Products")
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

        Item_Number = StringVar()
        Item_Category = StringVar()
        Item_Description = StringVar()
        HSN_Code = StringVar()
        Opening_Balance_Date = StringVar()
        Opening_Balance_Quantity = StringVar()
        Opening_Balance_Value_In_INR = StringVar()
        Job_Default = StringVar()
        Default_Unit_Of_Measure = StringVar()
        Pricing_Group = StringVar()
        Purchases = StringVar()
        Adjustments = StringVar()
        RFQs = StringVar()
        Total = StringVar()
        Sales = StringVar()
        Quotes = StringVar()
        Total_Allocated = StringVar()
        Available_Quantity = StringVar()
        Available_Value = StringVar()
        One_Inventory_Levels = StringVar()

        def clear():
            print("Products : Clear method called")
            itemnumber.delete(0, END)
            itemcategory.delete(0, END)
            itemdescription.delete(0, END)
            hsncode.delete(0, END)
            openingbalancedate.delete(0, END)
            openingbalancequantity.delete(0, END)
            openingbalancevalueininr.delete(0, END)
            jobdefault.delete(0, END)
            defaultunitofmeasure.delete(0, END)
            pricinggroup.delete(0, END)
            purchases.delete(0, END)
            adjustments.delete(0, END)
            rfqs.delete(0, END)
            total.delete(0, END)
            sales .delete(0, END)
            quotes.delete(0, END)
            totalallocated.delete(0, END)
            availablequantity.delete(0, END)
            availablevalue.delete(0, END)
            oneinventorylevels.delete(0, END)

            print("Products : Clear method finished\n")

        def delete():
            print("Products : Delete method called")
            DB.delete(pd[0])
            clear()
            showInProductList() 
            print("Products : Delete method finished\n")

        
        def search():
            print("Products : Search method called")
            productList.delete(0,END)
            for row in DB.search(Item_Number.get()):
                productList.insert(END, row, str(""))
            print("Products : Search method finished\n")

        def insert():
            print("Products : Insert method called")
            if (Item_Number.get() != 0):
                DB.insert(
                    Item_Number.get(), Item_Category.get(), Item_Description.get(), HSN_Code.get(), Opening_Balance_Date.get(), Opening_Balance_Quantity.get(), Opening_Balance_Value_In_INR.get(),
                    Job_Default.get(), Default_Unit_Of_Measure.get(), Pricing_Group.get(), Purchases.get(),
                    Adjustments.get(), RFQs.get(), Total.get(), Sales.get(), Quotes.get(), Total_Allocated.get(), Available_Quantity.get(), Available_Value.get(), One_Inventory_Levels.get()
                )
                productList.delete(0, END)
                productList.insert(END, Item_Number.get(), Item_Category.get(), Item_Description.get(), HSN_Code.get(), Opening_Balance_Date.get(), Opening_Balance_Quantity.get(), Opening_Balance_Value_In_INR.get(),
                    Job_Default.get(), Default_Unit_Of_Measure.get(), Pricing_Group.get(), Purchases.get(),
                    Adjustments.get(), RFQs.get(), Total.get(), Sales.get(), Quotes.get(), Total_Allocated.get(), Available_Quantity.get(), Available_Value.get(), One_Inventory_Levels.get()
                )
                showInProductList()
                clear()
                print("Products : Insert method finished\n")
            else:
                messagebox.showerror("Warehouse Inventry Sales Purchase Management System", "Really ....Enter Product ID")

        def showInProductList():
            print("Products : ShowInProductList method called")
            productList.delete(0, END)
            for row in DB.show():
                productList.insert(END, row, str(""))
            print("Products : ShowInProductList method finished\n")

        def update():
            print("Products : Update method called")
            print("pd[0]", pd[0])
            DB.delete(pd[0])
            DB.insert(
                Item_Number.get(), Item_Category.get(), Item_Description.get(), HSN_Code.get(), Opening_Balance_Date.get(), Opening_Balance_Quantity.get(), Opening_Balance_Value_In_INR.get(),
                Job_Default.get(), Default_Unit_Of_Measure.get(), Pricing_Group.get(), Purchases.get(),
                Adjustments.get(), RFQs.get(), Total.get(), Sales.get(), Quotes.get(), Total_Allocated.get(), Available_Quantity.get(), Available_Value.get(), One_Inventory_Levels.get()
                )
            productList.delete(0, END)
            productList.insert(END, Item_Number.get(), Item_Category.get(), Item_Description.get(), HSN_Code.get(), Opening_Balance_Date.get(), Opening_Balance_Quantity.get(), Opening_Balance_Value_In_INR.get(),
                Job_Default.get(), Default_Unit_Of_Measure.get(), Pricing_Group.get(), Purchases.get(),
                Adjustments.get(), RFQs.get(), Total.get(), Sales.get(), Quotes.get(), Total_Allocated.get(), Available_Quantity.get(), Available_Value.get(), One_Inventory_Levels.get()
            )
            showInProductList()
            clear()
            print("Products : Update method finished\n")

        Label(f2, text="Item Number: ").grid(row=0, column=0)
        itemnumber = Entry(f2, font="bold", textvariable=Item_Number)
        itemnumber.grid(row=0, column=1)

        Label(f2, text="Item Category: ", ).grid(row=0, column=2)
        itemcategory = Entry(f2, font="bold",textvariable=Item_Category)
        itemcategory.grid(row=0, column=3)

        Label(f2, text="Item Description: ").grid(row=1, column=0)
        itemdescription = Entry(f2, font="bold", textvariable=Item_Description)
        itemdescription.grid(row=1, column=1)

        Label(f2, text="HSN Code: ").grid(row=1, column=2)
        hsncode = Entry(f2, font="bold", textvariable=HSN_Code)
        hsncode.grid(row=1, column=3)

        Label(f2, text="Opening Balance Date: ").grid(row=2, column=0)
        openingbalancedate = Entry(f2, font="bold", textvariable=Opening_Balance_Date)
        openingbalancedate.grid(row=2, column=1)

        Label(f2, text="Opening Balance Quantity: ").grid(row=2, column=2)
        openingbalancequantity = Entry(f2, font="bold", textvariable=Opening_Balance_Quantity)
        openingbalancequantity.grid(row=2, column=3)

        Label(f2, text="Opening Balance Value in INR: ").grid(row=3, column=0)
        openingbalancevalueininr = Entry(f2, font="bold", textvariable=Opening_Balance_Value_In_INR)
        openingbalancevalueininr.grid(row=3, column=1)

        Label(f2, text="Job Default: ").grid(row=4, column=0)
        jobdefault = Entry(f2, font="bold", textvariable=Job_Default)
        jobdefault.grid(row=4, column=1)

        Label(f2, text="Default Unit of Measure: ").grid(row=4, column=2)
        defaultunitofmeasure = Entry(f2, font="bold", textvariable=Default_Unit_Of_Measure)
        defaultunitofmeasure.grid(row=4, column=3)

        Label(f2, text="Pricing Group: ").grid(row=5, column=0)
        pricinggroup = Entry(f2, font="bold", textvariable=Pricing_Group)
        pricinggroup.grid(row=5, column=1)

        Checkbutton(f2, text="Item is Inventoried").grid(row=5, column=2)

        Checkbutton(f2, text="Item is Sold").grid(row=6, column=0)

        Checkbutton(f2, text="Item is Bought").grid(row=6, column=1)

        Checkbutton(f2, text="Is iTuneConnect Product").grid(row=6, column=2)

        Label(f2, text="Purchases: ").grid(row=7, column=0)
        purchases = Entry(f2, font="bold", textvariable=Purchases)
        purchases.grid(row=7, column=1)

        Label(f2, text="Adjustments: ").grid(row=7, column=2)
        adjustments = Entry(f2, font="bold", textvariable=Adjustments)
        adjustments.grid(row=7, column=3)

        Label(f2, text="RFQs: ").grid(row=8, column=0)
        rfqs = Entry(f2, font="bold", textvariable=RFQs)
        rfqs.grid(row=8, column=1)

        Label(f2, text="Total: ").grid(row=8, column=2)
        total = Entry(f2, font="bold", textvariable=Total)
        total.grid(row=8, column=3)

        Label(f2, text="Sales: ").grid(row=9, column=0)
        sales = Entry(f2, font="bold", textvariable=Sales)
        sales.grid(row=9, column=1)

        Label(f2, text="Quotes: ").grid(row=9, column=2)
        quotes = Entry(f2, font="bold", textvariable=Quotes)
        quotes.grid(row=9, column=3)

        Label(f2, text="Total Allocated: ").grid(row=10, column=0)
        totalallocated = Entry(f2, font="bold", textvariable=Total_Allocated)
        totalallocated.grid(row=10, column=1)

        Label(f2, text="Available Quantity: ").grid(row=10, column=2)
        availablequantity = Entry(f2, font="bold", textvariable=Available_Quantity)
        availablequantity.grid(row=10, column=3)

        Label(f2, text="Available Value: ").grid(row=16, column=0)
        availablevalue = Entry(f2, font="bold", textvariable=Available_Value)
        availablevalue.grid(row=16, column=1)

        Label(f2, text="1 Inventory Levels: ").grid(row=17, column=0)
        oneinventorylevels = Entry(f2, font="bold", textvariable=One_Inventory_Levels)
        oneinventorylevels.grid(row=17, column=1)

        buttonSaveData = Button(f3, text='Save', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=insert)
        buttonSaveData.grid(row=0, column=0, pady=10)

        buttonShowData = Button(f3, text='Show Data', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command= showInProductList)
        buttonShowData.grid(row=0, column=1, pady=10, padx=10)

        buttonClearData = Button(f3, text='Reset', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=clear)
        buttonClearData.grid(row=0, column=2, pady=10)

        buttonDeleteData = Button(f3, text='Delete', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=delete)
        buttonDeleteData.grid(row=1, column=0)

        buttonsearchData = Button(f3, text='Search', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=search)
        buttonsearchData.grid(row=1, column=1, padx=10)

        buttonUpdate = Button(f3, text='Update', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=update)
        buttonUpdate.grid(row=1, column=2)

        def productRec(event):
            print("Products : ProductRec method called")
            global pd 
            searchPd = productList.curselection()[0]
            pd = productList.get(searchPd)
            itemnumber.delete(0, END)
            itemnumber.insert(END, pd[0])
            itemcategory.delete(0, END)
            itemcategory.insert(END, pd[1])
            itemdescription.delete(0, END)
            itemdescription.insert(END, pd[2])
            hsncode.delete(0, END)
            hsncode.insert(END, pd[3])
            openingbalancedate.delete(0, END)
            openingbalancedate.insert(END, pd[4])
            openingbalancequantity.delete(0, END)
            openingbalancequantity.insert(END, pd[5])
            openingbalancevalueininr.delete(0, END)
            openingbalancevalueininr.insert(END, pd[6])
            jobdefault.delete(0, END)
            jobdefault.insert(END, pd[7])
            defaultunitofmeasure.delete(0, END)
            defaultunitofmeasure.insert(END, pd[8])
            pricinggroup.delete(0, END)
            pricinggroup.insert(END, pd[9])
            purchases.delete(0, END)
            purchases.insert(END, pd[10])
            adjustments.delete(0, END)
            adjustments.insert(END, pd[11])
            rfqs.delete(0, END)
            rfqs.insert(END, pd[12])
            total.delete(0, END)
            total.insert(END, pd[13])
            sales.delete(0, END)
            sales.insert(END, pd[14])
            quotes.delete(0, END)
            quotes.insert(END, pd[15])
            totalallocated.delete(0, END)
            totalallocated.insert(END, pd[16])
            availablequantity.delete(0, END)
            availablequantity.insert(END, pd[17])
            availablevalue.delete(0, END)
            availablevalue.insert(END, pd[18])
            oneinventorylevels.delete(0, END)
            oneinventorylevels.insert(END, pd[19])
            print("Products : ProductRec method finished\n")

        scroll = Scrollbar(f1)
        scroll.grid(row=0, column=1, sticky='ns')

        scroll2 = Scrollbar(f1, orient=HORIZONTAL)
        scroll2.grid(row=1, column=0, sticky='ew')

        productList = Listbox(f1, width=60, height=18, font=('arial', 12, 'bold'), xscrollcommand=scroll2.set, yscrollcommand=scroll.set)
        productList.bind('<<ListboxSelect>>', productRec)
        productList.grid(row=0, column=0)

        scroll.config(command=productList.yview)
        scroll2.config(command=productList.xview)

        css.mainloop()


class DatabaseProducts:
    def conn(self):
        print("Database : Connection method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "create table if not exists Products(Item_Number text, Item_Category text, Item_Description text, HSN_Code text, Opening_Balance_Date text, Opening_Balance_Quantity text, Opening_Balance_Value_In_INR text, Job_Default text, Default_Unit_Of_Measure text, Pricing_Group text, Purchases text, Adjustments text, RFQs text, Total text, Sales text, Quotes text, Total_Allocated text, Available_Quantity text, Available_Value text, One_Inventory_Levels text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : Connection method finished\n")

    def insert(self, Item_Number, Item_Category, Item_Description, HSN_Code, Opening_Balance_Date, Opening_Balance_Quantity, Opening_Balance_Value_In_INR, Job_Default, Default_Unit_Of_Measure, Pricing_Group, Purchases, Adjustments, RFQs, Total, Sales, Quotes, Total_Allocated, Available_Quantity, Available_Value, One_Inventory_Levels):
        print("Database : Insert method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "insert into Products values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, (Item_Number, Item_Category, Item_Description, HSN_Code, Opening_Balance_Date, Opening_Balance_Quantity, Opening_Balance_Value_In_INR, Job_Default, Default_Unit_Of_Measure, Pricing_Group, Purchases, Adjustments, RFQs, Total, Sales, Quotes, Total_Allocated, Available_Quantity, Available_Value, One_Inventory_Levels))
        con.commit()
        con.close()
        print("Database : Insert method finished\n")

    def show(self):
        print("Database : Show method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "select * from Products"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : Show method finished\n")
        return rows

    def delete(self, Item_Number):
        print("Database : Delete method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("delete from Products where Item_Number=?", (Item_Number,))
        con.commit()
        con.close()
        print("Database : Delete method finished\n")

    def search(self, Item_Number=""):
        print("Database : Search method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("select * from Products where Item_Number=?", (Item_Number))
        row = cur.fetchall()   
        con.commit()
        con.close()
        print("Database : Search method finished\n")
        return row

    def update(self, Item_Number=""):
        print("Database : Update method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("update Customer set Item_Number=?", (Item_Number))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Update method finished\n")
