import json 
from pathlib import Path 
from typing import List 


THIS_DIR = Path(__file__).parent  # to grab the parent directory 
CITIES_JSON_PATH = THIS_DIR / "./cities.json"

def is_city_capital_of_state(city_name : str, state : str) -> bool: 
    cities_json_contents = CITIES_JSON_PATH.read_text()
    cities: List[dict] = json.loads(cities_json_contents)
    matching_cities: List[dict] = [city for city in cities if city["city"] == city_name]

    if len(matching_cities) == 0: 
        return False 
    matched_city = matching_cities[0]

    return matched_city["state"] == state



if __name__ == "__main__": 
    is_capital = is_city_capital_of_state(city_name="Mongomery", state="Alabama")

    print(is_capital)


## python -m packaging_demo.states_info 