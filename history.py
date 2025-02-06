from tkinter import *
import ttkbootstrap as tb
from datetime import datetime
class tab_history:
    def __init__(self,screen,my_labelInfo,myLabelTime):
        self.my_labelInfo=tb.Label(screen,text=my_labelInfo,bootstyle="info",font=20)
        self.my_labelTime=tb.Label(screen,text=myLabelTime,bootstyle="info",font=20)
        self.my_button=tb.Button(screen,text="Clear this",bootstyle="success",command=lambda :remove_list_history(self,screen))
    def create_tab(self,i):
        self.my_labelInfo.grid(row=i,column=0,sticky='w',pady=20)
        self.my_labelTime.grid(row=i,column=1,pady=20,padx=(200,0))
        self.my_button.grid(row=i,column=2,pady=20)
list_history=[]

def get_list_history():
    global list_history
    return list_history
def set_list_history():
    global list_history
    list_history=[]
def add_list_history(value):
    global list_history
    current_time = datetime.now().strftime('%H:%M:%S')
    if len(list_history)==0 or list_history[-1][0] !=value:
        list_history.append([value,current_time])
def remove_list_history(self,screen):
    global list_history
    list_history.remove([self.my_labelInfo.cget('text'),self.my_labelTime.cget('text')])
    display_history(screen)
def display_history(screen):
    global list_history
    for widget in screen.winfo_children():
        widget.destroy()
    cnt=0
    for item in reversed(list_history):
        tab=tab_history(screen,item[0],item[1])
        tab.create_tab(cnt)
        cnt+=1