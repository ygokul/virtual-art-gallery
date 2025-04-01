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
-- Table structure for table `artwork`
--

DROP TABLE IF EXISTS `artwork`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artwork` (
  `ArtworkID` int NOT NULL AUTO_INCREMENT,
  `Title` varchar(100) DEFAULT NULL,
  `Description` varchar(250) DEFAULT NULL,
  `CreationDate` date DEFAULT NULL,
  `Medium` text,
  `ImageURL` varchar(500) DEFAULT NULL,
  `ArtistID` int DEFAULT NULL,
  PRIMARY KEY (`ArtworkID`),
  KEY `ar_foreign` (`ArtistID`),
  CONSTRAINT `ar_foreign` FOREIGN KEY (`ArtistID`) REFERENCES `artist` (`ArtistID`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artwork`
--

LOCK TABLES `artwork` WRITE;
/*!40000 ALTER TABLE `artwork` DISABLE KEYS */;
INSERT INTO `artwork` VALUES (1,'Emperia Images','Emperia Art Gallery is an immersive, futuristic digital space showcasing innovative and interactive virtual artworks.','2023-01-15','Digital Painting','https://emperiavr.com/wp-content/uploads/2021/03/ArtGalleries-1.jpg',NULL),(2,'Art meets AR','Where art meets augmented reality, creating immersive, interactive, and dynamic experiences that blend the physical and digital worlds.','2022-11-20','Augmented Reality (AR) Art','https://www.plugxr.com/augmented-reality/wp-content/uploads/2022/09/AR-art-1024x536.jpg',NULL),(3,'DIGITAL MUSEUM','A virtual art gallery within a digital museum, showcasing immersive 3D artworks, interactive exhibits, and multimedia experiences.','2021-05-10','Multimedia Installation','https://www.invaluable.com/blog/wp-content/uploads/sites/77/2019/05/01-Kremer-Museum.jpg',NULL),(4,'Human Metamorphosis','An immersive virtual exhibit exploring human metamorphosis through dynamic digital transformations and evolving 3D forms.','2023-03-08','Motion Graphics','https://img.freepik.com/premium-vector/natural-metamorphosis-human-head-tranquil-landscape-merge-art-prints_961038-5507.jpg?w=740',NULL),(5,'Time meets Virtual Art','A captivating fusion where the concept of time intertwines with virtual art, creating immersive, ever-evolving digital experiences.','2023-07-01','3D Digital Art','https://static.tnn.in/thumb/msid-117633497,thumbsize-1366252,width-1280,height-720,resizemode-75/117633497.jpg',NULL),(6,'Kids Favourite Art','A joyful collection of vibrant, playful, and whimsical digital artworks designed to spark imagination and delight young minds.','2022-12-05','Hand Painting','https://familyforeverychild.org/wp-content/uploads/2022/01/69824735.jpeg',NULL),(7,'Galaxy meets Virtual Art','An awe-inspiring virtual experience where cosmic wonders collide with digital artistry, immersing viewers in a galaxy of surreal visuals and interstellar creativity.','2024-01-10','Animation','https://c02.purpledshub.com/uploads/sites/48/2021/06/solar-system-planets-2dff1b1.jpg?w=940&webp=1',NULL),(8,'Delicious Explains the Art','A mouthwatering visual feast where vibrant colors, textures, and digital artistry come together to create deliciously captivating artworks.','2021-09-22','Canva Painting','https://cdn11.bigcommerce.com/s-x49po/images/stencil/800w/products/127776/294765/prints%2Fdownscaled%2Fp_rp771ai9bxp_2000x2000__65157.1713421001.jpg?c=2',NULL),(9,'Exploring Simple and Wow Nature','A serene yet stunning virtual showcase capturing the simplicity and grandeur of nature through breathtaking digital landscapes and immersive art.','2024-02-28','Digital Painting','https://imgcdn.stablediffusionweb.com/2024/4/10/27d94784-0cd7-4096-ad0f-3b9a4cf53904.jpg',NULL),(10,'Music Therapy','A harmonious blend of digital art and soothing soundscapes, offering a therapeutic, immersive experience that calms the mind and uplifts the spirit.','2023-10-18','Digital Art','https://i0.wp.com/london-post.co.uk/wp-content/uploads/2023/12/image002.jpeg?fit=649%2C433&ssl=1',NULL),(11,NULL,NULL,NULL,NULL,NULL,NULL),(12,NULL,NULL,NULL,NULL,NULL,NULL),(13,NULL,NULL,NULL,NULL,NULL,NULL),(14,NULL,NULL,NULL,NULL,NULL,NULL),(15,NULL,NULL,NULL,NULL,NULL,NULL),(16,NULL,NULL,NULL,NULL,NULL,NULL),(17,NULL,NULL,NULL,NULL,NULL,NULL),(18,NULL,NULL,NULL,NULL,NULL,NULL),(19,NULL,NULL,NULL,NULL,NULL,NULL),(20,NULL,NULL,NULL,NULL,NULL,NULL),(21,NULL,NULL,NULL,NULL,NULL,101),(22,NULL,NULL,NULL,NULL,NULL,102),(23,NULL,NULL,NULL,NULL,NULL,103),(24,NULL,NULL,NULL,NULL,NULL,102),(25,NULL,NULL,NULL,NULL,NULL,105),(26,NULL,NULL,NULL,NULL,NULL,104),(27,NULL,NULL,NULL,NULL,NULL,106),(28,NULL,NULL,NULL,NULL,NULL,107),(29,NULL,NULL,NULL,NULL,NULL,108),(30,NULL,NULL,NULL,NULL,NULL,109);
/*!40000 ALTER TABLE `artwork` ENABLE KEYS */;
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
