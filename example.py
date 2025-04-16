from util.db_utils import DBConnection
from dao.implementation import VirtualArtGalleryDAO
from entity.artwork import Artwork
from entity.gallery import Gallery
from entity.artist import Artist
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
        print("8. get multiple galleries by artistid/curator ")
        print("9. get artistid/curator associated with gallery")
        print("10. Back to main menu")

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
            artist_id = int(input("Enter Artist ID to find all galleries: "))
            dao.get_galleries_by_curator(artist_id)
            print()
        elif choice == '9':
            gallery_id = int(input("Enter Gallery ID to find curator: "))
            print()
            dao.get_curator_by_gallery(gallery_id)
           
        elif choice == '10':
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
        print("Welcome to the landing page")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Please choose an option: ")

        if choice == "1":
            while True:
                print("\n=================================================")
                print("---------------Virtual Art Gallery---------------")
                print("Moving to login page")
                print("1. Login as artist")
                print("2. Login as admin")
                print("3. Back to main menu")
                
                user_type = input("Enter your choice: ")
                
                if user_type == "1":
                    while True:
                        print("\n=================================================")
                        print("---------------Virtual Art Gallery---------------")
                        print(":::::::::::::  Logged in as artist  :::::::::::::")
                        print("Choose the system to work")
                        print("1. Artwork Management System")
                        print("2. Gallery Management System")
                        print("3. Back to previous menu")
                        
                        system_choice = input("Enter your choice: ")
                        
                        if system_choice == "1":
                            artwork_management_system(dao)
                        elif system_choice == "2":
                            gallery_management_system(dao)
                        elif system_choice == "3":
                            break
                        else:
                            print("Invalid choice, please try again.")
                
                elif user_type == "2":
                    while True:
                        print("\n=================================================")
                        print("---------------Virtual Art Gallery---------------")
                        print(":::::::::::::  Logged in as Admin  ::::::::::::::")
                        print("Choose the system to work")
                        print("1. Artwork Management System")
                        print("2. Gallery Management System")
                        print("3. Back to previous menu")
                        
                        system_choice = input("Enter your choice: ")
                        
                        if system_choice == "1":
                            artwork_management_system_admin(dao)
                        elif system_choice == "2":
                            gallery_management_system_admin(dao)
                        elif system_choice == "3":
                            break
                        else:
                            print("Invalid choice, please try again.")
                
                elif user_type == "3":
                    break
                else:
                    print("Invalid choice, please try again.")
        
        elif choice == "2":
            print("\n=================================================")
            print("Moving to register page")
            print("1. Create Account for artist")
            print("2. Create Account for user")
            print("3. Back to main menu")
            
            register_choice = input("Enter your choice: ")
            
            if register_choice == "1":
                print("\nCreating account for artist")
                name = input("Name: ")
                biography = input("Biography: ")
                birth_date = input("Birth Date (YYYY-MM-DD): ")
                nationality = input("Nationality: ")
                website = input("Website: ")
                contact_info = input("Contact Information: ")
                artist = Artist(None, name, biography, birth_date, nationality, website, contact_info)
                dao.add_artist(artist)
                print("Artist account created successfully!")
            
            elif register_choice == "2":
                print("\nCreating account for user")
                Username = input("Name: ")
                Password = input("Enter password: ")
                Email = input("Enter your email: ")
                FirstName = input("Firstname: ")
                LastName = input("Lastname: ")
                DateOfBirth = input("Birth Date (YYYY-MM-DD): ")
                ProfilePicture = input("Link for profile picture: ")
                dao.add_users(Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture)
                print("User account created successfully!")
            
            elif register_choice == "3":
                continue
            else:
                print("Invalid choice, returning to main menu.")
        
        elif choice == "3":
            print("Exiting the Virtual Art Gallery. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

    conn.close()


if __name__ == "__main__":
    mainlogin()