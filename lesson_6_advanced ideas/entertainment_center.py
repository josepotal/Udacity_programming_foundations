#file to use my new class 'Movie'
# 'media' is the file name where I created the class Movie

import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://ecx.images-amazon.com/images/I/51NpxQ0ma8L.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print toy_story.storyline

avatar = media.Movie ("Avatar",
                      "A marine in an alien planet",
                      "http://img.goldposter.com/2015/05/Avatar_poster_goldposter_com_10.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print avatar.storyline

#avatar.show_trailer()


inside_out = media.Movie("Insie_Out",
                         "Feelings explained",
                         "http://screenrant.com/wp-content/uploads/inside-out-poster.jpg",
                         "https://www.youtube.com/watch?v=7ZLOYXKmIkw")

moneyball = media.Movie("Moneyball",
                        "Stadistics applied to baseball",
                        "http://cdn.collider.com/wp-content/uploads/moneyball-poster.jpg",
                        "https://www.youtube.com/watch?v=-4QPVo0UIzc")
#moneyball.show_trailer()


the_martian = media.Movie("The_Martian",
                          "An astronaust alone in Mars",
                          "http://vignette1.wikia.nocookie.net/the-martian/images/5/52/The_Martian_poster_3.jpg/revision/latest?cb=20150923000824",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

movies=[toy_story, avatar, inside_out, moneyball, the_martian]

#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.valid_ratings)

print(media.Movie.__doc__)

print(media.Movie.__name__)

print ("The module of this class is " + media.Movie.__module__)
