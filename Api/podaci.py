import requests
import json

url = "https://getpantry.cloud/apiv1/pantry/3ab3757e-2586-4248-8cd5-843b30ae8ab8/basket/basket"

payload = json.dumps({
	"id": "1000",
	"ime": "Lazar",
	"prezime": "Pavlovic",
	"smer": "Inzenjerstvo",
	"predmeti": [
		"Analiza",
		"Operativni sistemi",
		"Namenski racunari",
		"Algoritmi",
		"Kompresija podataka"
	],
	"prosek": 8.11,
	"kontakt": {
		"adresa": "Knez Mihailova 6",
		"mesto": "Beograd",
		"telefon": "0641234567"
	}
})
headers = {
	'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
