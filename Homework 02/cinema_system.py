from film import Film


class CinemaSystem:
    def __init__(self):
        self.film_database = []

    def add_film(self):
        title = input("Enter the film title: ")
        director = input("Enter the director's name: ")
        year = input("Enter the release year: ")
        genre = input("Enter the genre: ")

        film = Film(title, director, year, genre)
        self.film_database.append(film)
        print("Film added successfully.")

    def search_film(self):
        title = input("Enter the film title to search: ")
        found_films = []

        for film in self.film_database:
            if film.title.lower() == title.lower():
                found_films.append(film)

        if len(found_films) > 0:
            print("Search results:")
            for film in found_films:
                print(film)
        else:
            print("The film you searched for could not be found.")

    def delete_film(self):
        title = input("Enter the film title to delete: ")
        deleted_count = 0

        for film in self.film_database:
            if film.title.lower() == title.lower():
                self.film_database.remove(film)
                deleted_count += 1

        if deleted_count > 0:
            print(f"{deleted_count} film(s) deleted.")
        else:
            print("The film to delete could not be found.")
