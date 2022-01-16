#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:43:12 2020

@author: pankajdhyani
"""


import pandas as pd
from scipy import sparse
from gtts import gTTS
from pygame import mixer
import time

###########
def msg():
    msg = "I found 20 related movies"
    language = "en"
    messagecb = gTTS(text=msg, lang=language, slow=False)
    messagecb.save("messagecb.mp3")
    mixer.init()
    mixer.music.load("messagecb.mp3")
    mixer.music.play()
##########
ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")
ratings = pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)


userRatings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
userRatings.head()

userRatings = userRatings.dropna(thresh=10, axis=1).fillna(0,axis=1)
#userRatings.fillna(0, inplace=True)

corrMatrix = userRatings.corr(method='pearson')
corrMatrix.head(100)


def get_similar(movie_name,rating):
    similar_ratings = corrMatrix[movie_name]*(rating-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    #print(type(similar_ratings))
    return similar_ratings

#romantic_lover = [("(500) Days of Summer (2009)",5),("Alice in Wonderland (2010)",3),("Aliens (1986)",1),("2001: A Space Odyssey (1968)",2)]
def collaborate(movie,rating):
	print(movie, rating)
	similar = [(movie,rating)]
	similar_movies = pd.DataFrame()
	for movie,rating in similar:
	    similar_movies = similar_movies.append(get_similar(movie,rating),ignore_index = True)

	print(similar_movies.sum().sort_values(ascending=False).head(20)) if len(similar_movies) else print("No Match found") 
	msg()
	time.sleep(2.2)
#collaborate("No Strings Attached ",5)