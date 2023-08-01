import requests

BASE_URL = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'

def get_weather():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

def get_temp(date):
    weather_data = get_weather()
    if not weather_data:
        return

    for data in weather_data['list']:
        if date in data['dt_txt']:
            print("Temperature on {date}: {data['main']['temp']}°C")
            return
    print("Data not available for the specified date.")

def get_wind_speed(date):
    weather_data = get_weather()
    if not weather_data:
        return

    for data in weather_data['list']:
        if date in data['dt_txt']:
            print("Wind Speed on {date}: {data['wind']['speed']} m/s")
            return
    print("Data not available for the specified date.")

def get_pressure(date):
    weather_data = get_weather()
    if not weather_data:
        return

    for data in weather_data['list']:
        if date in data['dt_txt']:
            print("Pressure on {date}: {data['main']['pressure']} hPa")
            return
    print("Data not available for the specified date.")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == '1':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            get_temp(date)
        elif option == '2':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            get_wind_speed(date)
        elif option == '3':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            get_pressure(date)
        elif option == '0':
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
