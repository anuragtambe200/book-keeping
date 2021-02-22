from tkinter import *
from tkinter import ttk
import sqlite3
from itertools import chain
from Employee import Employees
from Employee import DatabaseEmployee


class EmployeeEntitlement:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Keeping - Employee - New Employee Entitlement")
        self.root.state('zoomed')
        self.root.iconbitmap('./icon.ico')

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

        root = second_frame
        
        DB = DatabaseEmployeeEntitlement()
        DB.conn()

        EmployeeName = StringVar()
        Entitlement = StringVar()
        Entitlement_Id = StringVar()
        Entitlement_Expense_Account = StringVar()
        Entitlement_Payment__Accural_Account = StringVar()

        f2 = ttk.Frame(root, width=100, height=100)
        f2.grid(row=0, column=0)

        f1 = ttk.Frame(root, width=600, height=380)
        f1.grid(row=0, column=1, padx=20)

        f3 = ttk.Frame(root, width=10, height=10)
        f3.grid(row=1, column=0)

        def employeeEntitlementRec(event):
            print("Employee Entitlement : CustomerRec method called")
            global pd
            searchpd = employeeEntitlementList.curselection()[0]
            pd = employeeEntitlementList.get(searchpd)
            employeename.delete(0, END)
            employeename.insert(END, pd[0])
            entitlement_id.delete(0, END)
            entitlement_id.insert(END, pd[1])
            entitlement.delete(0, END)
            entitlement.insert(END, pd[2])
            entitlement_expense_account.delete(0, END)
            entitlement_expense_account.insert(END,pd[3])
            entitlement_payment__accural_account.delete(0, END)
            entitlement_payment__accural_account.insert(END, pd[4])
            print("Employee Entitlement : CustomerRec method finished")

        def clear():
            print("Employee Entitlement : Clear method called")
            employeename.delete(0, END)
            entitlement_id.delete(0, END)
            entitlement.delete(0, END)
            entitlement_expense_account.delete(0, END)
            entitlement_payment__accural_account.delete(0, END)
            print("Employee Entitlement : Clear method finished\n")

        def insert():
            print("Employee Entitlement : Insert method called")
            DB.insert(employeename.get(), Entitlement_Id.get(), Entitlement.get(), Entitlement_Expense_Account.get(), Entitlement_Payment__Accural_Account.get())
            employeeEntitlementList.delete(0, END)
            employeeEntitlementList.insert(END, employeename.get(), Entitlement_Id.get(), Entitlement.get(), Entitlement_Expense_Account.get(), Entitlement_Payment__Accural_Account.get())
            showInEmployeeEntitlementList()
            clear()
            print("Employee Entitlement : Insert method finished\n")
            
        def showInEmployeeEntitlementList():
            print("Employee Entitlement : ShowInEmployeeList method called")
            employeeEntitlementList.delete(0, END)
            for row in DB.show():
                employeeEntitlementList.insert(END, row, str(""))
            print("Employee Entitlement : ShowInEmployeeList method finished\n")
        
        def search():
            print("Employee Entitlement : Search method called")
            employeeEntitlementList.delete(0,END)
            for row in DB.search(Entitlement_Id.get()):
                employeeEntitlementList.insert(END, row, str(""))
            print("Employee Entitlement : Search method finished\n")
        
        def delete():
            print("Employee Entitlement : Delete method called")
            DB.delete(pd[1])
            clear()
            showInEmployeeEntitlementList() 
            print("Employee Entitlement : Delete method finished\n")

        def update():
            print("Employee Entitlement : Update method called")
            print("pd[1]", pd[1])
            DB.delete(pd[1])
            DB.insert(employeename.get(), Entitlement_Id.get(), Entitlement.get(), Entitlement_Expense_Account.get(), Entitlement_Payment__Accural_Account.get())
            employeeEntitlementList.delete(0, END)
            employeeEntitlementList.insert(END, employeename.get(), Entitlement_Id.get(), Entitlement.get(), Entitlement_Expense_Account.get(), Entitlement_Payment__Accural_Account.get())
            showInEmployeeEntitlementList()
            clear()
            print("Employee Entitlement : Update method finished")

        def employee():
            root = Toplevel()
            app = Employees(root)
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

        for row in DB.employeename(EmployeeName):
            test_list.append(row)

        test_list = list(flattern(test_list))

        employeename = Entry(f2)
        employeename.grid(row=1, column=1)
        employeename.bind('<KeyPress>', on_keypress)

        def on_select(event):
            print('(event) previous:', event.widget.get('active'))
            print('(event)  current:', event.widget.get(event.widget.curselection()))
            print('---')
            searchpds = listbox.curselection()[0]
            pds = listbox.get(searchpds)
            employeename.delete(0, END)
            employeename.insert(END, pds)

        listbox = Listbox(f2, height=5)
        listbox.grid(row=1, column=2)
        listbox.bind('<<ListboxSelect>>', on_select)
        listbox_update(test_list)

        Label(f2, text="Employee Name").grid(row=1, column=0)
        
        ttk.Button(f2, text="+", command=employee).grid(row=1, column=3, padx=5, pady=5)

        Label(f2, text="Entitlement Id").grid(row=2, column=0)
        entitlement_id = Entry(f2, font=10, textvariable=Entitlement_Id)
        entitlement_id.grid(row=2, column=1, padx=5, pady=5)

        Label(f2, text="Entitlement").grid(row=3, column=0)
        entitlement = Entry(f2, font=10, textvariable=Entitlement)
        entitlement.grid(row=3, column=1, padx=5, pady=5)

        Label(f2, text="Entitlement Expense Account").grid(row=4, column=0)
        entitlement_expense_account = Entry(f2, font=10, textvariable = Entitlement_Expense_Account)
        entitlement_expense_account.grid(row=4, column=1, padx=5, pady=5)

        Label(f2, text="Entitlement Payment / Accural Account").grid(row=5, column=0)
        entitlement_payment__accural_account = Entry(f2, font=10, textvariable=Entitlement_Payment__Accural_Account)
        entitlement_payment__accural_account.grid(row=5, column=1, padx=5, pady=5)

        buttonSaveData = Button(f3, text='Save', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=insert)
        buttonSaveData.grid(row=0, column=0, pady=10)

        buttonShowData = Button(f3, text='Show Data', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command= showInEmployeeEntitlementList)
        buttonShowData.grid(row=0, column=1, padx=10, pady=10)

        buttonClearData = Button(f3, text='Reset', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=clear)
        buttonClearData.grid(row=0, column=2, pady=10)

        buttonDeleteData = Button(f3, text='Delete', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=delete)
        buttonDeleteData.grid(row=1, column=0, pady=10)

        buttonsearchData = Button(f3, text='Search', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=search)
        buttonsearchData.grid(row=1, column=1, padx=10, pady=10)

        buttonUpdate = Button(f3, text='Update', font=('arial', 12, 'bold'), height=1, width=10, bd=4, command=update)
        buttonUpdate.grid(row=1, column=2, pady=10)

        scroll = Scrollbar(f1)
        scroll.grid(row=0, column=16, sticky='ns', rowspan=15)

        scroll2 = Scrollbar(f1, orient=HORIZONTAL)
        scroll2.grid(row=16, column=14, sticky='ew', columnspan=4)

        employeeEntitlementList = Listbox(f1, width=60, height=10, font=('arial', 12, 'bold'), yscrollcommand=scroll.set, xscrollcommand=scroll2.set)

        employeeEntitlementList.bind('<<ListboxSelect>>', employeeEntitlementRec)
        employeeEntitlementList.grid(row=0, column=15, rowspan=15)
        
        scroll.config(command=employeeEntitlementList.yview)
        scroll2.config(command=employeeEntitlementList.xview)

        root.mainloop()


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
