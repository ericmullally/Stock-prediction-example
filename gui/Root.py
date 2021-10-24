from tkinter import *

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title = "Stock Chart"
        self.root.geometry("1000x550")

    
    def show(self):
        self.root.mainloop()