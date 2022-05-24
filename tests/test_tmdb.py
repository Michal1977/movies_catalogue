import unittest
from flask import Flask, render_template, request
from main import app
from movies_API import get_backdrop_url, get_configuration, get_movie_credits, get_movie_details, get_poster_url, get_movies_list, get_cast
from unittest.mock import Mock, MagicMock

def test_get_poster_url_uses_default_size():
   # Przygotowanie danych
   conf = {
		"secure_base_url": "https://image.tmdb.org/t/p/",

		"poster_sizes": [
			"w92",
			"w154",
			"w185",
			"w342",
			"w500",
			"w780",
			"original"
		]}
   # Wywołanie kodu, który testujemy
   poster_url = get_poster_url(conf, '/poster_api_path')
   # Porównanie wyników
   assert poster_url=="https://image.tmdb.org/t/p/w342/poster_api_path"



def test_get_poster_url_uses_set_size():
   # Przygotowanie danych
   conf = {
		"secure_base_url": "https://image.tmdb.org/t/p/",

		"poster_sizes": [
			"w92",
			"w154",
			"w185",
			"w342",
			"w500",
			"w780",
			"original"
		]}
   # Wywołanie kodu, który testujemy
   poster_url = get_poster_url(conf, '/poster_api_path', 'w780')
   # Porównanie wyników
   assert poster_url=="https://image.tmdb.org/t/p/w780/poster_api_path"


def test_get_poster_url_uses_not_existing_size():
   # Przygotowanie danych
   conf = {
		"secure_base_url": "https://image.tmdb.org/t/p/",

		"poster_sizes": [
			"w92",
			"w154",
			"w185",
			"w342",
			"w500",
			"w780",
			"original"
		]}
   # Wywołanie kodu, który testujemy
   poster_url = get_poster_url(conf, '/poster_api_path', 'w678')
   # Porównanie wyników
   assert poster_url=="https://image.tmdb.org/t/p/w92/poster_api_path"


def test_get_movies_list_type_popular():
   movies_list = get_movies_list(list_type="popular")
   assert movies_list is not None


#single movie
def test_get_movie_details():
   movie_details = get_movie_details(movie_id="1396")
   assert movie_details is not None


def test_get_movies_list(monkeypatch):
   # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = [{'id':526896}]

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = {"results": mock_movies_list }
   monkeypatch.setattr("requests.get", requests_mock)
   movies_list = get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list


def test_get_cast(monkeypatch):

    mock_cast = [{'id':7499}, {'id':136532}]
    requests_mock = MagicMock()
    response = requests_mock.return_value
    response.json.return_value = {"cast":mock_cast}
    monkeypatch.setattr("requests.get", requests_mock)
    cast = get_cast(movie_id="526896", how_many=2)
    assert cast == mock_cast


def test_homepage_empty(monkeypatch):
   api_mock = Mock(return_value=[])
   monkeypatch.setattr("movies_API.get_movies_list", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('popular')


def test_homepage(monkeypatch):
   api_mock = Mock(return_value=[{"id":390}])
   monkeypatch.setattr("movies_API.get_movies_list", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('popular')