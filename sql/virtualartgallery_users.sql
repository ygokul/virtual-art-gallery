-- Active: 1742092772736@@127.0.0.1@3306@virtualartgallery
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: virtualartgallery
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(50) DEFAULT NULL,
  `Password` varchar(200) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `FirstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `DateOfBirth` date DEFAULT NULL,
  `ProfilePicture` varchar(200) DEFAULT NULL,
  `FavoriteArtwork` int DEFAULT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `Username` (`Username`),
  UNIQUE KEY `Email` (`Email`),
  KEY `FavoriteArtwork` (`FavoriteArtwork`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`FavoriteArtwork`) REFERENCES `artwork` (`ArtworkID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'priya','Priya@123','priya@example.com','Priya','Sharma','1995-04-10','https://example.com/profiles/priya.jpg',4),(2,'charlie','Charlie@456','charlie@example.com','Charlie','Dawson','1990-08-09','https://example.com/profiles/charlie.jpg',6),(3,'ram','Ram@789','ram@example.com','Ram','Patel','1992-12-01','https://example.com/profiles/ram.jpg',5),(4,'sai','Sai@234','sai@example.com','Sai','Krishnan','1998-06-15','https://example.com/profiles/sai.jpg',4),(5,'suba','Suba@567','suba@example.com','Suba','Iyer','1994-11-23','https://example.com/profiles/suba.jpg',2),(6,'sudeesh','Sudeesh@890','sudeesh@example.com','Sudeesh','Menon','1991-03-05','https://example.com/profiles/sudeesh.jpg',5),(7,'pradeep','Pradeep@321','pradeep@example.com','Pradeep','Verma','1989-07-11','https://example.com/profiles/pradeep.jpg',6),(8,'alice','Alice@654','alice@example.com','Alice','Bennett','1993-05-30','https://example.com/profiles/alice.jpg',1),(9,'bob','Bob@987','bob@example.com','Bob','Lee','1996-01-17','https://example.com/profiles/bob.jpg',9),(10,'rocky','Rocky@543','rocky@example.com','Rocky','Desai','1997-09-29','https://example.com/profiles/rocky.jpg',1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-23 19:15:49

CREATE TABLE favorites (
    UserID INT,
    ArtworkID INT,
    PRIMARY KEY (UserID, ArtworkID),
    FOREIGN KEY (UserID) REFERENCES users(UserID),
    FOREIGN KEY (ArtworkID) REFERENCES artwork(ArtworkID)
);
