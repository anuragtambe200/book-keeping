from tkinter import *
from Customer_Sales import CustomerSales
from Employees_Btn import EmployeesBtn
from Products_Services import ProductsServices
from Supplier_Purchase import SupplierPurchase
from Help_About import HelpAbout
from Change_Account_Settings import ChangeAccountSettings


class MainApp:
    def __init__(self, root):
        main_app = root
        main_app.title("Book Keeping")
        main_app.iconbitmap("./icon.ico")
        main_app.state('zoomed')

        def customer_sales():
            root = Toplevel()
            customersales = CustomerSales(root)
            root.mainloop()

        def employees():
            root = Toplevel()
            application = EmployeesBtn(root)
            root.mainloop()

        def products_services():
            root = Toplevel()
            productsservices = ProductsServices(root)
            root.mainloop()

        def supplier_purchase():
            root = Toplevel()
            supplierpurchase = SupplierPurchase(root)
            root.mainloop()

        def help_about():
            root = Toplevel()
            helpabout = HelpAbout(root)
            root.mainloop()

        def changeaccountsettings():
            root = Toplevel()
            helpabout = ChangeAccountSettings(root)
            root.mainloop()

        menu = Menu(main_app)

        menu.add_cascade(label="Products", command=products_services)
        menu.add_cascade(label="Customers", command=customer_sales)
        menu.add_cascade(label="Suppliers / Purchase", command=supplier_purchase)
        menu.add_cascade(label="Reports")
        menu.add_cascade(label="Backup")
        menu.add_cascade(label="Verify Books")
        menu.add_cascade(label="Calculator")
        menu.add_cascade(label="Alerts")
        menu.add_cascade(label="Book Details")
        menu.add_cascade(label="Log Out")
        menu.add_cascade(label="App Settings")
        menu.add_cascade(label="Book Settings")
        menu.add_cascade(label="Help / About", command=help_about)
        menu.add_cascade(label="Exit", command=main_app.destroy)

        main_app.config(menu=menu)

        main_frame = Frame(main_app)    
        main_frame.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scroll = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scroll.pack(side=RIGHT, fill=Y)

        my_scroll2 = Scrollbar(main_app, orient=HORIZONTAL, command=my_canvas.xview)
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

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Book Details").grid(row=0, column=0)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Administration").grid(row=0, column=1, padx=10)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Accounts").grid(row=0, column=2)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Alerts").grid(row=0, column=3, padx=10)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="About / Help", command=help_about).grid(row=0, column=4)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Customer / Sales", command=customer_sales).grid(row=1, column=0, pady=10)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Current P & L").grid(row=1, column=1)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Banking").grid(row=1, column=2)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Data Processing").grid(row=1, column=3)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="General Help").grid(row=1, column=4)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Current / Balance").grid(row=2, column=0)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Employees", command=employees).grid(row=2, column=1)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Expense / Budget").grid(row=2, column=2)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Drop Box").grid(row=2, column=3)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Reports").grid(row=2, column=4)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Products / Services", command=products_services).grid(row=3, column=0, pady=10)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Jobs").grid(row=3, column=1)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="General Journal").grid(row=3, column=2)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Sync").grid(row=3, column=3)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Rate This App").grid(row=3, column=4)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Suppliers / Purchase", command=supplier_purchase).grid(row=4, column=0)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Share Portfolio").grid(row=4, column=1)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Lager Entries").grid(row=4, column=2)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Search").grid(row=4, column=3)

        Button(second_frame, height=1, width=15, padx=16, bd=8, font=15, text="Change Account Settings", command=changeaccountsettings).grid(row=4, column=4)

        main_app.mainloop()

root = Tk()
mainapp = MainApp(root)
root.mainloop()