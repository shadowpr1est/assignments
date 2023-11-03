Weather API Adapter
This project consists of two Python scripts that act as adapters for different weather APIs and standardize the retrieved weather data into a common format for use by a mobile application. The two supported APIs are VisualCrossing and OpenWeatherMap.

VisualCrossing API Adapter
Description
The visualcrossing_weather_adapter.py script fetches weather data from the VisualCrossing API and maps it to a common data model. The retrieved data is then formatted and displayed in a standardized format.

Usage
Make sure you have the required Python libraries installed. You can install them using pip:

bash
Copy code
pip install requests
Run the script using the following command:

bash
Copy code
python visualcrossing_weather_adapter.py
Enter the name of the city for which you want to fetch weather data when prompted.

The script will fetch and display the weather data, including description, conditions, temperature, feels like, humidity, wind speed, visibility, and the API source (VisualCrossing).

OpenWeatherMap API Adapter
Description
The openweathermap_weather_adapter.py script fetches weather data from the OpenWeatherMap API and maps it to a common data model. The retrieved data is then formatted and displayed in a standardized format.

Usage
Make sure you have the required Python libraries installed. You can install them using pip:

bash
Copy code
pip install requests
Run the script using the following command:

bash
Copy code
python openweathermap_weather_adapter.py
Enter the name of the city for which you want to fetch weather data when prompted.

The script will fetch and display the weather data, including description, temperature, feels like, visibility, wind speed, humidity, and the API source (OpenWeatherMap).

Common Data Model
Both scripts use a common data model for weather data, which includes the following fields:

description: A brief description of the weather.
temperature: The temperature in degrees Celsius.
feels_like: The "feels like" temperature in degrees Celsius.
visibility: Visibility in meters.
wind_speed: Wind speed in kilometers per hour.
humidity: Humidity percentage.
source: The source API (either VisualCrossing or OpenWeatherMap).
By using this common data model, the retrieved data from different APIs is standardized for use in a mobile application.
