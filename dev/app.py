import tkinter as tk
from tkinter import filedialog, messagebox

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )
    if file_path:
        file_path_var.set(file_path)

def select_output_dir():
    directory = filedialog.askdirectory(title="Select Output Directory")
    if directory:
        output_dir_var.set(directory)

def start_prediction():
    # Placeholder for prediction logic
    messagebox.showinfo("Prediction", "Prediction started (logic not yet implemented).")

# Main window
root = tk.Tk()
root.title("Meningitis Prediction Tool")
root.geometry("500x250")
root.resizable(False, False)

# Variables to hold paths
file_path_var = tk.StringVar(value="No file selected")
output_dir_var = tk.StringVar(value="No output directory selected")

# Layout
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# CSV file selection
tk.Label(frame, text="Input CSV File:").grid(row=0, column=0, sticky="w")
tk.Button(frame, text="Browse...", command=select_file).grid(row=0, column=1, sticky="e")
tk.Label(frame, textvariable=file_path_var, wraplength=400, fg="blue").grid(row=1, column=0, columnspan=2, sticky="w")

# Output directory selection
tk.Label(frame, text="Output Directory:").grid(row=2, column=0, sticky="w", pady=(10, 0))
tk.Button(frame, text="Browse...", command=select_output_dir).grid(row=2, column=1, sticky="e", pady=(10, 0))
tk.Label(frame, textvariable=output_dir_var, wraplength=400, fg="green").grid(row=3, column=0, columnspan=2, sticky="w")

# Start prediction button
tk.Button(frame, text="Start Prediction", command=start_prediction, bg="#4CAF50", fg="white", padx=10, pady=5).grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()