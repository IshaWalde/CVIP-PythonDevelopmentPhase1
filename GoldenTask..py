import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    length = int(length_entry.get())
    
    if length < 5:
        messagebox.showerror("Error", "Password length should be at least 5 characters.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Increase the font size and label size
        result_label.config(text="Generated Password:\n" + password, font=("Arial", 20))
        result_label.configure(width=20, height=3)
        
        
# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and Entry for password length
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password with larger font size and size
result_label = tk.Label(root, text="", font=("Arial", 20), width=20, height=3)
result_label.pack()



# Run the application
root.mainloop()