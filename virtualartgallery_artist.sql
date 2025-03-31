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
-- Table structure for table `artist`
--

DROP TABLE IF EXISTS `artist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist` (
  `ArtistID` int NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Biography` varchar(200) DEFAULT NULL,
  `BirthDate` date DEFAULT NULL,
  `Nationality` varchar(20) DEFAULT NULL,
  `Website` varchar(100) DEFAULT NULL,
  `ContactInformation` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`ArtistID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist`
--

LOCK TABLES `artist` WRITE;
/*!40000 ALTER TABLE `artist` DISABLE KEYS */;
INSERT INTO `artist` VALUES (101,'Arjun Mehta','Contemporary digital artist specializing in virtual art galleries.','1990-04-15','Indian','https://www.emperiavr.com','arjun.mehta@example.com'),(102,'Alex Rivera','Mixed media artist known for augmented reality exhibits.','1987-09-21','American','https://www.artivive.com','alex.rivera@example.com'),(103,'Ishita Sharma','Abstract artist whose works are featured in major global tours.','1993-07-03','Indian','https://www.theguardian.com/travel/2020/mar/23','ishita.sharma@example.com'),(104,'Taylor Morgan','Sculptor blending traditional and AR techniques.','1985-02-10','Canadian','https://www.artstation.com/artwork/wrJm5L','taylor.morgan@example.com'),(105,'Rohan Patel','Painter focusing on nature and landscape themes.','1992-05-27','Indian','https://www.shine.cn/feature/art-culture/2311227602/','rohan.patel@example.com'),(106,'Jordan Lee','Photographer and digital artist specializing in virtual spaces.','1990-03-19','Australian','https://thinkplaycreate.org/explore/virtual-tours/','jordan.lee@example.com'),(107,'Ananya Iyer','Installation artist with a focus on virtual reality environments.','1995-06-11','Indian','https://www.twinkl.cz/blog/twinkl-virtual-earth-day-art-gallery','ananya.iyer@example.com'),(108,'Casey Bennett','Artist known for interactive digital installations.','1988-12-22','British','https://huwmessie.com/2020/03/04/the-virtual-artifact-gallery/','casey.bennett@example.com'),(109,'Kunal Desai','Oil painter blending traditional and digital techniques.','1994-01-18','Indian','https://www.fizdi.com/trees-and-house-art_4551_27736-handpainted-art-painting-20in-x-20in/','kunal.desai@example.com'),(110,'Charlie Dawson','Multimedia artist specializing in music and art fusion.','1986-08-09','American','https://harmonyarts.com/products/guitars-musical-instruments-paintings-artworks','charlie.dawson@example.com');
/*!40000 ALTER TABLE `artist` ENABLE KEYS */;
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
