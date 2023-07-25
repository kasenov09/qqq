import tkinter as tk
from tkinter import ttk

def on_button_click(button_number):
    print(f"Button {button_number} clicked!")

def create_beautiful_buttons(root):
    style = ttk.Style()
    style.configure("Beautiful.TButton", 
                    foreground="white", 
                    background="#4CAF50", 
                    font=("Helvetica", 16),
                    padding=10)

    button_frame = ttk.Frame(root)
    button_frame.grid(row=0, column=0, padx=10, pady=10)

    button1 = ttk.Button(button_frame, style="Beautiful.TButton", command=lambda: on_button_click(1))
    button2 = ttk.Button(button_frame, style="Beautiful.TButton", command=lambda: on_button_click(2))
    button3 = ttk.Button(button_frame, style="Beautiful.TButton", command=lambda: on_button_click(3))
    button4 = ttk.Button(button_frame, style="Beautiful.TButton", command=lambda: on_button_click(4))

    button1.grid(row=0, column=0, padx=10)
    button2.grid(row=0, column=1, padx=10)
    button3.grid(row=0, column=2, padx=10)
    button4.grid(row=0, column=3, padx=10)

    update_button_texts()

def update_button_texts():
    if language == "русский":
    button1.config(text="Создать")
        button2.config(text="Читать")
        button3.config(text="Обновить")
        button4.config(text="Удалить")
        language_button.config(text=f"Переключить язык ({language})")
    else:
        button1.config(text="Create")
        button2.config(text="Read")
        button3.config(text="Update")
        button4.config(text="Delete")
        language_button.config(text=f"Toggle Language ({language})")

def on_language_toggle():
    global language
    if language == "русский":
        language = "английский"
    else:
        language = "русский"
    update_button_texts()

if __name__ == "__main__":
    language = "русский"

    root = tk.Tk()
    root.title("Красивые кнопки")
    create_beautiful_buttons(root)

    language_button = ttk.Button(root, text=f"Переключить язык ({language})", command=on_language_toggle)
    language_button.grid(row=1, column=0, columnspan=4, pady=10)

    root.columnconfigure((0, 1, 2, 3), weight=1)

    root.mainloop()
