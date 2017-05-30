-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: testdb
-- ------------------------------------------------------
-- Server version	5.7.18-log

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
-- Table structure for table `sentences_test`
--

DROP TABLE IF EXISTS `sentences_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sentences_test` (
  `sentenceid` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(100) NOT NULL,
  `sentencedutch` varchar(200) NOT NULL,
  `sentenceenglish` varchar(200) NOT NULL,
  `sentencemaas` varchar(200) NOT NULL,
  `nrofrecordings` int(11) NOT NULL,
  PRIMARY KEY (`sentenceid`),
  UNIQUE KEY `sentencedutch_UNIQUE` (`sentencedutch`),
  UNIQUE KEY `sentenceenglish_UNIQUE` (`sentenceenglish`),
  UNIQUE KEY `sentencemaas_UNIQUE` (`sentencemaas`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sentences_test`
--

LOCK TABLES `sentences_test` WRITE;
/*!40000 ALTER TABLE `sentences_test` DISABLE KEYS */;
INSERT INTO `sentences_test` VALUES (1,'handig','Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag, Zaterdag, Zondag','Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday','Maondag, Dinsdag, Goonsdag, Donderdag, Vriedag, Zaoterdag, Zoondag',0),(2,'getallen','een, twee, drie, vier, vijf, zes, zeven, acht, negen, tien, elf, twaalf, dertien, veertien, vijftien, twintig, eenentwintig, tweeentwintig, dertig, veertig, vijftig, honderd, duizend, miljoen','one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, twenty, twenty-one, twenty-two, thirty, fourty, fifty, hundred, one-thousand, one-million','ein, twie, drei, veer, vijf, zès, zeve, ach, nege, tien, èlf, twaalf, dertien, veertien, vieftien, twinteg, einentwinteg, twieëntwinteg, derteg, veerteg, viefteg, hoonderd, doezend, miljoen',0),(3,'getallen','elfde van de elfde','Eleventh of the eleventh','èlfde vaan d’n èlfde',0),(4,'praktische zaken','Waar is hier ergens een bank of een geldautomaat?','Where is a bank or ATM somewhere around here?','Boe is hei örges ’n baank of ‘ne geldotomaat?',0),(5,'praktische zaken','Wat is het wachtwoord om internettoegang te krijgen?','What is the password to get internet access?','Wat is ’t wachwoord um internèttouwgaank te kriege?',0),(6,'praktische zaken','Weet iemand ergens een internetcafé?','Does anyone know an internet cafe around?','Wèt iemes örges ’n internètcafé?',0),(7,'praktische zaken','Hoeveel foto’s kan ik met deze geheugenkaart maken?','How many pictures can I take with this memory card?','Wieväöl foto’s kin iech mèt dees geheugekaart make?',0),(8,'praktische zaken','Waar kan ik rustig een goede brief schrijven?','Where can I quietly write a good letter?','Boe kin iech rösteg ‘ne gooje breef sjrieve?',0),(9,'weer','Gaat het vandaag regenen?','Is it going to rain today?','Geit ’t vendaog regene?',0),(10,'weer','Wat voor ’n weer wordt het morgen?','What kind of weather will it be tomorrow?','Wat veur e weer weurt ’t mörge?',0),(11,'transport','Hoeveel kilometer heb je vandaag gefietst?/gewandeld?','How many kilometres did you ride/walk today?','Wieväöl kilometer höbste vendaog gefiets?/gewandeld?',0),(12,'transport','Hoe ver is het naar de parkeergarage?','How far is it to the parking garage?','Wie wied is ’t nao de parkeergraasj?',0),(13,'transport','Ik heb het leren zadel van de fiets kapot.','I broke the saddle of the bike.','Iech höb ’t lere zadel vaan m’ne fiets kepot.',0),(14,'transport','Hoe kan ik al lopend het station vinden?','How can I find the station while walking?','Wie kin iech al loupentere de statie vinde?',0),(15,'transport','Waar in Eijsden is het goed koffie met vlaai eten na het wandelen?','Where in Eijsden can one have good coffee with pie to eat after walking?','Boe in Eijsde is ’t good koffie mèt vlaoj ete nao ’t wandele?',0),(16,'ontmoetingen','Gefeliciteerd met uw verjaardag!','Congratulations on your birthday!','Perficia mèt eure verjaordaag!',0),(17,'ontmoetingen','Waar woont Andre Rieu en Beppie Kraft?','Where do Andre Rieu and Beppie Kraft live?','Boe woent André Rieu en Beppie Kraft?',0),(18,'ontmoetingen','Goeiemorgen, Haije, Dag, Tot ziens, Welterusten, Gezondheid','Good morning, Hi, Bye, See you later, Goodnight, feel better','Goojemörge, Hoi, Dag, Tot zeens, Welteröste, Gezoondheid',0),(19,'Iemand versieren','Wat kan ik hier doen?','What can I do here?','Wat kin iech hei doen?',0),(20,'Iemand versieren','Geef me eens een zoen','Give me a kiss','Geef miech ‘ns ‘ne poen',0),(21,'Iemand versieren','Wat denk je, zijn zij verliefd aan het praten?','What do you think, are they in love with talking?','Wat dinkste, zien zie verleef aon ’t praote?',0),(22,'Iemand versieren','Je bent een schatje','You are a darling','De bis ‘ne sjat',0),(23,'Iemand versieren','Wanneer zien we elkaar weer?','When do we see each other again?','Wienie zien v’r us weer?',0),(24,'Iemand versieren','Ik weet zeker dat ik lang over je gedroomd hebt','I\'m sure that I\'ve dreamt for a long time','Iech wèt zeker tot iech lang euver d’ch gedruimp höb',0),(25,'Iemand versieren','Mijn mannetje, wat ben je mooi!','My man, what a beauty you are!','Mie menneke, wat biste sjoen!',0),(26,'Iemand versieren','Zij zien elkaar in de grote spiegel','They see each other in the big mirror','Zie zien z’ch in de groete spiegel',0),(27,'Iemand versieren','Je hebt een mooie jas, een mooie broek en een mooi hemd aan','You have a nice coat, nice pants and a beautiful shirt.','De höbs ‘ne sjoene jas, ’n sjoen brook en e sjoen humme aon',0),(28,'hotel, winkel en cafe','Kan ik mijn mooie hemden hier laten stomen?','Can I put my beautiful shirt here?','Kin iech mien sjoen hummes hei laote stome?',0),(29,'hotel, winkel en cafe','Mag je hond mee naar onze kamer?','Can you bring your dog to our room?','Maag dienen hoond mèt nao us kamer?',0),(30,'hotel, winkel en cafe','Heeft u vier grote glazen sjoes voor me?','Do you have four big glasses for me?','Höb g’r veer groete glazer sjoes veur m’ch?',0);
/*!40000 ALTER TABLE `sentences_test` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-30 15:17:27
