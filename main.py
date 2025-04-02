import mysql.connector
import sys
from tabulate import tabulate

# Database Connection Utility (Encapsulated in a Class)
class DBConnection:
    @staticmethod
    def connect():
        try:
            return mysql.connector.connect(
                user="root",
                password="root",
                host="127.0.0.1",
                database="virtualartgallery"
            )
        except mysql.connector.Error as e:
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

# DAO Class for Database Operations
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

            headers = [desc[0] for desc in self.cursor.description]
            formatted_rows = [[self.break_long_text(str(item)) if isinstance(item, str) else item for item in row] for row in rows]

            print("\nArtworks:\n")
            print(tabulate(formatted_rows, headers=headers, tablefmt="fancy_grid"))
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")

    def add_artist(self, artist):
        try:
            query = ("INSERT INTO artist (ArtistID, Name, Biography, BirthDate, Nationality, Website, ContactInformation) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            data = (artist.artist_id, artist.name, artist.biography, artist.birth_date, artist.nationality, artist.website, artist.contact_info)
            self.cursor.execute(query, data)
            self.conn.commit()
            print("Artist added successfully!")
        except mysql.connector.Error as e:
            print(f"Error Adding Artist: {e}")

    def update_gallery(self, gallery):
        try:
            query = ("UPDATE gallery SET Name = %s, Description = %s, Location = %s, Curator = %s, OpeningHours = %s "
                     "WHERE GalleryID = %s")
            data = (gallery.name, gallery.description, gallery.location, gallery.curator, gallery.opening_hours, gallery.gallery_id)
            self.cursor.execute(query, data)
            self.conn.commit()

            if self.cursor.rowcount == 0:
                raise GalleryNotFoundException("Gallery ID not found.")
            
            print("Gallery updated successfully!")
        except mysql.connector.Error as e:
            print(f"Error Updating Gallery: {e}")

    @staticmethod
    def break_long_text(text, word_limit=3):
        words = text.split()
        if len(words) > word_limit:
            return "\n".join([" ".join(words[i:i+word_limit]) for i in range(0, len(words), word_limit)])
        return text

# Menu-Driven Main Function
def main():
    conn = DBConnection.connect()
    dao = VirtualArtGalleryDAO(conn)

    while True:
        print("\nVirtual Art Gallery")
        print("1. View Artworks")
        print("2. Add Artist")
        print("3. Update Gallery Details")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            dao.view_artworks()
        elif choice == '2':
            artist = Artist(
                input("Enter Artist ID: "),
                input("Enter Name: "),
                input("Enter Biography: "),
                input("Enter Birth Date (YYYY-MM-DD): "),
                input("Enter Nationality: "),
                input("Enter Website: "),
                input("Enter Contact Information: ")
            )
            dao.add_artist(artist)
        elif choice == '3':
            gallery = Gallery(
                input("Enter Gallery ID: "),
                input("Enter Name: "),
                input("Enter Description: "),
                input("Enter Location: "),
                input("Enter Curator ID: "),
                input("Enter Opening Hours: ")
            )
            dao.update_gallery(gallery)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
