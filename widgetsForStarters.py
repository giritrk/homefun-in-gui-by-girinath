import tkinter as tk

def check_in():
    name = name_entry.get()

    welcome_text.delete("1.0", tk.END)

    message = f"""Welcome, {name}!

Thank you for participating in our workshop.

Workshop Date: 27 September 2026

We hope you have a great learning experience!
"""

    welcome_text.insert("1.0", message)


# Create the main window
window = tk.Tk()
window.title("Workshop Participant Greeting")
window.geometry("500x400")

# Instruction label
instruction_label = tk.Label(
    window,
    text="Please enter your name:",
    font=("Arial", 14)
)
instruction_label.pack(pady=15)

# Entry widget
name_entry = tk.Entry(
    window,
    width=35,
    font=("Arial", 12)
)
name_entry.pack(pady=10)

# Check-in button
check_in_button = tk.Button(
    window,
    text="Check In",
    command=check_in,
    font=("Arial", 12)
)
check_in_button.pack(pady=15)

# Text widget for welcome message
welcome_text = tk.Text(
    window,
    width=50,
    height=10,
    font=("Arial", 11)
)
welcome_text.pack(pady=10)

# Run the application
window.mainloop()