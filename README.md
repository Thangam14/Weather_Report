# Weather Information Retrieval Program

This is a Python program that interacts with the OpenWeatherMap API to provide users with hourly weather forecast data for a specific city. The program allows users to choose from different options to retrieve weather-related information based on a date and time.

## Features

- Get the hourly weather forecast for a specified city using the OpenWeatherMap API.
- Choose from the following options:
  1. Get weather information (temperature) for a specific date and time.
  2. Get wind speed information for a specific date and time.
  3. Get pressure information for a specific date and time.
  0. Exit the program.

## How to Use

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine or download the `weather_app.py` file directly.
3. Open a terminal or command prompt and navigate to the folder containing `weather_app.py`.
4. Run the program by executing the following command:
   ```
   python weather_app.py
   ```
5. The program will prompt you to enter a city name (press Enter to use the default city, "London,us").
6. Choose the desired option (1, 2, 3, or 0) to retrieve weather information for a specific date and time.
7. Enter the date and time in the format "YYYY-MM-DD HH:MM:SS" to fetch the relevant data.
8. The program will display the requested weather information or indicate if the data is unavailable for the specified date.

## Dependencies

This program requires the `requests` library to make HTTP requests to the OpenWeatherMap API. You can install it using `pip` with the following command:
```
pip install requests
```

## API Key

The program uses an API key to access the OpenWeatherMap API. The API key (`appid`) is provided as part of the API request URL. Ensure that you keep your API key secure and avoid sharing it publicly.

## Disclaimer

This program is a simple demonstration of how to interact with an external API and retrieve weather data. It may have limitations and is not intended for production use. Users should refer to the OpenWeatherMap API documentation for real-world applications and to obtain a valid API key for their own projects.

For more information about the OpenWeatherMap API, please visit: [OpenWeatherMap API Documentation](https://openweathermap.org/api).

---
