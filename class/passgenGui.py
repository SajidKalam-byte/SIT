import random
import string
import tkinter as tk
from tkinter import messagebox

# Define colors from the theme
COLORS = {
    "space_cadet": "#1f2041",
    "english_violet": "#4b3f72",
    "sunglow": "#ffc857",
    "dark_cyan": "#119da4",
    "paynes_gray": "#19647e",
}

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number for length.")
        return

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()
    avoid_similar = similar_var.get()
    avoid_ambiguous = ambiguous_var.get()

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if avoid_similar:
        similar_chars = "il1Lo0O"
        characters = ''.join([c for c in characters if c not in similar_chars])

    if avoid_ambiguous:
        ambiguous_chars = "{}[]()/\\'\"`~,;:.<>"
        characters = ''.join([c for c in characters if c not in ambiguous_chars])

    if not characters:
        messagebox.showwarning("Warning", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        app.clipboard_clear()
        app.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_symbols = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digits, has_symbols])
    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Medium"
    else:
        return "Weak"

def paste_password():
    password = app.clipboard_get()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    strength = check_password_strength(password)
    strength_label.config(text=f"Strength: {strength}")

# Set up the GUI
app = tk.Tk()
app.title("Advanced Password Generator")
app.geometry("400x550")
app.configure(bg=COLORS["space_cadet"])

# Password Length Input
tk.Label(app, text="Password Length:", fg=COLORS["sunglow"], bg=COLORS["space_cadet"]).pack()
length_entry = tk.Entry(app, font=("Arial", 12), width=10)
length_entry.pack(pady=5)
length_entry.insert(0, "12")

# Checkboxes for character types
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()
similar_var = tk.BooleanVar()
ambiguous_var = tk.BooleanVar()

tk.Checkbutton(app, text="Include Uppercase Letters", variable=upper_var, fg=COLORS["sunglow"], bg=COLORS["space_cadet"]).pack()
tk.Checkbutton(app, text="Include Lowercase Letters", variable=lower_var, fg=COLORS["sunglow"], bg=COLORS["space_cadet"]).pack()
tk.Checkbutton(app, text="Include Digits", variable=digits_var, fg=COLORS["sunglow"], bg=COLORS["space_cadet"]).pack()
tk.Checkbutton(app, text="Include Symbols", variable=symbols_var, fg=COLORS["sunglow"], bg=COLORS["space_cadet"]).pack()
tk.Checkbutton(app, text="Avoid Similar Characters (e.g., i, l, 1, L, o, 0, O)", variable=similar_var, fg=COLORS["sunglow"], bg=COLORS["space_cadet"]).pack()
tk.Checkbutton(app, text="Avoid Ambiguous Characters (e.g., { } [ ] / \\ ' \" ` ~ , ; : . < >)", variable=ambiguous_var, fg=COLORS["sunglow"], bg=COLORS["space_cadet"]).pack()

# Password display entry
password_entry = tk.Entry(app, font=("Arial", 14), width=30)
password_entry.pack(pady=20)

# Buttons
generate_button = tk.Button(app, text="Generate Password", command=generate_password, font=("Arial", 12), bg=COLORS["english_violet"], fg="white")
generate_button.pack(pady=10)
copy_button = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg=COLORS["dark_cyan"], fg="white")
copy_button.pack(pady=5)
paste_button = tk.Button(app, text="Paste and Check Strength", command=paste_password, font=("Arial", 12), bg=COLORS["paynes_gray"], fg="white")
paste_button.pack(pady=5)

# Password Strength Label
strength_label = tk.Label(app, text="Strength: ", font=("Arial", 12), fg=COLORS["sunglow"], bg=COLORS["space_cadet"])
strength_label.pack(pady=10)

# Run the GUI loop
app.mainloop()
