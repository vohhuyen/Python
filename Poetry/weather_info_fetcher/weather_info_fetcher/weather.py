# weather_info_fetcher/weather.py

import requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "ca208a968f8949edbe1ed0fcafb62281"

def get_weather(city: str):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(API_URL, params=params) 
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}") 
        return None

def display_weather(city: str):
    weather_data = get_weather(city)
    if weather_data:
        print(f"Weather in {city}: {weather_data['weather'][0]['description'].capitalize()}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
    else:
        print(f"Could not retrieve weather data for {city}.")

def main():
    city = input("Enter the city name: ")
    display_weather(city)

if __name__ == "__main__":
    main()