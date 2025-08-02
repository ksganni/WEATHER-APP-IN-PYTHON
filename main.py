import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv

# Loading the API key
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather():
    city = city_entry.get() # Getting city name from input box
    
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    if not API_KEY:
        messagebox.showerror("Configuration Error", "API key not found in environment.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        result = f"Temperature: {temperature}°C\n"
        result += f"Weather: {description}\n"
        result += f"Wind Speed: {wind_speed} m/s"

        result_label.config(text=result)

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# Setting up GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("300x300")

# Creating and placing a label for the title
title_label = tk.Label(root, text="Enter City Name:", font=("Helvetica", 14))
title_label.pack(pady=10)

# Creating and placing an entry widget to take city name input
city_entry = tk.Entry(root, font=("Helvetica", 12))
city_entry.pack(pady=5)

# Creating and placing a button that calls get_weather() when clicked
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# Creating and placing a label to show weather results
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Starting the GUI event loop
root.mainloop()
