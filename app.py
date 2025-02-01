import tkinter as tk
from tkinter import messagebox

# Function to check prime number
def is_prime():
    try:
        num = int(entry.get())  # Get the number from the entry box
        if num < 2:
            messagebox.showinfo("Result", f"{num} is NOT a prime number")
            return
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                messagebox.showinfo("Result", f"{num} is NOT a prime number")
                return
        
        messagebox.showinfo("Result", f"{num} is a PRIME number")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

# Create the main window
root = tk.Tk()
root.title("Prime Number Checker")
root.geometry("300x200")

# Label and Entry for user input
tk.Label(root, text="Enter a number:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack()

# Button to check prime
tk.Button(root, text="Check Prime", command=is_prime, font=("Arial", 12), bg="lightblue").pack(pady=10)

# Run the application
root.mainloop()
