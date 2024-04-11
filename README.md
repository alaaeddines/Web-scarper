#  Cars data web scarper

This Python script scrapes car listings from the specified website, focusing on Peugeot cars for sale in Morocco. It extracts essential information such as car model, price, city, fuel type, horsepower (CV), transmission, and description. The scraped data is then saved to a CSV file named "data.csv".

## Requirements:

* Python 3
* requests library 
* beautifulsoup4 library 
* csv library
  
## Instructions:

Install Libraries using pip:

`pip install requests beautifulsoup4`

Execute the script using Python:

`python code.py`.

## Output:

The script will create a CSV file named "data.csv" containing the scraped car data in the following columns:

* voiture (car model)

* prix (price)

* ville (city)

* carburant (fuel type)

* CV (horsepower)

* transmission (transmission)

* description (car description)
