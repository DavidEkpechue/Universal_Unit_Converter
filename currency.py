import requests
import json

def jprint_to_file(obj, filename):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    # write to file
    with open(filename, 'w') as file:
        file.write(text)
    print(f"Data written to {filename}")

url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur.json'
response = requests.get(url)
data = response.json()

# Call the function with the JSON data and the filename
jprint_to_file(data, 'currency_data.json')
