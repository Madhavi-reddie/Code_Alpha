pip install ttkthemes
import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
def translate_text():
    try:
        # Get the input text from the text field
        text_to_translate = input_text.get("1.0", tk.END).strip()

        # Get the selected language from the dropdown menu
        selected_language = language_var.get()

        # Perform translation
        translator = Translator()
        translated_text = translator.translate(text_to_translate, dest=selected_language)

        # Update the output text field with the translated text
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text.text)
        output_text.config(state=tk.DISABLED)
    except Exception as e:
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "An error occurred. Please try again later.")
        output_text.config(state=tk.DISABLED)
# Create the main window
root = tk.Tk()
root.title("Language Translator")

# Apply a theme to the ttk widgets
style = ttk.Style(root)
style.theme_use("clam") 
# Create input and output text fields with placeholder text
input_text = tk.Text(root, height=5, width=50)
input_text.insert(tk.END, "Enter text to translate here...")
output_text = tk.Text(root, height=5, width=50, state=tk.DISABLED)
# Add labels
input_label = ttk.Label(root, text="Input Text:")
output_label = ttk.Label(root, text="Translated Text:")
language_label = ttk.Label(root, text="Select Language:")
# Create a list of available languages for the dropdown menu (Full language names)
language_options = list(LANGUAGES.values())
language_var = tk.StringVar(root)
language_var.set("English")  # Set the default language to English
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=language_options, state="readonly")
# Create the translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
# Place the widgets using grid layout
input_label.grid(row=0, column=0, padx=10, pady=5)
input_text.grid(row=1, column=0, padx=10, pady=5, columnspan=3)
language_label.grid(row=2, column=0, padx=10, pady=5)
language_dropdown.grid(row=2, column=1, padx=10, pady=5)
translate_button.grid(row=2, column=2, padx=10, pady=5)
output_label.grid(row=3, column=0, padx=10, pady=5)
output_text.grid(row=4, column=0, padx=10, pady=5, columnspan=3)
# Center the window on the screen
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - root.winfo_reqwidth()) // 2
y = (screen_height - root.winfo_reqheight()) // 2
root.geometry("+{}+{}".format(x, y))
root.mainloop()
