-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: sesite
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `borrow_borrow_item`
--

DROP TABLE IF EXISTS `borrow_borrow_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrow_borrow_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `borrow_amount` int(11) DEFAULT NULL,
  `borrow_id_id` int(11) NOT NULL,
  `item_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `borrow_borrow_item_borrow_id_id_785cdfcb_fk_borrow_borrow_id` (`borrow_id_id`),
  KEY `borrow_borrow_item_item_id_id_212a43a5_fk_item_item_id` (`item_id_id`),
  CONSTRAINT `borrow_borrow_item_borrow_id_id_785cdfcb_fk_borrow_borrow_id` FOREIGN KEY (`borrow_id_id`) REFERENCES `borrow_borrow` (`id`),
  CONSTRAINT `borrow_borrow_item_item_id_id_212a43a5_fk_item_item_id` FOREIGN KEY (`item_id_id`) REFERENCES `item_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=242 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrow_borrow_item`
--

LOCK TABLES `borrow_borrow_item` WRITE;
/*!40000 ALTER TABLE `borrow_borrow_item` DISABLE KEYS */;
INSERT INTO `borrow_borrow_item` VALUES (118,1,43,1),(120,2,44,2),(121,1,45,4),(122,2,45,5),(123,1,45,6),(124,1,45,7),(125,1,46,2),(126,1,46,3),(127,1,47,5),(128,1,47,6),(129,2,47,7),(130,1,48,7),(131,1,48,9),(149,1,52,3),(170,1,61,1),(171,1,62,1),(172,1,63,2),(173,1,64,1),(174,1,64,2),(175,2,65,1),(176,2,66,3),(177,1,67,2),(178,1,67,3),(179,1,66,2),(180,1,66,1),(181,1,68,8),(182,1,68,6),(183,1,68,7),(184,1,67,1),(195,3,72,1),(196,2,72,2),(197,2,74,1),(198,1,74,2),(199,3,75,1),(200,1,76,1),(202,3,78,3),(205,3,79,1),(206,3,80,1),(209,3,82,9),(212,3,83,1),(214,3,84,2),(215,1,84,1),(218,1,87,4),(219,1,88,2),(225,3,90,1),(226,2,90,2),(227,1,91,1),(228,1,91,2),(229,3,92,1),(231,1,93,4),(232,2,93,7),(233,1,94,2),(234,1,94,3),(235,1,95,5),(236,1,95,6),(237,2,95,7),(238,3,96,9),(239,1,97,1),(240,2,97,5),(241,1,97,6);
/*!40000 ALTER TABLE `borrow_borrow_item` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-28  6:44:33
