import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import os

FILE_NAME = r"C:\yash_important data\project sic\Inventory_Data.xlsx"

# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("800x600")

# ---------- BACKGROUND IMAGE FULL WINDOW ----------
bg_original = Image.open(r"C:\yash_important data\dark-geometric-background-with-copy-space.png")
bg_image = ImageTk.PhotoImage(bg_original)

bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def resize_bg(event):
    resized = bg_original.resize((event.width, event.height), Image.LANCZOS)
    new_bg = ImageTk.PhotoImage(resized)
    bg_label.config(image=new_bg)
    bg_label.image = new_bg

root.bind("<Configure>", resize_bg)

# ---------- APP CLASS ----------
class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Inventory Management System",
                         font=("Arial", 18, "bold"),
                         bg="black", fg="white")
        title.pack(pady=10)

        # Form Frame
        frame = tk.Frame(self.root, bg="white")
        frame.pack(pady=10)

        tk.Label(frame, text="ID", bg="white").grid(row=0, column=0)
        tk.Label(frame, text="Name", bg="white").grid(row=0, column=1)
        tk.Label(frame, text="Stock", bg="white").grid(row=0, column=2)
        tk.Label(frame, text="Amount", bg="white").grid(row=0, column=3)

        self.id_entry = tk.Entry(frame)
        self.name_entry = tk.Entry(frame)
        self.stock_entry = tk.Entry(frame)
        self.amount_entry = tk.Entry(frame)

        self.id_entry.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)
        self.stock_entry.grid(row=1, column=2)
        self.amount_entry.grid(row=1, column=3)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="white")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Item", width=12, command=self.add_item).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update Item", width=12, command=self.update_item).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete Item", width=12, command=self.delete_item).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Refresh", width=12, command=self.load_data).grid(row=0, column=3, padx=5)

        # Listbox
        self.listbox = tk.Listbox(self.root, width=100, height=15, font=("Consolas", 11))
        self.listbox.pack(padx=20, pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.fill_entries)

    # ---------- LOAD DATA ----------
    def load_data(self):
        if not os.path.exists(FILE_NAME):
            messagebox.showerror("Error", "Excel file not found!")
            return

        self.df = pd.read_excel(FILE_NAME)
        self.listbox.delete(0, tk.END)

        # Header
        self.listbox.insert(tk.END, "ID     Name           Stock     Amount")
        self.listbox.insert(tk.END, "-"*70)

        for index, row in self.df.iterrows():
            text = f"{row['C_ID']:<6} {row['C_Name']:<15} {row['C_Stock']:<9} {row['C_Amount']}"
            self.listbox.insert(tk.END, text)

    # ---------- ADD ITEM ----------
    def add_item(self):
        try:
            new_row = {
                "C_ID": int(self.id_entry.get()),
                "C_Name": self.name_entry.get(),
                "C_Stock": int(self.stock_entry.get()),
                "C_Amount": float(self.amount_entry.get())
            }

            self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
            self.df.to_excel(FILE_NAME, index=False)
            self.load_data()
            messagebox.showinfo("Success", "Item added successfully")

        except:
            messagebox.showerror("Error", "Please enter valid values")

    # ---------- UPDATE ITEM ----------
    def update_item(self):
        selected = self.listbox.curselection()
        if not selected or selected[0] < 2:
            messagebox.showwarning("Warning", "Select a valid item to update")
            return

        index = selected[0] - 2

        self.df.at[index, "C_ID"] = int(self.id_entry.get())
        self.df.at[index, "C_Name"] = self.name_entry.get()
        self.df.at[index, "C_Stock"] = int(self.stock_entry.get())
        self.df.at[index, "C_Amount"] = float(self.amount_entry.get())

        self.df.to_excel(FILE_NAME, index=False)
        self.load_data()
        messagebox.showinfo("Updated", "Item updated successfully")

    # ---------- DELETE ITEM ----------
    def delete_item(self):
        selected = self.listbox.curselection()
        if not selected or selected[0] < 2:
            messagebox.showwarning("Warning", "Select a valid item to delete")
            return

        index = selected[0] - 2

        self.df = self.df.drop(index).reset_index(drop=True)
        self.df.to_excel(FILE_NAME, index=False)
        self.load_data()
        messagebox.showinfo("Deleted", "Item deleted successfully")

    # ---------- FILL FORM ----------
    def fill_entries(self, event):
        selected = self.listbox.curselection()
        if not selected or selected[0] < 2:
            return

        index = selected[0] - 2
        row = self.df.iloc[index]

        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

        self.id_entry.insert(0, row["C_ID"])
        self.name_entry.insert(0, row["C_Name"])
        self.stock_entry.insert(0, row["C_Stock"])
        self.amount_entry.insert(0, row["C_Amount"])

# ---------- RUN ----------
if __name__ == "__main__":
    app = InventoryApp(root)
    root.mainloop()
