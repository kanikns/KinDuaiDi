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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-12-14 07:53:02.175285'),(2,'auth','0001_initial','2019-12-14 07:53:10.904636'),(3,'item','0001_initial','2019-12-14 07:53:11.075181'),(4,'item','0002_remove_item_item_amount','2019-12-14 07:53:11.183889'),(5,'item','0003_auto_20191031_1204','2019-12-14 07:53:11.330500'),(6,'item','0004_item_create_date','2019-12-14 07:53:11.629885'),(7,'item','0005_auto_20191031_1528','2019-12-14 07:53:11.763503'),(8,'item','0006_auto_20191031_1542','2019-12-14 07:53:11.882211'),(9,'item','0007_auto_20191031_1544','2019-12-14 07:53:12.041756'),(10,'item','0008_auto_20191031_1546','2019-12-14 07:53:12.126557'),(11,'item','0009_auto_20191031_1558','2019-12-14 07:53:12.304057'),(12,'item','0010_auto_20191101_2317','2019-12-14 07:53:12.440718'),(13,'item','0011_auto_20191102_0009','2019-12-14 07:53:12.684040'),(14,'item','0012_auto_20191102_0035','2019-12-14 07:53:12.883507'),(15,'item','0013_auto_20191102_0043','2019-12-14 07:53:12.983267'),(16,'item','0014_auto_20191102_0048','2019-12-14 07:53:13.069035'),(17,'item','0015_auto_20191102_0049','2019-12-14 07:53:13.239553'),(18,'item','0016_auto_20191102_0058','2019-12-14 07:53:13.358240'),(19,'item','0017_auto_20191102_0059','2019-12-14 07:53:13.516843'),(20,'item','0018_auto_20191102_0101','2019-12-14 07:53:13.702340'),(21,'item','0019_auto_20191102_1550','2019-12-14 07:53:13.805044'),(22,'item','0020_auto_20191102_1551','2019-12-14 07:53:13.948658'),(23,'item','0021_auto_20191102_1552','2019-12-14 07:53:14.082302'),(24,'item','0022_auto_20191102_1555','2019-12-14 07:53:14.168098'),(25,'item','0023_auto_20191102_1556','2019-12-14 07:53:14.278802'),(26,'item','0024_auto_20191102_1559','2019-12-14 07:53:14.381529'),(27,'item','0025_auto_20191102_2210','2019-12-14 07:53:14.626843'),(28,'item','0026_item_current_amount','2019-12-14 07:53:14.723586'),(29,'item','0027_item_reserve_status','2019-12-14 07:53:14.822322'),(30,'item','0028_item_amount_forreserve','2019-12-14 07:53:14.955966'),(31,'item','0029_auto_20191120_0020','2019-12-14 07:53:15.055726'),(32,'item','0030_auto_20191124_1333','2019-12-14 07:53:15.166428'),(33,'item','0031_auto_20191124_1334','2019-12-14 07:53:15.324978'),(34,'borrow','0001_initial','2019-12-14 07:53:15.514472'),(35,'borrow','0002_tab_tab_type','2019-12-14 07:53:15.698979'),(36,'borrow','0003_auto_20191127_1925','2019-12-14 07:53:15.812700'),(37,'borrow','0004_auto_20191127_1954','2019-12-14 07:53:15.923407'),(38,'borrow','0005_auto_20191214_0002','2019-12-14 07:53:16.035097'),(39,'item','0032_auto_20191213_2346','2019-12-14 07:53:22.926258'),(40,'item','0033_auto_20191213_2348','2019-12-14 07:53:23.090817'),(41,'admin','0001_initial','2019-12-14 07:53:29.994880'),(42,'admin','0002_logentry_remove_auto_add','2019-12-14 07:53:35.955653'),(43,'admin','0003_logentry_add_action_flag_choices','2019-12-14 07:53:36.101268'),(44,'contenttypes','0002_remove_content_type_name','2019-12-14 07:53:43.019113'),(45,'auth','0002_alter_permission_name_max_length','2019-12-14 07:53:45.921627'),(46,'auth','0003_alter_user_email_max_length','2019-12-14 07:53:46.456197'),(47,'auth','0004_alter_user_username_opts','2019-12-14 07:53:46.708521'),(48,'auth','0005_alter_user_last_login_null','2019-12-14 07:53:47.222149'),(49,'auth','0006_require_contenttypes_0002','2019-12-14 07:53:47.274010'),(50,'auth','0007_alter_validators_add_error_messages','2019-12-14 07:53:47.603129'),(51,'auth','0008_alter_user_username_max_length','2019-12-14 07:53:48.176596'),(52,'auth','0009_alter_user_last_name_max_length','2019-12-14 07:53:48.796937'),(53,'auth','0010_alter_group_name_max_length','2019-12-14 07:53:49.152985'),(54,'auth','0011_update_proxy_permissions','2019-12-14 07:53:49.218809'),(55,'sessions','0001_initial','2019-12-14 07:53:50.246062');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-14 16:03:39
