import requests
import json
# Ask the user input from the user

city=input("Enter a city name:")

#Api details
base_Url="https://api.openweathermap.org/data/2.5/weather"
api_key="ae8a74c3a01ef4a7170ffcab187ed29f"

#parameters are inputs for the api
A={
    "q":city,
    "appid":api_key,
    "units":"metric"
}

#how do i finally make a api call or requests
response=requests.get(base_Url,A)
data=response.json()
print(json.dumps(data,indent=3))
D=data["weather"][0]["description"]
T=data["main"]["temp"]
print(f"The current temperature of the {city} is {T} and it's {D} ")
