import json
import requests
from datetime import date

ldn_airports = ["LHR-sky", "STN-sky", "LGW-sky", "LTN-sky"]
ldn_arr = []
today = str(date.today())

headers = {
    'x-rapidapi-key': "422894374fmsh023eb926213aa23p1b8967jsn96e86f739667",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
}


for i in ldn_airports:
    x = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/pl/pln/pl-PL/KRK-sky/" + i + "/" + today
    response = requests.request("GET", x, headers=headers)
    response_data = response.json()
    	
    ldn_arr.append(response_data)	

    with open('results.json', 'w') as f: 
    	json.dump(ldn_arr, f, indent=2)

    
print(ldn_arr)
