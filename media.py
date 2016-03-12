import webbrowser

class Movie():
    
    def __init__(self,movie_title,movie_story_line,movie_image,movie_video):
        self.title=movie_title
        self.storyline=movie_story_line
        self.poster_image_url=movie_image
        self.trailer_youtube_url=movie_video

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
