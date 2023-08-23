#Exercise: Create a function that adds a dictionary element to a list

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country_visited, num_of_visits, cities_visited):
    '''
    The idea is we create a new dictionary and add all values to the corresponding keys. And then, we append that dictionary to the designated list.
    Parameters
    ----------
    country_visited : TYPE: str
    num_of_visits : TYPE: int
    cities_visited : TYPE: list of string

    Returns
    -------
    None.

    '''
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = num_of_visits
    new_country["cities"] = cities_visited
    travel_log.append(new_country)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
for element in travel_log:
    for position in element:
        print(f"{position} : {element[position]}")
    print("\n")







