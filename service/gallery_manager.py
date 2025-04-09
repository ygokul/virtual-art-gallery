# service/gallery_manager.py
from exception.exceptions import GalleryNotAddedException, GalleryNotFoundException
from entity.gallery import Gallery
import pymysql

class GalleryManager:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def add_gallery(self, gallery: Gallery):
        try:
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
        except pymysql.Error as e:
            raise GalleryNotAddedException(f"❌ Error Adding Gallery: {e}")

    def update_gallery(self, gallery: Gallery):
        try:
            self.cursor.execute("SELECT 1 FROM gallery WHERE GalleryID = %s", (gallery.get_gallery_id(),))
            if not self.cursor.fetchone():
                raise GalleryNotFoundException(f"Gallery with ID {gallery.get_gallery_id()} not found.")

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
        except pymysql.Error as e:
            raise e

    def remove_gallery(self, gallery_id):
        try:
            self.cursor.execute("SELECT * FROM gallery WHERE GalleryID = %s", (gallery_id,))
            if not self.cursor.fetchone():
                raise GalleryNotFoundException(f"Gallery with ID {gallery_id} not found.")

            self.cursor.execute("DELETE FROM gallery WHERE GalleryID = %s", (gallery_id,))
            self.conn.commit()
        except pymysql.Error as e:
            raise e

    def search_gallery_by_name(self, name_keyword):
        try:
            self.cursor.execute("SELECT * FROM gallery WHERE Name LIKE %s", ('%' + name_keyword + '%',))
            results = self.cursor.fetchall()
            if not results:
                raise GalleryNotFoundException(f"No galleries found matching name: '{name_keyword}'.")
            return results
        except pymysql.Error as e:
            raise e
