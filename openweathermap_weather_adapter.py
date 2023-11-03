import requests


class WeatherData:
    def __init__(self, description, temperature, feels_like, visibility, wind_speed, humidity, source):
        self.description = description
        self.temperature = temperature
        self.feels_like = feels_like
        self.visibility = visibility
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.source = source


def fetch_and_map_weather_data(api_key, city):
    if not city:
        print('Enter your city')
        return

    api_endpoint = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    weather_data = requests.get(api_endpoint)
    if weather_data.status_code == 404:
        print('City not found')
        return

    api_data = weather_data.json()

    description = api_data['weather'][0]['main']
    temperature = round(api_data['main']['temp'] - 273.15, 1)
    feels_like = round(api_data['main']['feels_like'] - 273.15, 1)
    visibility = api_data['visibility']
    wind_speed = api_data['wind']['speed']
    humidity = api_data['main']['humidity']

    weather_obj = WeatherData(description, temperature, feels_like, visibility, wind_speed, humidity, "OpenWeatherMap")

    return weather_obj


if __name__ == "__main__":
    api_key = "f6f54cdbb0e26f074fa7c853292b2368"
    city = input("Enter a city: ")

    weather_data = fetch_and_map_weather_data(api_key, city)

    if weather_data:
        formatted_data = (
            f"\nDescription: {weather_data.description}\n"
            f"Temperature: {weather_data.temperature} ℃\n"
            f"Feels like: {weather_data.feels_like} ℃\n"
            f"Visibility: {weather_data.visibility:,} m\n"
            f"Wind speed: {weather_data.wind_speed} km/h\n"
            f"Humidity: {weather_data.humidity}%\n"
            f"API source: {weather_data.source}"
        )
        print(formatted_data)
