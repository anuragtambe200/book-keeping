import sqlite3


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


DatabaseCustomer().conn()


class DatabaseEmployeeEntitlement:
    def conn(self):
        print("Database : Connection method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "create table if not exists Employee_Entitlement(Employee_Name, Entitlement_Id text, Entitlement text, Entitlement_Expense_Account text, Entitlement_Payment__Accural_Account text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : Connection method finished\n")

    def insert(self, Employee_Name, Entitlement_Id, Entitlement, Entitlement_Expense_Account, Entitlement_Payment__Accural_Account):
        print("Database : Insert method called abc")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "insert into Employee_Entitlement values(?, ?, ?, ?, ?)"
        cur.execute(query, (Employee_Name, Entitlement_Id, Entitlement, Entitlement_Expense_Account, Entitlement_Payment__Accural_Account))
        con.commit()
        con.close()
        print("Database : Insert method finished abc\n")

    def show(self):
        print("Database : Show method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "select * from Employee_Entitlement"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : Show method finished\n")
        return rows

    def delete(self, Entitlement_Id):
        print("Database : Delete method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("delete from Employee_Entitlement where Entitlement_Id=?", (Entitlement_Id,))
        con.commit()
        con.close()
        print("Database : Delete method finished\n")

    def search(self, Entitlement_Id=""):
        print("Database : Search method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("select * from Employee_Entitlement where Entitlement_Id=?", (Entitlement_Id))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Search method finished\n")
        return row

    def update(self, Entitlement_Id=""):
        print("Database : Update method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("update Customer set Entitlement_Id", (Entitlement_Id))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Update method finished\n")

    def employeename(self, Employee_Name):
        print("Database : Employeename method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("select Employee_Name from Employees")
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Employeename method finished")
        return row


DatabaseEmployeeEntitlement().conn()


class DatabaseEmployee:
    def conn(self):
        print("Database : Connection method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "create table if not exists Employees(Employee_Name text, Employee_Number text, Birth_Date, Tax_File_Number text, Address text, Department text, Income_Tax_Band text, Salary_Expense_Account text, Tax_Owing__Accural_Account text, Pay_From_Account text, Salary_Payment_Period text, Default_Salary_Amount text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : Connection method finished\n")

    def insert(self, Employee_Name, Employee_Number, Birth_Date, Tax_File_Number, Address, Department, Income_Tax_Band, Salary_Expense_Account, Tax_Owing__Accural_Account, Pay_From_Account, Salary_Payment_Period, Default_Salary_Amount):
        print("Database : Insert method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "insert into Employees values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, (Employee_Name, Employee_Number, Birth_Date, Tax_File_Number, Address, Department, Income_Tax_Band, Salary_Expense_Account, Tax_Owing__Accural_Account, Pay_From_Account, Salary_Payment_Period, Default_Salary_Amount))
        con.commit()
        con.close()
        print("Database : Insert method finished\n")

    def show(self):
        print("Database : Show method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "select * from Employees"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : Show method finished\n")
        return rows

    def delete(self, Employee_Number):
        print("Database : Delete method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("delete from Employees where Employee_Number=?", (Employee_Number,))
        con.commit()
        con.close()
        print("Database : Delete method finished\n")

    def search(self, Employee_Number=""):
        print("Database : Search method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("select * from Employees where Employee_Number=?", (Employee_Number))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Search method finished\n")
        return row

    def update(self, Employee_Number=""):
        print("Database : Update method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("update Customer set Employee_Number=?", (Employee_Number))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Update method finished\n")


DatabaseEmployee().conn()


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


DatabaseProducts().conn()


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


DatabasePurchase().conn()


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


DatabaseSaleItemList().conn()


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


DatabaseSales().conn()


class DatabaseServiceReport:
    def conn(self):
        print("Database : Connection method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "create table if not exists Service(Customer_Name text, Service_Number text, Service_Type text, Service_Date text, Due_Date text, Service_Description text, INR_Total text, INR_Balance_Due text, Ex_Tax text, Bill_To_Address text, Ship_To_Address text, Service_Comments text, Service_Reference text, Ship_To_Name text, Shipment_Date text, Notes text, Salesperson text, Department text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : Connection method finished")

    def insert(self, Customer_Name, Service_Number, Service_Type, Service_Date, Due_Date, Service_Description, INR_Total, INR_Balance_Due, Ex_Tax, Bill_To_Address, Ship_To_Address, Service_Comments, Service_Reference, Ship_To_Name, Shipment_Date, Notes, Salesperson, Department):
        print("Database : Insert method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "insert into Service values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, (Customer_Name, Service_Number, Service_Type, Service_Date, Due_Date, Service_Description, INR_Total, INR_Balance_Due, Ex_Tax, Bill_To_Address, Ship_To_Address, Service_Comments, Service_Reference, Ship_To_Name, Shipment_Date, Notes, Salesperson, Department))
        con.commit()
        con.close()
        print("Database : Insert method finished\n")

    def show(self):
        print("Database : Show method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        query = "select * from Service"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : Show method finished\n")
        return rows

    def delete(self, Service_Number):
        print("Database : Delete method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("delete from Service where Service_Number=?", (Service_Number,))
        con.commit()
        con.close()
        print("Database : Delete method finished\n")

    def search(self, Service_Number):
        print("Database : Search method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("select * from Service where Service_Number=?", (Service_Number))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Search method finished\n")
        return row

    def update(self, Service_Number=""):
        print("Database : Update method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("update Customer set Service_Number=?", (Service_Number))
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Update method finished\n")

    def customername(self, Customer_Name):
        print("Database : Customername method called")
        con = sqlite3.connect("Book Keeping.db")
        cur = con.cursor()
        cur.execute("select Customer_Name from Customer")
        row = cur.fetchall()
        con.commit()
        con.close()
        print("Database : Customername method finished\n")
        return row


DatabaseServiceReport().conn()


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


DatabaseSupplier().conn()
