import tkinter as tk
from tkinter import messagebox

def on_add_site():
    site_name = entry.get().strip()
    if site_name:
        messagebox.showinfo("Site Added", f"Site '{site_name}' has been added.")
        # Add logic to save to file here
    else:
        messagebox.showerror("Error", "Site name cannot be empty.")

root = tk.Tk()
root.title("Site Manager")

tk.Label(root, text="Enter Site Name:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
tk.Button(root, text="Add Site", command=on_add_site).pack(pady=5)

root.mainloop()
