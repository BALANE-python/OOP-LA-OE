import tkinter as tk

your_name = "Merchell Balane"
your_section = "BSIT - 2B"
window = tk.Tk()
window.title(f"OOP") 
window.geometry("400x300") 

frame = tk.Frame(window)
frame.pack(pady = 20)

label_win = tk.Label(frame, text = f"OOP LA29 {your_name} {your_section}")
label_win.grid(row = 0, column = 0, padx = 10, pady = 10)

window.mainloop()