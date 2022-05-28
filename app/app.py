#IMPORTING LIBRARIES
import streamlit as st
import pickle
import pandas as pd
import requests
import re
import string
from PIL import Image

img = Image.open('picture.jpg')

st.set_page_config(page_title='Movie Recommender', page_icon=img)



#FETCH DETAILS OF A MOVIE USING TMDB API

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3a0c5eedf725534a2717947b936dbe40&language=en-US'.format(movie_id))
    data = response.json()
    if(data['poster_path']==None):
        return "data:image/png;base64,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"
    return "https://image.tmdb.org/t/p/original"+data['poster_path']

def fetch_overview(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3a0c5eedf725534a2717947b936dbe40&language=en-US'.format(movie_id))
    data = response.json()
    return data['overview']

def fetch_date(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3a0c5eedf725534a2717947b936dbe40&language=en-US'.format(movie_id))
    data = response.json()
    return data['release_date']

def fetch_vote(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3a0c5eedf725534a2717947b936dbe40&language=en-US'.format(movie_id))
    data = response.json()
    return data['vote_average']

def fetch_genres(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3a0c5eedf725534a2717947b936dbe40&language=en-US'.format(movie_id))
    data = response.json()
    object=  data['genres']
    res=""

    for obj in object:
        res=res+obj['name']+", "
    res = res.rstrip(res[-1])
    res = res.rstrip(res[-1])
    return res


def fetch_cast(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}/credits?api_key=3a0c5eedf725534a2717947b936dbe40&language=en-US'.format(movie_id))
    data = response.json()
    object=  data['cast']
    res=""
    count = 0
    for obj in object:
        if (count == 4):
            break
        res = res + obj['name'] + ", "
        count+=1
    res = res.rstrip(res[-1])
    res = res.rstrip(res[-1])
    return res



def fetch_provider(movie_id):
    response = requests.get('https://api.themoviedb.org/3/watch/providers/movie?api_key=3a0c5eedf725534a2717947b936dbe40&language=en-US'.format(movie_id))
    data = response.json()
    object=  data['results']
    res=""
    count=0
    for obj in object:
        if(count==5):
            break
        if(obj['display_priority']==0 or obj['display_priority']==1):
            res=res+obj['provider_name']+", "
            count+=1
        else:
            break
    res = res.rstrip(res[-1])
    res = res.rstrip(res[-1])
    return res

#FUNCTION FOR RECOMMENDING MOVIES AND FETCHING DETAILS USING API
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:11]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_overview = []
    recommended_movies_date = []
    recommended_movies_vote = []
    recommended_movies_genres = []
    movie_cast = []
    watch_provider = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id


        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_overview.append(fetch_overview(movie_id))
        recommended_movies_date.append(fetch_date(movie_id))
        recommended_movies_vote.append(fetch_vote(movie_id))
        recommended_movies_genres.append(fetch_genres(movie_id))
        movie_cast.append(fetch_cast(movie_id))
        watch_provider.append(fetch_provider(movie_id))
    return recommended_movies, recommended_movies_posters, recommended_movies_overview, recommended_movies_date,recommended_movies_vote, recommended_movies_genres, movie_cast, watch_provider



#LOAD PICKLE FILES CONTAINING MODEL AND DATASET
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))



#TITLE OF THE WEBSITE
st.title('Recommend me some movies')


#SELECTBOX TO SELECT A MOVIE OF THE USER'S CHOICE
selected_movie_name = st.selectbox(
"What's your taste!",
movies['title'].values
)


#RECOMMEND BUTTON TO SHOW THE RECOMMENDATIONS
if st.button('Recommend'):

    names, posters ,overview,date, vote, genres, cast,provider = recommend(selected_movie_name)

    col1,col2,col3 = st.columns(3)
    with col1:
        st.write("")
    with col2:
        with st.container():
            st.subheader(names[0])
            st.image(posters[0], width=300)
            st.write("**Top Cast** - " + str(cast[0]))
            st.write("**Release Date** - " + date[0])
            st.write(":star2: " + str(vote[0]))
            with st.expander("Overview"):
                st.write(overview[0])

            with st.expander("Genres"):
                st.write(genres[0])
            with st.expander("Watch Options"):
                st.write(provider[0])

    with col3:
        st.write("")


    st.subheader('Recommended Movies')
    col1, col2 = st.columns(2)


    with col1:
        with st.container():
            st.subheader(names[1])
            st.image(posters[1],width=225)
            st.write("**Top Cast** - " + str(cast[1]))
            st.write("**Release Date** - " + date[1])
            st.write(":star2: " + str(vote[1]))
            with st.expander("Storyline"):
                 st.write(overview[1])

            with st.expander("Genres"):
                st.write(genres[1])
            with st.expander("Watch Options"):
                st.write(provider[1])


    with col2:
        with st.container():
            st.subheader(names[2])

            st.image(posters[2],width=225)
            st.write("**Top Cast** - " + str(cast[2]))
            st.write("**Release Date** - " + date[2])
            st.write(":star2: " + str(vote[2]))
            with st.expander("Storyline"):
                 st.write(overview[2])

            with st.expander("Genres"):
                st.write(genres[2])
            with st.expander("Watch Options"):
                st.write(provider[2])
    col3, col4 = st.columns(2)
    with col3:
        with st.container():
            st.subheader(names[3])
            st.image(posters[3],width=225)
            st.write("**Top Cast** - " + str(cast[3]))
            st.write("**Release Date** - " + date[3])
            st.write(":star2: " + str(vote[3]))
            with st.expander("Storyline"):
                 st.write(overview[3])

            with st.expander("Genres"):
                st.write(genres[3])

            with st.expander("Watch Options"):
                st.write(provider[3])


    with col4:
        with st.container():
            st.subheader(names[4])
            st.image(posters[4],width=225)
            st.write("**Top Cast** - " + str(cast[4]))
            st.write("**Release Date** - " + date[4])
            st.write(":star2: " + str(vote[4]))
            with st.expander("Storyline"):
                 st.write(overview[4])

            with st.expander("Genres"):
                st.write(genres[4])
            with st.expander("Watch Options"):
                st.write(provider[4])





    col5, col6 = st.columns(2)
    with col5:
        with st.container():
            st.subheader(names[5])
            st.image(posters[5],width=225)
            st.write("**Top Cast** - " + str(cast[5]))
            st.write("**Release Date** - " + date[5])
            st.write(":star2: " + str(vote[5]))
            with st.expander("Storyline"):
                st.write(overview[5])

            with st.expander("Genres"):
                st.write(genres[5])
            with st.expander("Watch Options"):
                st.write(provider[5])

    with col6:
        with st.container():
            st.subheader(names[6])
            st.image(posters[6],width=225)
            st.write("**Top Cast** - " + str(cast[6]))
            st.write("**Release Date** - " + date[6])
            st.write(":star2: " + str(vote[6]))
            with st.expander("Storyline"):
                st.write(overview[6])

            with st.expander("Genres"):
                st.write(genres[6])
            with st.expander("Watch Options"):
                st.write(provider[6])


    col7, col8 = st.columns(2)
    with col7:
        with st.container():
            st.subheader(names[7])
            st.image(posters[7],width=225)
            st.write("**Top Cast** - " + str(cast[7]))
            st.write("**Release Date** - " + date[7])
            st.write(":star2: " + str(vote[7]))
            with st.expander("Storyline"):
                st.write(overview[7])

            with st.expander("Genres"):
                st.write(genres[7])
            with st.expander("Watch Options"):
                st.write(provider[7])



    with col8:
        with st.container():
            st.subheader(names[8])
            if(posters[8]=="data:image/png;base64,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"):
                st.image(posters[8],width=283)
            else:
                st.image(posters[8],width=225)
            st.write("**Top Cast** - " + str(cast[8]))
            st.write("**Release Date** - " + date[8])
            st.write(":star2: " + str(vote[8]))
            with st.expander("Storyline"):
                st.write(overview[8])

            with st.expander("Genres"):
                st.write(genres[8])
            with st.expander("Watch Options"):
                st.write(provider[8])

    col9, col10 = st.columns(2)
    with col9:
        with st.container():
            st.subheader(names[9])
            st.image(posters[9],width=225)
            st.write("**Top Cast** - " + str(cast[9]))
            st.write("**Release Date** - " + date[9])
            st.write(":star2: " + str(vote[9]))
            with st.expander("Storyline"):
                st.write(overview[9])

            with st.expander("Genres"):
                st.write(genres[9])
            with st.expander("Watch Options"):
                st.write(provider[9])

    with col10:
        with st.container():
            st.subheader(names[10])
            st.image(posters[10],width=225)
            st.write("**Top Cast** - " + str(cast[10]))
            st.write("**Release Date** - " + date[10])
            st.write(":star2: " + str(vote[10]))
            with st.expander("Storyline"):
                st.write(overview[10])

            with st.expander("Genres"):
                st.write(genres[10])
            with st.expander("Watch Options"):
                st.write(provider[10])


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


st.write(':copyright: 2022 movie recommendations')
