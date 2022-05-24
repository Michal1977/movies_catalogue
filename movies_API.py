import requests


#def call_tmdb_api(endpoint):
#   full_url = f"https://api.themoviedb.org/3/{endpoint}"
#   api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYzY4ZDMxNDhjOTU3ZGIxMmQ5MmI0MmFiOTI0YjRiNCIsInN1YiI6IjYyNjkzMTE4NWFiODFhMTMyZTFmOTM2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TTcpJnh0eCNiXJlTdIBLqNF6qcqeIm0_Li2fUKWtxMk"
#   headers = {
#       "Authorization": f"Bearer {api_token}"
#   }
#   response = requests.get(full_url, headers=headers)
#   response.raise_for_status()
#   return response.json()


#def get_movies_list(list_type):
#  return call_tmdb_api(f"movie/{list_type}")


def get_configuration():
    endpoint = "https://api.themoviedb.org/3/configuration"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYzY4ZDMxNDhjOTU3ZGIxMmQ5MmI0MmFiOTI0YjRiNCIsInN1YiI6IjYyNjkzMTE4NWFiODFhMTMyZTFmOTM2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TTcpJnh0eCNiXJlTdIBLqNF6qcqeIm0_Li2fUKWtxMk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['images']


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYzY4ZDMxNDhjOTU3ZGIxMmQ5MmI0MmFiOTI0YjRiNCIsInN1YiI6IjYyNjkzMTE4NWFiODFhMTMyZTFmOTM2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TTcpJnh0eCNiXJlTdIBLqNF6qcqeIm0_Li2fUKWtxMk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['results']


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data[:min(how_many, len(data))]


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYzY4ZDMxNDhjOTU3ZGIxMmQ5MmI0MmFiOTI0YjRiNCIsInN1YiI6IjYyNjkzMTE4NWFiODFhMTMyZTFmOTM2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TTcpJnh0eCNiXJlTdIBLqNF6qcqeIm0_Li2fUKWtxMk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()['results']


def get_now_playing_movies():
    endpoint = "https://api.themoviedb.org/3/movie/now_playing"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYzY4ZDMxNDhjOTU3ZGIxMmQ5MmI0MmFiOTI0YjRiNCIsInN1YiI6IjYyNjkzMTE4NWFiODFhMTMyZTFmOTM2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TTcpJnh0eCNiXJlTdIBLqNF6qcqeIm0_Li2fUKWtxMk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['results']


def get_movie_details(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYzY4ZDMxNDhjOTU3ZGIxMmQ5MmI0MmFiOTI0YjRiNCIsInN1YiI6IjYyNjkzMTE4NWFiODFhMTMyZTFmOTM2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TTcpJnh0eCNiXJlTdIBLqNF6qcqeIm0_Li2fUKWtxMk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movie_credits(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYzY4ZDMxNDhjOTU3ZGIxMmQ5MmI0MmFiOTI0YjRiNCIsInN1YiI6IjYyNjkzMTE4NWFiODFhMTMyZTFmOTM2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TTcpJnh0eCNiXJlTdIBLqNF6qcqeIm0_Li2fUKWtxMk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"][:6]


def get_cast(how_many, movie_id):
    data = get_movie_credits(movie_id)
    return data[:how_many]


def get_poster_url(conf, poster_api_path, size="w342"):
    base_url = conf['secure_base_url']
    if size not in conf['poster_sizes']:
        size = conf['poster_sizes'][0]

    return f"{base_url}{size}{poster_api_path}"


def get_backdrop_url(conf, backdrop_api_path, size="w780"):
    base_url = conf['secure_base_url']
    if size not in conf['backdrop_sizes']:
        size = conf['backdrop_sizes'][0]
    return f"{base_url}{size}{backdrop_api_path}"


