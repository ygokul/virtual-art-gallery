import mysql.connector
import sys

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