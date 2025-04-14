def mainlogin():
    while (input != "exit"):
        print("Welcome to the login page")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Please choose an option: ")

        if choice == "1":
            print("moving to login page")
            print("1. Login as artist")
            print("2. Login as admin")
            if input("Enter 1 for artist or 2 for admin: ") == "1":
                print(f"Logged in as artist")
                print("choose the sytem to work in")
                print("1. artwork management system")
                print("2. gallery management system")
                if input("Enter 1 for artwork or 2 for gallery: ") == "1":
                    print("moving to artwork management system")
                    print("Please enter your choice")
                    print("1. View Artworks")
                    print("3. Search Artworks")
                    print("4. Add Artwork to Favorites")
                    print("5. View User's Favorite Artworks")
                    print("6. View Your Artwork with ID")
                    print("7. back to main menu")
                else:
                    print("moving to gallery management system")
                    print("Please enter your choice")
                    print("1. View Galleries")
                    print("3. Search Gallery by name")
                    print("3. Search Gallery by id")
                    print("4. Gallery Artist Impact Report")
                    print("5. Get Artworks From Gallery")
                    print("6. Get Artworks From Gallery")
                    print("6. Top Exhibited Artworks")
                    print("7. back to main menu")

            else:
                print(f"Logged in as admin")
                print("choose the sytem to work in")
                print("1. artwork management system")
                print("2. gallery management system")
                if input("Enter 1 for artwork or 2 for gallery: ") == "1":
                    print("moving to artwork management system")
                    print("Please enter your choice")
                    print("2. Add Artwork")
                    print("4. Update Artwork")
                    print("5. Remove Artwork")
                    print("7. back to main menu")
                else:
                    print("moving to gallery management system")
                    print("Please enter your choice")
                    print("2. Create Gallery")
                    print("3. Update Gallery")
                    print("6. Remove gallery")
                    print("7. back to main menu")
            
        elif choice == "2":
            print("moving to register page")
            print("1. Create Account for artist")
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")
mainlogin()
