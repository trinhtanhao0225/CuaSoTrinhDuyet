from newTab import new_tab
from newWindow import new_window
from createWidgets import createWidget


root=new_window()
root.root.geometry("1500x800")
root.root.resizable(False, False)
createWidget(root)
tab=new_tab("Home",root.my_notebook)
tab.create_tab()

root.root.mainloop()