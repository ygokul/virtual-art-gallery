from util.db_utils import DBConnection
from dao.implementation import VirtualArtGalleryDAO
from entity.artwork import Artwork
from entity.gallery import Gallery
from entity.userfavoriteartwork import UserFavoriteArtwork


def artwork_management_system(dao):
    while True:
        print("\nArtwork Management System")
        print("1. View Artworks")
        print("2. View Artists")
        print("3. Add Artwork")
        print("4. Search Artworks")
        print("5. Add Artwork to Favorites")
        print("6. View User's Favorite Artworks")
        print("7. View Your Artwork with ID")
        print("8. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            dao.view_artworks()
        elif choice == '2':
            dao.view_artists()
        elif choice == '3':
            title = input("Title: ")
            description = input("Description: ")
            medium = input("Medium: ")
            image_url = input("Image URL: ")
            dao.add_artwork(title, description, medium, image_url)
        elif choice == '4':
            keyword = input("Enter keyword to search in artwork titles: ")
            dao.search_artworks(keyword)
        elif choice == '5':
            dao.view_users2()
            user_id = int(input("Enter User ID: "))
            dao.view_artworks2()
            artwork_id = int(input("Enter Artwork ID: "))

            favorite = UserFavoriteArtwork()
            favorite.set_user_id(user_id)
            favorite.set_artwork_id(artwork_id)

            dao.add_artwork_to_favorite(favorite)
        elif choice == '6':
            dao.view_users2()
            user_id = int(input("Enter User ID to view favorite artworks: "))
            dao.get_user_favorite_artworks(user_id)
        elif choice == '7':
            dao.view_artworks2()
            artwork_id = int(input("Enter Artwork ID to view: "))
            dao.get_artwork_by_id(artwork_id)
        elif choice == '8':
            break
        else:
            print("Invalid choice, please try again.")


def gallery_management_system(dao):
    while True:
        print("\nGallery Management System")
        print("1. display all Galleries")
        print("2. Create Gallery")
        print("3. Update Gallery")
        print("4. Search Gallery by Name")
        print("5. view Gallery by ID")
        print("6. Remove Gallery")
        print("7. Gallery Artist Impact Report")
        print("8. Get Artworks From Gallery")
        print("9. Top Exhibited Artworks")
        print("10. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            dao.view_all_galleries()
        elif choice == '2':
            name = input("Enter Gallery Name: ")
            description = input("Enter Description: ")
            location = input("Enter Location: ")
            curator = input("Enter Curator ID (leave blank if none): ")
            opening_hours = input("Enter Opening Hours: ")
            curator = int(curator) if curator.strip() else None
            gallery = Gallery(None, name, description, location, curator, opening_hours)
            dao.add_gallery(gallery)
        elif choice == '3':
            gallery_id = int(input("Enter Gallery ID to update: "))
            name = input("Enter New Name: ")
            description = input("Enter New Description: ")
            location = input("Enter New Location: ")
            curator = input("Enter New Curator ID: ")
            opening_hours = input("Enter New Opening Hours: ")
            updated_gallery = Gallery(gallery_id, name, description, location, curator, opening_hours)
            dao.update_gallery(updated_gallery)
        elif choice == '4':
            keyword = input("Enter gallery name keyword to search: ")
            dao.search_gallery_by_name(keyword)
        elif choice == '5':
            dao.view_all_galleries2()
            gallery_id = input("Enter Gallery ID to view details: ")
            dao.search_gallery_by_id(gallery_id)
        elif choice == '6':
            gallery_id = input("Enter Gallery ID to remove: ")
            dao.remove_gallery(gallery_id)
        elif choice == '7':
            dao.gallery_artist_impact_report()
        elif choice == '8':
            dao.view_all_galleries2()
            gallery_id = int(input("Enter Gallery ID: "))
            dao.get_artworks_in_gallery(gallery_id)
        elif choice == '9':
            top_n = int(input("Enter how many top artworks you want to view: "))
            dao.get_top_exhibited_artworks(top_n)
        elif choice == '10':
            break
        else:
            print("Invalid choice, please try again.")


def mainlogin():
    conn = DBConnection.connect()
    dao = VirtualArtGalleryDAO(conn)

    while True:
        print("Welcome to the login page")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Please choose an option: ")

        if choice == "1":
            print("Moving to login page")
            print("1. Login as artist")
            print("2. Login as admin")
            user_type = input("Enter 1 for artist or 2 for admin: ")

            if user_type == "1":
                print("Logged in as artist")
                print("Choose the system to work in")
                print("1. Artwork Management System")
                print("2. Gallery Management System")
                system_choice = input("Enter 1 for artwork or 2 for gallery: ")

                if system_choice == "1":
                    artwork_management_system(dao)
                elif system_choice == "2":
                    gallery_management_system(dao)
                else:
                    print("Invalid choice, returning to login page.")

            elif user_type == "2":
                print("Logged in as admin")
                print("Choose the system to work in")
                print("1. Artwork Management System")
                print("2. Gallery Management System")
                system_choice = input("Enter 1 for artwork or 2 for gallery: ")

                if system_choice == "1":
                    artwork_management_system(dao)
                elif system_choice == "2":
                    gallery_management_system(dao)
                else:
                    print("Invalid choice, returning to login page.")
            else:
                print("Invalid user type, returning to login page.")

        elif choice == "2":
            print("Moving to register page")
            print("1. Create Account for artist")
            print("2. Create Account for user")
            if input("Enter 1 for artist or 2 for user: ") == "1":
                print("Creating account for artist")
                name = input("Name: ")
                biography = input("Biography: ")
                birth_date = input("Birth Date (YYYY-MM-DD): ")
                nationality = input("Nationality: ")
                website = input("Website: ")
                contact_info = input("Contact Information: ")
            
                # Call the DAO method to add the artist
                dao.add_artist(name, biography, birth_date, nationality, website, contact_info)
                print("Artist account created successfully!")
            else:
                print("Creating account for user")
                Username = input("Name: ")
                Password = input("enter password: ")
                Email = input("enter your email: ")
                FirstName = input("firstname: ")
                LastName = input("Lastname: ")
                DateOfBirth = input("Birth Date (YYYY-MM-DD): ")
                ProfilePicture = input("link for profile picture: ")

                dao.add_users(Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture)
                print("User account created successfully!")
        elif choice == "3":
            print("Exiting the login page. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

    conn.close()


if __name__ == "__main__":
    mainlogin()