import requests
import json

class Country:
    def __init__(self, name, capital, flag_url, maps,population,currency,region,languages,area):
        self.name = name
        self.capital = capital
        self.flag_url = flag_url
        self.maps = maps
        self.population = population
        self.currency = currency
        self.region = region
        self.languages = languages
        self.area = area
