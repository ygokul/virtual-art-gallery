import pymysql
import sys

class DBConnection:
    @staticmethod
    def connect():
        try:
            return pymysql.connect(
                user="root",
                password="root",
                host="127.0.0.1",
                database="virtualartgallery"
            )
        except pymysql.Error as e:
            print(f"Database Connection Error: {e}")
            sys.exit(1)