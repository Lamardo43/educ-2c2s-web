-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: std-mysql    Database: std_2408_exam
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book_genres`
--

DROP TABLE IF EXISTS `book_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_genres` (
  `book_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  PRIMARY KEY (`book_id`,`genre_id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `book_genres_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE,
  CONSTRAINT `book_genres_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_genres`
--

LOCK TABLES `book_genres` WRITE;
/*!40000 ALTER TABLE `book_genres` DISABLE KEYS */;
INSERT INTO `book_genres` VALUES (105,1),(105,2),(107,6),(107,7),(107,9),(86,10);
/*!40000 ALTER TABLE `book_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `year` int(11) NOT NULL,
  `publisher` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `pages` int(11) NOT NULL,
  `cover_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cover_id` (`cover_id`),
  CONSTRAINT `books_ibfk_1` FOREIGN KEY (`cover_id`) REFERENCES `covers` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (13,'Things Fall Apart','',1958,'','Chinua Achebe',209,18),(14,'Fairy tales','',1836,'','Hans Christian Andersen',784,19),(15,'The Divine Comedy','',1315,'','Dante Alighieri',928,20),(16,'The Epic Of Gilgamesh','',-1700,'','Unknown',160,21),(17,'The Book Of Job','',-600,'','Unknown',176,22),(18,'One Thousand and One Nights','',1200,'','Unknown',288,23),(19,'Njel\'s Saga','',1350,'','Unknown',384,24),(20,'Pride and Prejudice','',1813,'','Jane Austen',226,25),(21,'Molloy, Malone Dies, The Unnamable, the trilogy','',1952,'','Samuel Beckett',256,26),(22,'The Decameron','',1351,'','Giovanni Boccaccio',1024,27),(23,'Ficciones','',1965,'','Jorge Luis Borges',224,28),(24,'Wuthering Heights','',1847,'','Emily Bronter',342,29),(25,'Journey to the End of the Night','',1932,'','Louis-Ferdinand Caine',505,30),(26,'Don Quijote De La Mancha','',1610,'','Miguel de Cervantes',1056,31),(27,'The Canterbury Tales','',1450,'','Geoffrey Chaucer',544,32),(28,'Stories','',1886,'','Anton Chekhov',194,33),(29,'Nostromo','',1904,'','Joseph Conrad',320,34),(30,'Great Expectations','',1861,'','Charles Dickens',194,35),(31,'Jacques the Fatalist','',1796,'','Denis Diderot',596,36),(32,'Berlin Alexanderplatz','',1929,'','Alfred Dublin',600,37),(33,'Crime and Punishment','',1866,'','Fyodor Dostoevsky',551,38),(34,'The Idiot','',1869,'','Fyodor Dostoevsky',656,39),(35,'The Possessed','',1872,'','Fyodor Dostoevsky',768,40),(36,'The Brothers Karamazov','',1880,'','Fyodor Dostoevsky',824,41),(37,'Middlemarch','',1871,'','George Eliot',800,42),(38,'Invisible Man','',1952,'','Ralph Ellison',581,43),(39,'Medea','',-431,'','Euripides',104,44),(40,'Absalom, Absalom!','',1936,'','William Faulkner',313,45),(41,'The Sound and the Fury','',1929,'','William Faulkner',326,46),(42,'Madame Bovary','',1857,'','Gustave Flaubert',528,47),(43,'Sentimental Education','',1869,'','Gustave Flaubert',606,48),(44,'One Hundred Years of Solitude','',1967,'','Gabriel Garcia Morquez',417,49),(45,'Love in the Time of Cholera','',1985,'','Gabriel Garcia Marquez',368,50),(49,'The Devil to Pay in the Backlands','',1956,'','Joao Guimaraes Rosa',494,54),(50,'Hunger','',1890,'','Knut Hamsun',176,55),(51,'The Old Man and the Sea','',1952,'','Ernest Hemingway',128,56),(52,'Iliad','',-735,'','Homer',608,57),(53,'Odyssey','',-800,'','Homer',374,58),(54,'A Doll\'s House','',1879,'','Henrik Ibsen',68,59),(55,'Ulysses','',1922,'','James Joyce',228,60),(56,'Stories','',1924,'','Franz Kafka',488,61),(57,'The Trial','',1925,'','Franz Kafka',160,62),(58,'The Castle','',1926,'','Franz Kafka',352,63),(60,'The Sound of the Mountain','',1954,'','Yasunari Kawabata',288,65),(63,'Independent People','',1934,'','Halldar Laxness',470,68),(64,'The Golden Notebook','',1962,'','Doris Lessing',688,69),(65,'Pippi Longstocking','',1945,'','Astrid Lindgren',160,70),(69,'Moby Dick','',1851,'','Herman Melville',378,74),(70,'Essays','',1595,'','Michel de Montaigne',404,75),(71,'History','',1974,'','Elsa Morante',600,76),(72,'Beloved','',1987,'','Toni Morrison',321,77),(73,'The Tale of Genji','',1006,'','Murasaki Shikibu',1360,78),(75,'Lolita','',1955,'','Vladimir Nabokov',317,80),(76,'Nineteen Eighty-Four','',1949,'','George Orwell',272,81),(77,'Metamorphoses','',100,'','Ovid',576,82),(78,'The Book of Disquiet','',1928,'','Fernando Pessoa',272,83),(79,'Tales','',1950,'','Edgar Allan Poe',842,84),(80,'In Search of Lost Time','',1920,'','Marcel Proust',2408,85),(81,'Gargantua and Pantagruel','',1533,'','Francois Rabelais',623,86),(82,'The Masnavi','',1236,'','Rumi',438,87),(83,'Midnight\'s Children','',1981,'','Salman Rushdie',536,88),(85,'Season of Migration to the North','',1966,'','Tayeb Salih',139,90),(86,'Blindness','',1995,'publisher','Jose Saramago',352,91),(87,'Hamlet','',1603,'','William Shakespeare',432,92),(88,'King Lear','',1608,'','William Shakespeare',384,93),(89,'Othello','',1609,'','William Shakespeare',314,94),(90,'Oedipus the King','',-430,'','Sophocles',88,95),(91,'The Red and the Black','',1830,'','Stendhal',576,96),(92,'The Life And Opinions of Tristram Shandy','',1760,'','Laurence Sterne',640,97),(94,'Gulliver\'s Travels','',1726,'','Jonathan Swift',178,99),(105,'Иван и его путешествие в Чернобыль','**\"Иван и его путешествие в Чернобыль\"** — это захватывающая история о мужестве и решимости одного человека, который решает исследовать зону отчуждения Чернобыльской АЭС. Иван, главный герой книги, сталкивается с вызовом познания запретной зоны, где ещё витает тень катастрофы 1986 года.\r\n\r\nВ своём путешествии Иван сталкивается с различными трудностями и опасностями, но его любопытство и стремление к пониманию истории места подталкивают его вперёд. Он встречает местных жителей и исследователей, каждый из которых вносит свой вклад в понимание последствий Чернобыльской катастрофы.\r\n\r\nКнига предлагает читателю уникальную возможность заглянуть в сердце запретной зоны через глаза отважного исследователя. Она обращает внимание на экологические и социальные аспекты последствий катастрофы, а также на силу человеческого духа в условиях экстремальных испытаний. **\"Иван и его путешествие в Чернобыль\"** является увлекательной и вдохновляющей книгой о том, как исследование прошлого может помочь нам лучше понять наше настоящее.\r\n',2004,'Неизвестен','Жизнь',228,101),(107,'Книга1','# Заголовок первого уровня\n\n## Заголовок второго уровня\n\n### Заголовок третьего уровня\n\nТекст с *курсивом* и **жирным**.\n\nСписок:\n\n- Элемент списка 1\n- Элемент списка 2\n  - Вложенный элемент списка\n- Элемент списка 3\n\nНумерованный список:\n\n1. Пункт 1\n2. Пункт 2\n3. Пункт 3&gt;&gt;\n\nГоризонтальная черта:\n\n---\n\n&gt; Цитата. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\n[Ссылка на Google](https://www.google.com)\n\n![Изображение](https://sun1-27.userapi.com/s/v1/ig2/Qx6X-jJaWZvAYbvYCMs9_qz8vfm0OExQMM-pNlagK6RJcZVCi1iP0dgtlLSvrQzqlbufMfQekR2a8u1Dgvr7IFen.jpg?size=200x0&amp;quality=96&amp;crop=0,0,1000,1000&amp;ava=1)\n\nТаблица:\n\n| Заголовок 1 | Заголовок 2 |\n|-------------|-------------|\n| Ячейка 1    | Ячейка 2    |\n| Ячейка 3    | Ячейка 4    |\n\n',50001,'publisher1','author1',2,101);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `covers`
--

DROP TABLE IF EXISTS `covers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `covers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mime_type` varchar(255) NOT NULL,
  `filename` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `covers`
--

LOCK TABLES `covers` WRITE;
/*!40000 ALTER TABLE `covers` DISABLE KEYS */;
INSERT INTO `covers` VALUES (18,'','531bd571bbc87445042e637f6d58e091.png'),(19,'','0530ffda1b9c8df570400e16fef5c59a.png'),(20,'','57ed28b1e35a49656f765102d02c2cdb.png'),(21,'','626bac166a315817310958a2499a7248.png'),(22,'','28e862da8ca2adcaf8a8c42bf5637833.png'),(23,'','359acd8b6bdc9b8fefceb90483589d20.png'),(24,'','3230c81589dc581ad0c34fa31c08e724.png'),(25,'','a046a633792a0645a105023593130283.png'),(26,'','df9668db3f4143b06e4f3647c68e3e78.png'),(27,'','5715b0098ad324b118a2bd593e873f65.png'),(28,'','bddef27a7ccc603744cfa37ddb27affd.png'),(29,'','1df6b550c6256314c4ddd7b7460e2968.png'),(30,'','33658c6e93131923bbcad23f0d0f738d.png'),(31,'','f3049e88ca7ea9dcd990438ed63b0336.png'),(32,'','9b9777fc2d3b6e98da68905c0f9d6b1f.png'),(33,'','74f2a846847a3030f04f7519de1e4161.png'),(34,'','4171ba1252c915ec13fc9bdd3829a956.png'),(35,'','f2f1576816cd78babf1f87418a8bdf3b.png'),(36,'','1c525574a11e3302a1e7875b6e01df5d.png'),(37,'','091e66b93625bed5541aa0878329127d.png'),(38,'','ad7311ca9e16626568b7ae0f29be8655.png'),(39,'','f07c2b2e0dfd8195cad5be860acd9821.png'),(40,'','3a2c0ba0efde6b8878771e5168b622fc.png'),(41,'','9109a16ee90133e2413ec53b7c865f1a.png'),(42,'','067d317d2f71a48b9ab508c2fedc49fd.png'),(43,'','338648af3fe1b849a6c1fe1fad47aa3c.png'),(44,'','ba58c0e49ea5424933409982586e95e0.png'),(45,'','d4fb56bb4f6d81380a03a92d541334e0.png'),(46,'','327702d36948ec57530954f6985ceda6.png'),(47,'','24928a16c85740d9d8d0a8fb987e4aea.png'),(48,'','46f220dccbdebeaba2da91c22a8f7a1e.png'),(49,'','d152116e371b2dc585c140ba4f22f049.png'),(50,'','333c86de3013efcd3bf28091a02f8db7.png'),(54,'','0af9492ad8a9e7492a7da8f0beaca8e8.png'),(55,'','b92e2ea3a681c964e02926d2e72e1c01.png'),(56,'','ca6917e9a627bade6cb258ba1e9ae527.png'),(57,'','60d940501c18541fef0a8445ae7d611a.png'),(58,'','3b0101d241f0f8b22e4c6d18be4b5041.png'),(59,'','d9dff0d6836f51fc4ded25047fffe78a.png'),(60,'','f13cd6f01f149428ebd3f31029f35c74.png'),(61,'','2d3de7a74891bf39de0700cf4b6f2d9c.png'),(62,'','854be0f272d86dfcc91aaa25fb91e5a4.png'),(63,'','ba804f34d017dd43ced15917ba4e5150.png'),(65,'','63a470c061c36583a2a879f4d6c593dd.png'),(68,'','8344d8f92d228ae24a989630482e1473.png'),(69,'','0d52dd84a140693a427ef2eedf80cbb6.png'),(70,'','dc47c3179552351901a84d24e3683a66.png'),(74,'','fff638c7f4b0c890e5a5aa2ef99b480b.png'),(75,'','39656a4a0f77627cbf6a7df4aeaa7663.png'),(76,'','93dc4ce206bd2eef67cf0a2a6ce455a9.png'),(77,'','60f5d74716bdb1c31fa132c4150d5c02.png'),(78,'','2a78606de7eabd11bd23821123d52e37.png'),(80,'','a515ae66ec75c5d6482fafe04e8035d7.png'),(81,'','a59d6c81ea2bdd0bb1197bb4f0549646.png'),(82,'','f9d9bf2259d2713d5bedc305cbcf4d5e.png'),(83,'','30f9669290197d253fe67d972345b756.png'),(84,'','e14fccabc69d147a5e001b0253f09981.png'),(85,'','60cb285dba4c01198d144a7bf02ce24a.png'),(86,'','6a4baa8066cedac9770fe3c6e81e1a8d.png'),(87,'','01eb4a1bf51a2d3dbd15599814b90b1e.png'),(88,'','3a3d1a5562d33a52283e4dbe7523a43f.png'),(90,'','1b1025b56cc9a5e2f31507f0c939c1a0.png'),(91,'','85cb785ff29d39e8e75726899938d794.png'),(92,'','913f4b39eb70897e361316c9f3ca7eb5.png'),(93,'','b9ce80571e8e44ea2cd8509926ec0f37.png'),(94,'','a7aa09eb723a22479f20d20d5ccfbbe8.png'),(95,'','5bfddc38fdb0996f7f6522a357e29662.png'),(96,'','91e03978c6eba0271167b06421d8ff68.png'),(97,'','a70b3b75099ee660aef9ba9177d240d9.png'),(99,'','e89e8c25be09502584e05f1fa62ce09c.png'),(101,'image/jpeg','03ea1b5400cd14940871dd9e97f87eaf.png');
/*!40000 ALTER TABLE `covers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES `genres` WRITE;
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
INSERT INTO `genres` VALUES (5,'Biography'),(4,'Fantasy'),(1,'Fiction'),(6,'History'),(7,'Mystery'),(2,'Non-Fiction'),(9,'Romance'),(3,'Science Fiction'),(8,'Thriller'),(10,'Young Adult');
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `review_text` text NOT NULL,
  `date_added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `book_id` (`book_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE,
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,86,1,5,'Super!','2024-06-14 13:00:21'),(2,86,2,4,'Не такое((','2024-06-14 13:27:44'),(3,105,1,5,'Я в восторге!!!!','2024-06-14 14:50:10'),(4,107,1,1,'Фотография не понравилась','2024-06-15 10:59:07');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Admin','Administrator with full access'),(2,'Moderator','Moderator with not full access'),(3,'User','Regular user with limited access');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) DEFAULT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8','Admin','Admin',NULL,1),(2,'user','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8','Doe','John','A.',3),(3,'moderator','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8','Smith','Jane','B.',2);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-15 14:01:09
