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
-- Table structure for table `item_item`
--

DROP TABLE IF EXISTS `item_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `item_amount` int(11) DEFAULT NULL,
  `item_image` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `create_date` date NOT NULL,
  `update_date` date NOT NULL,
  `current_amount` int(11) DEFAULT NULL,
  `reserve_status` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `amount_forreserve` int(11) NOT NULL,
  `item_price` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_item`
--

LOCK TABLES `item_item` WRITE;
/*!40000 ALTER TABLE `item_item` DISABLE KEYS */;
INSERT INTO `item_item` VALUES (1,'คัตเตอร์',7,'pictures/2019/11/24/a.jpg','2019-11-24','2019-11-28',3,'02',0,NULL),(2,'ปากกาน้ำเงิน',7,'pictures/2019/11/24/blue-pen.jpg','2019-11-24','2019-11-28',7,'01',0,NULL),(3,'ปากกาแดง',7,'pictures/2019/11/24/red-pen.jpg','2019-11-24','2019-11-28',7,'01',0,NULL),(4,'กาว TOA',4,'pictures/2019/11/24/glue.jpg','2019-11-24','2019-11-28',5,'01',0,NULL),(5,'ดินสอ',7,'pictures/2019/11/24/pencil.jpg','2019-11-24','2019-11-28',6,'02',0,NULL),(6,'ไม้บรรทัด',5,'pictures/2019/11/24/ruler.jpg','2019-11-24','2019-11-28',4,'02',0,NULL),(7,'กรรไกร',6,'pictures/2019/11/24/scissors.jpg','2019-11-24','2019-11-28',5,'01',0,NULL),(8,'เทป',5,'pictures/2019/11/24/tape.jpg','2019-11-24','2019-11-28',5,'01',0,NULL),(9,'กาวสองหน้า',3,'pictures/2019/11/24/tape2side.jpg','2019-11-24','2019-11-28',3,'01',0,NULL);
/*!40000 ALTER TABLE `item_item` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-14 16:03:40
