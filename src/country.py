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
        
    def __str__(self):
            print(f"Name: {self.name}, Capital: {self.capital}")

    # Fetches all country data from an external API endpoint and returns the data.
    def fetch_countries():
        try:
            response = requests.get("https://restcountries.com/v3.1/all")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print("Error", f"Failed to fetch data: {e}")
            return []
        
    # Processes a list of country data dictionaries and instantiates Country objects with relevant data, returning a list of these objects.
    @staticmethod
    def process_countries(data):
        try:
            countries = []
            for country in data:
                if  country.get("capital"):
                    name = country["name"]["common"]
                    capital = country["capital"][0]
                    flag_url = country["flags"]["png"]
                    maps = country['maps']['openStreetMaps']
                    population = country['population']
                    currency = country['currencies']
                    region = country['region']
                    languages = list(country['languages'].values()) if country.get('languages') else []
                    area = country['area']
                    countryObject = Country(name,capital,flag_url,maps,population,currency,region,languages,area)
                    countries.append(countryObject)
            return countries
        except Exception as e:
            print(e)

    # Wraps the fetch_countries() and process_countries() methods to fetch and return all country objects in a list.
    def fetch_all_countries():
        return Country.process_countries(Country.fetch_countries())

    # Returns a list of unique regions from all countries.
    def get_regions():
        countries = Country.fetch_all_countries()
        return list(dict.fromkeys(country.region for country in countries))
    
    # Returns a list of all countries in the specified region.
    def get_countries_in_region(region_name):
        return [country for country in Country.fetch_all_countries() if country.region == region_name]

   # Saves a list of countries (as instances of the Country class) to a JSON file. 
    def save_countries_to_file(data, filename="countries.json"):
            """Save the country data to a JSON file."""
            try:
                with open(filename, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                print(f"Data successfully saved to {filename}")
            except IOError as e:
                print(f"Error: Unable to save data to file: {e}")

    # Loads a list of countries from a JSON file and instanciates the Country class for each country            
    @staticmethod
    def load_countries_from_file(filename="data/countries.json"):
        """Load country data from a JSON file and instantiate Country objects."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                countries = []
                for country in data:
                    name = country["name"]["common"]
                    capital = country["capital"][0] if "capital" in country and country["capital"] else "N/A"
                    flag_url = country["flags"]["png"]
                    maps = country.get("maps", {}).get("openStreetMaps", "")
                    population = country.get("population", 0)
                    currency = country.get("currencies", {})
                    region = country.get("region", "Unknown")
                    languages = list(country.get("languages", {}).values())
                    area = country.get("area", 0)
                    country_object = Country(name, capital, flag_url, maps, population, currency, region, languages, area)
                    countries.append(country_object)
                return countries
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error: Unable to load data from file: {e}")
            return []