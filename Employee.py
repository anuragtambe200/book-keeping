from tkinter import *
from tkinter import messagebox, ttk
import sqlite3


class Employees:
    def __init__(self, root):
        DB = DatabaseEmployee()
        DB.conn()

        self.root = root
        self.root.title("Book Keeping - Employee")
        self.root.state('zoomed')
        self.root.iconbitmap("./icon.ico")

        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scroll = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scroll.pack(side=RIGHT, fill=Y)

        my_scroll2 = Scrollbar(my_canvas, orient=HORIZONTAL, command=my_canvas.xview)
        my_scroll2.pack(side=BOTTOM, fill=X)

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

        emp1 = second_frame

        DB = DatabaseEmployee()
        DB.conn()

        Employee_Name = StringVar()
        Employee_Number = StringVar()
        Birth_Date = StringVar()
        Tax_File_Number = StringVar()
        Department = StringVar()
        Income_Tax_Band = StringVar()
        Salary_Expense_Account = StringVar()
        Address = StringVar()
        Tax_Owing__Accural_Account = StringVar()
        Pay_From_Account = StringVar()
        Salary_Payment_Period = StringVar()
        Default_Salary_Amount = StringVar()

        f2 = ttk.Frame(emp1, width=100, height=100)
        f2.grid(row=0, column=0)

        f1 = ttk.Frame(emp1, width=600, height=380)
        f1.grid(row=0, column=1, padx=20)

        f3 = ttk.Frame(emp1, width=10, height=10)
        f3.grid(row=1, column=0)

        def employeeRec(event):
            print("Employee : CustomerRec method called")
            global pd
            searchpd = employeeList.curselection()[0]
            pd = employeeList.get(searchpd)
            employeename.delete(0, END)
            employeename.insert(END, pd[0])
            employeenumber.delete(0, END)
            employeenumber.insert(END, pd[1])
            birthdate.delete(0, END)
            birthdate.insert(END, pd[2])
            taxfilenumber.delete(0, END)
            taxfilenumber.insert(END, pd[3])
            address.delete(0, END)
            address.insert(END, pd[4])
            department.delete(0, END)
            department.insert(END, pd[5])
            incometaxband.delete(0, END)
            incometaxband.insert(END, pd[6])
            salaryexpenseaccount.delete(0, END)
            salaryexpenseaccount.insert(END, pd[7])
            taxowing_accuralaccount.delete(0, END)
            taxowing_accuralaccount.insert(END, pd[8])
            payfromaccount.delete(0, END)
            payfromaccount.insert(END, pd[9])
            salarypaymentperiod.delete(0, END)
            salarypaymentperiod.insert(END, pd[10])
            defaultsalaryamount.delete(0, END)
            defaultsalaryamount.insert(END, pd[11])
            print("Employee : CustomerRec method finished\n")

        def clear():
            print("Employee : Clear method called")
            employeename.delete(0, END)
            employeenumber.delete(0, END)
            birthdate.delete(0, END)
            taxfilenumber.delete(0, END)
            address.delete(0, END)
            department.delete(0, END)
            incometaxband.delete(0, END)
            salaryexpenseaccount.delete(0, END)
            taxowing_accuralaccount.delete(0, END)
            payfromaccount.delete(0, END)
            salarypaymentperiod.delete(0, END)
            defaultsalaryamount.delete(0, END)
            print("Employee : Clear method finished\n")

        def insert():
            print("Employee : Insert method called")
            if (Employee_Number.get() != 0):
                DB.insert(
                    Employee_Name.get(), Employee_Number.get(), Birth_Date.get(), Tax_File_Number.get(), Address.get(), Department.get(), Income_Tax_Band.get(), 
                    Salary_Expense_Account.get(), Tax_Owing__Accural_Account.get(), Pay_From_Account.get(), Salary_Payment_Period.get(), Default_Salary_Amount.get()
                )
                employeeList.delete(0, END)
                employeeList.insert(
                    END, Employee_Name.get(), Employee_Number.get(), Birth_Date.get(), Tax_File_Number.get(), Address.get(), Department.get(), Income_Tax_Band.get(), 
                    Salary_Expense_Account.get(), Tax_Owing__Accural_Account.get(), Pay_From_Account.get(), Salary_Payment_Period.get(), Default_Salary_Amount.get()
                )
                showInEmployeeList()
                clear()
                print("Employee : Insert method finished\n")
            else:
                messagebox.showerror("Book Keeping", "Enter Employee Number")

        def showInEmployeeList():
            print("Employee : ShowInEmployeeList method called")
            employeeList.delete(0, END)
            for row in DB.show():
                employeeList.insert(END, row, str(""))
            print("Employee : ShowInEmployeeList method finished\n")

        def search():
            print("Employee : Search method called")
            employeeList.delete(0, END)
            for row in DB.search(Employee_Number.get()):
                employeeList.insert(END, row, str(""))

            print("Employee : Search method finished\n")

        def delete():
            print("Employee : Delete method called")
            DB.delete(pd[1])
            clear()
            showInEmployeeList()
            print("Employee : Delete method finished\n")

        def update():
            print("Employee : Update method called")
            print("pd[1]", pd[1])
            DB.delete(pd[1])
            DB.insert(
                Employee_Name.get(), Employee_Number.get(), Birth_Date.get(), Tax_File_Number.get(), Address.get(), Department.get(), Income_Tax_Band.get(), 
                Salary_Expense_Account.get(), Tax_Owing__Accural_Account.get(), Pay_From_Account.get(), Salary_Payment_Period.get(), Default_Salary_Amount.get()
            )
            employeeList.delete(0, END)
            employeeList.insert(
                END, Employee_Name.get(), Employee_Number.get(), Birth_Date.get(), Tax_File_Number.get(), Address.get(), Department.get(), Income_Tax_Band.get(), \
                Salary_Expense_Account.get(), Tax_Owing__Accural_Account.get(), Pay_From_Account.get(), Salary_Payment_Period.get(), Default_Salary_Amount.get()
            )
            showInEmployeeList()
            clear()
            print("Employee : Update method finished")

        Label(f2, text="Employee Name:").grid(row=0, column=0, padx=5, pady=5)
        employeename = Entry(f2, font=10, textvariable=Employee_Name)
        employeename.grid(row=0, column=1, padx=5, pady=5)

        Label(f2, text="Employee Number:").grid(row=1, column=0, padx=5, pady=5)
        employeenumber = Entry(f2, font=10, textvariable=Employee_Number)
        employeenumber.grid(row=1, column=1, pady=5, padx=5)

        Checkbutton(f2, text="Is Income Tax Incremental").grid(row=2, column=0, padx=5, pady=5)

        Label(f2, text="Birth Date:").grid(row=3, column=0, padx=5, pady=5)
        birthdate = Entry(f2, font=10, textvariable=Birth_Date)
        birthdate.grid(row=3, column=1, padx=5, pady=5)

        Label(f2, text="Tax File Number:").grid(row=3, column=2, padx=5, pady=5)
        taxfilenumber = Entry(f2, font=10, textvariable=Tax_File_Number)
        taxfilenumber.grid(row=3, column=3, padx=5, pady=5)

        Label(f2, text="Address:").grid(row=4, column=0, padx=5, pady=5)
        address = Entry(f2, font=10, textvariable=Address)
        address.grid(row=4, column=1, padx=5, pady=5)

        Label(f2, text="Department:").grid(row=4, column=2, padx=5, pady=5)
        department = Entry(f2, font=10, textvariable=Department)
        department.grid(row=4, column=3, padx=5, pady=5)

        Label(f2, text="Income Tax Band:").grid(row=5, column=0, padx=5, pady=5)
        incometaxband = Entry(f2, font=10, textvariable=Income_Tax_Band)
        incometaxband.grid(row=5, column=1, padx=5, pady=5)

        Label(f2, text="Salary Expense Account:").grid(row=6, column=0, padx=5, pady=5)
        salaryexpenseaccount = Entry(f2, font=10, textvariable=Salary_Expense_Account)
        salaryexpenseaccount.grid(row=6, column=1, padx=5, pady=5)

        Label(f2, text="Tax Owing / Accural Account:").grid(row=7, column=0, padx=5, pady=5)
        taxowing_accuralaccount = Entry(f2, font=10, textvariable=Tax_Owing__Accural_Account)
        taxowing_accuralaccount.grid(row=7, column=1, padx=5, pady=5)

        Label(f2, text="Pay From Account:").grid(row=8, column=0, padx=5, pady=5)
        payfromaccount = Entry(f2, font=10, textvariable=Pay_From_Account)
        payfromaccount.grid(row=8, column=1, padx=5, pady=5)

        Label(f2, text="Salary Payment Period:").grid(row=9, column=0, padx=5, pady=5)
        salarypaymentperiod = Entry(f2, font=10, textvariable=Salary_Payment_Period)
        salarypaymentperiod.grid(row=9, column=1, padx=5, pady=5)

        Label(f2, text="Default Salary Amount:").grid(row=10, column=0, padx=5, pady=5)
        defaultsalaryamount = Entry(f2, font=10, textvariable=Default_Salary_Amount)
        defaultsalaryamount.grid(row=10, column=1, padx=5, pady=5)

        issalesperson = Checkbutton(f2, text="Is Sales Person").grid(row=11, column=0, padx=5, pady=5)

        Checkbutton(f2, text="Is Purchase Person").grid(row=11, column=2, padx=5, pady=5)

        scroll = Scrollbar(f1)
        scroll.grid(row=15, column=5, sticky='ns')

        scroll2 = Scrollbar(f1, orient=HORIZONTAL)
        scroll2.grid(row=16, column=0, sticky='ew', columnspan=4)

        employeeList = Listbox(f1, width=60, height=20, font=('arial', 12, 'bold'), yscrollcommand=scroll.set, xscrollcommand=scroll2.set)

        # called above created productRec function of init
        employeeList.bind('<<ListboxSelect>>', employeeRec)
        employeeList.grid(row=15, column=0, columnspan=4)

        scroll.config(command=employeeList.yview)
        scroll2.config(command=employeeList.xview)

        buttonSaveData = Button(f3, text='Save', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=insert)
        buttonSaveData.grid(row=0, column=0, pady=10)

        buttonShowData = Button(f3, text='Show Data', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=showInEmployeeList)
        buttonShowData.grid(row=0, column=1, pady=10, padx=10)

        buttonClearData = Button(f3, text='Reset', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=clear)
        buttonClearData.grid(row=0, column=2, pady=10)

        buttonDeleteData = Button(f3, text='Delete', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=delete)
        buttonDeleteData.grid(row=1, column=0)

        buttonsearchData = Button(f3, text='Search', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=search)
        buttonsearchData.grid(row=1, column=1, padx=10)

        buttonUpdate = Button(f3, text='Update', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=update)
        buttonUpdate.grid(row=1, column=2)

        emp1.mainloop()


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
