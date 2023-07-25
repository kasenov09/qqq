# from tkinter import *       
 
# # Following will import tkinter.ttk module and
# # automatically override all the widgets
# # which are present in tkinter module.
# from tkinter.ttk import *
 
# # Create Object
# root = Tk()
 
# # Initialize tkinter window with dimensions 100x100            
# root.geometry('100x100')    
 
# btn = Button(root, text = 'Click me !',
#                 command = root.destroy)
# root.geometry('150x100')    
 
# b = Button(root, text = 'Click me !',
#                 command = root.destroy)
# root.geometry('500x100')    
 
# a = Button(root, text = 'Click me !',
#                 command = root.destroy)
# root.geometry('100x100')    
 
# c = Button(root, text = 'Click me !',
#                 command = root.destroy)
 
# # Set the position of button on the top of window
# btn.place(x=50, y=5, width=200,height=30)
# b.place(x=350, y=5, width=200,height=30)
# a.place(x=650, y=5, width=200,height=30)
# c.place(x=950, y=5, width=200,height=30)
# root.mainloop()






import tkinter as tk
from tkinter import ttk

def on_button_click(button_number):
    print(f"Button {button_number} clicked!")

def create_beautiful_buttons(root):
    def on_language_toggle():
        global language
        if language == "русский":
            language = "английский"
        else:
            language = "русский"
        update_button_texts()

    def update_button_texts():
        button1.config(text=f"{language} - Создать")
        button2.config(text=f"{language} - Читать")
        button3.config(text=f"{language} - Обновить")
        button4.config(text=f"{language} - Удалить")

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

    language_button = ttk.Button(root, text="Переключить язык", command=on_language_toggle)
    language_button.grid(row=1, column=0, columnspan=4, pady=10)

    root.columnconfigure((0, 1, 2, 3), weight=1)

if __name__ == "__main__":
    language = "русский"

    root = tk.Tk()
    root.title("Красивые кнопки")
    create_beautiful_buttons(root)
    root.mainloop()
