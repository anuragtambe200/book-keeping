from tkinter import *


class Help():
    def __init__(self, root):
        root = root
        root.title("Book Keeping - Help / About - Help")
        root.iconbitmap('./icon.ico')
        root.state('zoomed')

        Label(root, text="You are on Right Platform Now", font=20).pack()

        root.mainloop()
