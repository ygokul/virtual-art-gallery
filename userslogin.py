import pwinput
from util.db_utils import DBConnection
from dao.implementation import VirtualArtGalleryDAO
from entity.artwork import Artwork
from entity.gallery import Gallery
from entity.artist import Artist
from entity.user import User
from entity.userfavoriteartwork import UserFavoriteArtwork

def user_logged_in(user,dao):
    print(f"Welcome, {user.get_first_name()}! You're now logged in.")

    while True:
        print("\n1. View all artworks")
        print("2. Add artwork to favorites")
        print("3. Checking- A user can have many favorite artworks")
        print("4. Checking -an artwork can be a favorite of multiple users")
        print("5. Remove artwork from favorites")
        print("6. Top Exhibited Artworks")
        print("7. Search Artworks by titles")
        print("8. Search Galleries by id")
        print("9. An artwork can be displayed in multiple galleries")
        print("10. A gallery can have multiple artworks.")
        print("11. logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            dao.view_artworks()
        elif choice == '2':
            dao.view_artworks2()
            artwork_id = int(input("Enter Artwork ID: "))
            favorite = UserFavoriteArtwork()
            favorite.set_user_id(user.get_user_id())
            favorite.set_artwork_id(artwork_id)
            dao.add_artwork_to_favorite(favorite)
        elif choice == '3':
            fav = UserFavoriteArtwork(user_id=user.get_user_id())
            dao.get_user_favorite_artworks(fav)
        elif choice == '4':
            artwork_id = int(input("Enter Artwork ID: "))
            fav = UserFavoriteArtwork(artwork_id=artwork_id)
            dao.get_artwork_favorited_by_users(fav.get_artwork_id())  # Extract artwork_id

        elif choice == '5':
            artwork_id = int(input("Enter Artwork ID to remove: "))
            favorite = UserFavoriteArtwork()
            favorite.set_user_id(user.get_user_id())
            favorite.set_artwork_id(artwork_id)
            dao.remove_artwork_from_favorite(favorite)
        elif choice == '6':
            top_n = int(input("Enter how many top artworks you want to view: "))
            dao.get_top_exhibited_artworks(top_n)
        elif choice == '7':
            keyword = input("Enter keyword to search in artwork titles: ")
            dao.search_artworks(keyword)
        elif choice == '8':
            dao.view_all_galleries2()
            gallery_id = input("Enter Gallery ID to view details: ")
            dao.search_gallery_by_id(gallery_id)
        elif choice == '10':
            dao.view_all_galleries2()
            gallery_id = int(input("Enter Gallery ID: "))
            dao.get_artworks_in_gallery(gallery_id)
        elif choice == '9':
            print("\n🏛 View Galleries Displaying an Artwork")
            artwork_id = int(input("Enter Artwork ID: "))
            dao.get_galleries_for_artwork(artwork_id)
        elif choice == '11':
            print("Logged out.")
            break
        else:
            print("Invalid choice.")
def admin_logged_in(dao):
    while True:
        print("1. View Galleries")
        print("2. Create Gallery")
        print("3. Update Gallery")
        print("4. Remove Gallery")
        print("5. View Artworks")
        print("6. View Artists")
        print("7. View Users")
        print("8. Logout")

        choice = input("Enter Your Choice: ")
        if choice == '1':
            dao.view_all_galleries()

        elif choice == '2':
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

        elif choice == '3':
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

        elif choice == '4':
            print("                 remove Gallery                   ")
            gallery_id = input("Enter Gallery ID to remove: ")
            dao.remove_gallery(gallery_id)

        elif choice == '5':
            dao.view_artworks()

        elif choice == '6':
            dao.view_artists()

        elif choice == '7':
            dao.view_users()

        elif choice == '8':
            break

        else:
            print("Invalid option,enter valid one")
def artist_logged_in(artist, dao):
    while True:
        print('1.View Artworks -- Checking(Many-one)')
        print('2.search artwork by keyword')
        print('3.create artwork')
        print('4.update artwork')
        print('5.remove artwork')
        print('6.gallery artist impact report')
        print("7.An artist can be associated with multiple galleries")
        print("8.A gallery can have only one curator (artist)")
        print('9. Logout')
        choice = input('Enter your choice: ')
        if choice == '1':
            dao.view_artworks(artist.get_artist_id())
        elif choice == '2':
            keyword = input("Enter keyword to search in artwork titles: ")
            dao.search_artworks(keyword)
        elif choice == '3':
            print("                 Create Artwork                   ")
            title = input("Title: ")
            description = input("Description: ")
            medium = input("Medium: ")
            image_url = input("Image URL: ")
            artist_id = artist.get_artist_id()
            artwork = Artwork(None, title, description, None, medium, image_url)
            dao.add_artwork(artwork,artist_id)
        elif choice == '4':
            print("                 Update Artwork                   ")
            dao.view_artworks(artist.get_artist_id())
            artist_id = artist.get_artist_id()

            artwork_id = int(input("Enter Artwork ID to update: "))
            title = input("New Title: ")
            description = input("New Description: ")
            medium = input("New Medium: ")
            image_url = input("New Image URL: ")

            artwork = Artwork(artwork_id, title, description, None, medium, image_url)
            dao.update_artwork(artwork, artist_id)
        elif choice == '5':
            print("                 Remove Artwork                   ")
            dao.view_artworks(artist.get_artist_id())
            artwork_id = int(input("Enter the Artwork ID to remove: "))
            artist_id = artist.get_artist_id()
            dao.remove_artwork(artwork_id, artist_id)

        elif choice == '6':
            artist_id = artist.get_artist_id()
            dao.gallery_artist_impact_report(artist_id)

        elif choice == '7':
            artist_id = int(input("Enter Artist ID to find all galleries: "))
            dao.get_galleries_by_curator(artist_id)
            print()
        elif choice == '8':
            gallery_id = int(input("Enter Gallery ID to find curator: "))
            print()
            dao.get_curator_by_gallery(gallery_id)
        elif choice == '9':
            break
        else:
            print('Invalid option /n enter valid option')
        
        

 
def mainlogin():
    conn = DBConnection.connect()
    dao = VirtualArtGalleryDAO(conn)
    try:
        while True:
            print("\n=================================================")
            print("---------------Virtual Art Gallery---------------")
            print("\n=================================================")
            print("1. user login")
            print("2. admin login")
            print("3. artist login")
            print("4. exit")
            choice=input("enter ur choice: ")
            if choice == '1':
                print("Welcome to User's dashboard ")
                try:
                    user_id = int(input("Enter UserID: "))
                except ValueError:
                    print("Invalid UserID. Please enter a number.")
                    continue

                user = dao.get_user_by_id(user_id)

                if user:
                    print("User exists.")
                    password = pwinput.pwinput(prompt="Enter password: ", mask="*")

                    if password == user.get_password():
                        user_logged_in(user,dao)
                    else:
                        print("Incorrect password.")

                else:
                    print("User not found.")
                    create = input("Would you like to create a new account? (yes/no): ").strip().lower()
                    if create == 'yes':
                        print("\nCreating account for user")
                        Username = input("Username: ")
                        Password = pwinput.pwinput(prompt="Enter password: ", mask="*")
                        Email = input("Enter your email: ")
                        FirstName = input("Firstname: ")
                        LastName = input("Lastname: ")
                        DateOfBirth = input("Birth Date (YYYY-MM-DD): ")
                        ProfilePicture = input("Link for profile picture: ")

                        dao.add_users(Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture)
                        print("User account created successfully!")

                        # Get the newly created user and log them in
                        user = dao.get_user_by_username(Username)
                        if user:
                            user_logged_in(user,dao)
            elif choice == '2':
                print("  Welcome to admin's dashboard ")
                while True:
                    password = pwinput.pwinput(prompt="Enter password: ", mask="*")
                    if password == 'admin@123':
                        admin_logged_in(dao)
                        break  # Successful login
                    else:
                        print("Invalid Password.")
                        retry = input("Do you want to try again? (yes/no): ").strip().lower()
                        if retry != 'yes':
                            print("Exiting admin login.")
                            break
            elif choice == '3':
                print("  Welcome to artist's dashboard ")
                try:
                    artist_id = int(input("Enter Artist ID: "))
                except ValueError:
                    print("Invalid Artist ID. Please enter a number.")
                    continue

                artist = dao.get_artist_by_id(artist_id)

                if artist:
                    print("Artist exists.")
                    password = pwinput.pwinput(prompt="Enter password: ", mask="*")

                    if password == f"{artist.get_name()}@123":
                        print(f"Welcome, {artist.get_name()}! You're now logged in.")
                        # Add artist-specific functionality here
                        artist_logged_in(artist, dao)
                    else:
                        print("Incorrect password.")

                else:
                    print("Artist not found.")
                    create = input("Would you like to create a new account? (yes/no): ").strip().lower()
                    if create == 'yes':
                        name = input("Name: ")
                        biography = input("Biography: ")
                        birth_date = input("Birth Date (YYYY-MM-DD): ")
                        nationality = input("Nationality: ")
                        website = input("Website: ")
                        contact_info = input("Contact Information: ")
                        artist = Artist(None, name, biography, birth_date, nationality, website, contact_info)
                        dao.add_artist(artist)
                        print("Artist account created successfully!")
                        if artist:
                            print(f"Welcome, {artist.get_name()}! You're now logged in.")
                            # Add artist-specific functionality here
                            artist_logged_in(artist, dao)
            elif choice == '4':
                break
            else:
                print("enter valid option")
    finally:
        conn.close()


       

    # Make sure to close connection outside the loop


if __name__ == "__main__":
    mainlogin()