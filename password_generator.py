
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Enter a positive number greater than 0")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")
        return
    
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(chars)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    pwd = password_entry.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard")

root = tk.Tk()
root.title("Password Generator")
root.geometry("450x420")
root.resizable(0, 0)
root.configure(bg="#2c3e50")  

heading = tk.Label(root, text="Password Generator", font=("Helvetica", 20, "bold"), fg="white", bg="#2c3e50")
heading.pack(pady=20)

frame = tk.Frame(root, bg="#34495e")
frame.pack(pady=10, padx=20, fill="x")

tk.Label(frame, text="Enter password length:", font=("Helvetica", 12), bg="#34495e", fg="white").pack(pady=10)
length_entry = tk.Entry(frame, font=("Helvetica", 12), justify="center")
length_entry.pack(pady=5)

generate_btn = tk.Button(frame, text="Generate Password", font=("Helvetica", 12, "bold"), bg="#27ae60", fg="white", activebackground="#2ecc71", command=generate_password)
generate_btn.pack(pady=10)

password_entry = tk.Entry(frame, font=("Helvetica", 14), justify="center", width=30, bd=2, relief="solid")
password_entry.pack(pady=10)

copy_btn = tk.Button(frame, text="Copy Password", font=("Helvetica", 12, "bold"), bg="#2980b9", fg="white", activebackground="#3498db", command=copy_password)
copy_btn.pack(pady=5)

root.mainloop()
