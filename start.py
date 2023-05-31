# import required modules
import requests, json

# Enter your API key here
api_key = "1af89baf2df5b4a53aacdf69b931dbad"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input("Enter city name : ")

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

print(complete_url)
# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()
print(x['cod'])
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x['cod'] == 401 or x['cod'] == 404 :

	print(" City Not Found ")

else:
    # store the value of "main"
	# key in variable y
	y = x["main"]
 
	z= x['weather']
 
 
	weathertype=z[0]['main']
	icon=z[0]['icon'] 
 	
	# store the value corresponding
	# to the "temp" key of y
	current_temperature = y["temp"]

	# store the value corresponding
	# to the "pressure" key of y
	current_pressure = y["pressure"]

	# store the value corresponding
	# to the "humidity" key of y
	current_humidity = y["humidity"]

	# store the value of "weather"
	# key in variable z
	z = x["weather"]

	# store the value corresponding
	# to the "description" key at
	# the 0th index of z
	weather_description = z[0]["description"]

	# print following values
	print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidity) +
		"\n description = " +
					str(weather_description)+
     	"\n weather type = " +
					str(weathertype)+
		"\n weather icon = " +"https://openweathermap.org/img/wn/"+
					str(icon)+ "@2x.png")
	
