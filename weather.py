# Weather App using OpenWeatherMap API
import requests

#Step 1: API SETUP
API_KEY = "2012545d13d8da772b440b0d8792d17d"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
SAVE_FILE = "weather_searches.txt"

# Step 2: Get Weather Data
from datetime import datetime
def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime("%Y-%m-%d %H:%M")
            sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime("%Y-%m-%d %H:%M")
            weather = {
                "City": data["name"],
                "Temperature": f"{data['main']['temp']}C",
                "Weather": data["weather"][0]['description'].title(),
                "Humidity": f"{data['main']['humidity']}%",
                "Wind Speed": f"{data['wind']['speed']}m/s",
                "Sunrise": sunrise,
                "Sunset": sunset
            }
            return weather
        elif response.status_code == 404:
            print("City not found.")
        else:
            print("An error occurred. Status Code: ", response.status_code)
    except Exception as e:
        print("An error occurred: ", e)
    return None

def get_5day_forecast(city):
    try:
        url = f"{FORECAST_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            forecast_list = data['list']
            
            # Collect one forecast per midday for 5 days
            daily_forecast = {}
            for entry in forecast_list:
                dt_txt = entry['dt_txt']
                date_str, hour = dt_txt.split()
                if hour == "12:00:00":
                    daily_forecast[date_str] = {
                        "Temperature": entry['main']['temp'],
                        "Weather": entry['weather'][0]['description'],
                        "Humidity": entry['main']['humidity']
                    }
            return daily_forecast
        elif response.status_code == 404:
            print("City not found for forecast.")
        else:
            print("An error occurred. Status Code: ", response.status_code)
    except Exception as e:
        print("An error occurred: ", e)
    return None

# Step 3: Display Weather Information
def display_weather(weather):
  print("\n--- Weather Information ---")
  for key,value in weather.items():
    print(f"{key}: {value}")

def display_forecast(forecast):
    print("\n--- 5 Day Forecast (Midday) ---")
    if forecast:
        for date, info in forecast.items():
            print(f"{date}: Temp={info['Temperature']}C, Weather={info['Weather'].title()}, Humidity={info['Humidity']}%")
    else:
        print("No forecast data.")

# Step 4: Save Research
def save_search(city, weather, forecast):
    with open(SAVE_FILE, "a", encoding='utf-8') as file:
        file.write(f"\nSearch for: {city}\n")
        for key, value in weather.items():
            file.write(f"{key}: {value}\n")
        file.write("--- 5 Day Forecast ---\n")
        if forecast:
            for date, info in forecast.items():
                file.write(f"{date}: Temp={info['Temperature']}C, Weather={info['Weather'].title()}, Humidity={info['Humidity']}%\n")
        file.write("\n")

# Step 5: Main Program Loop
while True:
    print("\n--- Weather App ---")
    city = input("Enter a city name (or 'q' to quit): ").strip()
    if city.lower() == 'q':
        break

    weather = get_weather(city)
    forecast = get_5day_forecast(city)

    if weather:
        display_weather(weather)
        display_forecast(forecast)
        save_option = input("Save this search to text file? (y/n): ").strip().lower()
        if save_option == 'y':
            save_search(city, weather, forecast)
            print(f"Weather data saved to {SAVE_FILE}")