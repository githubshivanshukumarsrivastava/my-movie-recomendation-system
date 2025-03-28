# import pickle
# import streamlit as st
# import requests

# #https://api.themoviedb.org/3/movie/{movie_id}/recommendations

# def fetch_poster(movie_id):
#     #url= "https://api.themoviedb.org/3/movie/{movie_id}/recommendations".format(movie_id)
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data= requests.get(url)
#     data= data.json()
#     #poster_path= data['results'][0]['poster_path']
#     poster_path =data['poster_path']
#     full_path="https://image.tmdb.org/t/p/w500/"+poster_path
#     return full_path
    
# def recommend(movies):
#     if movies not in movies['title'].values:
#         print(f"Movie '{movies}' not found in the dataset.")
#         return
#     index = movies[movies['title'] == movies].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movies_name=[]
#     recommended_movies_poster=[]
#     for i in distances[1:6]:
#         #print(movies.iloc[i[0]].title)
#         movies_id = movies.iloc[i[0]].movies_id
#         recommended_movies_poster.append(fetch_poster(movies_id))
       
#         recommended_movies_name.append(movies.iloc[i[0]].title)
#     return recommended_movies_name,recommended_movies_poster    
        




# st.header("Movies Recomendation system using machine lerning")
# movies =pickle.load(open('artificats/movie_list.pkl','rb'))
# similarity=pickle.load(open('artificats/similarity.pkl','rb'))

# movies_list= movies['title'].values
# selected_movies=st.selectbox(
#     'Type or select a movie to get recommendations',
#     movies_list

# )

# if st.button('show recommendations'):
#     recommended_movies_name  ,recommended_movies_poster = recommend(selected_movies)
#     col1 ,col2,col3,col4,col5=st.columns(5)
#     with col1:
#         st.text(recommended_movies_name[0])
#         st.image(recommended_movies_poster[0])

#     with col2:
#         st.text(recommended_movies_name[1])
#         st.image(recommended_movies_poster[1])

#     with col3:
#         st.text(recommended_movies_name[3])
#         st.image(recommended_movies_poster[3])

#     with col4:
#         st.text(recommended_movies_name[4])
#         st.image(recommended_movies_poster[4]) 

#     with col5:
#         st.text(recommended_movies_name[5])
#         st.image(recommended_movies_poster[5])           

import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=04d4076bd651ca66af7c59acca0e0824&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    # print(data)

    if "poster_path" in data and data["poster_path"]:
        full_path = "http://image.tmdb.org/t/p/w500" + data["poster_path"]
        print(full_path)

        return full_path
    else:
        return "https://via.placeholder.com/500x750.png?text=No+Image+Available"

def recommend(movie_name):
    if movie_name not in movies['title'].values:
        print(f"Movie '{movie_name}' not found in the dataset.")
        return [], []
    
    index = movies[movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]["movie_id"]  # ✅ Corrected line
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]]["title"])
    
    return recommended_movies_name, recommended_movies_poster


st.header("Movies Recommendation System using Machine Learning")

movies = pickle.load(open('artificats/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artificats/similarity.pkl', 'rb'))

movies_list = movies['title'].values
selected_movies = st.selectbox(
    'Type or select a movie to get recommendations',
    movies_list
)

if st.button('Show Recommendations'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movies)

    if recommended_movies_name:
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.text(recommended_movies_name[0])
            st.image(recommended_movies_poster[0])
        with col2:
            st.text(recommended_movies_name[1])
            st.image(recommended_movies_poster[1])
        with col3:
            st.text(recommended_movies_name[2])
            st.image(recommended_movies_poster[2])
        with col4:
            st.text(recommended_movies_name[3])
            st.image(recommended_movies_poster[3])
        with col5:
            st.text(recommended_movies_name[4])
            st.image(recommended_movies_poster[4])
