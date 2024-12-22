import tkinter as tk

game_title = "Valorant"
window = tk.Tk()
window.title(f"LA 30") 
window.geometry("400x300") 

counter = 1
def fav_game():
    global counter
    print(f"{counter}. My all-time favorite game is {game_title}")
    counter += 1
    
button_print = tk.Button(window, text = "Run Function", command = fav_game)
button_print.grid(row = 0, column = 0, padx = 20, pady = 20)
window.mainloop()