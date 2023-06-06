class Film:
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"Title: {self.title}, Director: {self.director}, Year: {self.year}, Genre: {self.genre}"
