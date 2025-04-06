ALTER TABLE Gallery DROP FOREIGN KEY gallery_ibfk_1;

ALTER TABLE Artist MODIFY ArtistID INT AUTO_INCREMENT;

ALTER TABLE Gallery ADD CONSTRAINT gallery_ibfk_1 FOREIGN KEY (Curator) REFERENCES Artist(ArtistID);

DESC Artist;

+---------------------+--------------+------+-----+---------+----------------+
| Field               | Type         | Null | Key | Default | Extra          |
+---------------------+--------------+------+-----+---------+----------------+
| ArtistID            | int          | NO   | PRI | NULL    | auto_increment |
| Name                | varchar(20)  | YES  |     | NULL    |                |
| Biography           | varchar(200) | YES  |     | NULL    |                |
| BirthDate           | date         | YES  |     | NULL    |                |
| Nationality         | varchar(20)  | YES  |     | NULL    |                |
| Website             | varchar(100) | YES  |     | NULL    |                |
| ContactInformation  | varchar(500) | YES  |     | NULL    |                |
+---------------------+--------------+------+-----+---------+----------------+