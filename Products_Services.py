from tkinter import *
from tkinter import messagebox
from Products import Products
from Products import DatabaseProducts


class ProductsServices:
    def __init__(self, root):
        ps = root
        ps.title("Book Keeping - Products / Services")
        ps.iconbitmap('./icon.ico')
        ps.state('zoomed')

        main_frame = Frame(ps)
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

        def products():
            ps = Toplevel()
            application = Products(ps)
            ps.mainloop()

        def services():
            ps.destroy()
            messagebox.showinfo("Book Keeping", "This feature is not avaliable right now.")

        products_btn = Button(second_frame, text="Products", command=products, height=1, width=15, padx=16, bd=8, font=15)
        products_btn.grid(row=0, column=0, padx=20, pady=5)

        services_btn = Button(second_frame, text="Services", command=services, height=1, width=15, padx=16, bd=8, font=15)
        services_btn.grid(row=0, column=1, pady=5)

        ps.mainloop()
