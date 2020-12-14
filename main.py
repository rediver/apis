import requests
import pandas as pd
import tablib
import openpyxl
from datetime import date
import json
import logging

def handler(event): 

	logger.info("Received event: {}".format(event))

	ldn_airports = ["LHR-sky", "STN-sky", "LGW-sky", "LTN-sky"]
	ldn_arr = []
	today = str(date.today())

	headers = {
	    'x-rapidapi-key': "422894374fmsh023eb926213aa23p1b8967jsn96e86f739667",
	    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
	    }

	for i in ldn_airports:
	  x = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/pl/pln/pl-PL/KRK-sky/" + i + "/" + today
	  ldn_arr.append(x)

	for i in ldn_arr:
		response = requests.request("GET", i, headers=headers)
		response_data = response.json()
		print(response_data)


print('json END')

