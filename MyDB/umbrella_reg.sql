-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: umbrella
-- ------------------------------------------------------
-- Server version	8.2.0

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
-- Table structure for table `reg`
--

DROP TABLE IF EXISTS `reg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reg` (
  `idreg` int NOT NULL,
  `regname` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `ypost` varchar(45) DEFAULT NULL,
  `postkey` tinyint DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `pacients_idpacients` int NOT NULL,
  `doctors_iddoctors` int NOT NULL,
  PRIMARY KEY (`idreg`),
  KEY `fk_reg_pacients1_idx` (`pacients_idpacients`),
  KEY `fk_reg_doctors1_idx` (`doctors_iddoctors`),
  CONSTRAINT `fk_reg_doctors1` FOREIGN KEY (`doctors_iddoctors`) REFERENCES `doctors` (`iddoctors`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_reg_pacients1` FOREIGN KEY (`pacients_idpacients`) REFERENCES `pacients` (`idpacients`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reg`
--

LOCK TABLES `reg` WRITE;
/*!40000 ALTER TABLE `reg` DISABLE KEYS */;
/*!40000 ALTER TABLE `reg` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-24 11:23:00
