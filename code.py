import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "761fae22"
CITY = "London,us"

def get_weather_data():
    response = requests.get(f"{API_BASE_URL}?q={CITY}&appid={API_KEY}")
    data = response.json()
    return data["list"]

def get_weather_by_date(date):
    weather_data = get_weather_data()
    for forecast in weather_data:
        if forecast["dt_txt"] == date:
            return forecast["main"]["temp"]
    return None

def get_wind_speed_by_date(date):
    weather_data = get_weather_data()
    for forecast in weather_data:
        if forecast["dt_txt"] == date:
            return forecast["wind"]["speed"]
    return None

def get_pressure_by_date(date):
    weather_data = get_weather_data()
    for forecast in weather_data:
        if forecast["dt_txt"] == date:
            return forecast["main"]["pressure"]
    return None

def main():
    while True:
        print("1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            temperature = get_weather_by_date(date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature}°C")
            else:
                print("No data available for the specified date.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            wind_speed = get_wind_speed_by_date(date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("No data available for the specified date.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            pressure = get_pressure_by_date(date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("No data available for the specified date.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
