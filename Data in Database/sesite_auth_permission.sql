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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',2,'add_permission'),(2,'Can change permission',2,'change_permission'),(3,'Can delete permission',2,'delete_permission'),(4,'Can view permission',2,'view_permission'),(5,'Can add group',3,'add_group'),(6,'Can change group',3,'change_group'),(7,'Can delete group',3,'delete_group'),(8,'Can view group',3,'view_group'),(9,'Can add user',4,'add_user'),(10,'Can change user',4,'change_user'),(11,'Can delete user',4,'delete_user'),(12,'Can view user',4,'view_user'),(13,'Can add content type',1,'add_contenttype'),(14,'Can change content type',1,'change_contenttype'),(15,'Can delete content type',1,'delete_contenttype'),(16,'Can view content type',1,'view_contenttype'),(17,'Can add borrow',5,'add_borrow'),(18,'Can change borrow',5,'change_borrow'),(19,'Can delete borrow',5,'delete_borrow'),(20,'Can view borrow',5,'view_borrow'),(21,'Can add borrow_ item',6,'add_borrow_item'),(22,'Can change borrow_ item',6,'change_borrow_item'),(23,'Can delete borrow_ item',6,'delete_borrow_item'),(24,'Can view borrow_ item',6,'view_borrow_item'),(25,'Can add tab',7,'add_tab'),(26,'Can change tab',7,'change_tab'),(27,'Can delete tab',7,'delete_tab'),(28,'Can view tab',7,'view_tab'),(29,'Can add reserve',8,'add_reserve'),(30,'Can change reserve',8,'change_reserve'),(31,'Can delete reserve',8,'delete_reserve'),(32,'Can view reserve',8,'view_reserve'),(33,'Can add item',9,'add_item'),(34,'Can change item',9,'change_item'),(35,'Can delete item',9,'delete_item'),(36,'Can view item',9,'view_item'),(37,'Can add log entry',10,'add_logentry'),(38,'Can change log entry',10,'change_logentry'),(39,'Can delete log entry',10,'delete_logentry'),(40,'Can view log entry',10,'view_logentry'),(41,'Can add session',11,'add_session'),(42,'Can change session',11,'change_session'),(43,'Can delete session',11,'delete_session'),(44,'Can view session',11,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-14 16:03:38
