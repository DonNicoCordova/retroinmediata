-- MySQL dump 10.13  Distrib 5.5.61, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: TI
-- ------------------------------------------------------
-- Server version	5.5.61-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alertas_answerreport`
--

DROP TABLE IF EXISTS `alertas_answerreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alertas_answerreport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(500) NOT NULL,
  `publish_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alertas_answerreport`
--

LOCK TABLES `alertas_answerreport` WRITE;
/*!40000 ALTER TABLE `alertas_answerreport` DISABLE KEYS */;
INSERT INTO `alertas_answerreport` VALUES (1,'El profe no responde','2018-11-07 17:06:21');
/*!40000 ALTER TABLE `alertas_answerreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alertas_answerreportuser`
--

DROP TABLE IF EXISTS `alertas_answerreportuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alertas_answerreportuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `report_id` int(11) NOT NULL,
  `student_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `report_id` (`report_id`),
  UNIQUE KEY `alertas_answerreportuser_report_id_student_id_tea_68425e33_uniq` (`report_id`,`student_id`,`teacher_id`),
  KEY `alertas_answerreport_student_id_368f2c06_fk_retro_aut` (`student_id`),
  KEY `alertas_answerreport_teacher_id_e29afe46_fk_retro_aut` (`teacher_id`),
  CONSTRAINT `alertas_answerreport_teacher_id_e29afe46_fk_retro_aut` FOREIGN KEY (`teacher_id`) REFERENCES `retro_auth_userprofile` (`id`),
  CONSTRAINT `alertas_answerreport_report_id_304ce7a2_fk_alertas_a` FOREIGN KEY (`report_id`) REFERENCES `alertas_answerreport` (`id`),
  CONSTRAINT `alertas_answerreport_student_id_368f2c06_fk_retro_aut` FOREIGN KEY (`student_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alertas_answerreportuser`
--

LOCK TABLES `alertas_answerreportuser` WRITE;
/*!40000 ALTER TABLE `alertas_answerreportuser` DISABLE KEYS */;
INSERT INTO `alertas_answerreportuser` VALUES (2,1,1,4);
/*!40000 ALTER TABLE `alertas_answerreportuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auditorias_foroaudit`
--

DROP TABLE IF EXISTS `auditorias_foroaudit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auditorias_foroaudit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `publish_date` datetime NOT NULL,
  `alert_id` int(11) NOT NULL,
  `director_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `alert_id` (`alert_id`),
  UNIQUE KEY `auditorias_foroaudit_director_id_student_id_t_239e94ab_uniq` (`director_id`,`student_id`,`teacher_id`),
  KEY `auditorias_foroaudit_student_id_7023deae_fk_retro_aut` (`student_id`),
  KEY `auditorias_foroaudit_teacher_id_5e17a022_fk_retro_aut` (`teacher_id`),
  CONSTRAINT `auditorias_foroaudit_teacher_id_5e17a022_fk_retro_aut` FOREIGN KEY (`teacher_id`) REFERENCES `retro_auth_userprofile` (`id`),
  CONSTRAINT `auditorias_foroaudit_alert_id_4abcd3c1_fk_alertas_a` FOREIGN KEY (`alert_id`) REFERENCES `alertas_answerreport` (`id`),
  CONSTRAINT `auditorias_foroaudit_director_id_88c1a191_fk_retro_aut` FOREIGN KEY (`director_id`) REFERENCES `retro_auth_userprofile` (`id`),
  CONSTRAINT `auditorias_foroaudit_student_id_7023deae_fk_retro_aut` FOREIGN KEY (`student_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auditorias_foroaudit`
--

LOCK TABLES `auditorias_foroaudit` WRITE;
/*!40000 ALTER TABLE `auditorias_foroaudit` DISABLE KEYS */;
INSERT INTO `auditorias_foroaudit` VALUES (1,'2018-11-07 17:15:31',1,3,1,4);
/*!40000 ALTER TABLE `auditorias_foroaudit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auditorias_minutesaudit`
--

DROP TABLE IF EXISTS `auditorias_minutesaudit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auditorias_minutesaudit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `publish_date` datetime NOT NULL,
  `director_id` int(11) DEFAULT NULL,
  `userprofile_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `auditorias_minutesau_director_id_54312cee_fk_retro_aut` (`director_id`),
  KEY `auditorias_minutesau_userprofile_id_9060ed61_fk_retro_aut` (`userprofile_id`),
  CONSTRAINT `auditorias_minutesau_userprofile_id_9060ed61_fk_retro_aut` FOREIGN KEY (`userprofile_id`) REFERENCES `retro_auth_userprofile` (`id`),
  CONSTRAINT `auditorias_minutesau_director_id_54312cee_fk_retro_aut` FOREIGN KEY (`director_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auditorias_minutesaudit`
--

LOCK TABLES `auditorias_minutesaudit` WRITE;
/*!40000 ALTER TABLE `auditorias_minutesaudit` DISABLE KEYS */;
INSERT INTO `auditorias_minutesaudit` VALUES (1,'2018-11-07 17:20:02',3,4),(2,'2018-11-07 17:20:14',3,4);
/*!40000 ALTER TABLE `auditorias_minutesaudit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add user',2,'add_user'),(5,'Can change user',2,'change_user'),(6,'Can delete user',2,'delete_user'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add permission',4,'add_permission'),(11,'Can change permission',4,'change_permission'),(12,'Can delete permission',4,'delete_permission'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add user profile',7,'add_userprofile'),(20,'Can change user profile',7,'change_userprofile'),(21,'Can delete user profile',7,'delete_userprofile'),(22,'Can add student',8,'add_student'),(23,'Can change student',8,'change_student'),(24,'Can delete student',8,'delete_student'),(25,'Can add subject',9,'add_subject'),(26,'Can change subject',9,'change_subject'),(27,'Can delete subject',9,'delete_subject'),(28,'Can add post ranking',10,'add_postranking'),(29,'Can change post ranking',10,'change_postranking'),(30,'Can delete post ranking',10,'delete_postranking'),(31,'Can add post',11,'add_post'),(32,'Can change post',11,'change_post'),(33,'Can delete post',11,'delete_post'),(34,'Can add thread',12,'add_thread'),(35,'Can change thread',12,'change_thread'),(36,'Can delete thread',12,'delete_thread'),(37,'Can add thread ranking',13,'add_threadranking'),(38,'Can change thread ranking',13,'change_threadranking'),(39,'Can delete thread ranking',13,'delete_threadranking'),(40,'Can add section',14,'add_section'),(41,'Can change section',14,'change_section'),(42,'Can delete section',14,'delete_section'),(43,'Can add post follower',15,'add_postfollower'),(44,'Can change post follower',15,'change_postfollower'),(45,'Can delete post follower',15,'delete_postfollower'),(46,'Can add career',16,'add_career'),(47,'Can change career',16,'change_career'),(48,'Can delete career',16,'delete_career'),(49,'Can add user type',17,'add_usertype'),(50,'Can change user type',17,'change_usertype'),(51,'Can delete user type',17,'delete_usertype'),(52,'Can add threshold',18,'add_threshold'),(53,'Can change threshold',18,'change_threshold'),(54,'Can delete threshold',18,'delete_threshold'),(55,'Can add comment archive',19,'add_commentarchive'),(56,'Can change comment archive',19,'change_commentarchive'),(57,'Can delete comment archive',19,'delete_commentarchive'),(58,'Can add comment ranking',20,'add_commentranking'),(59,'Can change comment ranking',20,'change_commentranking'),(60,'Can delete comment ranking',20,'delete_commentranking'),(61,'Can add thread follower',21,'add_threadfollower'),(62,'Can change thread follower',21,'change_threadfollower'),(63,'Can delete thread follower',21,'delete_threadfollower'),(64,'Can add career subject section',22,'add_careersubjectsection'),(65,'Can change career subject section',22,'change_careersubjectsection'),(66,'Can delete career subject section',22,'delete_careersubjectsection'),(67,'Can add comment',23,'add_comment'),(68,'Can change comment',23,'change_comment'),(69,'Can delete comment',23,'delete_comment'),(70,'Can add meeting',24,'add_meeting'),(71,'Can change meeting',24,'change_meeting'),(72,'Can delete meeting',24,'delete_meeting'),(73,'Can add refuse minute',25,'add_refuseminute'),(74,'Can change refuse minute',25,'change_refuseminute'),(75,'Can delete refuse minute',25,'delete_refuseminute'),(76,'Can add member',26,'add_member'),(77,'Can change member',26,'change_member'),(78,'Can delete member',26,'delete_member'),(79,'Can add minute',27,'add_minute'),(80,'Can change minute',27,'change_minute'),(81,'Can delete minute',27,'delete_minute'),(82,'Can add answer report user',28,'add_answerreportuser'),(83,'Can change answer report user',28,'change_answerreportuser'),(84,'Can delete answer report user',28,'delete_answerreportuser'),(85,'Can add answer report',29,'add_answerreport'),(86,'Can change answer report',29,'change_answerreport'),(87,'Can delete answer report',29,'delete_answerreport'),(88,'Can add foro audit',30,'add_foroaudit'),(89,'Can change foro audit',30,'change_foroaudit'),(90,'Can delete foro audit',30,'delete_foroaudit'),(91,'Can add minutes audit',31,'add_minutesaudit'),(92,'Can change minutes audit',31,'change_minutesaudit'),(93,'Can delete minutes audit',31,'delete_minutesaudit');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$dpKevfimPXYg$5uUEmktH/XYWxG3Tx5cmlsxu2y1yEtEVU0K2Uk4al7E=','2018-11-07 04:15:58',1,'root','','','asdasd@gmail.com',1,1,'2018-11-07 04:15:52'),(2,'pbkdf2_sha256$100000$ElOU4xdbAlyo$EEMh+AlhRW4O0DNr1yM7GSYGgs0Ou+k4f1qTc05gEOs=',NULL,0,'g.diaz','Gabriel','D','',0,1,'2018-11-07 04:16:12'),(3,'pbkdf2_sha256$100000$XKGEChqTubbc$0c/ZJcOUBL6MnR5T3JZxaSbxY2eRcbOKNTbIWpnUmQA=',NULL,0,'m.tejos','Matías','T','',0,1,'2018-11-07 04:16:23'),(4,'pbkdf2_sha256$100000$6PEvGT1i54qg$cpxgFv90vTj0tNuNzNgw2YkBdnT20pqQU9tk3taPTEg=',NULL,0,'e.quiroga','Eduardo','Q','',0,1,'2018-11-07 04:16:32'),(5,'pbkdf2_sha256$100000$iRg2k62GxZSr$sHV4mu18L8dcvg0YwRWv+UeJaICmxaL3lsaKs0wfuL4=',NULL,0,'r.caballero','Rodrigo','C','',0,1,'2018-11-07 04:16:43');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-11-07 04:16:12','2','g.diaz',1,'[{\"added\": {}}]',2,1),(2,'2018-11-07 04:16:14','1','  Rut: 1',1,'[{\"added\": {}}]',7,1),(3,'2018-11-07 04:16:23','3','m.tejos',1,'[{\"added\": {}}]',2,1),(4,'2018-11-07 04:16:25','2','  Rut: 2',1,'[{\"added\": {}}]',7,1),(5,'2018-11-07 04:16:32','4','e.quiroga',1,'[{\"added\": {}}]',2,1),(6,'2018-11-07 04:16:36','3','  Rut: 3',1,'[{\"added\": {}}]',7,1),(7,'2018-11-07 04:16:43','5','r.caballero',1,'[{\"added\": {}}]',2,1),(8,'2018-11-07 04:16:45','4','  Rut: Sin Rut',1,'[{\"added\": {}}]',7,1),(9,'2018-11-07 04:16:54','4','e.quiroga',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]',2,1),(10,'2018-11-07 04:16:59','2','g.diaz',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]',2,1),(11,'2018-11-07 04:17:05','3','m.tejos',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]',2,1),(12,'2018-11-07 04:17:10','5','r.caballero',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]',2,1),(13,'2018-11-07 04:17:25','1','COmputación director: Eduardo Q',1,'[{\"added\": {}}]',16,1),(14,'2018-11-07 04:17:33','1','Programación I',1,'[{\"added\": {}}]',9,1),(15,'2018-11-07 04:17:40','1','25413',1,'[{\"added\": {}}]',14,1),(16,'2018-11-07 04:17:42','1','Programación I sección 25413, está en la carrera de COmputación',1,'[{\"added\": {}}]',22,1),(17,'2018-11-07 04:17:53','1','Pregunta \'Wena loh cabroh\' a la seccion 25413',1,'[{\"added\": {}}]',12,1),(18,'2018-11-07 04:18:04','1','Threshold object (1)',1,'[{\"added\": {}}]',18,1),(19,'2018-11-07 04:20:59','2','Gabriel D es: Profesor: False, Estudiante: True, S.Académico: False, D.Carrera: False',1,'[{\"added\": {}}]',17,1),(20,'2018-11-07 04:21:11','3','Matías T es: Profesor: True, Estudiante: True, S.Académico: False, D.Carrera: False',1,'[{\"added\": {}}]',17,1),(21,'2018-11-07 04:21:15','4','Eduardo Q es: Profesor: False, Estudiante: False, S.Académico: False, D.Carrera: True',1,'[{\"added\": {}}]',17,1),(22,'2018-11-07 04:21:21','5','Rodrigo C es: Profesor: True, Estudiante: False, S.Académico: False, D.Carrera: False',1,'[{\"added\": {}}]',17,1),(23,'2018-11-07 04:22:11','2','El usuario \'Gabriel D\' sigue el hilo Wena loh cabroh',1,'[{\"added\": {}}]',21,1),(24,'2018-11-07 04:22:20','3','El usuario \'Matías T\' sigue el hilo Wena loh cabroh',1,'[{\"added\": {}}]',21,1),(25,'2018-11-07 04:22:27','4','El usuario \'Rodrigo C\' sigue el hilo Wena loh cabroh',1,'[{\"added\": {}}]',21,1),(26,'2018-11-07 04:22:40','1','ThreadRanking object (1)',1,'[{\"added\": {}}]',13,1),(27,'2018-11-07 04:23:26','2','El usuario \'Matías T\' evaluó el hilo Wena loh cabroh con 5',1,'[{\"added\": {}}]',13,1),(28,'2018-11-07 04:25:55','4','El usuario Gabriel D en el hilo Wena loh cabroh preguntó Uwu',1,'[{\"added\": {}}]',11,1),(29,'2018-11-07 04:26:09','5','El usuario Gabriel D en el hilo Wena loh cabroh preguntó <3',1,'[{\"added\": {}}]',11,1),(30,'2018-11-07 04:26:17','6','El usuario Matías T en el hilo Wena loh cabroh preguntó 123',1,'[{\"added\": {}}]',11,1),(31,'2018-11-07 04:26:40','1','PostFollower object (1)',1,'[{\"added\": {}}]',15,1),(32,'2018-11-07 04:27:28','2','El usuario \'Matías T\' sigue el la pregunta Uwu',1,'[{\"added\": {}}]',15,1),(33,'2018-11-07 04:31:15','1','PostRanking object (1)',1,'[{\"added\": {}}]',10,1),(34,'2018-11-07 04:32:15','2','El usuario \'Matías T\' evaluó la pregunta Uwu con 7',1,'[{\"added\": {}}]',10,1),(35,'2018-11-07 04:36:52','1','el usuario Gabriel D comentó Wena pregunta men en la publicación Uwu',1,'[{\"added\": {}}]',23,1),(36,'2018-11-07 04:37:27','1','el usuario Matías T comentó Wena pregunta men en la publicación Uwu',2,'[{\"changed\": {\"fields\": [\"author\"]}}]',23,1),(37,'2018-11-07 04:37:41','2','el usuario Matías T comentó Te la creiste we en la publicación Uwu',1,'[{\"added\": {}}]',23,1),(38,'2018-11-07 04:38:03','1','CommentArchive object (1)',1,'[{\"added\": {}}]',19,1),(39,'2018-11-07 04:39:49','1','CommentRanking object (1)',1,'[{\"added\": {}}]',20,1),(40,'2018-11-07 04:40:52','2','El usuario \'Gabriel D\' evaluó el comentario Te la creiste we con 1',1,'[{\"added\": {}}]',20,1),(41,'2018-11-07 04:41:00','3','El usuario \'Matías T\' evaluó el comentario Wena pregunta men con 5',1,'[{\"added\": {}}]',20,1),(42,'2018-11-07 04:43:44','2','El usuario \'Matías T\' evaluó el hilo Wena loh cabroh con 5',2,'[]',13,1),(43,'2018-11-07 04:43:47','2','El usuario \'Matías T\' evaluó el hilo Wena loh cabroh con 0',2,'[{\"changed\": {\"fields\": [\"rating\"]}}]',13,1),(44,'2018-11-07 04:43:55','2','El usuario \'Matías T\' evaluó el hilo Wena loh cabroh con 0',2,'[]',13,1),(45,'2018-11-07 04:45:03','2','El usuario \'Matías T\' evaluó el hilo Wena loh cabroh con 1',2,'[{\"changed\": {\"fields\": [\"rating\"]}}]',13,1),(46,'2018-11-07 16:45:57','1','Meeting object (1)',1,'[{\"added\": {}}]',24,1),(47,'2018-11-07 16:47:45','1','Eduardo Q creó la reunión de: 2',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',24,1),(48,'2018-11-07 16:48:40','1','Minute object (1)',1,'[{\"added\": {}}]',27,1),(49,'2018-11-07 16:49:21','1','Member object (1)',1,'[{\"added\": {}}]',26,1),(50,'2018-11-07 16:52:18','2','Miembro Rodrigo C (Secretario Académico) de la Minuta: Asignación de salas con voto: Aceptada',1,'[{\"added\": {}}]',26,1),(51,'2018-11-07 16:54:41','1','El miembro Rodrigo C rechazó la minuta Asignación de salas por: no me gusta uwu',1,'[{\"added\": {}}]',25,1),(52,'2018-11-07 16:54:51','2','El miembro Matías T rechazó la minuta Asignación de salas por: <3',1,'[{\"added\": {}}]',25,1),(53,'2018-11-07 17:06:36','1','Reporte: El profe no responde con fecha 2018-11-07 14:06:21-03:00',1,'[{\"added\": {}}]',29,1),(54,'2018-11-07 17:07:41','2','Reporte: El profe no responde con fecha 2018-11-07 17:06:21+00:00 studiante Gabriel D al profesor Rodrigo C',1,'[{\"added\": {}}]',28,1),(55,'2018-11-07 17:15:42','1','El director Eduardo Q creó una auditoría a través de una alerta El profe no responde enviada por el alumno Gabriel D al profesor Rodrigo C',1,'[{\"added\": {}}]',30,1),(56,'2018-11-07 17:20:10','1','El director Eduardo Q creó una auditoría de minutas al usuario Rodrigo C',1,'[{\"added\": {}}]',31,1),(57,'2018-11-07 17:20:19','2','El director Eduardo Q creó una auditoría de minutas al usuario Rodrigo C',1,'[{\"added\": {}}]',31,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(29,'alertas','answerreport'),(28,'alertas','answerreportuser'),(30,'auditorias','foroaudit'),(31,'auditorias','minutesaudit'),(3,'auth','group'),(4,'auth','permission'),(2,'auth','user'),(5,'contenttypes','contenttype'),(24,'minutas','meeting'),(26,'minutas','member'),(27,'minutas','minute'),(25,'minutas','refuseminute'),(16,'retro','career'),(22,'retro','careersubjectsection'),(23,'retro','comment'),(19,'retro','commentarchive'),(20,'retro','commentranking'),(11,'retro','post'),(15,'retro','postfollower'),(10,'retro','postranking'),(14,'retro','section'),(8,'retro','student'),(9,'retro','subject'),(12,'retro','thread'),(21,'retro','threadfollower'),(13,'retro','threadranking'),(18,'retro','threshold'),(17,'retro','usertype'),(7,'retro_auth','userprofile'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-11-07 04:15:37'),(2,'auth','0001_initial','2018-11-07 04:15:38'),(3,'admin','0001_initial','2018-11-07 04:15:38'),(4,'admin','0002_logentry_remove_auto_add','2018-11-07 04:15:38'),(5,'contenttypes','0002_remove_content_type_name','2018-11-07 04:15:38'),(6,'auth','0002_alter_permission_name_max_length','2018-11-07 04:15:38'),(7,'auth','0003_alter_user_email_max_length','2018-11-07 04:15:38'),(8,'auth','0004_alter_user_username_opts','2018-11-07 04:15:38'),(9,'auth','0005_alter_user_last_login_null','2018-11-07 04:15:38'),(10,'auth','0006_require_contenttypes_0002','2018-11-07 04:15:38'),(11,'auth','0007_alter_validators_add_error_messages','2018-11-07 04:15:38'),(12,'auth','0008_alter_user_username_max_length','2018-11-07 04:15:38'),(13,'auth','0009_alter_user_last_name_max_length','2018-11-07 04:15:38'),(14,'retro_auth','0001_initial','2018-11-07 04:15:38'),(15,'retro_auth','0002_auto_20181107_0042','2018-11-07 04:15:38'),(16,'retro','0001_initial','2018-11-07 04:15:40'),(17,'sessions','0001_initial','2018-11-07 04:15:40'),(18,'retro','0002_auto_20181107_0135','2018-11-07 04:36:02'),(19,'retro','0003_auto_20181107_1343','2018-11-07 16:44:02'),(20,'minutas','0001_initial','2018-11-07 16:45:40'),(21,'minutas','0002_meeting_name','2018-11-07 16:47:12'),(22,'minutas','0003_auto_20181107_1404','2018-11-07 17:04:20'),(23,'alertas','0001_initial','2018-11-07 17:05:18'),(24,'auditorias','0001_initial','2018-11-07 17:14:55'),(25,'auditorias','0002_auto_20181107_1419','2018-11-07 17:19:55');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('gd38joueripphmk6zsf3c3bryh2aijig','YjRjN2QxYTM4MzBlMjA2Y2M1NjJjMGQ1MzFlOTUwNjk4ZWZkMjQyYTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDFhNDExZDNkZjBjNWMxYWVmNWY1NDY1YzY5YzgzZTdlNzJmZTQ5ZiIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2018-11-21 04:15:58');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `minutas_meeting`
--

DROP TABLE IF EXISTS `minutas_meeting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `minutas_meeting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `publish_date` datetime NOT NULL,
  `time` int(10) unsigned NOT NULL,
  `userprofile_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `minutas_meeting_userprofile_id_babfc4b2_fk_retro_aut` (`userprofile_id`),
  CONSTRAINT `minutas_meeting_userprofile_id_babfc4b2_fk_retro_aut` FOREIGN KEY (`userprofile_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `minutas_meeting`
--

LOCK TABLES `minutas_meeting` WRITE;
/*!40000 ALTER TABLE `minutas_meeting` DISABLE KEYS */;
INSERT INTO `minutas_meeting` VALUES (1,'2018-11-07 16:45:49',2,3,'Nombre Reunión');
/*!40000 ALTER TABLE `minutas_meeting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `minutas_member`
--

DROP TABLE IF EXISTS `minutas_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `minutas_member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(2) NOT NULL,
  `privilege` varchar(2) NOT NULL,
  `minute_id` int(11) NOT NULL,
  `userprofile_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `minutas_member_userprofile_id_minute_id_4a83f492_uniq` (`userprofile_id`,`minute_id`),
  KEY `minutas_member_minute_id_b86c1967_fk_minutas_minute_id` (`minute_id`),
  CONSTRAINT `minutas_member_userprofile_id_03c1d597_fk_retro_aut` FOREIGN KEY (`userprofile_id`) REFERENCES `retro_auth_userprofile` (`id`),
  CONSTRAINT `minutas_member_minute_id_b86c1967_fk_minutas_minute_id` FOREIGN KEY (`minute_id`) REFERENCES `minutas_minute` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `minutas_member`
--

LOCK TABLES `minutas_member` WRITE;
/*!40000 ALTER TABLE `minutas_member` DISABLE KEYS */;
INSERT INTO `minutas_member` VALUES (1,'EP','DC',1,3),(2,'AC','SA',1,4);
/*!40000 ALTER TABLE `minutas_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `minutas_minute`
--

DROP TABLE IF EXISTS `minutas_minute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `minutas_minute` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thematic` varchar(50) NOT NULL,
  `description` varchar(500) NOT NULL,
  `address` varchar(100) NOT NULL,
  `status` varchar(2) NOT NULL,
  `publish_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `minutas_minute`
--

LOCK TABLES `minutas_minute` WRITE;
/*!40000 ALTER TABLE `minutas_minute` DISABLE KEYS */;
INSERT INTO `minutas_minute` VALUES (1,'Asignación de salas','Curabitur suscipit suscipit tellus. Sed libero. Phasellus volutpat, metus eget egestas mollis, lacus lacus blandit dui, id egestas quam mauris ut lacus. Proin faucibus arcu quis ante. Sed augue ipsum, egestas nec, vestibulum et, malesuada adipiscing, dui.','Fusce pharetra convallis urna','EP','2018-11-07 17:04:20');
/*!40000 ALTER TABLE `minutas_minute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `minutas_refuseminute`
--

DROP TABLE IF EXISTS `minutas_refuseminute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `minutas_refuseminute` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(500) NOT NULL,
  `minute_id` int(11) NOT NULL,
  `userprofile_id` int(11) DEFAULT NULL,
  `publish_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `minutas_refuseminute_userprofile_id_minute_id_aeede31c_uniq` (`userprofile_id`,`minute_id`),
  KEY `minutas_refuseminute_minute_id_32baaf4d_fk_minutas_minute_id` (`minute_id`),
  CONSTRAINT `minutas_refuseminute_minute_id_32baaf4d_fk_minutas_minute_id` FOREIGN KEY (`minute_id`) REFERENCES `minutas_minute` (`id`),
  CONSTRAINT `minutas_refuseminute_userprofile_id_9ce2dba3_fk_retro_aut` FOREIGN KEY (`userprofile_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `minutas_refuseminute`
--

LOCK TABLES `minutas_refuseminute` WRITE;
/*!40000 ALTER TABLE `minutas_refuseminute` DISABLE KEYS */;
INSERT INTO `minutas_refuseminute` VALUES (1,'no me gusta uwu',1,4,'2018-11-07 17:04:20'),(2,'<3',1,2,'2018-11-07 17:04:20');
/*!40000 ALTER TABLE `minutas_refuseminute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_auth_userprofile`
--

DROP TABLE IF EXISTS `retro_auth_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_auth_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rut` varchar(12) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `retro_auth_userprofile_user_id_3f94f3bc_fk_auth_user_id` (`user_id`),
  CONSTRAINT `retro_auth_userprofile_user_id_3f94f3bc_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_auth_userprofile`
--

LOCK TABLES `retro_auth_userprofile` WRITE;
/*!40000 ALTER TABLE `retro_auth_userprofile` DISABLE KEYS */;
INSERT INTO `retro_auth_userprofile` VALUES (1,'1',2),(2,'2',3),(3,'3',4),(4,'Sin Rut',5);
/*!40000 ALTER TABLE `retro_auth_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_career`
--

DROP TABLE IF EXISTS `retro_career`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_career` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `director_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `retro_career_director_id_12f97c4e_fk_retro_auth_userprofile_id` (`director_id`),
  CONSTRAINT `retro_career_director_id_12f97c4e_fk_retro_auth_userprofile_id` FOREIGN KEY (`director_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_career`
--

LOCK TABLES `retro_career` WRITE;
/*!40000 ALTER TABLE `retro_career` DISABLE KEYS */;
INSERT INTO `retro_career` VALUES (1,'COmputación',1,3);
/*!40000 ALTER TABLE `retro_career` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_careersubjectsection`
--

DROP TABLE IF EXISTS `retro_careersubjectsection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_careersubjectsection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `career_id` int(11) NOT NULL,
  `section_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `retro_careersubjectsecti_career_id_subject_id_sec_89b249f4_uniq` (`career_id`,`subject_id`,`section_id`),
  KEY `retro_careersubjects_section_id_3024b49f_fk_retro_sec` (`section_id`),
  KEY `retro_careersubjects_subject_id_44be7682_fk_retro_sub` (`subject_id`),
  CONSTRAINT `retro_careersubjectsection_career_id_508f9fd5_fk_retro_career_id` FOREIGN KEY (`career_id`) REFERENCES `retro_career` (`id`),
  CONSTRAINT `retro_careersubjects_section_id_3024b49f_fk_retro_sec` FOREIGN KEY (`section_id`) REFERENCES `retro_section` (`id`),
  CONSTRAINT `retro_careersubjects_subject_id_44be7682_fk_retro_sub` FOREIGN KEY (`subject_id`) REFERENCES `retro_subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_careersubjectsection`
--

LOCK TABLES `retro_careersubjectsection` WRITE;
/*!40000 ALTER TABLE `retro_careersubjectsection` DISABLE KEYS */;
INSERT INTO `retro_careersubjectsection` VALUES (1,1,1,1);
/*!40000 ALTER TABLE `retro_careersubjectsection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_comment`
--

DROP TABLE IF EXISTS `retro_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(500) NOT NULL,
  `publish_date` datetime NOT NULL,
  `last_mod` datetime NOT NULL,
  `status` tinyint(1) NOT NULL,
  `author_id` int(11) DEFAULT NULL,
  `post_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `retro_comment_author_id_db72c0f9_fk_retro_auth_userprofile_id` (`author_id`),
  KEY `retro_comment_post_id_203f752c_fk_retro_post_id` (`post_id`),
  CONSTRAINT `retro_comment_author_id_db72c0f9_fk_retro_auth_userprofile_id` FOREIGN KEY (`author_id`) REFERENCES `retro_auth_userprofile` (`id`),
  CONSTRAINT `retro_comment_post_id_203f752c_fk_retro_post_id` FOREIGN KEY (`post_id`) REFERENCES `retro_post` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_comment`
--

LOCK TABLES `retro_comment` WRITE;
/*!40000 ALTER TABLE `retro_comment` DISABLE KEYS */;
INSERT INTO `retro_comment` VALUES (1,'Wena pregunta men','2018-11-07 04:36:06','2018-11-07 04:36:06',1,2,4),(2,'Te la creiste we','2018-11-07 04:37:29','2018-11-07 04:37:29',1,2,4);
/*!40000 ALTER TABLE `retro_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_commentarchive`
--

DROP TABLE IF EXISTS `retro_commentarchive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_commentarchive` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document` varchar(100) NOT NULL,
  `comment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `retro_commentarchive_comment_id_1dada43a_fk_retro_comment_id` (`comment_id`),
  CONSTRAINT `retro_commentarchive_comment_id_1dada43a_fk_retro_comment_id` FOREIGN KEY (`comment_id`) REFERENCES `retro_comment` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_commentarchive`
--

LOCK TABLES `retro_commentarchive` WRITE;
/*!40000 ALTER TABLE `retro_commentarchive` DISABLE KEYS */;
INSERT INTO `retro_commentarchive` VALUES (1,'Foro/Comment/2018/11/07/maxresdefault.jpg',2);
/*!40000 ALTER TABLE `retro_commentarchive` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_commentranking`
--

DROP TABLE IF EXISTS `retro_commentranking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_commentranking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` int(10) unsigned NOT NULL,
  `comment_id` int(11) NOT NULL,
  `userprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `retro_commentranking_userprofile_id_comment_id_b5dddfd7_uniq` (`userprofile_id`,`comment_id`),
  KEY `retro_commentranking_comment_id_31af9f7b_fk_retro_comment_id` (`comment_id`),
  CONSTRAINT `retro_commentranking_comment_id_31af9f7b_fk_retro_comment_id` FOREIGN KEY (`comment_id`) REFERENCES `retro_comment` (`id`),
  CONSTRAINT `retro_commentranking_userprofile_id_9557d7f4_fk_retro_aut` FOREIGN KEY (`userprofile_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_commentranking`
--

LOCK TABLES `retro_commentranking` WRITE;
/*!40000 ALTER TABLE `retro_commentranking` DISABLE KEYS */;
INSERT INTO `retro_commentranking` VALUES (1,5,1,1),(2,1,2,1),(3,5,1,2);
/*!40000 ALTER TABLE `retro_commentranking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_post`
--

DROP TABLE IF EXISTS `retro_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` varchar(500) NOT NULL,
  `publish_date` datetime NOT NULL,
  `last_mod` datetime NOT NULL,
  `status` tinyint(1) NOT NULL,
  `author_id` int(11) DEFAULT NULL,
  `thread_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `retro_post_author_id_12e2a141_fk_retro_auth_userprofile_id` (`author_id`),
  KEY `retro_post_thread_id_7fbbb220_fk_retro_thread_id` (`thread_id`),
  CONSTRAINT `retro_post_author_id_12e2a141_fk_retro_auth_userprofile_id` FOREIGN KEY (`author_id`) REFERENCES `retro_auth_userprofile` (`id`),
  CONSTRAINT `retro_post_thread_id_7fbbb220_fk_retro_thread_id` FOREIGN KEY (`thread_id`) REFERENCES `retro_thread` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_post`
--

LOCK TABLES `retro_post` WRITE;
/*!40000 ALTER TABLE `retro_post` DISABLE KEYS */;
INSERT INTO `retro_post` VALUES (4,'¿Cómo dejar de ser perkin?','Uwu','2018-11-07 04:23:59','2018-11-07 04:23:59',1,1,1),(5,'<3','<3','2018-11-07 04:26:00','2018-11-07 04:26:00',1,1,1),(6,'123123','123','2018-11-07 04:26:12','2018-11-07 04:26:12',1,2,1);
/*!40000 ALTER TABLE `retro_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_postfollower`
--

DROP TABLE IF EXISTS `retro_postfollower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_postfollower` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) NOT NULL,
  `userprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `retro_postfollower_post_id_userprofile_id_3ea72ba3_uniq` (`post_id`,`userprofile_id`),
  KEY `retro_postfollower_userprofile_id_a4adc9a2_fk_retro_aut` (`userprofile_id`),
  CONSTRAINT `retro_postfollower_post_id_80d8d64c_fk_retro_post_id` FOREIGN KEY (`post_id`) REFERENCES `retro_post` (`id`),
  CONSTRAINT `retro_postfollower_userprofile_id_a4adc9a2_fk_retro_aut` FOREIGN KEY (`userprofile_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_postfollower`
--

LOCK TABLES `retro_postfollower` WRITE;
/*!40000 ALTER TABLE `retro_postfollower` DISABLE KEYS */;
INSERT INTO `retro_postfollower` VALUES (1,4,1),(2,4,2);
/*!40000 ALTER TABLE `retro_postfollower` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_postranking`
--

DROP TABLE IF EXISTS `retro_postranking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_postranking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` int(10) unsigned NOT NULL,
  `post_id` int(11) NOT NULL,
  `userprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `retro_postranking_userprofile_id_post_id_e97709b9_uniq` (`userprofile_id`,`post_id`),
  KEY `retro_postranking_post_id_00f3094b_fk_retro_post_id` (`post_id`),
  CONSTRAINT `retro_postranking_post_id_00f3094b_fk_retro_post_id` FOREIGN KEY (`post_id`) REFERENCES `retro_post` (`id`),
  CONSTRAINT `retro_postranking_userprofile_id_ff644046_fk_retro_aut` FOREIGN KEY (`userprofile_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_postranking`
--

LOCK TABLES `retro_postranking` WRITE;
/*!40000 ALTER TABLE `retro_postranking` DISABLE KEYS */;
INSERT INTO `retro_postranking` VALUES (1,4,4,1),(2,7,4,2);
/*!40000 ALTER TABLE `retro_postranking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_section`
--

DROP TABLE IF EXISTS `retro_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_section` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nrc` varchar(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `retro_section_teacher_id_64546eef_fk_retro_auth_userprofile_id` (`teacher_id`),
  CONSTRAINT `retro_section_teacher_id_64546eef_fk_retro_auth_userprofile_id` FOREIGN KEY (`teacher_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_section`
--

LOCK TABLES `retro_section` WRITE;
/*!40000 ALTER TABLE `retro_section` DISABLE KEYS */;
INSERT INTO `retro_section` VALUES (1,'25413',1,4);
/*!40000 ALTER TABLE `retro_section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_student`
--

DROP TABLE IF EXISTS `retro_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `section_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `retro_student_student_id_section_id_4d4e1f43_uniq` (`student_id`,`section_id`),
  KEY `retro_student_section_id_0ca7fec6_fk_retro_section_id` (`section_id`),
  CONSTRAINT `retro_student_section_id_0ca7fec6_fk_retro_section_id` FOREIGN KEY (`section_id`) REFERENCES `retro_section` (`id`),
  CONSTRAINT `retro_student_student_id_22c4737a_fk_retro_auth_userprofile_id` FOREIGN KEY (`student_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_student`
--

LOCK TABLES `retro_student` WRITE;
/*!40000 ALTER TABLE `retro_student` DISABLE KEYS */;
/*!40000 ALTER TABLE `retro_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_subject`
--

DROP TABLE IF EXISTS `retro_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `subject_code` varchar(40) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_subject`
--

LOCK TABLES `retro_subject` WRITE;
/*!40000 ALTER TABLE `retro_subject` DISABLE KEYS */;
INSERT INTO `retro_subject` VALUES (1,'Programación I','1234',1);
/*!40000 ALTER TABLE `retro_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_thread`
--

DROP TABLE IF EXISTS `retro_thread`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_thread` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `publish_date` datetime NOT NULL,
  `status` tinyint(1) NOT NULL,
  `section_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `retro_thread_section_id_21bdb2fc_fk_retro_section_id` (`section_id`),
  CONSTRAINT `retro_thread_section_id_21bdb2fc_fk_retro_section_id` FOREIGN KEY (`section_id`) REFERENCES `retro_section` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_thread`
--

LOCK TABLES `retro_thread` WRITE;
/*!40000 ALTER TABLE `retro_thread` DISABLE KEYS */;
INSERT INTO `retro_thread` VALUES (1,'Wena loh cabroh','2018-11-07 04:17:46',1,1);
/*!40000 ALTER TABLE `retro_thread` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_threadfollower`
--

DROP TABLE IF EXISTS `retro_threadfollower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_threadfollower` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thread_id` int(11) NOT NULL,
  `userprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `retro_threadfollower_thread_id_userprofile_id_bc95f453_uniq` (`thread_id`,`userprofile_id`),
  KEY `retro_threadfollower_userprofile_id_3a0d596d_fk_retro_aut` (`userprofile_id`),
  CONSTRAINT `retro_threadfollower_thread_id_3d1adcbe_fk_retro_thread_id` FOREIGN KEY (`thread_id`) REFERENCES `retro_thread` (`id`),
  CONSTRAINT `retro_threadfollower_userprofile_id_3a0d596d_fk_retro_aut` FOREIGN KEY (`userprofile_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_threadfollower`
--

LOCK TABLES `retro_threadfollower` WRITE;
/*!40000 ALTER TABLE `retro_threadfollower` DISABLE KEYS */;
INSERT INTO `retro_threadfollower` VALUES (2,1,1),(3,1,2),(4,1,4);
/*!40000 ALTER TABLE `retro_threadfollower` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_threadranking`
--

DROP TABLE IF EXISTS `retro_threadranking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_threadranking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` int(10) unsigned NOT NULL,
  `thread_id` int(11) NOT NULL,
  `userprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `retro_threadranking_userprofile_id_thread_id_7b482c92_uniq` (`userprofile_id`,`thread_id`),
  KEY `retro_threadranking_thread_id_dc3d2021_fk_retro_thread_id` (`thread_id`),
  CONSTRAINT `retro_threadranking_thread_id_dc3d2021_fk_retro_thread_id` FOREIGN KEY (`thread_id`) REFERENCES `retro_thread` (`id`),
  CONSTRAINT `retro_threadranking_userprofile_id_ba519ae4_fk_retro_aut` FOREIGN KEY (`userprofile_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_threadranking`
--

LOCK TABLES `retro_threadranking` WRITE;
/*!40000 ALTER TABLE `retro_threadranking` DISABLE KEYS */;
INSERT INTO `retro_threadranking` VALUES (1,1,1,1),(2,1,1,2);
/*!40000 ALTER TABLE `retro_threadranking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_threshold`
--

DROP TABLE IF EXISTS `retro_threshold`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_threshold` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` int(10) unsigned NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `retro_threshold_teacher_id_5ab7c1b0_fk_retro_auth_userprofile_id` (`teacher_id`),
  CONSTRAINT `retro_threshold_teacher_id_5ab7c1b0_fk_retro_auth_userprofile_id` FOREIGN KEY (`teacher_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_threshold`
--

LOCK TABLES `retro_threshold` WRITE;
/*!40000 ALTER TABLE `retro_threshold` DISABLE KEYS */;
INSERT INTO `retro_threshold` VALUES (1,2,4);
/*!40000 ALTER TABLE `retro_threshold` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retro_usertype`
--

DROP TABLE IF EXISTS `retro_usertype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retro_usertype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher` tinyint(1) NOT NULL,
  `student` tinyint(1) NOT NULL,
  `sacademic` tinyint(1) NOT NULL,
  `dcareer` tinyint(1) NOT NULL,
  `userprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `retro_usertype_userprofile_id_09587f1e_fk_retro_aut` (`userprofile_id`),
  CONSTRAINT `retro_usertype_userprofile_id_09587f1e_fk_retro_aut` FOREIGN KEY (`userprofile_id`) REFERENCES `retro_auth_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retro_usertype`
--

LOCK TABLES `retro_usertype` WRITE;
/*!40000 ALTER TABLE `retro_usertype` DISABLE KEYS */;
INSERT INTO `retro_usertype` VALUES (2,0,1,0,0,1),(3,1,1,0,0,2),(4,0,0,0,1,3),(5,1,0,0,0,4);
/*!40000 ALTER TABLE `retro_usertype` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-07 20:29:04
