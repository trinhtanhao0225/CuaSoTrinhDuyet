import ttkbootstrap as tb
from tkinter import *
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import ImageTk,Image
import os

def get_folders(directory):
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
def get_file(directory):
    return [d for d in os.listdir(directory) if os.path.isfile(os.path.join(directory, d))]

def list_folder_file(self):
    root=tb.Toplevel()
    root.geometry("500x700")
    root.style.theme_use("darkly")
    my_frame = ScrolledFrame(root, autohide=False)
    my_frame.pack(pady=15, padx=15,fill=BOTH, expand=YES)
    my_title = tb.Label(my_frame, text="Favourite", font=("Helvetica", 35))
    my_title.pack()
    img_folder = ImageTk.PhotoImage(Image.open("img/folder.png"))
    img_file = ImageTk.PhotoImage(Image.open("img/file.png"))
    folder_label = tb.Label(my_frame, image=img_folder, text="Favourite", compound=LEFT)
    folder_label.pack(padx=20, pady=20, anchor=W)
    for item in os.listdir("bookmark"):
        if os.path.isdir("bookmark/" + item):
            folder_label = tb.Label(my_frame, image=img_folder, text=item, compound=LEFT)
            folder_label.pack(padx=80, pady=20, anchor=W)
            for file in os.listdir("bookmark/" + item):
                file_btn = tb.Button(my_frame, image=img_file, text=file, compound=LEFT, bootstyle="primary outline",command=lambda f=file:get_label(self,f,root))
                file_btn.pack(pady=15, padx=170, anchor=W)
        else:
            file_btn = tb.Button(my_frame, image=img_file, text=item, compound=LEFT, bootstyle="primary outline",command=lambda f=item:get_label(self,f,root))
            file_btn.pack(padx=80, pady=20, anchor=W)
    root.mainloop()
def get_label(self,file_name,screen):
    self.my_label.config(text=file_name)
    if len(self.listPage) == self.numPage + 1:
        self.listPage.append(file_name)
        self.numPage += 1
    else:
        length = len(self.listPage)
        del self.listPage[self.numPage + 1:length]
        self.numPage += 1
        self.listPage.append(file_name)
    screen.destroy()
