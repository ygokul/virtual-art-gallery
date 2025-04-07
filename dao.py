import pymysql
from tabulate import tabulate
from exceptions import (
    ArtworkNotFoundException,
    FavoriteNotFoundException
)

class VirtualArtGalleryDAO:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
    def view_artworks(self):
        try:
            self.cursor.execute("SELECT * FROM artwork")
            rows = self.cursor.fetchall()
            if not rows:
                raise ArtworkNotFoundException("No artworks found.")
            
            print("\nArtworks:")
            for row in rows:
                print(f"Artwork ID: {row[0]}")
                print(f"Title: {row[1]}")
                print(f"Medium: {row[2]}")
                print(f"Artist ID: {row[3]}")
                print(f"Year: {row[4]}")
                print("-" * 30)  # Separator for better readability
        except pymysql.Error as e:
            print(f"Database Error: {e}")

    def add_artwork(self, title, medium, artist_id, year):
        try:
            query = "INSERT INTO artwork (Title, Medium, ArtistID, Year) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (title, medium, artist_id, year))
            self.conn.commit()
            print("Artwork added successfully!")
        except pymysql.Error as e:
            print(f"Error Adding Artwork: {e}")
    def update_artwork(self, artwork):
        try:
            query = "UPDATE artwork SET Title=%s, Medium=%s, ArtistID=%s, Year=%s WHERE ArtworkID=%s"
            self.cursor.execute(query, (artwork.title, artwork.medium, artwork.artist_id, artwork.year, artwork.artwork_id))
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
                raise ArtworkNotFoundException("Artwork ID not found.")
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
            
            print("\nArtwork Details:")
            print(f"Artwork ID: {artwork[0]}")
            print(f"Title: {artwork[1]}")
            print(f"Medium: {artwork[2]}")
            print(f"Artist ID: {artwork[3]}")
            print(f"Year: {artwork[4]}")
        except pymysql.Error as e:
            print(f"Error Fetching Artwork: {e}")

    def search_artworks(self, keyword):
        try:
            query = "SELECT * FROM artwork WHERE Title LIKE %s OR Medium LIKE %s"
            self.cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
            rows = self.cursor.fetchall()
            if not rows:
                raise ArtworkNotFoundException("No matching artworks found.")
            
            print("\nSearch Results:")
            for row in rows:
                print(f"Artwork ID: {row[0]}")
                print(f"Title: {row[1]}")
                print(f"Medium: {row[2]}")
                print(f"Artist ID: {row[3]}")
                print(f"Year: {row[4]}")
                print("-" * 30)
        except pymysql.Error as e:
            print(f"Error Searching Artworks: {e}")

    def add_artwork_to_favorite(self, user_id, artwork_id):
        try:
            query = "INSERT INTO favorites (UserID, ArtworkID) VALUES (%s, %s)"
            self.cursor.execute(query, (user_id, artwork_id))
            self.conn.commit()
            print("Artwork added to favorites!")
        except pymysql.Error as e:
            print(f"Error Adding to Favorites: {e}")

    def remove_artwork_from_favorite(self, user_id, artwork_id):
        try:
            query = "DELETE FROM favorites WHERE UserID = %s AND ArtworkID = %s"
            self.cursor.execute(query, (user_id, artwork_id))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                raise FavoriteNotFoundException("Favorite not found.")
            print("Artwork removed from favorites!")
        except pymysql.Error as e:
            print(f"Error Removing from Favorites: {e}")

    def get_user_favorite_artworks(self, user_id):
        try:
            query = ("SELECT a.ArtworkID, a.Title, a.Medium, a.ArtistID, a.Year "
                    "FROM artwork a JOIN favorites f ON a.ArtworkID = f.ArtworkID WHERE f.UserID = %s")
            self.cursor.execute(query, (user_id,))
            rows = self.cursor.fetchall()
            if not rows:
                raise FavoriteNotFoundException("No favorite artworks found.")
            
            print("\nUser's Favorite Artworks:")
            for row in rows:
                print(f"Artwork ID: {row[0]}")
                print(f"Title: {row[1]}")
                print(f"Medium: {row[2]}")
                print(f"Artist ID: {row[3]}")
                print(f"Year: {row[4]}")
                print("-" * 30)
        except pymysql.Error as e:
            print(f"Error Fetching Favorites: {e}")
    
    def add_artist(self, name, biography, birth_date, nationality, website, contact_info):
        try:
            query = """
                INSERT INTO Artist (Name, Biography, BirthDate, Nationality, Website, ContactInformation)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (name, biography, birth_date, nationality, website, contact_info))
            self.conn.commit()

            # Fetch the auto-generated ArtistID
            artist_id = self.cursor.lastrowid

            print("\nArtist added successfully!")
            print(f"Artist ID: {artist_id}")
            print(f"Name: {name}")
            print(f"Biography: {biography}")
            print(f"Birth Date: {birth_date}")
            print(f"Nationality: {nationality}")
            print(f"Website: {website}")
            print(f"Contact Information: {contact_info}")
        except pymysql.Error as e:
            print(f"Error Adding Artist: {e}")