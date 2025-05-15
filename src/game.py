import random
from country import Country

class Game:
    def __init__(self):
        self.score = 0
        self.last_country = None
        self.countries = Country.fetch_all_countries()
        self.selected_region = None
        self.current_country = random.choice(self.countries)
        self.unknown_countries = []
        self.regions = Country.get_regions()

    def generate_suggestions(self):
        """
        Generates three suggestions for the capital (1 correct, 2 random)
        """
        all_capitals = [c.capital for c in self.countries]

        if not all_capitals:
            return [self.current_country['capital']] * 3
        
        suggestions = [self.current_country.capital]

        while len(suggestions) < 3:
            candidate = random.choice(all_capitals)
            if candidate not in suggestions:
                suggestions.append(candidate)

        random.shuffle(suggestions)
        return suggestions
    
    def init_region_countries(self):
        self.countries = Country.get_countries_in_region(self.selected_region)
        self.current_country = random.choice(self.countries)

    def check_answer(self,answer):
        if answer == self.current_country.capital:
            self.score += 1
            self.last_country = self.current_country
            self.current_country = random.choice(self.countries)
            return True
        else:
            print(self.score)
            self.score -= 1
            print(self.score)
            self.last_country = self.current_country
            self.unknown_countries.append(self.current_country)
            self.current_country = random.choice(self.countries)
            return False
    
    def get_current_country(self):
        if self.selected_region == None:
            self.countries = Country.fetch_all_countries()
            self.current_country = random.choice(self.countries)
        else:
            self.countries = Country.get_countries_in_region(self.selected_region)
            self.current_country = random.choice(self.countries)
        return self.current_country
    
    def get_regions(self):
        return self.regions
