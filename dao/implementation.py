import pymysql
from dao.interface import Interface
from tabulate import tabulate
from datetime import datetime
from entity.artwork import Artwork
from entity.gallery import Gallery
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
    def view_artworks(self):
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
                print(f"Medium: {row[2]}")
                print(f"Artist ID: {row[3]}")
                print(f"Year: {row[4]}")
                print("-" * 30)  # Separator for better readability
        except pymysql.Error as e:
            print(f"Database Error: {e}")


    def add_artwork(self, title, description, medium, image_url):
        try:
            creation_date = datetime.now().strftime('%Y-%m-%d')  # current date in YYYY-MM-DD format
            query = """
                INSERT INTO artwork (Title, Description, CreationDate, Medium, ImageURL)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (title, description, creation_date, medium, image_url))
            self.conn.commit()
            print()
            print("/n Artwork added successfully!")

            self.cursor.execute("SELECT * FROM artwork WHERE ArtworkID = LAST_INSERT_ID()")
            inserted_artwork = self.cursor.fetchone()

            if inserted_artwork:
                artwork_id, title, description, creation_date, medium, image_url = inserted_artwork
                print("\n--- Inserted Artwork ---")
                print(f"Artwork ID    : {artwork_id}")
                print(f"Title         : {title}")
                print(f"Description   : {description}")
                print(f"Creation Date : {creation_date}")
                print(f"Medium        : {medium}")
                print(f"Image URL     : {image_url}")
                print("-" * 40)
        except pymysql.Error as e:
            print(f"Error Adding Artwork: {e}")


    def add_artwork(self, title, description, medium, image_url):
        try:
            creation_date = datetime.now().strftime('%Y-%m-%d')  # current date in YYYY-MM-DD format
            query = """
                INSERT INTO artwork (Title, Description, CreationDate, Medium, ImageURL)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (title, description, creation_date, medium, image_url))
            self.conn.commit()

            print("\n🎉 Artwork added successfully!")

            self.cursor.execute("SELECT * FROM artwork WHERE ArtworkID = LAST_INSERT_ID()")
            inserted_artwork = self.cursor.fetchone()

            if inserted_artwork:
                artwork_id, title, description, creation_date, medium, image_url = inserted_artwork
                print("\n--- 🎨 Inserted Artwork ---")
                print(f"🆔 Artwork ID    : {artwork_id}")
                print(f"🖌️  Title         : {title}")
                print(f"📝 Description   : {description}")
                print(f"📅 Creation Date : {creation_date}")
                print(f"🎨 Medium        : {medium}")
                print(f"🌐 Image URL     : {image_url}")
                print("-" * 40)
            else:
                raise ArtworkNotFoundException("❌ Artwork not found after insertion.")

        except ArtworkNotFoundException as e:
            print(e)

        except pymysql.Error as e:
            print(f"❌ Error Adding Artwork: {e}")

    def remove_artwork(self, identifier):
        try:
            query = "DELETE FROM artwork WHERE ArtworkID = %s OR Title = %s"
            self.cursor.execute(query, (identifier, str(identifier)))
            self.conn.commit()

            if self.cursor.rowcount == 0:
                raise ArtworkNotFoundException(f"❌ Artwork with ID or Title '{identifier}' not found.")

            print()
            print("✅ Artwork removed successfully!")
            print("🚀 We're always evolving! Feel free to add your next masterpiece anytime.")
            print("🎭 Visit us again for more artistic inspiration!")

        except ArtworkNotFoundException as e:
            print(e)

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
                medium=row[3],
                image_url=row[4]
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

        except pymysql.Error as e:
            print(f"Error Fetching Artwork: {e}")


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

        except pymysql.Error as e:
            print(f"Error Searching Artworks: {e}")


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

            # Step 1: Check if artwork exists
            check_artwork_query = "SELECT * FROM artwork WHERE ArtworkID = %s"
            self.cursor.execute(check_artwork_query, (artwork_id,))
            artwork = self.cursor.fetchone()

            if not artwork:
                raise ArtworkNotFoundException(f"🎨 Artwork with ID {artwork_id} does not exist.")

            # Step 2: Attempt to remove from favorites
            delete_query = "DELETE FROM user_favorite_artwork WHERE ArtworkID = %s"
            self.cursor.execute(delete_query, (artwork_id,))
            self.conn.commit()

            if self.cursor.rowcount == 0:
                raise FavoriteNotFoundException(f"❤️ Favorite for artwork ID {artwork_id} not found.")

            print(f"💔 Farewell, Artwork #{artwork_id} — you've been unfavorited with style.")

        except ArtworkNotFoundException as e:
            print(f"❌ {e}")

        except FavoriteNotFoundException as e:
            print(f"⚠️ {e}")

        except pymysql.Error as e:
            print(f"❌ Error Removing from Favorites: {e}")
        def get_user_favorite_artworks(self, user_id):
            try:
                query = """
                    SELECT a.ArtworkID, a.Title, a.Description, a.CreationDate, a.Medium, a.ImageURL
                    FROM artwork a
                    JOIN user_favorite_artwork ufa ON a.ArtworkID = ufa.ArtworkID
                    WHERE ufa.UserID = %s
                """
                self.cursor.execute(query, (user_id,))
                rows = self.cursor.fetchall()

                if not rows:
                    raise FavoriteNotFoundException("No favorite artworks found.")

                print("\n🎨 User's Favorite Artworks:")
                for row in rows:
                    print(f"🆔 Artwork ID: {row[0]}")
                    print(f"🖌️ Title: {row[1]}")
                    print(f"📝 Description: {row[2]}")
                    print(f"📅 Created On: {row[3]}")
                    print(f"🎨 Medium: {row[4]}")
                    print(f"🖼️ Image URL: {row[5]}")
                    print("-" * 40)

            except FavoriteNotFoundException as e:
                print(f"⚠️ {e}")

            except pymysql.Error as e:
                print(f"❌ Error Fetching Favorites: {e}")

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


