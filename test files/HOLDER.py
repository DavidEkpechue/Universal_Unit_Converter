import requests
from datetime import datetime
from opencage.geocoder import OpenCageGeocode

def get_coordinates(city_name, api_key):
    geocoder = OpenCageGeocode(api_key)
    query = city_name
    results = geocoder.geocode(query)
    
    if results and len(results):
        latitude = results[0]['geometry']['lat']
        longitude = results[0]['geometry']['lng']
        country = results[0]['components']['country']
        return latitude, longitude, country
    else:
        return None, None, None

def test(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,is_day,rain",
        "hourly": "temperature_2m",
        "timezone": "Europe/London"
    }
    response = requests.get(url, params=params)
    data = response.json()

    temperatures = data['hourly']['temperature_2m']
    times = data['hourly']['time']

    for temp, time_str in zip(temperatures, times):
        time_obj = datetime.fromisoformat(time_str)
        friendly_time = time_obj.strftime("%B %d, %Y, at %H:%M")
        print(f"{temp} degrees Celsius at {friendly_time}")

    current_temperature = data['current']['temperature_2m']
    print(f"Current temperature: {current_temperature} degrees Celsius")

def main():
    OPEN_CAGE_API_KEY = '9c8980599c9b47d8a3f48b0a5127b839'
    city = input("Enter a city name: ")

    latitude, longitude, country = get_coordinates(city, OPEN_CAGE_API_KEY)
    
    if latitude is not None and longitude is not None:
        print(f"Coordinates for {city}, {country}: Latitude {latitude}, Longitude {longitude}")
        test(latitude, longitude)
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    main()
