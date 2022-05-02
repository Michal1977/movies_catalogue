from flask import Flask, render_template, request

from movies_API import get_backdrop_url, get_configuration, get_movie_credits, get_movie_details, get_popular_movies, \
    get_poster_url, get_upcoming_movies, get_movies, get_top_rated_movies, get_now_playing_movies

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
    selected_list = request.args.get('list_type', "popular")
    movies = get_movies(how_many=8, list_type=selected_list)
    config = get_configuration()
    return render_template("homepage.html", movies=movies, current_list=selected_list, config=config)


#@app.route('/upcoming')
#def upcoming():
    #movies = get_upcoming_movies()
    #config = get_configuration()
    #return render_template("homepage.html", movies=movies, config=config)


@app.route('/movies/<movie_id>')
def one_movie(movie_id):
    config = get_configuration()
    movie_details = get_movie_details(movie_id)
    credits = get_movie_credits(movie_id)
    return render_template("movie_details.html", movie=movie_details, config=config, credits=credits)


if __name__ == '__main__':
    app.run(debug=True)

