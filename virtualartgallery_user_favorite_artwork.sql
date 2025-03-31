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
-- Table structure for table `user_favorite_artwork`
--

DROP TABLE IF EXISTS `user_favorite_artwork`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_favorite_artwork` (
  `UserID` int NOT NULL,
  `ArtworkID` int NOT NULL,
  PRIMARY KEY (`UserID`,`ArtworkID`),
  KEY `ArtworkID` (`ArtworkID`),
  CONSTRAINT `user_favorite_artwork_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`),
  CONSTRAINT `user_favorite_artwork_ibfk_2` FOREIGN KEY (`ArtworkID`) REFERENCES `artwork` (`ArtworkID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_favorite_artwork`
--

LOCK TABLES `user_favorite_artwork` WRITE;
/*!40000 ALTER TABLE `user_favorite_artwork` DISABLE KEYS */;
INSERT INTO `user_favorite_artwork` VALUES (1,1),(2,1),(5,1),(8,1),(1,2),(3,2),(7,2),(8,2),(1,3),(4,3),(2,4),(4,5),(5,5),(3,6),(9,6),(6,7),(5,8),(10,8),(6,9),(7,9),(10,9);
/*!40000 ALTER TABLE `user_favorite_artwork` ENABLE KEYS */;
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
