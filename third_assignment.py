def add_movie(movies, title, rank):
    return movies + [{'title': title, 'rank': rank}]

def display_movies(movies):
    for movie in movies:
        print(f"Title: {movie['title']}, Rank: {movie['rank']}")

def search_movie(movies, title):
    return list(filter(lambda movie: movie['title'].lower() == title.lower(), movies))

def remove_movie(movies, title):
    return list(filter(lambda movie: movie['title'] != title, movies))

def switch_menu():
    movies = []

    while True:
        print("\nThird assignment/ Movie management:")
        print("1. Add a movie")
        print("2. Display all movies")
        print("3. Search for a movie")
        print("4. Remove a movie")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter the movie title: ")
            rank = float(input("Enter the movie rank: "))
            movies = add_movie(movies, title, rank)
            print("Movie added successfully!")
        elif choice == '2':
            print("\nAll Movies:")
            display_movies(movies)
        elif choice == '3':
            search_title = input("Enter the movie title to search: ")
            result = search_movie(movies, search_title)
            print("\nSearch Result:", result)
        elif choice == '4':
            remove_title = input("Enter the movie title to remove: ")
            movies = remove_movie(movies, remove_title)
            print("Movie removed successfully!")
        elif choice == '5':
            print("Exit!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
