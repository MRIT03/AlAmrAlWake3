# pip install pyahocorasick
# pip install pyarabic

import ahocorasick
import re

# Normalize Arabic text by removing diacritics and normalizing certain characters.
def normalize_arabic(text: str) -> str:
    text = re.sub(r'[\u0625\u0623\u0622\u0671]', '\u0623', text)
    text = text.replace('ة', 'ه')
    text = re.sub(r'[\u064B-\u0652\u0670]', '', text)
    text = text.replace('\u0640', '')
    text = text.lower()
    return text

# Find cities in the article using Aho-Corasick algorithm
def find_city(article: str, cities: list, is_arabic: bool = False) -> list:
    if not isinstance(article, str):
        raise TypeError("Article must be a string.")
    if not isinstance(cities, list) or not all(isinstance(city, str) for city in cities):
        raise TypeError("Cities must be a list of strings.")

    if not cities:
        return []

    original_city_map = {}

    if is_arabic:
        article = normalize_arabic(article)
        normalized_cities = []
        for city in cities:
            norm_city = normalize_arabic(city)
            original_city_map[norm_city] = city
            normalized_cities.append(norm_city)
    else:
        article = article.lower()
        normalized_cities = []
        for city in cities:
            norm_city = city.lower()
            original_city_map[norm_city] = city
            normalized_cities.append(norm_city)

    automaton = ahocorasick.Automaton()
    for idx, city in enumerate(normalized_cities):
        automaton.add_word(city, (idx, city))
    automaton.make_automaton()

    found_cities = set()
    for end_index, (idx, city) in automaton.iter(article):
        found_cities.add(original_city_map[city])

    return list(found_cities)

def main():

    cities = ['byblos', 'baalbek', 'بيروت', 'بعلبك', 'جبيل', 'جونية']

    article = input("Enter text: ")
    is_Arabic = input("Is it in arabic? (Y/N): ")
    found = find_city(article, cities, is_Arabic=="Y")
    print("Cities found: ", found)

if __name__ == "__main__":
    main()