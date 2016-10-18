# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 11:40:21 2016

@author: SAKSHI TRIPATHI
"""
import webbrowser

class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,movie_trailer_youtube_url):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=movie_trailer_youtube_url
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)