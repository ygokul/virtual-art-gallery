import pwinput
from util.db_utils import DBConnection
from dao.implementation import VirtualArtGalleryDAO
from entity.artwork import Artwork
from entity.gallery import Gallery
from entity.artist import Artist
from entity.userfavoriteartwork import UserFavoriteArtwork

def artist_logged_in(artist, dao):
    while True:
        print('1. View Artworks')
        print('2.search your artwork by keyword')
        print('3.create artwork')
        print('4.update artwork')
        print('5.remove artwork')
        print('6. View galleries with your artwork')
        print('7.gallery artist impact report')
        print('8. Logout')
        choice = input('Enter your choice: ')
        if choice == '1':
            dao.view_artworks(artist.get_artist_id())
        elif choice == '2':
            keyword = input("Enter keyword to search: ")
            dao.search_artwork_by_keyword(keyword)
        elif choice == '3':
            print("                 Create Artwork                   ")
            title = input("Title: ")
            description = input("Description: ")
            medium = input("Medium: ")
            image_url = input("Image URL: ")
            artwork = Artwork(None, title, description, None, medium, image_url)
            dao.add_artwork(artwork)
        elif choice == '4':
            print("                 Update Artwork                   ")
            dao.view_artworks(artist.get_artist_id())
            print("Select the artwork you want to update:")
            artwork_id = int(input("Enter Artwork ID to update: "))
            title = input("Enter New Title: ")
            description = input("Enter New Description: ")
            medium = input("Enter New Medium: ")
            year_created = input("Enter New Year Created: ")
            dimensions = input("Enter New Dimensions: ")
            price = float(input("Enter New Price: "))
            artist_id = artist.get_artist_id()
            updated_artwork = Artwork(artwork_id, title, description, medium, year_created, dimensions, price, artist_id)
            dao.update_artwork(updated_artwork)
        elif choice == '5':
            print("                 Remove Artwork                   ")
            dao.view_artworks(artist.get_artist_id())
            print("Select the artwork you want to remove:")
            artwork_id = int(input("Enter Artwork ID to remove: "))
            dao.remove_artwork(artwork_id)
        elif choice == '6':
            dao.view_galleries_with_your_artwork(artist.get_artist_id())
        elif choice == '7':
            dao.gallery_artist_impact_report(artist_id.get_artist_id())
        elif choice == '8':
            break
        else:
            print('Invalid option /n enter valid option')
        


def mainlogin():
    conn = DBConnection.connect()
    dao = VirtualArtGalleryDAO(conn)

    while True:
        print("\n=================================================")
        print("---------------Virtual Art Gallery---------------")
        print("1. Login as artist")
        print("2. Login as admin")
        print("3. Login as user")
        print("4. Exit")
        print("=================================================")
        print()
        print("Please select an option: ")
        choice = input("Enter your choice: ")
        print()
        if choice == '1':
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

        elif choice == '2':
            print('Admin login')
            password = input("Enter Admin Password: ")
            if password == 'admin123':
                print("Welcome back, Admin!")
                # view all users 
                # view all artworks
                # view all artists
                # view all galleries
                # create gallery
                # update gallery
                # remove gallery
            else:
                print("Invalid Admin Password.")
                continue
        elif choice == '3':
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

                   

        conn.close()


if __name__ == "__main__":
    mainlogin()