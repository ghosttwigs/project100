class MovieReview :
    def __init__(self , movie , story , actors , music):
        self.movieName = movie
        self.storyRating = story
        self.actorRating = actors
        self.musicRating = music

        self.average = (self.storyRating + self.actorRating + self.musicRating)/3

    def showAverage(self):
        print("The average ratings : " , self.average)


m1 = MovieReview("Young Sheldon" , 4 , 5 , 2)
m1.showAverage()








