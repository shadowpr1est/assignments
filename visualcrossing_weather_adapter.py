import requests


class WeatherData:
    def __init__(self, description, conditions, temperature, feels_like, humidity, wind_speed, visibility, source):
        self.description = description
        self.conditions = conditions
        self.temperature = temperature
        self.feels_like = feels_like
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.visibility = visibility
        self.source = source


def fetch_and_map_weather_data(api_key, city):
    if not city:
        print('Enter your city')
        return

    api_endpoint = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key={api_key}"

    weather_data = requests.get(api_endpoint)
    if weather_data.status_code == 404:
        print('City not found')
        return

    api_data = weather_data.json()

    description = api_data["description"]
    conditions = api_data["days"][0]["conditions"]
    temperature = round(api_data["days"][0]["temp"] - 25, 1)
    feels_like = round(api_data["days"][0]["feelslike"] - 25, 1)
    humidity = api_data["days"][0]["humidity"]
    wind_speed = round(api_data["days"][0]["windspeed"] - 15, 1)
    visibility = int(api_data["days"][0]["visibility"] * 1000)

    weather_obj = WeatherData(description, conditions, temperature, feels_like, humidity, wind_speed, visibility,
                              "VisualCrossing")

    return weather_obj


if __name__ == "__main__":
    api_key = "QRJFZNBVX6KAC7RDZUM29M2NV"
    city = input("Enter a city: ")

    weather_data = fetch_and_map_weather_data(api_key, city)

    if weather_data:
        formatted_data = (
            f"\nDescription: {weather_data.description}\n"
            f"Conditions: {weather_data.conditions}\n"
            f"Temperature: {weather_data.temperature} ℃\n"
            f"Feels like: {weather_data.feels_like} ℃\n"
            f"Humidity: {weather_data.humidity} %\n"
            f"Wind speed: {weather_data.wind_speed} km/h\n"
            f"Visibility: {weather_data.visibility} m\n"
            f"API source: {weather_data.source}"
        )
        print(formatted_data)
