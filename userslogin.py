from util.db_utils import DBConnection
from dao.implementation import VirtualArtGalleryDAO
from entity.artwork import Artwork
from entity.gallery import Gallery
from entity.artist import Artist
from entity.user import User
from entity.userfavoriteartwork import UserFavoriteArtwork


def artwork_management_system(dao):
    while True:
        print("\n=================================================")
        print("---------------Virtual Art Gallery---------------")
        print(":::::::::::::  Logged in as artist  :::::::::::::")
        print("            Artwork Management System           ")
        print("=================================================")
        print("1. View Artworks")
        print("2. View Artists")
        print("3. Search Artworks")
        print("4. Add Artwork to Favorites")
        print("5. View User's Favorite Artworks")
        print("6. View Your Artwork with ID")
        print("7. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            dao.view_artworks()
        elif choice == '2':
            dao.view_artists()
        elif choice == '3':
            keyword = input("Enter keyword to search in artwork titles: ")
            dao.search_artworks(keyword)
        elif choice == '4':
            dao.view_users2()
            user_id = int(input("Enter User ID: "))
            dao.view_artworks2()
            artwork_id = int(input("Enter Artwork ID: "))

            favorite = UserFavoriteArtwork()
            favorite.set_user_id(user_id)
            favorite.set_artwork_id(artwork_id)

            dao.add_artwork_to_favorite(favorite)
        elif choice == '5':
            dao.view_users2()
            user_id = int(input("Enter User ID to view favorite artworks: "))
            user_fav_artwork = UserFavoriteArtwork(user_id=user_id)
            dao.get_user_favorite_artworks(user_fav_artwork)
        elif choice == '6':
            dao.view_artworks2()
            artwork_id = int(input("Enter Artwork ID to view: "))
            dao.get_artwork_by_id(artwork_id)
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")


def artwork_management_system_admin(dao):
    while True:
        print("\n=================================================")
        print("---------------Virtual Art Gallery---------------")
        print(":::::::::::::  Logged in as Admin  :::::::::::::")
        print("            Artwork Management System            ")
        print("=================================================")
        print("1. Add Artwork")
        print("2. Remove Artwork")
        print("3. Update Artwork")
        print("4. Remove Artwork from Favorites")
        print("5. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Title: ")
            description = input("Description: ")
            medium = input("Medium: ")
            image_url = input("Image URL: ")
            artwork = Artwork(None, title, description, None, medium, image_url)
            dao.add_artwork(artwork)
        elif choice == '2':
            dao.view_artworks2()
            identifier = input("Enter Artwork ID or Title to remove: ")
            if identifier.isdigit():
                identifier = int(identifier)
            dao.remove_artwork(identifier)
        elif choice == '3':
            print("\n✏️ Update Artwork")
            artwork_id = int(input("Enter Artwork ID to update: "))
            title = input("Title: ")
            description = input("Description: ")
            medium = input("Medium: ")
            image_url = input("Image URL: ")
            artwork = Artwork(
                artwork_id=artwork_id,
                title=title,
                description=description,
                creation_date=None,
                medium=medium,
                image_url=image_url
            )
            dao.update_artwork(artwork)
        elif choice == '4':
            dao.view_artworks2()
            artwork_id = int(input("Enter Artwork ID to remove from favorites: "))
            print()
            favorite = UserFavoriteArtwork()
            favorite.set_artwork_id(artwork_id)
            dao.remove_artwork_from_favorite(favorite)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")


def gallery_management_system(dao):
    while True:
        print("\n=================================================")
        print("---------------Virtual Art Gallery---------------")
        print(":::::::::::::  Logged in as artist  :::::::::::::")
        print("            Gallery Management System            ")
        print("=================================================")
        print("1. Display all Galleries")
        print("2. Search Gallery by Name")
        print("3. View Gallery by ID")
        print("4. Gallery Artist Impact Report")
        print("5. View Artworks in a specific Gallery")
        print("6. View Galleries Displaying the Artwork")
        print("7. Top Exhibited Artworks")
        print("8. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            dao.view_all_galleries()
        elif choice == '2':
            keyword = input("Enter gallery name keyword to search: ")
            dao.search_gallery_by_name(keyword)
        elif choice == '3':
            dao.view_all_galleries2()
            gallery_id = input("Enter Gallery ID to view details: ")
            dao.search_gallery_by_id(gallery_id)
        elif choice == '4':
            dao.gallery_artist_impact_report()
        elif choice == '5':
            dao.view_all_galleries2()
            gallery_id = int(input("Enter Gallery ID: "))
            dao.get_artworks_in_gallery(gallery_id)
        elif choice == '6':
            print("\n🏛 View Galleries Displaying an Artwork")
            artwork_id = int(input("Enter Artwork ID: "))
            print()
            dao.get_galleries_for_artwork(artwork_id)
        elif choice == '7':
            top_n = int(input("Enter how many top artworks you want to view: "))
            dao.get_top_exhibited_artworks(top_n)
        elif choice == '8':
            break
        else:
            print("Invalid choice, please try again.")


def gallery_management_system_admin(dao):
    while True:
        print("\n=================================================")
        print("---------------Virtual Art Gallery---------------")
        print(":::::::::::::  Logged in as Admin  :::::::::::::")
        print("            Gallery Management System            ")
        print("=================================================")
        print("1. Create Gallery")
        print("2. Update Gallery")
        print("3. Remove Gallery")
        print("4. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("                 Create Gallery                   ")
            name = input("Enter Gallery Name: ")
            description = input("Enter Description: ")
            location = input("Enter Location: ")
            print("Available Artists:")
            dao.view_artists2()
            curator = input("Enter Curator ID (leave blank if none): ")
            opening_hours = input("Enter Opening Hours: ")
            curator = int(curator) if curator.strip() else None
            gallery = Gallery(None, name, description, location, curator, opening_hours)
            dao.add_gallery(gallery)
        elif choice == '2':
            print("                 Update Gallery                   ")
            dao.view_all_galleries2()
            gallery_id = int(input("Enter Gallery ID to update: "))
            name = input("Enter New Name: ")
            description = input("Enter New Description: ")
            location = input("Enter New Location: ")
            dao.view_artists2()
            curator = input("Enter New Curator ID: ")
            opening_hours = input("Enter New Opening Hours: ")
            updated_gallery = Gallery(gallery_id, name, description, location, curator, opening_hours)
            dao.update_gallery(updated_gallery)
        elif choice == '3':
            print("                 remove Gallery                   ")
            gallery_id = input("Enter Gallery ID to remove: ")
            dao.remove_gallery(gallery_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")


def mainlogin():
    conn = DBConnection.connect()
    dao = VirtualArtGalleryDAO(conn)

    while True:
        print("\n=================================================")
        print("---------------Virtual Art Gallery---------------")
        print("\n=================================================")
        print("welcome to  users dashboard")
        try:
            user_id = int(input("Enter UserID: "))
        except ValueError:
            print("Invalid UserID. Please enter a number.")
            continue

        user = dao.get_user_by_id(user_id)

        if user:
            print("User exists.")
            password = input("Enter your password: ")

            if password == user.get_password():
                print(f"Welcome back, {user.get_first_name()}!")
            else:
                print("Incorrect password.")
        else:
            print("User not found.")
            create = input("Would you like to create a new account? (yes/no): ").strip().lower()
            if create == 'yes':
                print("\nCreating account for user")
                Username = input("Username: ")
                Password = input("Enter password: ")
                Email = input("Enter your email: ")
                FirstName = input("Firstname: ")
                LastName = input("Lastname: ")
                DateOfBirth = input("Birth Date (YYYY-MM-DD): ")
                ProfilePicture = input("Link for profile picture: ")

                dao.add_users(Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture)
                print("User account created successfully!")

       

    # Make sure to close connection outside the loop
        conn.close()

if __name__ == "__main__":
    mainlogin()