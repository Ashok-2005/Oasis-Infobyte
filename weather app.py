import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None

def display_weather(weather_data):
    if weather_data:
        print("\nCurrent Weather:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather Conditions: {weather_data['weather'][0]['description']}")
    else:
        print("Unable to display weather data.")

def main():
    print("Command-Line Weather App")
    print("------------------------")

    api_key = input("Enter your OpenWeatherMap API key: ")
    location = input("Enter the location (city or ZIP code): ")

    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()

    c574c353b83ae6d712bd6c731dc034aa
