# add background image
import tkinter
from tkinter import PhotoImage
root=tkinter.Tk()
root.title("Welcome to my app")
root.geometry("300x500")

path=PhotoImage(file=r"C:\yash_important data\tkinter bg.png")
bg_image=tkinter.Label(root,image=path)
bg_image.place(relheight=1,relwidth=1)

text_label=tkinter.Label(root,text="welcome to my app")
text_label.pack()



root.mainloop()

# morning me tkinter aur pandas 
# new project on kinter 
