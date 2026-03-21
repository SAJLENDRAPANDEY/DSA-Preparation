
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
import pandas as pd
import os
# root=tk.Tk()

FILE_NAME = r"C:\yash_important data\project sic\Inventory_Data.xlsx"

root = tk.Tk()
root.title("Inventory Management System")
root.geometry("800x600")


bg_img = PhotoImage(file=r"C:\yash_important data\dark-geometric-background-with-copy-space.png")
bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("800x600")

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        title = tk.Label(self.root, text="Inventory Management System", font=("Arial", 18, "bold"))
        title.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="ID").grid(row=0, column=0)
        tk.Label(frame, text="Name").grid(row=0, column=1)
        tk.Label(frame, text="Stock").grid(row=0, column=2)
        tk.Label(frame, text="Amount").grid(row=0, column=3)

        self.id_entry = tk.Entry(frame)
        self.name_entry = tk.Entry(frame)
        self.stock_entry = tk.Entry(frame)
        self.amount_entry = tk.Entry(frame)

        self.id_entry.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)
        self.stock_entry.grid(row=1, column=2)
        self.amount_entry.grid(row=1, column=3)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Item", command=self.add_item).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update Item", command=self.update_item).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete Item", command=self.delete_item).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Refresh", command=self.load_data).grid(row=0, column=3, padx=5)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Stock", "Amount"), show="headings")
        for col in ("ID", "Name", "Stock", "Amount"):
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.fill_entries)

    def load_data(self):
        if not os.path.exists(FILE_NAME):
            messagebox.showerror("Error", "Excel file not found!")
            return

        self.df = pd.read_excel(FILE_NAME)
        self.tree.delete(*self.tree.get_children())

        for _, row in self.df.iterrows():
            self.tree.insert("", tk.END, values=(row["C_ID"], row["C_Name"], row["C_Stock"], row["C_Amount"]))

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

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select an item to update")
            return

        index = self.tree.index(selected[0])

        self.df.at[index, "C_ID"] = int(self.id_entry.get())
        self.df.at[index, "C_Name"] = self.name_entry.get()
        self.df.at[index, "C_Stock"] = int(self.stock_entry.get())
        self.df.at[index, "C_Amount"] = float(self.amount_entry.get())

        self.df.to_excel(FILE_NAME, index=False)
        self.load_data()
        messagebox.showinfo("Updated", "Item updated successfully")

    def delete_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select an item to delete")
            return

        index = self.tree.index(selected[0])
        self.df = self.df.drop(index).reset_index(drop=True)
        self.df.to_excel(FILE_NAME, index=False)
        self.load_data()
        messagebox.showinfo("Deleted", "Item deleted successfully")

    def fill_entries(self, event):
        selected = self.tree.selection()
        if not selected:
            return

        values = self.tree.item(selected[0], "values")

        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

        self.id_entry.insert(0, values[0])
        self.name_entry.insert(0, values[1])
        self.stock_entry.insert(0, values[2])
        self.amount_entry.insert(0, values[3])


if __name__ == "__main__":
    # root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
