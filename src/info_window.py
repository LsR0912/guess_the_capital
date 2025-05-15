import tkinter as tk
import webview

def open_country_info_window(root, current_country):
    """
    Opens a new window with information about the current country.
    """
    new_window = tk.Toplevel(root)
    new_window.title(f"About {current_country.name}")
    
    # Set the dimensions of the new window
    window_width = 400
    window_height = 300
    
    # Get the screen width and height
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()
    
    # Calculate the position to center the window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    
    # Set the geometry of the new window
    new_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    
    # Add content to the new window
    info_label = tk.Label(new_window, text=f"Country: {current_country.name}\nCapital: {current_country.capital}\nRegion: {current_country.region}\nPopulation: {current_country.population}\nLanguages: {current_country.languages}", font=("Arial", 14))
    info_label.pack(pady=20)
    
    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)

    webview.create_window("Open Street Maps", current_country.maps)
    webview.start()
