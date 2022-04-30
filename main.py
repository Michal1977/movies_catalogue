from flask import Flask, render_template

from movies_project.movies_catalogue.movies_API import get_popular_movies, get_configuration, get_poster_url

app = Flask(__name__)


#@app.route('/')
#def homepage():
#    return render_template("index.html")


@app.route('/')
def homepage():
    movies = get_popular_movies()
    config = get_configuration()
    a = get_poster_url(config, "poster", "w185")
    return render_template("homepage.html", movies=movies, config=config)


if __name__ == '__main__':
    app.run(debug=True)