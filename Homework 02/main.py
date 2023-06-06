from cinema_system import CinemaSystem

cinema = CinemaSystem()

menu = """
Cinema System

1. Add Film
2. Search Film
3. Delete Film
4. Exit
"""

while True:
    print(menu)
    choice = input("Enter an option (1-4): ")

    if choice == '1':
        cinema.add_film()
    elif choice == '2':
        cinema.search_film()
    elif choice == '3':
        cinema.delete_film()
    elif choice == '4':
        print("Exiting the Cinema System...")
        break
    else:
        print("Invalid option. Please try again.")
