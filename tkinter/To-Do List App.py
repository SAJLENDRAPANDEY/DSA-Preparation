import tkinter
from tkinter import messagebox,ttk
from tkinter import PhotoImage

root=tkinter.Tk()
root.geometry("400x600")
root.title("TO DO LIST")

path=PhotoImage(file=r"C:\yash_important data\dark-geometric-background-with-copy-space.png")
bg_image=tkinter.Label(root,image=path)
bg_image.place(relheight=1,relwidth=1)

title_label=tkinter.Label(root,text="TO DO LIST",background='#8DC6D8',border=2,relief='groove',font=("Arial",13, "bold"))
title_label.place(relx=0.5,rely=0.03,anchor="center")


entry_label=tkinter.Label(root,text="Enter data",border=2,background="#C1C6BD",relief='groove',font=("Arial", 10, "bold"))
entry_label.place(relx=0.5,rely=0.10,anchor='center')
entry_data=tkinter.Entry(root,relief='solid',background="#B7C4AE")
entry_data.place(relx=0.5, rely=0.16, anchor="center",height=28,width=90)

listbox=tkinter.Listbox(root,width=40,height=10,border="2px",borderwidth="3px",relief="groove")
listbox.place(relx=0.5, rely=0.38, anchor="center",bordermode='inside')


def add_item():
    item=entry_data.get()
    if item.strip()=="":
        messagebox.showwarning("Warning","Please enter some data!")
        return
    
    # count number
    # count=listbox.size()+1
    # item=f"{count}.{item}"

    listbox.insert(tkinter.END,item)
    entry_data.delete(0,tkinter.END)



def edit_task():
    global edit_index
    selected=listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning","select an item ")
        return
    edit_index=selected[0]
    task=listbox.get(edit_index)
    entry_data.delete(0,tkinter.END)
    entry_data.insert(0,task)

def update_task():
    global edit_index
    if 'edit_index' not in globals():
        messagebox.showwarning("Warning","Please edit a task first")
        return
    
    new_task=entry_data.get().strip()

    if new_task=="":
        messagebox.showwarning("Warning","Please select task")
        return
    listbox.delete(edit_index)
    listbox.insert(edit_index,new_task)
    entry_data.delete(0,tkinter.END)

    del edit_index

def delete_item():
    selected=listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning","Please select an item")
        return
    
    # index=selected[0]
    listbox.delete(selected[0])

# clear all 

def clear_all():
    if listbox.size()==0:
        messagebox.showwarning("warning","List is empty ⚠️")
        return
    listbox.delete(0,tkinter.END)

clear_button=tkinter.Button(root,text="Clear all",command=clear_all,font=("Arial", 10, "bold"))
clear_button.place(relx=0.5,rely=0.90,anchor='center')

edit_button=tkinter.Button(root,text="Edit task",font=("Arial", 10, "bold"),command=edit_task)
edit_button.place(relx=0.5,rely=0.75,anchor='center')

update_button=tkinter.Button(root,text="Update",command=update_task,font=("Arial", 10, "bold"))
update_button.place(relx=0.5,rely=0.83,anchor='center')
    

delete_button=tkinter.Button(root,text="Deleted Selected",background="#FF9999",font=("Arial", 10,"bold"),command=delete_item)
delete_button.place(relx=0.5, rely=0.68, anchor="center")

submit_buttom=tkinter.Button(root,text="Submit",anchor='center',background='#ADD8E6',takefocus=True,font=("Arial", 12, "bold"),command=add_item)
submit_buttom.place(relx=0.5, rely=0.60, anchor="center",height=30,width=90)



root.mainloop()
