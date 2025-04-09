# service/artwork_manager.py

from entity.artwork import Artwork
from exception.exceptions import ArtworkNotFoundException
import pymysql

class ArtworkManager:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

    def add_artwork(self, title, description, creation_date, medium, image_url):
        try:
            query = """
                INSERT INTO artwork (Title, Description, CreationDate, Medium, ImageURL)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (title, description, creation_date, medium, image_url))
            self.conn.commit()

            artwork_id = self.cursor.lastrowid
            return Artwork(artwork_id, title, description, creation_date, medium, image_url)
        except pymysql.MySQLError as e:
            raise Exception(f"Failed to add artwork: {e}")

    def update_artwork(self, artwork: Artwork):
        try:
            query = """
                UPDATE artwork
                SET Title = %s, Description = %s, CreationDate = %s, Medium = %s, ImageURL = %s
                WHERE ArtworkID = %s
            """
            self.cursor.execute(query, (
                artwork.get_title(),
                artwork.get_description(),
                artwork.get_creation_date(),
                artwork.get_medium(),
                artwork.get_image_url(),
                artwork.get_artwork_id()
            ))
            if self.cursor.rowcount == 0:
                raise ArtworkNotFoundException(f"Artwork with ID {artwork.get_artwork_id()} not found.")
            self.conn.commit()
        except pymysql.MySQLError as e:
            raise Exception(f"Failed to update artwork: {e}")

    def remove_artwork(self, artwork_id):
        try:
            query = "DELETE FROM artwork WHERE ArtworkID = %s"
            self.cursor.execute(query, (artwork_id,))
            if self.cursor.rowcount == 0:
                raise ArtworkNotFoundException(f"Artwork with ID {artwork_id} not found.")
            self.conn.commit()
        except pymysql.MySQLError as e:
            raise Exception(f"Failed to remove artwork: {e}")

    def get_artwork_by_id(self, artwork_id):
        try:
            query = "SELECT * FROM artwork WHERE ArtworkID = %s"
            self.cursor.execute(query, (artwork_id,))
            row = self.cursor.fetchone()
            if not row:
                raise ArtworkNotFoundException(f"Artwork with ID {artwork_id} not found.")
            return Artwork(*row)
        except pymysql.MySQLError as e:
            raise Exception(f"Failed to retrieve artwork: {e}")
