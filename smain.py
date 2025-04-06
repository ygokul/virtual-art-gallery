import pymysql
import sys
from tabulate import tabulate
# created by sara
# Database Connection Utility
class DBConnection:
    @staticmethod
    def connect():
        try:
            return pymysql.connect(
                user="root",
                password="root",
                host="127.0.0.1",
                database="virtualartgallery",
                port=3306
            )
        except pymysql.Error as e:
            print(f"Database Connection Error: {e}")
            sys.exit(1)

# Custom Exception Classes
class ArtGalleryException(Exception):
    pass

class ArtworkNotFoundException(ArtGalleryException):
    pass

class ArtistNotFoundException(ArtGalleryException):
    pass

class GalleryNotFoundException(ArtGalleryException):
    pass

class FavoriteNotFoundException(ArtGalleryException):
    pass

# Entity Classes
class Artist:
    def __init__(self, artist_id, name, biography, birth_date, nationality, website, contact_info):
        self.artist_id = artist_id
        self.name = name
        self.biography = biography
        self.birth_date = birth_date
        self.nationality = nationality
        self.website = website
        self.contact_info = contact_info

class Gallery:
    def __init__(self, gallery_id, name, description, location, curator, opening_hours):
        self.gallery_id = gallery_id
        self.name = name
        self.description = description
        self.location = location
        self.curator = curator
        self.opening_hours = opening_hours

class Artwork:
    def __init__(self, artwork_id, title, description, creation_date, medium, image_url):
        self.artwork_id = artwork_id
        self.title = title
        self.description = description
        self.creation_date = creation_date
        self.medium = medium
        self.image_url = image_url

class User:
    def __init__(self, user_id, username, password, email, first_name, last_name, date_of_birth, profile_picture, favorite_artwork):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.profile_picture = profile_picture
        self.favorite_artwork = favorite_artwork

class UserFavoriteArtwork:
    def __init__(self, user_id, artwork_id):
        self.user_id = user_id
        self.artwork_id = artwork_id

class ArtworkGallery:
    def __init__(self, artwork_id, gallery_id):
        self.artwork_id = artwork_id
        self.gallery_id = gallery_id





# DAO Class for Database Operations
class VirtualArtGalleryDAO:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    # View Artworks
    def view_artworks(self):
        try:
            self.cursor.execute("SELECT * FROM artwork")
            rows = self.cursor.fetchall()
            if not rows:
                raise ArtworkNotFoundException("No artworks found.")
            headers = [desc[0] for desc in self.cursor.description]
            print("\nArtworks:\n")
            print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
        except pymysql.Error as e:
            print(f"Database Error: {e}")

    # Artwork Management
    def add_artwork(self, artwork):
        try:
            query = """INSERT INTO artwork (Title, Description, CreationDate, Medium, ImageURL) 
                    VALUES (%s, %s, %s, %s, %s)"""
            self.cursor.execute(query, (artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url))
            self.conn.commit()
            print("Artwork added successfully!")
        except pymysql.Error as e:
            print(f"Error Adding Artwork: {e}")


    def update_artwork(self, artwork):
        try:
            query = """UPDATE artwork 
                    SET Title=%s, Description=%s, CreationDate=%s, Medium=%s, ImageURL=%s 
                    WHERE ArtworkID=%s"""
            self.cursor.execute(query, (artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url, artwork.artwork_id))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                raise ArtworkNotFoundException("Artwork ID not found.")
            print("Artwork updated successfully!")
        except pymysql.Error as e:
            print(f"Error Updating Artwork: {e}")

    def remove_artwork(self, artwork_id):
        try:
            query = "DELETE FROM artwork WHERE ArtworkID=%s"
            self.cursor.execute(query, (artwork_id,))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                raise ArtworkNotFoundException(f"Artwork with ID {artwork_id} not found.")
            print("Artwork removed successfully!")
        except pymysql.Error as e:
            print(f"Error Removing Artwork: {e}")

    def get_artwork_by_id(self, artwork_id):
        try:
            query = "SELECT * FROM artwork WHERE ArtworkID=%s"
            self.cursor.execute(query, (artwork_id,))
            artwork = self.cursor.fetchone()
            if not artwork:
                raise ArtworkNotFoundException("Artwork not found.")
            print("\nArtwork Details:\n", artwork)
        except pymysql.Error as e:
            print(f"Error Fetching Artwork: {e}")

    def search_artworks(self, keyword):
        try:
            query = "SELECT * FROM artwork WHERE Title LIKE %s OR Medium LIKE %s"
            self.cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
            rows = self.cursor.fetchall()
            if not rows:
                raise ArtworkNotFoundException("No matching artworks found.")
            print("\nSearch Results:\n")
            print(tabulate(rows, tablefmt="fancy_grid"))
        except pymysql.Error as e:
            print(f"Error Searching Artworks: {e}")

    # User Favorites
    def add_artwork_to_favorite(self, user_id, artwork_id):
        try:
            query = "INSERT INTO user_favorite_artwork (UserID, ArtworkID) VALUES (%s, %s)"
            self.cursor.execute(query, (user_id, artwork_id))
            self.conn.commit()
            print("Artwork added to favorites!")
        except pymysql.Error as e:
            print(f"Error Adding to Favorites: {e}")

    def remove_artwork_from_favorite(self, user_id,artwork_id):
        try:
            query = "DELETE FROM user_favorite_artwork WHERE UserId=%s and ArtworkID = %s"
            self.cursor.execute(query, (user_id,artwork_id))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                raise FavoriteNotFoundException("Favorite not found.")
            print("Artwork removed from favorites!")
        except pymysql.Error as e:
            print(f"Error Removing from Favorites: {e}")

    def get_user_favorite_artworks(self, user_id):
        try:
            query = ("SELECT a.ArtworkID, a.Title FROM artwork a "
                     "JOIN favorites f ON a.ArtworkID = f.ArtworkID WHERE f.UserID = %s")
            self.cursor.execute(query, (user_id,))
            rows = self.cursor.fetchall()
            if not rows:
                raise FavoriteNotFoundException("No favorite artworks found.")
            print("\nUser's Favorite Artworks:\n")
            print(tabulate(rows, tablefmt="fancy_grid"))
        except pymysql.Error as e:
            print(f"Error Fetching Favorites: {e}")

# Main Function
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
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            dao.view_artworks()
        elif choice == '2': 
            dao.add_artwork(Artwork(None, input("Title: "), input("Description: "), input("Creation Date (YYYY-MM-DD): "), input("Medium: "), input("Image URL: ")))
        elif choice == '3': 
            dao.update_artwork(Artwork(input("ID: "), input("Title: "), input("Description: "), input("Creation Date (YYYY-MM-DD): "), input("Medium: "), input("Image URL: ")))

        elif choice == '4': dao.remove_artwork(input("Enter Artwork ID to remove: "))

        elif choice == '5':
            dao.search_artworks(input("Enter keyword for title: "))
        elif choice == '6':
            dao.add_artwork_to_favorite(input("User ID: "), input("Artwork ID: "))
        elif choice == '7':
            dao.remove_artwork_from_favorite(input("User ID: "), input("Artwork ID: "))
        elif choice == '8':
            dao.get_user_favorite_artworks(input("User ID: "))
        elif choice == '9':
            break

    conn.close()

if __name__ == "__main__":
    main()
