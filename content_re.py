#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:38:55 2020

@author: manyu dhyani
"""


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gtts import gTTS
from pygame import mixer
import time
###########
def msg():
    msg = "I found 50 related movies"
    language = "en"
    messagec = gTTS(text=msg, lang=language, slow=False)
    messagec.save("messagec.mp3")
    mixer.init()
    mixer.music.load("messagec.mp3")
    mixer.music.play()

###### helper functions. Use them when needed #######
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	try:
		return df[df.title == title]["index"].values[0] 
	except:
		return -1
##################################################

##Step 1: Read CSV File
df = pd.read_csv("movie_dataset.csv")

##Step 2: Select Features

features = ['keywords','cast','genres','director']
##Step 3: Create a column in DF which combines all selected features
for feature in features:
	df[feature] = df[feature].fillna('')
    
def combine_features(row):
	try:
		return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
	except:
		print ("Error:", row	)

df["combined_features"] = df.apply(combine_features,axis=1)

def content(movie_user_likes):

##Step 4: Create count matrix from this new combined column
	cv = CountVectorizer() 

	count_matrix = cv.fit_transform(df["combined_features"])

	##Step 5: Compute the Cosine Similarity based on the count_matrix
	cosine_sim = cosine_similarity(count_matrix) 
	

	## Step 6: Get index of this movie from its title
	movie_index = get_index_from_title(movie_user_likes)

	if movie_index == -1:
		print("no match found")
		return 

	similar_movies =  list(enumerate(cosine_sim[movie_index]))
	
	## Step 7: Get a list of similar movies in descending order of similarity score
	sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)

	## Step 8: Print titles of first 50 movies
	i=0
	for element in sorted_similar_movies:
			print (get_title_from_index(element[0]))
			i=i+1
			if i>50:
				msg()
				time.sleep(2.1)
				break

#content("Avatar")