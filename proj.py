import tkinter as tk
from tkinter import filedialog, messagebox

# Function to select a .conf file
def select_conf_file():
    conf_file_path = filedialog.askopenfilename(title="Select .conf file", filetypes=[("Config files", "*.conf")])
    if conf_file_path:
        file_path_var.set(conf_file_path)
    else:
        messagebox.showinfo("File Selection", "No file selected.")

# Function to extract the site code from a line
def get_site_code(site_line):
    if '_' in site_line:
        return site_line.rsplit('_', 1)[-1]
    return None

# Function to count duplicates for each site code in the file
def count_duplicates(conf_file_path, new_sites):
    site_code_count = {}
    try:
        with open(conf_file_path, 'r') as conf_file:
            lines = conf_file.readlines()

        # Count occurrences of each site code in the file
        for line in lines:
            line = line.strip()
            site_code = get_site_code(line)
            if site_code:
                site_code_count[site_code] = site_code_count.get(site_code, 0) + 1

        # Count duplicates for each entered site code
        duplicates_info = []
        for new_site in new_sites:
            site_code = get_site_code(new_site)
            if site_code:
                count = site_code_count.get(site_code, 0)
                duplicates_info.append(f"{new_site} -> Site Code: {site_code} -> Duplicates: {count}")
        
        return duplicates_info
    except FileNotFoundError:
        messagebox.showerror("Error", "The selected file does not exist.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to insert text and display duplicates count
def insert_text_to_conf():
    conf_file_path = file_path_var.get().strip()
    site_entries = entry_text.get("1.0", "end").strip().splitlines()
    
    if not conf_file_path:
        messagebox.showerror("Error", "No file selected.")
        return
    if not site_entries or all(not line.strip() for line in site_entries):
        messagebox.showerror("Error", "No text to insert.")
        return

    duplicates_info = count_duplicates(conf_file_path, site_entries)
    
    # Display site code and duplicates information
    result_display.delete("1.0", "end")
    result_display.insert("1.0", "\n".join(duplicates_info))
    
    try:
        # Append new entries to the file
        with open(conf_file_path, 'a') as conf_file:
            for site_entry in site_entries:
                conf_file.write(site_entry + "\n")
        messagebox.showinfo("Success", "All sites inserted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to insert data: {e}")

# Create the main window
root = tk.Tk()
root.title("Edit .conf File")

# UI Elements
file_path_var = tk.StringVar()

tk.Label(root, text="Selected .conf File:").pack(pady=5)
tk.Entry(root, textvariable=file_path_var, width=50).pack(pady=5)
tk.Button(root, text="Select .conf File", command=select_conf_file).pack(pady=5)

tk.Label(root, text="Text to Insert (one entry per line):").pack(pady=5)
entry_text = tk.Text(root, height=10, width=50)
entry_text.pack(pady=5)

tk.Button(root, text="Insert Text and Count Duplicates", command=insert_text_to_conf).pack(pady=10)

tk.Label(root, text="Site Codes and Duplicates Count:").pack(pady=5)
result_display = tk.Text(root, height=10, width=50)
result_display.pack(pady=5)

# Start the GUI loop
root.mainloop()
