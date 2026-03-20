from flask import Flask, render_template, request
import pickle
import pandas as pd
import requests
import gdown
import os

app = Flask(__name__)

# ---------------- DOWNLOAD FILE FROM GOOGLE DRIVE ---------------- #

FILE_ID = "1IMBrGlgWYGXbP2pV98joCcCOBAIy-hvg"
SIMILARITY_FILE = "similarity.pkl"

def download_similarity():
    if not os.path.exists(SIMILARITY_FILE):
        url = f"https://drive.google.com/uc?id={FILE_ID}"
        print("Downloading similarity.pkl...")
        gdown.download(url, SIMILARITY_FILE, quiet=False)

download_similarity()

# ---------------- LOAD DATA ---------------- #

movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open(SIMILARITY_FILE, "rb"))

# ---------------- FUNCTIONS ---------------- #

def fetch_poster(movie_id):
    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=431f1599769535dae79f75e0abca9f5f&language=en-US"
        )
        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            return "https://via.placeholder.com/500"
    except:
        return "https://via.placeholder.com/500"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# ---------------- ROUTES ---------------- #

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_movie = None
    recommendations = []
    posters = []

    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        recommendations, posters = recommend(selected_movie)

    return render_template(
        'index.html',
        movie_list=movies['title'].values,
        recommendations=recommendations,
        posters=posters,
        selected_movie=selected_movie   # ✅ important fix
    )


# ---------------- RUN ---------------- #

if __name__ == "__main__":
    app.run(debug=True)