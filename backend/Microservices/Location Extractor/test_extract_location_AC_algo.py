import pytest
from extract_location_AC_algo import find_city

# Cities for English and Arabic
english_cities = ["Cairo", "Alexandria", "Giza", "Luxor", "Aswan"]
arabic_cities = ["القاهرة", "الإسكندرية", "الجيزة", "الأقصر", "أسوان"]

def test_regular():
    article = "I visited Cairo this summer."
    assert find_city(article, english_cities) == ["Cairo"]

def test_no_location():
    article = "I love programming and coffee."
    assert find_city(article, english_cities) == []

def test_multiple_locs():
    article = "Giza, Luxor, and Cairo are popular tourist destinations."
    result = find_city(article, english_cities)
    assert set(result) == {"Cairo", "Giza", "Luxor"}

def test_case_sensitive():
    article = "alexandria is beautiful in the summer."
    assert find_city(article, english_cities) == ["Alexandria"]

def test_diacretics():
    article = "زُرْتُ القَاهِرَةَ وَالأَقْصُرَ."
    result = find_city(article, arabic_cities, is_arabic=True)
    assert set(result) >= {"القاهرة", "الأقصر"}

def test_numerical_input():
    with pytest.raises(TypeError):
        find_city(12345, english_cities)

def test_empty_input():
    assert find_city("", english_cities) == []

def test_no_cities():
    assert find_city("I visited Cairo.", []) == []

# Stress testing
def test_long_text():
    text = " ".join(["Cairo"] * 1000)
    assert find_city(text, english_cities) == ["Cairo"]
