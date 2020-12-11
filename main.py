import requests
import pandas as pd
import tablib
import openpyxl

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/pl/pln/pl-PL/KRK-sky/STN-sky/2021-01-01"

headers = {
    'x-rapidapi-key': "422894374fmsh023eb926213aa23p1b8967jsn96e86f739667",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

data = pd.DataFrame.from_dict(response)
print(data)

data.to_excel("loty.xlsx")