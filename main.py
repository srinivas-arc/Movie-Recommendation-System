import pandas as pd
import requests
import streamlit as st
import pickle

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c5007266d8fbcf8f66c28d13df4e3d6d'.format(movie_id))
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']
def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    recommend=[]
    rec_posters=[]
    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommend.append(movies.iloc[i[0]].title)
        # poster from api
        rec_posters.append(fetch_poster(movie_id))
    return recommend,rec_posters

movies_dict=pickle.load(open('movies_todict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommender System")
selected_movie=st.selectbox('Movie',movies['title'].values)
if st.button("Recommend"):
    names,post=recommend(selected_movie)
    c1,c2,c3,c4,c5=st.columns(5)
    with c1:
        st.text(names[0])
        st.image(post[0])
    with c2:
        st.text(names[1])
        st.image(post[1])
    with c3:
        st.text(names[2])
        st.image(post[2])
    with c4:
        st.text(names[3])
        st.image(post[3])
    with c5:
        st.text(names[4])
        st.image(post[4])