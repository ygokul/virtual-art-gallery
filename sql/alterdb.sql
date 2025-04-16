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


ALTER TABLE artwork_gallery DROP FOREIGN KEY artwork_gallery_ibfk_2;

 ALTER TABLE gallery MODIFY GalleryID INT NOT NULL AUTO_INCREMENT;

 ALTER TABLE artwork_gallery ADD CONSTRAINT artwork_gallery_ibfk_2 FOREIGN KEY (GalleryID) REFERENCES gallery(GalleryID) ON DELETE CASCADE;


ALTER TABLE artwork
ADD ArtistID INT;

ALTER TABLE artwork
ADD CONSTRAINT fk_artist
FOREIGN KEY (ArtistID) REFERENCES artist(ArtistID);

UPDATE artwork SET ArtistID = 101 WHERE ArtworkID = 1;
UPDATE artwork SET ArtistID = 102 WHERE ArtworkID = 2;
UPDATE artwork SET ArtistID = 103 WHERE ArtworkID = 3;
UPDATE artwork SET ArtistID = 104 WHERE ArtworkID = 4;
UPDATE artwork SET ArtistID = 105 WHERE ArtworkID = 5;
UPDATE artwork SET ArtistID = 106 WHERE ArtworkID = 6;
UPDATE artwork SET ArtistID = 107 WHERE ArtworkID = 7;
UPDATE artwork SET ArtistID = 108 WHERE ArtworkID = 8;
UPDATE artwork SET ArtistID = 109 WHERE ArtworkID = 9;
UPDATE artwork SET ArtistID = 110 WHERE ArtworkID = 10;


UPDATE artwork SET ArtistId = 113 WHERE ArtworkID = 32;
UPDATE artwork SET ArtistId = 114 WHERE ArtworkID = 33;
UPDATE artwork SET ArtistId = 115 WHERE ArtworkID = 34;
UPDATE artwork SET ArtistId = 113 WHERE ArtworkID = 35;
UPDATE artwork SET ArtistId = 114 WHERE ArtworkID = 39;
UPDATE artwork SET ArtistId = 115 WHERE ArtworkID = 40;
UPDATE artwork SET ArtistId = 113 WHERE ArtworkID = 41;
UPDATE artwork SET ArtistId = 114 WHERE ArtworkID = 42;

UPDATE artwork SET ArtistID = 102 WHERE ArtworkID = 5;
UPDATE artwork SET ArtistID = 101 WHERE ArtworkID = 7;

update user_favorite_artwork set artworkid=3 where artworkid=30

