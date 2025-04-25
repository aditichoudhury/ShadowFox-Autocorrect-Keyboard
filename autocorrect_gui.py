import tkinter as tk
from spellchecker import SpellChecker

# Initialize spell checker
spell = SpellChecker()

# Function to autocorrect the typed word
def autocorrect_text(event=None):
    input_text = entry.get()
    words = input_text.split()
    corrected_words = []

    for word in words:
        if word in spell:
            corrected_words.append(word)
        else:
            corrected_words.append(spell.correction(word))

    corrected_output.set(" ".join(corrected_words))

# Create the GUI window
root = tk.Tk()
root.title("Autocorrect Keyboard")
root.geometry("400x200")

# Input field
entry = tk.Entry(root, width=40, font=('Arial', 14))
entry.pack(pady=20)
entry.bind("<KeyRelease>", autocorrect_text)  # Real-time typing

# Output field (read-only)
corrected_output = tk.StringVar()
corrected_label = tk.Label(root, textvariable=corrected_output, font=('Arial', 14), fg='green')
corrected_label.pack(pady=10)

# Start the GUI
root.mainloop()