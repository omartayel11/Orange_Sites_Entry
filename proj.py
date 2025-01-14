import tkinter as tk
from tkinter import filedialog, messagebox

# Function to select a .conf file
def select_conf_file():
    conf_file_path = filedialog.askopenfilename(title="Select .conf file", filetypes=[("Config files", "*.conf")])
    if conf_file_path:
        file_path_var.set(conf_file_path)
    else:
        messagebox.showinfo("File Selection", "No file selected.")

# Function to insert text into the selected .conf file
def insert_text_to_conf():
    conf_file_path = file_path_var.get().strip()
    text_to_insert = entry_text.get("1.0", "end").strip()  # Get text from input box
    if not conf_file_path:
        messagebox.showerror("Error", "No file selected.")
        return
    if not text_to_insert:
        messagebox.showerror("Error", "No text to insert.")
        return
    try:
        with open(conf_file_path, 'a') as conf_file:
            conf_file.write("\n" + text_to_insert)
        messagebox.showinfo("Success", "Text successfully inserted into the .conf file.")
    except FileNotFoundError:
        messagebox.showerror("Error", "The selected file does not exist.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Edit .conf File")

# UI Elements
file_path_var = tk.StringVar()

tk.Label(root, text="Selected .conf File:").pack(pady=5)
tk.Entry(root, textvariable=file_path_var, width=50).pack(pady=5)
tk.Button(root, text="Select .conf File", command=select_conf_file).pack(pady=5)

tk.Label(root, text="Text to Insert:").pack(pady=5)
entry_text = tk.Text(root, height=5, width=50)
entry_text.pack(pady=5)

tk.Button(root, text="Insert Text", command=insert_text_to_conf).pack(pady=10)

# Start the GUI loop
root.mainloop()
