# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 11:40:21 2016

@author: SAKSHI TRIPATHI
"""
import webbrowser

class Movie():
    """The class Movie defines the attribute and behaviour of a movie.
    Attributes:
       title
       story
       poster
       trailer
    Instance Method:
       show_trailer()
    """
    def __init__(self,movie_title,movie_storyline,poster_image,movie_trailer_youtube_url):
        """__init__ initailizes or creates space in memory for every object. To remember title,storyline,poster,youtube_link."""
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=movie_trailer_youtube_url
        
    def show_trailer(self):
        """show trailer takes the current object as input and opens the youtube link on web browser."""
        webbrowser.open(self.trailer_youtube_url)
     
   