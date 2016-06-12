# file that defines the Class (keep it here)

import webbrowser


class Movie():
    """ This class provides a way to store movie related information """ ## this is documentation creation we access to it "(media.Movie.__doc__)'
    
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    




#Class
#Instance
#Constructor
#self: points to the object
#variables
#instance variables: (title,storyline, poster_image_url,trailer_youtube_url)
#instance method
#class variables: VALID_RATINGS

    
