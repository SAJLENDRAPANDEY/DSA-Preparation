import tkinter
root=tkinter.Tk()


# create a label
name_label=tkinter.Label(root,text="Enter name:")
name_label.pack()
# creaate a text box
name_textbox=tkinter.Entry(root)
name_textbox.pack()
root.mainloop()