# 🌦️ Weather App in Python (tkinter + OpenWeatherMap API)

A beginner-friendly desktop GUI application built in Python using **tkinter** that shows **live weather information** (temperature, description, and wind speed) based on **city input** using the **OpenWeatherMap API**.

---

## 📌 Features

- 🌡️ Real-time weather data (temperature, weather description, wind speed)
- 🖥️ tkinter-based GUI
- ⚠️ API error handling (invalid city, no input, internet errors)

---

## 📷 Screenshots

<img width="300" height="330" alt="Screenshot 2025-08-01 at 9 05 33 PM" src="https://github.com/user-attachments/assets/03c99108-fdfd-4ac2-a1d7-d9edbad205cb" />
<img width="300" height="330" alt="Screenshot 2025-08-01 at 9 05 42 PM" src="https://github.com/user-attachments/assets/d95376e2-9cd1-4a86-a13a-a3b3bf135369" />
<img width="564" height="330" alt="Screenshot 2025-08-01 at 9 06 22 PM" src="https://github.com/user-attachments/assets/c0f2fba3-e6e1-4883-98da-f66d944aab08" />

## 🎥 Demo Video

https://github.com/user-attachments/assets/a9389d80-acb6-4eae-9af4-c83cf7e0bc2f

---

## 🛠️ Tech Stack

- Python 
- tkinter (standard GUI library)
- OpenWeatherMap API
- requests
- python-dotenv

---

## 📁 Project Structure

```
weather_app/
│
├── main.py          # Main app code
├── .env             # Stored API key ( not pushed to Github repo )
├── .gitignore       # Hides files
├── requirements.txt # Project dependencies
└── README.md        # This file
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/weather_app.git
cd weather_app
```

### 2️⃣ Create Virtual Environment

🔹 **Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

🔹 **macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Get Your API Key

1. Go to [OpenWeatherMap API](https://openweathermap.org/api)
2. Sign up for a free account
3. Copy your API key from the **"API Keys"** section

### 5️⃣ Add API Key to `.env` File

Create a `.env` file in the root of your project and add:

```ini
OPENWEATHER_API_KEY=your_api_key_here
```

🔐 **Never share this file or commit it to GitHub**

### 6️⃣ Run the App

```bash
python main.py
```

---

## 🧪 How to Use

1. Launch the app
2. Enter a **city name** (e.g., `London`)
3. Click the **"Get Weather"** button
4. View the temperature, weather condition, and wind speed

---

Initially developed in **February 2022** and later refined for GitHub.

---
