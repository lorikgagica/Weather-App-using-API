# ☀️🌥️ Weather App

A simple Python console app that retrieves weather information and a 5-day forecast using OpenWeatherMap’s API. View current conditions, 5-day trends, sunrise and sunset times, and save your searches for future reference!

---

## ✨ Features

- **Current weather and description for any city**
- **5-day weather forecast (selected midday readings for each day)**
- **Displays sunrise and sunset times**
- **Option to save weather searches to a text file (`weather_searches.txt`)**
- **Clean menu-driven interface with continued usage**

---

## 🚀 How to Use

1. Make sure Python is installed.
2. Save your script as `weather.py`.
3. Obtain your free API key from [OpenWeatherMap](https://openweathermap.org/api) and place it in the script where specified.
4. Open your terminal or command prompt in the script’s folder.
5. Run: `python weather.py`
6. Enter the city name.  
7. Optionally save the displayed weather information and 5-day forecast to a file.

---

## 💡 Example Session

--- Weather App ---
Enter a city name (or 'q' to quit): Paris

--- Weather Information ---
City: Paris
Temperature: 17.5C
Weather: Clear Sky
Humidity: 65%
Wind Speed: 2.5m/s
Sunrise: 2025-11-01 07:22
Sunset: 2025-11-01 18:14

--- 5 Day Forecast (Midday) ---
2025-11-02: Temp=18.2C, Weather=Clear Sky, Humidity=60%
2025-11-03: Temp=16.9C, Weather=Cloudy, Humidity=68%
...

Save this search to text file? (y/n): y
Weather data saved to weather_searches.txt

---

## 🗂 Data Storage

- All saved searches go to `weather_searches.txt` in your script folder for later review.

---

## 📄 License

MIT License — free for personal and commercial use.

---

Stay prepared — check your weather anytime!
