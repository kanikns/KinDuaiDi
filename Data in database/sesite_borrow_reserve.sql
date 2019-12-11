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
-- Table structure for table `borrow_reserve`
--

DROP TABLE IF EXISTS `borrow_reserve`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrow_reserve` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `can_borrow` int(11) DEFAULT NULL,
  `borrow_id_id` int(11) NOT NULL,
  `borrow_item_id_id` int(11) NOT NULL,
  `item_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `borrow_reserve_borrow_id_id_42548b1f_fk_borrow_borrow_id` (`borrow_id_id`),
  KEY `borrow_reserve_borrow_item_id_id_653e1d23_fk_borrow_bo` (`borrow_item_id_id`),
  KEY `borrow_reserve_item_id_id_60e9e307_fk_item_item_id` (`item_id_id`),
  CONSTRAINT `borrow_reserve_borrow_id_id_42548b1f_fk_borrow_borrow_id` FOREIGN KEY (`borrow_id_id`) REFERENCES `borrow_borrow` (`id`),
  CONSTRAINT `borrow_reserve_borrow_item_id_id_653e1d23_fk_borrow_bo` FOREIGN KEY (`borrow_item_id_id`) REFERENCES `borrow_borrow_item` (`id`),
  CONSTRAINT `borrow_reserve_item_id_id_60e9e307_fk_item_item_id` FOREIGN KEY (`item_id_id`) REFERENCES `item_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrow_reserve`
--

LOCK TABLES `borrow_reserve` WRITE;
/*!40000 ALTER TABLE `borrow_reserve` DISABLE KEYS */;
INSERT INTO `borrow_reserve` VALUES (21,7,44,120,2),(27,7,66,176,3),(28,7,66,179,2),(29,5,66,180,1),(30,5,68,181,8),(31,5,68,182,6),(32,6,68,183,7),(37,2,74,197,1),(38,7,74,198,2),(44,7,84,214,2),(45,1,84,215,1),(46,1,91,227,1),(47,4,91,228,2),(48,4,97,239,1),(49,8,97,240,5),(50,5,97,241,6);
/*!40000 ALTER TABLE `borrow_reserve` ENABLE KEYS */;
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
