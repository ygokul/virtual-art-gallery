from db_utils import DBConnection
from dao import VirtualArtGalleryDAO
from entities import Artist, Artwork

def main():
    conn = DBConnection.connect()
    dao = VirtualArtGalleryDAO(conn)

    while True:
        print("\nVirtual Art Gallery")
        print("1. View Artworks")
        print("2. Add Artwork")
        print("3. Update Artwork")
        print("4. Remove Artwork")
        print("5. Search Artworks")
        print("6. Add Artwork to Favorites")
        print("7. Remove Artwork from Favorites")
        print("8. View User's Favorite Artworks")
        print("9. Add Artist")  # New option for adding an artist
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            dao.view_artworks()
        elif choice == '2':
            title = input("Title: ")
            medium = input("Medium: ")
            artist_id = input("Artist ID: ")
            year = input("Year: ")
            dao.add_artwork(title, medium, artist_id, year)       
        elif choice == '3':
            dao.update_artwork(Artwork(input("ID: "), input("Title: "), input("Medium: "), input("Artist ID: "), input("Year: ")))
        elif choice == '4':
            dao.remove_artwork(input("Artwork ID: "))
        elif choice == '5':
            dao.search_artworks(input("Enter keyword: "))
        elif choice == '6':
            dao.add_artwork_to_favorite(input("User ID: "), input("Artwork ID: "))
        elif choice == '7':
            dao.remove_artwork_from_favorite(input("User ID: "), input("Artwork ID: "))
        elif choice == '8':
            dao.get_user_favorite_artworks(input("User ID: "))
        elif choice == '9':  # Add artist functionality
            name = input("Name: ")
            biography = input("Biography: ")
            birth_date = input("Birth Date (YYYY-MM-DD): ")
            nationality = input("Nationality: ")
            website = input("Website: ")
            contact_info = input("Contact Information: ")
            dao.add_artist(name, biography, birth_date, nationality, website, contact_info)
        
        elif choice == '10':
            break

    conn.close()

if __name__ == "__main__":
    main()