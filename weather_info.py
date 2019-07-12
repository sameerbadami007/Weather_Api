import requests
def we(city,units):
	if units=='imperial' or units=='metric':
		base="https://api.openweathermap.org/data/2.5/weather?q={city},uk&appid=086c7b8a6ddbf9390c03f5ca2a6a3e3e&units={units}"
	else:
		base='https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=086c7b8a6ddbf9390c03f5ca2a6a3e3e'
	return requests.get(base).json()
print(we('''B'lore''','metric'))
