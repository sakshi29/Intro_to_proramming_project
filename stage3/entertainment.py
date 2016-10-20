# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 11:43:11 2016

@author: SAKSHI TRIPATHI
"""
import fresh_tomatoes
import movies

toy_story=movies.Movie("Toy Story",
                       "Story of a boy whose toy come to life",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

a_walk_to_remember=movies.Movie("A Walk To Remember",
                                 "Landon Carter gets in trouble and has to do community service- including getting involved in the spring play. He then falls in love with Jamie Sulivan, the daughter of the town's minister",
                                 "https://upload.wikimedia.org/wikipedia/en/d/dc/A_Walk_to_Remember_Poster.jpg",
                                 "https://www.youtube.com/watch?v=i72wRvPw_ik")

iron_man=movies.Movie("Iron Men",
                      "An American billionaire playboy, business magnate, and ingenious engineer, Tony Stark suffers a severe chest injury during a kidnapping in which his captors attempt to force him to build a weapon of mass destruction. He instead creates a powered suit of armor to save his life and escape captivity.",
                      "https://upload.wikimedia.org/wikipedia/en/e/e0/Iron_Man_bleeding_edge.jpg",
                      "https://www.youtube.com/watch?v=8hYlB38asDY")

dhoni=movies.Movie("M.S. Dhoni: The Untold Story",
                   "M.S. Dhoni: The Untold Story is a 2016 Indian biographical sports film written and directed by Neeraj Pandey. It based on the life of Indian cricketer MS DHONI",
                   "https://upload.wikimedia.org/wikipedia/en/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg",
                   "https://www.youtube.com/watch?v=6L6XqWoS8tw")

znmd=movies.Movie("Zindagi Na Milegi Dobara",
                  "Imran and Arjun take a vacation in Spain before Kabir's marriage. The trip turns into an opportunity to mend fences, heal wounds, fall in love with life and combat their worst fears.",
                  "https://upload.wikimedia.org/wikipedia/en/3/3d/Zindaginamilegidobara.jpg",
                  "https://www.youtube.com/watch?v=lAuJoq6zeIQ")

mary_kom=movies.Movie("Mary Kom ", 
                      "Mary Kom, is an Indian boxer hailing from the Kom tribe in Manipur.When Mary Kom encounters a renowned coach in a boxing gym, she shares her boxing aspirations with him and convinces him to teach her. Despite her father's disapproval, she follows her passion",
                      "https://upload.wikimedia.org/wikipedia/en/c/c8/MaryKomPoster.jpg",
                      "https://www.youtube.com/watch?v=OxsKcx1IwI8")
#list of movies
movies=[toy_story,a_walk_to_remember,iron_man,dhoni,znmd,mary_kom]
# Uses list of movie instances as input to generate an HTML file
# and open it in the browser.
fresh_tomatoes.open_movies_page(movies)