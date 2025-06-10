# Create a class to represent a Movie with attributes like title, director, and rating.

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def display_info(self):
        return f"🎬 Title: {self.title}\n🎬 Director: {self.director}\n⭐ Rating: {self.rating}/10"

# Create movie instances
movie1 = Movie("Inception", "Christopher Nolan", 8.8)
movie2 = Movie("The Shawshank Redemption", "Frank Darabont", 9.3)
movie3 = Movie("Pulp Fiction", "Quentin Tarantino", 8.9)

# Display movie information
print(movie1.display_info())
print()
print(movie2.display_info())
print()
print(movie3.display_info())
