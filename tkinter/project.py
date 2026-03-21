import tkinter 
from tkinter import messagebox,ttk
from tkinter import PhotoImage
import openpyxl
from openpyxl import load_workbook

root=tkinter.Tk()
root.title("")

root.geometry("1600x800")

title_label=tkinter.Label(root,text="Inventory Management System",background="#257DAD",font=("Arial",20, "bold"),bg='#257DAD',
                          foreground="#000000")
title_label.place(x=0, y=0,relwidth=1, height=60)

# file 
path=r"C:\yash_important data\project sic\inventory.xlsx"
A=openpyxl.load_workbook(path)
B=A["Inventory"]


Transaction_title=tkinter.LabelFrame(root,text="Sale/Purchase Transactions :",font=("Arial", 12, "bold"),
                                  bd=2,relief="groove",
                                  padx=10,
                                  pady=10)
Transaction_title.place(x=650, y=250, width=850, height=500)


add_update_title=tkinter.LabelFrame(root,text="Add/Update",font=("Arial", 12, "bold"),bd=2,relief='groove',
                                    padx=10,
                                    pady=10)
add_update_title.place(x=670,y=280,width=810,height=220)


product_label=tkinter.Label(root,text="Product",font=("TkDefaultFont",12,"bold"))
product_label.place(relx=0.45,rely=0.395)
product_entry=ttk.Combobox(root,width=23)
product_entry.place(x=770, y=320,bordermode='outside')
product_entry["values"]=("Product1",("Product2"))

# Quantity box
quantity_label=tkinter.Label(root,text="Quantity",font=("TkDefaultFont",12,"bold"))
quantity_label.place(relx=0.65,rely=0.395)
quantity_entry=ttk.Entry(root,width=23)
quantity_entry.place(x=1100, y=320,bordermode='outside')

# Transaction type
Transaction_label=tkinter.Label(root,text="Transaction type",font=("TkDefaultFont",12,"bold"))
Transaction_label.place(relx=0.45,rely=0.50)
Transaction_entry=ttk.Combobox(root,width=23)
Transaction_entry.place(x=850, y=400,bordermode='outside')
Transaction_entry["values"]=("Product1",("Product2"))





tkinter.mainloop()