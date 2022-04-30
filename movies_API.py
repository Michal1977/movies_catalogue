import requests


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYzY4ZDMxNDhjOTU3ZGIxMmQ5MmI0MmFiOTI0YjRiNCIsInN1YiI6IjYyNjkzMTE4NWFiODFhMTMyZTFmOTM2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TTcpJnh0eCNiXJlTdIBLqNF6qcqeIm0_Li2fUKWtxMk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['results']


def get_configuration():
    endpoint = "https://api.themoviedb.org/3/configuration"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYzY4ZDMxNDhjOTU3ZGIxMmQ5MmI0MmFiOTI0YjRiNCIsInN1YiI6IjYyNjkzMTE4NWFiODFhMTMyZTFmOTM2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TTcpJnh0eCNiXJlTdIBLqNF6qcqeIm0_Li2fUKWtxMk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['images']


def get_poster_url(conf, poster_api_path, size="w342"):

    base_url = conf['secure_base_url']
    if size not in conf['poster_sizes']:
        size = conf['poster_sizes'][0]

    return f"{base_url}{size}{poster_api_path}"