from movies import add_movie, show_movies, delete_movie
from halls import add_hall, show_halls



while True:
    print("1. Add Movie")
    print("2. Show Movies")
    print("3. Delete Movie")
    print("4. Add Hall")
    print("5. Show Halls")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_movie(movies)
    elif choice == "2":
        show_movies(movies)
    elif choice == "3":
        delete_movie(movies)
    elif choice == "4":
        add_hall(halls)
    elif choice == "5":
        show_halls(halls)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")