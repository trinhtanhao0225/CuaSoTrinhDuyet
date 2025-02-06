from tkinter import *
from PIL import ImageTk,Image
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

from newTab import new_tab
import  ttkbootstrap as tb
from newWindow import new_window,new_window2
from ttkbootstrap.dialogs import Messagebox
from history import display_history,set_list_history
def create_window():
    screen=new_window2()
    screen.root.geometry("1500x800")
    screen.root.resizable(False,False)
    createWidget(screen)
    newtab=new_tab("Home",screen.my_notebook)
    newtab.create_tab()
    screen.root.mainloop()
def clear_all(screen):
    for widget in screen.winfo_children():
        widget.destroy()
    set_list_history()

def create_history():
    screen=new_window2()
    screen.root.geometry("500x700")
    my_title=tb.Label(screen.root,text="History",font=("Helvetica", 35))
    my_title.pack()
    my_frame = ScrolledFrame(screen.root, autohide=False)
    my_frame.pack(pady=15, padx=15, fill=BOTH,expand=YES)
    display_history(my_frame)
    btn_clear_all = tb.Button(screen.root, text="Clear all", bootstyle="danger",command=lambda :clear_all(my_frame))
    btn_clear_all.pack(pady=20)

    screen.root.mainloop()

def createWidget(screen):
    global bookmark
    btn_new_window=tb.Button(screen.root,text="New window",bootstyle="success",command=create_window)
    btn_new_window.place(x=105,y=20)
    btn_history=tb.Button(screen.root,text="History",bootstyle="primary",command=create_history)
    btn_history.place(x=230,y=20)


