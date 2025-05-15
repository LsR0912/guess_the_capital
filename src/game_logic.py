import tkinter as tk
import info_window as info
from game import Game
from utils import image_helper as helper
from tkinter import ttk

game = Game()

def update_display():
    name_label.config(text=f"Guess the capital of {game.current_country.name}")
    flag_photo = helper.load_flag(game.current_country.flag_url)
    flag_label.config(image=flag_photo)
    flag_label.image = flag_photo

    suggestions = game.generate_suggestions()
    button1.config(text=suggestions[0])
    button2.config(text=suggestions[1])
    button3.config(text=suggestions[2])

    # Reset score label for the next round
    score_label.config(text=f"Score: {game.score}")

    if game.last_country is not None:
        more_info_button.config(text=f"More info about {game.last_country.name}")
        more_info_button.pack(pady=10)

def button_clicked(button):
    if game.check_answer(button.cget("text")):
        update_display()
    else: 
        update_display()

def on_region_select(event):
    selected_region = region_combobox.get()
    game.selected_region = selected_region
    game.init_region_countries()
    update_display()

# Set up GUI
root = tk.Tk()
root.title("Capital Guesser")

# Set the dimensions of the root window
window_width = 600
window_height = 400

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

regions = game.get_regions()
region_combobox = ttk.Combobox(root, values=regions)
region_combobox.pack(pady=5)
region_combobox.bind("<<ComboboxSelected>>", on_region_select)

# Calculate the position to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry of the root window
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Widgets
name_label = tk.Label(root,text="What's the capital of this country?",font=("Arial",16))
name_label.pack(pady=10)

flag_photo = helper.load_flag(game.current_country.flag_url)
flag_label = tk.Label(root, image=flag_photo)
flag_label.pack()

button_frame = tk.Frame(root)
button_frame.pack()

button1 = tk.Button(button_frame, text="", width=20, height=2,command=lambda: button_clicked(button1))
button2 = tk.Button(button_frame, text="", width=20, height=2, command=lambda: button_clicked(button2))
button3 = tk.Button(button_frame, text="", width=20, height=2, command=lambda: button_clicked(button3))

button1.pack(side=tk.LEFT, padx=10,pady=20)
button2.pack(side=tk.LEFT, padx=10,pady=20)
button3.pack(side=tk.LEFT, padx=10,pady=20)

# Add a "More Info" button (initially hidden)
more_info_button = tk.Button(root, text=f"More Info", command=lambda: info.open_country_info_window(root,game.last_country))
more_info_button.pack_forget()

score_label = tk.Label(root, text=f"Score: {game.score}", font=("Helvetica", 14))
score_label.pack(pady=10)

correct_capital_label = tk.Label(root, text="",font=("Helvetica", 14))
correct_capital_label.pack(pady=10)

update_display()

def loop():
    return root
