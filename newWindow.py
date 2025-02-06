from PIL import ImageTk,Image
from ttkbootstrap.constants import *
import  ttkbootstrap as tb
class new_window():
    def __init__(self):
        self.root = tb.Window(themename="darkly")
        self.my_notebook=tb.Notebook(self.root,bootstyle="danger")
        self.my_notebook.pack(pady=70,padx=15)

class new_window2():
    def __init__(self):
        self.root = tb.Toplevel()
        self.root.style.theme_use("darkly")
        self.my_notebook=tb.Notebook(self.root,bootstyle="danger")
        self.my_notebook.pack(pady=70,padx=15)
