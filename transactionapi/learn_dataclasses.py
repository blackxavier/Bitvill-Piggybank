# A basic python class
from dataclasses import dataclass, field


class Country:
    def __init__(self, name: str, population: int, continent: str, official_lang: str):
        self.name = name
        self.population = population
        self.continent = continent
        self.official_lang = official_lang

    def print_data(self):
        return f"The name of my country is {self.name},with a population of {self.population}, in {self.continent}  with official language as {self.official_lang}"

    def __str__(self):
        return self.name


country1 = Country("Nigeria", 140000000, "Africa", "English")
country2 = Country("Mali", 1400000, "Africa", "French")
print(country1.print_data())
print(country1)
print(country2.print_data())
print(country2)
print("--------------------------------------")


@dataclass(order=True)
class Countries:
    name: str
    population: int
    continent: str
    will_migrate: bool = field(init=False)
    official_lang: str = field(init=False, repr=False)

    def __post_init__(self):
        if self.official_lang == "English":
            self.will_migrate == True
        else:
            self.will_migrate == False


country1 = Countries("Nigeria", 4000000, "Africa")
print(country1)
