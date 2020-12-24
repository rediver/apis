import requests
import pandas as pd

url = "https://alexnormand-dino-ipsum.p.rapidapi.com/"

querystring = {"format":"html","words":"30","paragraphs":"30"}

headers = {
    'x-rapidapi-key': "422894374fmsh023eb926213aa23p1b8967jsn96e86f739667",
    'x-rapidapi-host': "alexnormand-dino-ipsum.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


data = pd.DataFrame.from_dict(response)

print(data)

data.to_csv("a")