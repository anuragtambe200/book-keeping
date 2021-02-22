from tkinter import *

class About():
    def __init__(self, root):
        root = root
        root.title("Book Keeping - Help / About - About")
        root.iconbitmap('./icon.ico')
        root.state('zoomed')

        Label(root, text='''Book Keeping\nVersion 1.0\nCreator - Anurag Tambe\nVersion Release Date - XX XX 2020''', font=20, justify=CENTER).pack()

        root.mainloop()
