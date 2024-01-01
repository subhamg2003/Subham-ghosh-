import tkinter as tk
import random
import string

def generate_password():
    n = length_entry.get()
    try:
        n = int(n)
        if n > 7:
            l = string.ascii_letters + string.punctuation + string.digits
            result = "".join(random.choices(l, k=n))
            password_var.set(result)
        else:
            password_var.set("Password length should be greater than 7")
    except ValueError:
        password_var.set("Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Strong Password Generator")
root.geometry("300x200")
# Create and place the widgets
length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var)
password_label.pack()

root.mainloop()
