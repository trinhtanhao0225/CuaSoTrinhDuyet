from tkinter import *
from PIL import ImageTk,Image
from ttkbootstrap.constants import *
import  ttkbootstrap as tb
from newWindow import new_window
from bookmark import save_remove
from list_folder import list_folder_file
from history import add_list_history
class new_tab():
    def __init__(self, text,my_notebook):
        self.my_notebook=my_notebook
        self.listPage = []
        self.numPage = 0
        self.text=text
        self.img_star=ImageTk.PhotoImage(Image.open("img/star.png"))
        self.img_search=ImageTk.PhotoImage(Image.open("img/search.png"))
        self.tab = tb.Frame(self.my_notebook)
        self.btn_pre = tb.Button(self.tab, text="<", bootstyle='success outline',command=lambda: self.previousPage(my_notebook))
        self.btn_next = tb.Button(self.tab, text=">", bootstyle='success outline',command=lambda: self.nextPage(my_notebook))
        self.my_entry = tb.Entry(self.tab, bootstyle='dark', font=("Helvetica", 16), width=70)
        self.btn_search = tb.Button(self.tab, image=self.img_search, bootstyle='secondary',
                               command=lambda: self.search(self.my_label, self.my_entry.get(),my_notebook))
        self.btn_bookmark = tb.Button(self.tab, image=self.img_star, bootstyle='secondary',command=lambda :save_remove(self.my_label.cget('text')))


        self.btn_new_tab = tb.Button(self.tab, text="New tab", bootstyle='sucess',command=lambda :create_new_tab(self.my_notebook))

        self.btn_remove_tab = tb.Button(self.tab, text="Remove this tab", bootstyle='danger',command=lambda: remove_tab(self.my_notebook))

        self.btn_list_folder_file=tb.Button(self.tab,text="Folders and files",bootstyle="danger",command=lambda :list_folder_file(self))

        self.my_label = tb.Label(self.tab, text=self.text, font=("Helvetica", 25), bootstyle="success")


    def create_tab(self):
        self.listPage.append(self.text)
        self.btn_pre.grid(row=0, column=0, padx=(15, 2), pady=15)

        self.btn_next.grid(row=0, column=1, padx=(2, 10), pady=15)

        self.my_entry.grid(row=0, column=3, pady=15)

        self.btn_search.grid(row=0, column=2, pady=15)

        self.btn_bookmark.grid(row=0,column=4,pady=15,padx=(0,10))
        self.btn_new_tab.place(x=15,y=70)
        self.btn_remove_tab.place(x=15,y=120)

        self.btn_list_folder_file.place(y=70,x=1140)
        self.my_label.grid(row=2, column=0, columnspan=4, pady=50)

        self.my_notebook.add(self.tab,text=self.text)
        add_list_history(self.text)
    def previousPage(self,my_notebook):
        if self.numPage > 0:
            self.numPage -= 1
            self.my_label.config(text=self.listPage[self.numPage])

        changeTextOfTab(self,my_notebook)
        add_list_history(self.listPage[self.numPage])
    def nextPage(self,my_notebook):
        if self.numPage < len(self.listPage) - 1:
            self.numPage += 1
            self.my_label.config(text=self.listPage[self.numPage])
        changeTextOfTab(self,my_notebook)
        add_list_history(self.listPage[self.numPage])
    def search(self,my_label, entry_text,my_notebook):
        if entry_text=="":
            return
        my_label.config(text=entry_text)
        if len(self.listPage)==self.numPage+1:
            self.listPage.append(entry_text)
            self.numPage += 1
        else:
            length=len(self.listPage)
            del self.listPage[self.numPage+1:length]
            self.numPage+=1
            self.listPage.append(entry_text)
        changeTextOfTab(self, my_notebook)
        add_list_history(self.listPage[self.numPage])
def create_new_tab(my_notebook):
    tab=new_tab("Home",my_notebook)
    tab.create_tab()

def remove_tab(my_notebook):
    if my_notebook.index("end")==1:
        return
    current_tab=my_notebook.select()
    if current_tab:
        my_notebook.forget(current_tab)

def changeTextOfTab(self,my_notebook):
    text = self.my_label.cget('text')
    if len(text)>4:
        text=text[0:4]
        text+="..."
    my_notebook.tab(self.tab, text=text)

