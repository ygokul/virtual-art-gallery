import pymysql
from dao.interface import Interface
from tabulate import tabulate
from datetime import datetime
from entity.artwork import Artwork
from entity.artist import Artist
from entity.gallery import Gallery
from entity.user import User
from entity.userfavoriteartwork import UserFavoriteArtwork
from exception.exceptions import (
    ArtworkNotFoundException,
    FavoriteNotFoundException,
    UserNotFoundException,
    GalleryNotAddedException,
    GalleryNotFoundException,
    ArtistNotFoundException
)

class VirtualArtGalleryDAO(Interface):
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()


    def view_artworks(self, artist_id=None):
        try:
            if artist_id is not None:
                # Fetch only the artworks by the specified artist
                self.cursor.execute("SELECT * FROM artwork WHERE artist_id = %s", (artist_id,))
            else:
                # Fetch all artworks (if no artist_id is provided)
                self.cursor.execute("SELECT * FROM artwork")
                
            rows = self.cursor.fetchall()
            if not rows:
                raise ArtworkNotFoundException("No artworks found.")
            
            print("\nArtworks:")
            for row in rows:
                print(f"Artwork ID: {row[0]}")
                print(f"Title: {row[1]}")
                print(f"Description: {row[2]}")
                print(f"Creation Date: {row[3]}")
                print(f"Medium: {row[4]}")
                print(f"Image URL: {row[5]}")
                print("-" * 30)  # Separator for better readability
                
        except pymysql.Error as e:
            print(f"Database Error: {e}")
        except ArtworkNotFoundException as e:
            print(f"Error: {e}")


    def view_artworks2(self):
        try:
            self.cursor.execute("SELECT * FROM artwork")
            rows = self.cursor.fetchall()
            if not rows:
                raise ArtworkNotFoundException("No artworks found.")
            print()
            print("\nArtworks:")
            for row in rows:
                print(f"Artwork ID: {row[0]}")
                print(f"Title: {row[1]}")
                print("-" * 30)  # Separator for better readability
        except pymysql.Error as e:
            print(f"Database Error: {e}")

    
    def view_artists(self):
        try:
            self.cursor.execute("SELECT * FROM artist")
            rows = self.cursor.fetchall()
            if not rows:
                raise ArtistNotFoundException("No artists found.")
            print()
            print("\nArtists:")
            for row in rows:
                print(f"Artist ID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Biography: {row[2]}")
                print(f"Birth date: {row[3]}")
                print(f"Nationality: {row[4]}")
                print(f"Website: {row[5]}")
                print(f"contactinformation: {row[6]}")
                print("-" * 30)  # Separator for better readability
        except pymysql.Error as e:
            print(f"Database Error: {e}")

    def view_artists2(self):
        try:
            self.cursor.execute("SELECT * FROM artist")
            rows = self.cursor.fetchall()
            if not rows:
                raise ArtistNotFoundException("No artists found.")
            print()
            print("\nArtists:")
            for row in rows:
                print(f"Artist ID: {row[0]}")
                print(f"Name: {row[1]}")
                print("-" * 30)  # Separator for better readability
        except pymysql.Error as e:
            print(f"Database Error: {e}")
            
    def view_users2(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            rows = self.cursor.fetchall()
            if not rows:
                raise ArtistNotFoundException("No artists found.")
            print()
            print("\nUsers:")
            for row in rows:
                print(f"User ID: {row[0]}")
                print(f"Name: {row[1]}")
                print("-" * 30)  # Separator for better readability
        except pymysql.Error as e:
            print(f"Database Error: {e}")


    def view_users(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            rows = self.cursor.fetchall()
            if not rows:
                raise ArtistNotFoundException("No artists found.")
            print()
            print("\nUsers:")
            for row in rows:
                print(f"User ID         : {row[0]}")
                print(f"Username        : {row[1]}")
                print(f"Password        : {row[2]}")
                print(f"Email           : {row[3]}")
                print(f"First Name      : {row[4]}")
                print(f"Last Name       : {row[5]}")
                print(f"Date of Birth   : {row[6]}")
                print(f"Profile Picture : {row[7]}")
                print(f"Favorite Artwork: {row[8]}")
                print("-" * 40)  # Separator for better readability
        except pymysql.Error as e:
            print(f"Database Error: {e}")



    def add_artwork(self, artwork: Artwork):
        try:
            creation_date = datetime.now().strftime('%Y-%m-%d')
            artwork.set_creation_date(creation_date)

            query = """
                INSERT INTO artwork (Title, Description, CreationDate, Medium, ImageURL)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (
                artwork.get_title(),
                artwork.get_description(),
                artwork.get_creation_date(),
                artwork.get_medium(),
                artwork.get_image_url()
            ))
            self.conn.commit()

            print("\n✅ Artwork added successfully!")

            self.cursor.execute("SELECT * FROM artwork WHERE ArtworkID = LAST_INSERT_ID()")
            inserted_artwork = self.cursor.fetchone()

            if inserted_artwork:
                artwork.set_artwork_id(inserted_artwork[0])
                artwork.set_title(inserted_artwork[1])
                artwork.set_description(inserted_artwork[2])
                artwork.set_creation_date(inserted_artwork[3])
                artwork.set_medium(inserted_artwork[4])
                artwork.set_image_url(inserted_artwork[5])

                print("\n🎨 Inserted Artwork:")
                print("-" * 40)
                print(f"Artwork ID    : {artwork.get_artwork_id()}")
                print(f"Title         : {artwork.get_title()}")
                print(f"Description   : {artwork.get_description()}")
                print(f"Creation Date : {artwork.get_creation_date()}")
                print(f"Medium        : {artwork.get_medium()}")
                print(f"Image URL     : {artwork.get_image_url()}")
                print("-" * 40)

        except pymysql.Error as e:
            print(f"❌ Error Adding Artwork: {e}")


    def update_artwork(self, artwork):
        try:
            creation_date = datetime.now().strftime('%Y-%m-%d')

            query = """
                UPDATE artwork 
                SET Title=%s, Description=%s, CreationDate=%s, Medium=%s, ImageURL=%s 
                WHERE ArtworkID=%s
            """
            self.cursor.execute(query, (
                artwork.get_title(),
                artwork.get_description(),
                creation_date,
                artwork.get_medium(),
                artwork.get_image_url(),
                artwork.get_artwork_id()
            ))
            self.conn.commit()

            if self.cursor.rowcount == 0:
                raise ArtworkNotFoundException(f"🎨 Artwork with ID {artwork.get_artwork_id()} not found for update.")

            print("\n✅ Artwork updated successfully!")

            # Display updated artwork
            self.cursor.execute("SELECT * FROM artwork WHERE ArtworkID = %s", (artwork.get_artwork_id(),))
            updated_artwork = self.cursor.fetchone()

            if updated_artwork:
                artwork_id, title, description, creation_date, medium, image_url = updated_artwork
                print("\n--- 🎨 Updated Artwork ---")
                print(f"🆔 Artwork ID    : {artwork_id}")
                print(f"🖌️  Title         : {title}")
                print(f"📝 Description   : {description}")
                print(f"📅 Creation Date : {creation_date}")
                print(f"🎨 Medium        : {medium}")
                print(f"🌐 Image URL     : {image_url}")
                print("-" * 40)

        except ArtworkNotFoundException as e:
            print(f"❌ {e}")

        except pymysql.Error as e:
            print(f"❌ Error Updating Artwork: {e}")

    def remove_artwork(self, identifier):
        try:
            query = "DELETE FROM artwork WHERE ArtworkID = %s OR Title = %s"
            self.cursor.execute(query, (identifier, str(identifier)))
            self.conn.commit()

            if self.cursor.rowcount == 0:
                raise ArtworkNotFoundException(f"🎨 Artwork with ID or Title '{identifier}' not found.")

            print()
            print("✅ Artwork removed successfully!")
            print("🚀 We're always evolving! Feel free to add your next masterpiece anytime.")
            print("🎭 Visit us again for more artistic inspiration!")

        except ArtworkNotFoundException as e:
            print(f"❌ {e}")

        except pymysql.Error as e:
            print(f"❌ Error Removing Artwork: {e}")

    def get_artwork_by_id(self, artwork_id):
        try:
            query = "SELECT * FROM artwork WHERE ArtworkID = %s"
            self.cursor.execute(query, (artwork_id,))
            row = self.cursor.fetchone()

            if not row:
                raise ArtworkNotFoundException("Artwork not found.")

            # Create Artwork object
            artwork = Artwork(
                artwork_id=row[0],
                title=row[1],
                description=row[2],
                creation_date=row[3],
                medium=row[4],   # Fixed: was using creation_date (row[3]) again
                image_url=row[5]
            )

            # Print details with separator
            print("\n" + "-"*40)
            print("🎨 Artwork Details")
            print("-"*40)
            print(f"Artwork ID  : {artwork.get_artwork_id()}")
            print(f"Title       : {artwork.get_title()}")
            print(f"Description : {artwork.get_description()}")
            print(f"Medium      : {artwork.get_medium()}")
            print(f"Image URL   : {artwork.get_image_url()}")
            print("-"*40 + "\n")

            return artwork

        except ArtworkNotFoundException as e:
            print(f"Error: {e}")
            return None

        except pymysql.Error as e:
            print(f"Database Error: {e}")
            return None



    def search_artworks(self, keyword):
        try:
            query = "SELECT * FROM artwork WHERE Title LIKE %s"
            self.cursor.execute(query, (f"%{keyword}%",))

            rows = self.cursor.fetchall()

            if not rows:
                raise ArtworkNotFoundException("No matching artworks found.")

            print("\n🔍 Search Results:")
            print("-" * 40)
            for row in rows:
                artwork = Artwork(
                    artwork_id=row[0],
                    title=row[1],
                    description=row[2],
                    creation_date=None,
                    medium=row[3],
                    image_url=row[4]
                )
                print(f"Artwork ID  : {artwork.get_artwork_id()}")
                print(f"Title       : {artwork.get_title()}")
                print(f"Description : {artwork.get_description()}")
                print(f"Medium      : {artwork.get_medium()}")
                print(f"Image URL   : {artwork.get_image_url()}")
                print("-" * 40)

        except ArtworkNotFoundException as e:
            print(f"⚠️  {e}")

        except pymysql.Error as e:
            print(f"❌ Database Error: {e}")



    def add_artwork_to_favorite(self, favorite: UserFavoriteArtwork):
        try:
            user_id = favorite.get_user_id()
            artwork_id = favorite.get_artwork_id()

            # 1. Check if user exists
            check_user_query = "SELECT 1 FROM users WHERE UserID = %s"
            self.cursor.execute(check_user_query, (user_id,))
            if not self.cursor.fetchone():
                raise UserNotFoundException("User not found")

            # 2. Check if artwork exists
            check_artwork_query = "SELECT 1 FROM artwork WHERE ArtworkID = %s"
            self.cursor.execute(check_artwork_query, (artwork_id,))
            if not self.cursor.fetchone():
                raise ArtworkNotFoundException("Artwork not found")

            # 3. Insert into user_favorite_artwork table
            query = "INSERT INTO user_favorite_artwork (UserID, ArtworkID) VALUES (%s, %s)"
            self.cursor.execute(query, (user_id, artwork_id))
            self.conn.commit()
            print()
            print(f"🔔 Favorited! Artwork [{artwork_id}] is now saved for User [{user_id}].")

        except UserNotFoundException as e:
            print(f"User Error: {e}")
        except ArtworkNotFoundException as e:
            print(f"Artwork Error: {e}")
        except pymysql.IntegrityError:
            print("This favorite already exists.")
        except pymysql.Error as e:
            print(f"Database Error: {e}")


    def remove_artwork_from_favorite(self, favorite: UserFavoriteArtwork):
        try:
            artwork_id = favorite.get_artwork_id()

            query = "DELETE FROM user_favorite_artwork WHERE ArtworkID = %s"
            self.cursor.execute(query, (artwork_id,))
            self.conn.commit()

            if self.cursor.rowcount == 0:
                raise FavoriteNotFoundException("Favorite not found.")

            print(f"💔 Farewell, Artwork #{artwork_id} — you've been unfavorited with style.")

        except FavoriteNotFoundException as e:
            print(f"⚠️ {e}")

        except pymysql.Error as e:
            print(f"❌ Error Removing from Favorites: {e}")

    def get_user_favorite_artworks(self, user_fav_artwork):
        try:
            query = """
                SELECT a.ArtworkID, a.Title, a.Description, a.CreationDate, a.Medium, a.ImageURL
                FROM artwork a
                JOIN user_favorite_artwork ufa ON a.ArtworkID = ufa.ArtworkID
                WHERE ufa.UserID = %s
            """
            self.cursor.execute(query, (user_fav_artwork.get_user_id(),))
            rows = self.cursor.fetchall()

            if not rows:
                raise FavoriteNotFoundException("No favorite artworks found.")

            print("\n🎨 User's Favorite Artworks:")
            for row in rows:
                print(f"🆔 Artwork ID    : {row[0]}")
                print(f"🖌️  Title         : {row[1]}")
                print(f"📝 Description   : {row[2]}")
                print(f"📅 Created On    : {row[3]}")
                print(f"🎨 Medium        : {row[4]}")
                print(f"🖼️  Image URL     : {row[5]}")
                print("-" * 40)

        except FavoriteNotFoundException as e:
            print(f"⚠️ {e}")

        except pymysql.Error as e:
            print(f"❌ Error Fetching Favorites: {e}")


    def add_artist(self, artist):
        try:
            query = """
                INSERT INTO artist (Name, Biography, BirthDate, Nationality, Website, ContactInformation)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (
                artist.get_name(),
                artist.get_biography(),
                artist.get_birth_date(),
                artist.get_nationality(),
                artist.get_website(),
                artist.get_contact_info()
            ))
            self.conn.commit()

            # Fetch the auto-generated ArtistID
            artist_id = self.cursor.lastrowid
            artist.set_artist_id(artist_id)

            print("\n✅ Artist added successfully!")
            print(f"🎨 Artist ID         : {artist.get_artist_id()}")
            print(f"👤 Name              : {artist.get_name()}")
            print(f"📖 Biography         : {artist.get_biography()}")
            print(f"🎂 Birth Date        : {artist.get_birth_date()}")
            print(f"🌍 Nationality       : {artist.get_nationality()}")
            print(f"🔗 Website           : {artist.get_website()}")
            print(f"📞 Contact Info      : {artist.get_contact_info()}")

        except pymysql.Error as e:
            print(f"❌ Error Adding Artist: {e}")

            
    def add_users(self, Username, Password, Email, FirstName, LastName, DateOfBirth,ProfilePicture):
        try:
            query = """
                INSERT INTO users (Username, Password, Email, FirstName, LastName, DateOfBirth,ProfilePicture)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (Username, Password, Email, FirstName, LastName, DateOfBirth,ProfilePicture))
            self.conn.commit()

            # Fetch the auto-generated UserID
            user_id = self.cursor.lastrowid

            print("\nUser added successfully!")
            print(f"User ID: {user_id}")
            print(f"Name: {Username}")
        except pymysql.Error as e:
            print(f"Error Adding User: {e}")


    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE UserID = %s", (user_id,))
        result = self.cursor.fetchone()
        if result:
            return User(
                result[0],  # UserID
                result[1],  # Username
                result[2],  # Password
                result[3],  # Email
                result[4],  # FirstName
                result[5],  # LastName
                result[6],  # DateOfBirth
                result[7],  # ProfilePicture
                result[8] if len(result) > 8 else None  # FavoriteArtwork (optional)
            )
        return None
    
    def get_user_by_username(self, username):
        query = "SELECT * FROM users WHERE Username = %s"
        self.cursor.execute(query, (username,))
        row = self.cursor.fetchone()
        if row:
            return User(*row)  # Adjust depending on your User class constructor
        return None

   
    def get_artist_by_id(self, artist_id):
        self.cursor.execute("SELECT * FROM artist WHERE ArtistID = %s", (artist_id,))
        result = self.cursor.fetchone()
        if result:
            return Artist(
                result[0],  # ArtistID
                result[1],  # Name
                result[2],  # Biography
                result[3],  # BirthDate
                result[4],  # Nationality
                result[5],  # Website
                result[6]   # ContactInformation
            )
        return None


    
    def add_gallery(self, gallery: Gallery):
        try:
            # Check if Curator (Artist) exists
            check_query = "SELECT * FROM artist WHERE ArtistID = %s"
            self.cursor.execute(check_query, (gallery.get_curator(),))
            result = self.cursor.fetchone()

            if not result:
                raise ArtistNotFoundException(f"❌ Curator with ID {gallery.get_curator()} not found.")

            # Insert gallery if curator exists
            query = """
                INSERT INTO gallery (Name, Description, Location, Curator, OpeningHours)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (
                gallery.get_name(),
                gallery.get_description(),
                gallery.get_location(),
                gallery.get_curator(),
                gallery.get_opening_hours()
            ))
            self.conn.commit()

            gallery_id = self.cursor.lastrowid
            print("\n🏛️ Gallery Successfully Added!")
            print("=" * 40)
            print(f"🎨 Gallery ID     : {gallery_id}")
            print(f"🖼️  Name           : {gallery.get_name()}")
            print(f"📝 Description    : {gallery.get_description()}")
            print(f"📍 Location       : {gallery.get_location()}")
            print(f"👤 Curator ID     : {gallery.get_curator()}")
            print(f"⏰ Opening Hours  : {gallery.get_opening_hours()}")
            print("=" * 40 + "\n")

        except ArtistNotFoundException as e:
            print(e)

        except pymysql.Error as e:
            raise GalleryNotAddedException(f"❌ Error Adding Gallery: {e}")

    
    def update_gallery(self, gallery: Gallery):
        try:
            # Check if the gallery exists
            self.cursor.execute("SELECT 1 FROM gallery WHERE GalleryID = %s", (gallery.get_gallery_id(),))
            if not self.cursor.fetchone():
                raise GalleryNotFoundException(f"Gallery with ID {gallery.get_gallery_id()} not found.")

            # Check if the curator (artist) exists
            self.cursor.execute("SELECT 1 FROM artist WHERE ArtistID = %s", (gallery.get_curator(),))
            if not self.cursor.fetchone():
                raise ArtistNotFoundException(f"Curator with ID {gallery.get_curator()} not found.")

            # Perform the update
            query = """
                UPDATE gallery
                SET Name = %s, Description = %s, Location = %s, Curator = %s, OpeningHours = %s
                WHERE GalleryID = %s
            """
            self.cursor.execute(query, (
                gallery.get_name(),
                gallery.get_description(),
                gallery.get_location(),
                gallery.get_curator(),
                gallery.get_opening_hours(),
                gallery.get_gallery_id()
            ))
            self.conn.commit()
            print(f"\n✅ Gallery ID {gallery.get_gallery_id()} has been successfully updated!\n")

            # Display the updated gallery
            self.cursor.execute("SELECT * FROM gallery WHERE GalleryID = %s", (gallery.get_gallery_id(),))
            updated = self.cursor.fetchone()

            if updated:
                print("🎨 Updated Gallery Details:")
                print("=" * 50)
                print(f"Gallery ID     : {updated[0]}")
                print(f"Name           : {updated[1]}")
                print(f"Description    : {updated[2]}")
                print(f"Location       : {updated[3]}")
                print(f"Curator ID     : {updated[4]}")
                print(f"Opening Hours  : {updated[5]}")
                print("=" * 50)

        except GalleryNotFoundException as e:
            print(f"🚫 {e}")
        except ArtistNotFoundException as e:
            print(f"🚫 {e}")
        except pymysql.Error as e:
            print(f"❌ Database Error: {e}")

    def search_gallery_by_name(self, name_keyword):
        try:
            query = "SELECT * FROM gallery WHERE Name LIKE %s"
            self.cursor.execute(query, ('%' + name_keyword + '%',))
            results = self.cursor.fetchall()

            if not results:
                raise GalleryNotFoundException(f"No galleries found matching name: '{name_keyword}'.")

            print(f"\n🔍 Search Results for '{name_keyword}':")
            print("=" * 60)

            for result in results:
                # Create Gallery object
                gallery = Gallery(
                    result[0],  # GalleryID
                    result[1],  # Name
                    result[2],  # Description
                    result[3],  # Location
                    result[4],  # Curator
                    result[5]   # OpeningHours
                )

                print(f"🏛️ Gallery ID     : {gallery.get_gallery_id()}")
                print(f"📛 Name           : {gallery.get_name()}")
                print(f"📝 Description    : {gallery.get_description()}")
                print(f"📍 Location       : {gallery.get_location()}")
                print(f"👤 Curator ID     : {gallery.get_curator()}")
                print(f"🕒 Opening Hours  : {gallery.get_opening_hours()}")
                print("-" * 60)

        except GalleryNotFoundException as e:
            print(f"🚫 {e}")
        except pymysql.Error as e:
            print(f"❌ Database Error: {e}")


    def view_all_galleries(self):
        try:
            query = "SELECT * FROM gallery"
            self.cursor.execute(query)
            results = self.cursor.fetchall()

            if not results:
                raise GalleryNotFoundException("No galleries found in the database.")

            print("\n🖼️ All Galleries:")
            print("=" * 60)

            for result in results:
                gallery = Gallery(
                    result[0],  # GalleryID
                    result[1],  # Name
                    result[2],  # Description
                    result[3],  # Location
                    result[4],  # Curator
                    result[5]   # OpeningHours
                )

                print(f"🏛️ Gallery ID     : {gallery.get_gallery_id()}")
                print(f"📛 Name           : {gallery.get_name()}")
                print(f"📝 Description    : {gallery.get_description()}")
                print(f"📍 Location       : {gallery.get_location()}")
                print(f"👤 Curator ID     : {gallery.get_curator()}")
                print(f"🕒 Opening Hours  : {gallery.get_opening_hours()}")
                print("-" * 60)

        except GalleryNotFoundException as e:
            print(f"🚫 {e}")
        except pymysql.Error as e:
            print(f"❌ Database Error: {e}")
    def view_all_galleries2(self):
        try:
            query = "SELECT * FROM gallery"
            self.cursor.execute(query)
            results = self.cursor.fetchall()

            if not results:
                raise GalleryNotFoundException("No galleries found in the database.")

            print("\n🖼️ All Galleries:")
            print("=" * 60)

            for result in results:
                gallery = Gallery(
                    result[0],  # GalleryID
                    result[1],  # Name
                    result[2],  # Description
                    result[3],  # Location
                    result[4],  # Curator
                    result[5]   # OpeningHours
                )

                print(f"🏛️ Gallery ID     : {gallery.get_gallery_id()}")
                print(f"📛 Name           : {gallery.get_name()}")
                print("-" * 60)

        except GalleryNotFoundException as e:
            print(f"🚫 {e}")
        except pymysql.Error as e:
            print(f"❌ Database Error: {e}")
    
    def search_gallery_by_id(self, gallery_id):
        try:
            query = "SELECT * FROM gallery WHERE GalleryID = %s"
            self.cursor.execute(query, (gallery_id,))
            result = self.cursor.fetchone()

            if not result:
                raise GalleryNotFoundException(f"Gallery with ID {gallery_id} not found.")

            # Create Gallery object
            gallery = Gallery(
                result[0],  # GalleryID
                result[1],  # Name
                result[2],  # Description
                result[3],  # Location
                result[4],  # Curator
                result[5]   # OpeningHours
            )

            print("\n🔎 Gallery Details:")
            print("=" * 60)
            print(f"🏛️ Gallery ID     : {gallery.get_gallery_id()}")
            print(f"📛 Name           : {gallery.get_name()}")
            print(f"📝 Description    : {gallery.get_description()}")
            print(f"📍 Location       : {gallery.get_location()}")
            print(f"👤 Curator ID     : {gallery.get_curator()}")
            print(f"🕒 Opening Hours  : {gallery.get_opening_hours()}")
            print("-" * 60)

        except GalleryNotFoundException as e:
            print(f"🚫 {e}")
        except pymysql.Error as e:
            print(f"❌ Database Error: {e}")

    def remove_gallery(self, gallery_id):
        try:
            # Check if gallery exists
            self.cursor.execute("SELECT * FROM gallery WHERE GalleryID = %s", (gallery_id,))
            result = self.cursor.fetchone()
            if not result:
                raise GalleryNotFoundException(f"Gallery with ID {gallery_id} not found.")

            # Delete gallery
            query = "DELETE FROM gallery WHERE GalleryID = %s"
            self.cursor.execute(query, (gallery_id,))
            self.conn.commit()

            print(f"🗑️ Gallery with ID {gallery_id} has been successfully removed.\n")

        except GalleryNotFoundException as e:
            print(f"🚫 {e}")
        except pymysql.Error as e:
            print(f"❌ Database Error while removing gallery: {e}")
    

    def gallery_artist_impact_report(self):
        try:
            query = """
                SELECT ar.ArtistID, ar.Name, COUNT(g.GalleryID) AS TotalGalleriesCurated
                FROM artist ar
                LEFT JOIN gallery g ON ar.ArtistID = g.Curator
                GROUP BY ar.ArtistID, ar.Name
                ORDER BY TotalGalleriesCurated DESC
            """
            self.cursor.execute(query)
            rows = self.cursor.fetchall()

            print("\n🎨 Gallery Artist Impact Report 🎨")
            print("-" * 40)
            for row in rows:
                print(f"Artist ID   : {row[0]}")
                print(f"Name        : {row[1]}")
                print(f"Galleries   : {row[2]}")
                print("-" * 40)

        except pymysql.Error as e:
            print(f"❌ Error generating report: {e}")

  
  

    def get_artworks_in_gallery(self, gallery_id):
        try:
            query = """
                SELECT a.ArtworkID, a.Title, a.Description, a.CreationDate, a.Medium, a.ImageURL
                FROM artwork a
                JOIN artwork_gallery ag ON a.ArtworkID = ag.ArtworkID
                WHERE ag.GalleryID = %s
            """
            self.cursor.execute(query, (gallery_id,))
            rows = self.cursor.fetchall()

            if not rows:
                raise ArtworkNotFoundException(f"🎨 No artworks found in Gallery ID {gallery_id}.")

            print(f"\n🖼️ Artworks in Gallery ID {gallery_id}:")
            for row in rows:
                artwork = Artwork(
                    artwork_id=row[0],
                    title=row[1],
                    description=row[2],
                    creation_date=row[3],
                    medium=row[4],
                    image_url=row[5]
                )

                print(f"Artwork ID: {artwork.get_artwork_id()}")
                print(f"Title: {artwork.get_title()}")
                print(f"Description: {artwork.get_description()}")
                print(f"Created On: {artwork.get_creation_date()}")
                print(f"Medium: {artwork.get_medium()}")
                print(f"Image URL: {artwork.get_image_url()}")
                print("-" * 30)

        except ArtworkNotFoundException as e:
            print(e)

        except pymysql.Error as e:
            print(f"❌ Error fetching artworks: {e}")

    def get_galleries_for_artwork(self, artwork_id):
        try:
            query = """
                SELECT g.GalleryID, g.Name, g.Description, g.Location, g.Curator, g.OpeningHours
                FROM gallery g
                JOIN artwork_gallery ag ON g.GalleryID = ag.GalleryID
                WHERE ag.ArtworkID = %s
            """
            self.cursor.execute(query, (artwork_id,))
            rows = self.cursor.fetchall()

            if not rows:
                raise GalleryNotFoundException(f"🏛 No galleries found for Artwork ID {artwork_id}.")

            print(f"\n🏢 Galleries for Artwork ID {artwork_id}:")
            for row in rows:
                gallery = Gallery(*row)
                print(f"Gallery ID: {gallery.get_gallery_id()}")
                print(f"Name: {gallery.get_name()}")
                print(f"Location: {gallery.get_location()}")
                print(f"Curator ID: {gallery.get_curator()}")
                print(f"Opening Hours: {gallery.get_opening_hours()}")
                print("-" * 30)

        except GalleryNotFoundException as e:
            print(e)

        except pymysql.Error as e:
            print(f"❌ Database error: {e}")

    def get_top_exhibited_artworks(self, top_n):
        try:
            query = """
                SELECT a.ArtworkID, a.Title, COUNT(ag.GalleryID) as gallery_count
                FROM artwork a
                JOIN artwork_gallery ag ON a.ArtworkID = ag.ArtworkID
                GROUP BY a.ArtworkID, a.Title
                ORDER BY gallery_count DESC
                LIMIT %s
            """
            self.cursor.execute(query, (top_n,))
            rows = self.cursor.fetchall()

            if not rows:
                raise ArtworkNotFoundException("📉 No artwork exhibition data available.")

            print(f"\n🏆 Top {top_n} Most Exhibited Artworks:")
            for row in rows:
                print(f"Artwork ID: {row[0]}, Title: {row[1]}, Exhibited in {row[2]} galleries")

        except ArtworkNotFoundException as e:
            print(e)

        except pymysql.Error as e:
            print(f"❌ Database error: {e}")


    
    def get_galleries_by_curator(self, artist_id: int):
        try:
            query = "SELECT GalleryID, Name, Description, Location, Curator, OpeningHours FROM gallery WHERE Curator = %s"
            self.cursor.execute(query, (artist_id,))
            rows = self.cursor.fetchall()

            if not rows:
                raise ArtistNotFoundException(f"No galleries found for Artist ID [{artist_id}].")

            galleries = [Gallery(*row) for row in rows]

            print(f"\n🖼 Galleries curated by Artist [{artist_id}]:")
            for g in galleries:
                print(f" - Gallery ID: {g.get_gallery_id()}, Name: {g.get_name()}")
            print(f"\nTotal Galleries: {len(galleries)}")

            return galleries

        except ArtistNotFoundException as e:
            print(e)
            return []

        except Exception as e:
            print(f"Error fetching galleries: {e}")
            return []

    def get_curator_by_gallery(self, gallery_id: int):
        try:
            query = "SELECT Curator FROM gallery WHERE GalleryID = %s"
            self.cursor.execute(query, (gallery_id,))
            result = self.cursor.fetchone()

            if not result:
                raise GalleryNotFoundException(f"Gallery ID [{gallery_id}] not found.")

            curator_id = result[0]
            print(f"🎨 Gallery [{gallery_id}] is curated by Artist ID [{curator_id}].")
            return curator_id

        except GalleryNotFoundException as e:
            print(e)
            return None

        except Exception as e:
            print(f"Error fetching curator: {e}")
            return None
        
    
