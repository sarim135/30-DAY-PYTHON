# - Writing a Python script that asks the user to enter their favorite movies one by one and stores them in a list until they type 'stop', then prints the list
# Create an empty list to store movies
movies = []

# Ask the user to enter their favorite movies
while True:
    movie = input("Enter your favorite movie (type 'stop' to finish): ")
    if movie.lower() == 'stop':
        break
    movies.append(movie)

# Print the list of favorite movies
print("Your favorite movies are:")
for movie in movies:
    print(movie)
