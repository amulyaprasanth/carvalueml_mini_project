import requests

url = "https://car-data.p.rapidapi.com/cars"

querystring = {"limit": "10", "page": "0"}

headers = {
	"x-rapidapi-key": "4e0b8610b0mshbc5e897e6c4d40ap122cd2jsn3d27d6515891",
	"x-rapidapi-host": "car-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
