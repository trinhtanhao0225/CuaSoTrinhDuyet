import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from ttkbootstrap import Style
import ttkbootstrap as tb
from ttkbootstrap.toast import ToastNotification
bookmark=[]
def stull(x):
    folder_menu.config(text=x)
def get_folders(directory):
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
def get_file(directory):
    return [d for d in os.listdir(directory) if os.path.isfile(os.path.join(directory, d))]
def update_menu_folder():
    inside_menu.delete(0,END)

    for x in get_folders("bookmark"):
        x = x.center(len(x) + (50 - len(x)))
        inside_menu.add_radiobutton(label=x,variable=items_var, command=lambda x=x:stull(x))
    folder_menu['menu']=inside_menu
def toast(title,message,style):
    toast=ToastNotification(title=title,
    message=message,
    duration=5000,
    alert=True,
    position=(30,50,'sw'),
    bootstyle=style
    )
    toast.show_toast()
def click_create(screen,path):
    try:
        os.mkdir("bookmark/"+path)
    except OSError:
        toast("Create folder", "Creation of the directory :" + path + " was failed","danger")

    else:
        toast("Create folder","Successfully created the directory :"+path,"success")
        update_menu_folder()
    screen.destroy()

def click_cancle(screen):
    screen.destroy()
def click_remove(screen,file,folder):
    for files in get_file("bookmark/"+folder):
        if files==file:
            os.remove("bookmark/"+folder+"/"+file)
            toast("Remove File", "Successfully removed the file " + file + " from direction: " + folder, "success")
            screen.destroy()
            return
    toast("Remove File", "Remove file " + file + " from direction " + folder + " was failed", "danger")
    screen.destroy()
def click_done(screen,file,folder):
    try:
        open(os.path.join("bookmark/"+folder,file),'w')
    except OSError:
        toast("Add File", "Add file :" + file + " to direction: "+folder+" was failed", "danger")

    else:
        toast("Add File", "Successfully added the file :"+file+" to direction: "+folder, "success")
    screen.destroy()
def click_new_folder():
    new_tab_folder=tb.Toplevel()
    new_tab_folder.style.theme_use("darkly")
    new_tab_folder.geometry("300x150")
    folder_label=tb.Label(new_tab_folder,text="Name :")
    folder_label.grid(row=0,column=0,pady=20,padx=10)
    folder_entry = tb.Entry(new_tab_folder)
    folder_entry.grid(row=0,column=1,pady=20,padx=10)

    btn_create_folder=tb.Button(new_tab_folder,text="Create",bootstyle="primary",command=lambda :click_create(new_tab_folder,folder_entry.get()))
    btn_cancle_cancle=tb.Button(new_tab_folder,text="Cancle",bootstyle="danger",command=lambda :click_cancle(new_tab_folder))
    btn_create_folder.place(x=30,y=70)
    btn_cancle_cancle.place(x=130,y=70)

def save_remove(value):
    global inside_menu,folder_menu,items_var
    screen=tb.Toplevel()
    screen.style.theme_use("darkly")
    screen.geometry("400x190")
    label_name=tb.Label(screen,text="Name :")
    label_name.grid(row=0,column=0,padx=20,pady=(20,10))
    name_entry=tb.Entry(screen,width=30)
    name_entry.insert(0,value)
    name_entry.grid(row=0,column=1,padx=20,pady=(20,10))

    label_folder=tb.Label(screen,text="Folder :")
    label_folder.grid(row=1,column=0,padx=20,pady=10)

    folder_menu=tb.Menubutton(screen,text="                 Other folder",width=25,bootstyle="secondary")
    folder_menu.grid(row=1,column=1,padx=20,pady=10)
    items_var = StringVar()
    inside_menu=tb.Menu(folder_menu)
    update_menu_folder()
    btn_createFolder=tb.Button(screen,text="New folder",bootstyle="success",command=click_new_folder)
    btn_createFolder.place(x=10,y=130)
    btn_done=tb.Button(screen,text="Done",bootstyle="primary",width=8,command=lambda :click_done(screen,name_entry.get(),items_var.get().strip()))
    btn_done.place(x=150,y=130)
    btn_remove=tb.Button(screen,text="Remove",bootstyle="secondary",command=lambda :click_remove(screen,name_entry.get(),items_var.get().strip()))
    btn_remove.place(x=290,y=130)