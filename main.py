from flask import Flask, render_template

from movies_API import get_backdrop_url, get_configuration, get_movie_credits, get_movie_details, get_popular_movies, \
    get_poster_url, get_upcoming_movies

app = Flask(__name__)


@app.context_processor
def utility_processor():
    def get_poster_url_preprocesor(conf, poster_api_path, size="w342"):
        return get_poster_url(conf, poster_api_path, size)

    def get_backdrop_url_preprocesor(conf, backdrop_api_path, size="w300"):
        return get_backdrop_url(conf, backdrop_api_path, size)

    return dict(get_poster_url_in_html=get_poster_url_preprocesor,
                get_backdrop_url_in_html=get_backdrop_url_preprocesor)


@app.route('/')
def homepage():
    movies = get_popular_movies()
    config = get_configuration()
    return render_template("homepage.html", movies=movies, config=config)


@app.route('/upcoming')
def upcoming():
    movies = get_upcoming_movies()
    config = get_configuration()
    return render_template("homepage.html", movies=movies, config=config)


@app.route('/movies/<movie_id>')
def one_movie(movie_id):
    config = get_configuration()
    movie_details = get_movie_details(movie_id)
    credits = get_movie_credits(movie_id)
    return render_template("movie.html", movie=movie_details, config=config, credits=credits)


if __name__ == '__main__':
    app.run(debug=True)

