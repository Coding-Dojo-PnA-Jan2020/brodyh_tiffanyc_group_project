CREATE DATABASE  IF NOT EXISTS `order_application` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `order_application`;
-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: order_application
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
-- Table structure for table `addresses`
--

DROP TABLE IF EXISTS `addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addresses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `street` varchar(128) NOT NULL,
  `street2` varchar(128) DEFAULT NULL,
  `city` varchar(64) NOT NULL,
  `state` varchar(2) NOT NULL,
  `zip_code` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `addresses_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addresses`
--

LOCK TABLES `addresses` WRITE;
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `image_file_path` varchar(255) NOT NULL,
  `image_url_path` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (2,'Appetizers','2020-02-02 17:06:09','2020-02-02 17:06:09','F:\\Tiffany\\group-project/app/static/uploads/appetizers.jpg','uploads/appetizers.jpg'),(3,'Soups & Salads','2020-02-02 17:07:58','2020-02-02 17:07:58','F:\\Tiffany\\group-project/app/static/uploads/asian-chicken-salad.jpg','uploads/asian-chicken-salad.jpg'),(4,'Signature Dishes','2020-02-02 17:08:48','2020-02-02 17:08:48','F:\\Tiffany\\group-project/app/static/uploads/sweet-and-sour-chicken.jpg','uploads/sweet-and-sour-chicken.jpg'),(5,'Desserts','2020-02-02 17:09:26','2020-02-02 17:09:26','F:\\Tiffany\\group-project/app/static/uploads/the-great-wall-of-chocolate.jpg','uploads/the-great-wall-of-chocolate.jpg'),(6,'Beverages','2020-02-02 17:16:36','2020-02-02 17:16:36','F:\\Tiffany\\group-project/app/static/uploads/beverages.jpg','uploads/beverages.jpg');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menuitems`
--

DROP TABLE IF EXISTS `menuitems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menuitems` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `image_file_path` varchar(255) NOT NULL,
  `price` decimal(10,0) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `image_url_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_menuitems_categories1` (`category_id`),
  CONSTRAINT `fk_menuitems_categories1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menuitems`
--

LOCK TABLES `menuitems` WRITE;
/*!40000 ALTER TABLE `menuitems` DISABLE KEYS */;
INSERT INTO `menuitems` VALUES (10,'2020-02-02 17:18:32','2020-02-02 17:18:32','Crab Rangoon','Creamy crab filling, bell pepper and green onion, fried to perfection and served with a spicy plum sauce','F:\\Tiffany\\group-project/app/static/uploads/appetizers-crab-rangoon.jpg',10,2,'uploads/appetizers-crab-rangoon.jpg'),(11,'2020-02-02 17:19:17','2020-02-02 17:19:17','Edamame','Lightly steamed edamame, tossed in koscher salt with just a hint of spice','F:\\Tiffany\\group-project/app/static/uploads/appetizers-edamame.jpg',10,2,'uploads/appetizers-edamame.jpg'),(12,'2020-02-02 17:19:49','2020-02-02 17:19:49','Pork Dumplings','Steamed, then pan-fried, chive and pork dumplings, served with a light chili-soy sauce','F:\\Tiffany\\group-project/app/static/uploads/appetizers-pot-stickers.jpg',10,2,'uploads/appetizers-pot-stickers.jpg'),(13,'2020-02-02 17:20:11','2020-02-02 17:20:11','Pork Eggrolls','Hand-rolled and deep-fried savory pork, rice noodles, and julienned carrots, cabbage and mushrooms, served with a tangy sweet and sour sauce','F:\\Tiffany\\group-project/app/static/uploads/appetizers-eggrolls.jpg',10,2,'uploads/appetizers-eggrolls.jpg'),(14,'2020-02-02 17:21:32','2020-02-02 17:21:32','Tempura Calamari and Vegetables','A crisp medley of calamari, bell pepper, baby spinach and carrots, on a bed of rice noodles, drizzled with a sriracha-honey sauce','F:\\Tiffany\\group-project/app/static/uploads/appetizers-tempura.jpg',10,2,'uploads/appetizers-tempura.jpg'),(15,'2020-02-02 19:40:24','2020-02-02 19:40:24','Chinese Bird Nest','A trio of shrimp, scallops, and squid stir-fried with vegetables, aromatic garlic, ginger, and green onion in a spicy white sauce, served on a fried taro “nest”','F:\\Tiffany\\group-project/app/static/uploads/chinese-bird-nest.jpg',10,2,'uploads/chinese-bird-nest.jpg'),(16,'2020-02-02 19:41:07','2020-02-02 19:41:07','Coffee Chocolate Lava Cake','Molten chocolate cake and creamy milk chocolate ganache with a side of vanilla bean ice cream','F:\\Tiffany\\group-project/app/static/uploads/vietnamese-chocolate-lava-cake.jpg',6,5,'uploads/vietnamese-chocolate-lava-cake.jpg'),(17,'2020-02-02 19:41:30','2020-02-02 19:41:30','Six-Layer Chocolate Cake','Chocolate cake with a hint of roasted coffee, layered with chocolate frosting and semi-sweet chocolate chips, with fresh berries','F:\\Tiffany\\group-project/app/static/uploads/the-great-wall-of-chocolate.jpg',6,5,'uploads/the-great-wall-of-chocolate.jpg'),(18,'2020-02-02 19:42:18','2020-02-02 19:42:18','Bao Donuts','Deep-fried dough in cinnamon and sugar, served with miso-caramel, raspberry and coffee-vanilla dipping sauces','F:\\Tiffany\\group-project/app/static/uploads/bao-donuts.jpg',6,5,'uploads/bao-donuts.jpg'),(19,'2020-02-02 19:42:36','2020-02-02 19:42:36','Chinese Almond Tofu','Blended almond tofu over a strawberry coulis, topped with fresh strawberries and a blackberry','F:\\Tiffany\\group-project/app/static/uploads/strawberry-almond-tofu-dessert.jpg',6,5,'uploads/strawberry-almond-tofu-dessert.jpg'),(20,'2020-02-02 19:43:10','2020-02-02 19:43:10','Asian Caesar Salad','Grilled salmon on a bed of crisp romaine, parmesan, toasted sesame seeds and wonton croutons, served with a creamy Caesar dressing','F:\\Tiffany\\group-project/app/static/uploads/asian-caesar-salad.jpg',7,3,'uploads/asian-caesar-salad.jpg'),(21,'2020-02-02 19:44:38','2020-02-02 19:44:38','Egg Drop Soup','Egg, julienned carrots and green onion, in a velvety broth','F:\\Tiffany\\group-project/app/static/uploads/egg-drop-soup-bowl.jpg',7,3,'uploads/egg-drop-soup-bowl.jpg'),(22,'2020-02-02 19:45:31','2020-02-02 19:45:31','Hot & Sour Soup','Chicken, silken tofu, mushrooms, bamboo shoots and egg in a rich and tangy broth','F:\\Tiffany\\group-project/app/static/uploads/hot-and-sour-soup-bowl.jpg',7,3,'uploads/hot-and-sour-soup-bowl.jpg'),(23,'2020-02-02 19:45:50','2020-02-02 19:45:50','Mandarin Chicken Salad','Grilled chicken, julienned vegetables, cabbage, mandarin oranges, almonds, crispy chow mein, served with a mandarin vinaigrette','F:\\Tiffany\\group-project/app/static/uploads/asian-chicken-salad.jpg',7,3,'uploads/asian-chicken-salad.jpg'),(24,'2020-02-02 19:46:16','2020-02-02 19:46:16','Wonton Soup','House-made pork wontons, shrimp, mushrooms and green onion in a savory broth','F:\\Tiffany\\group-project/app/static/uploads/chinese-soups.jpg',7,3,'uploads/chinese-soups.jpg'),(25,'2020-02-02 19:47:14','2020-02-02 19:47:14','Sweet and Sour Chicken','Sweet & sour sauce, pineapple, onion, bell peppers, ginger, served with a side of steamed white rice','F:\\Tiffany\\group-project/app/static/uploads/sweet-and-sour-chicken.jpg',15,4,'uploads/sweet-and-sour-chicken.jpg'),(26,'2020-02-02 19:47:33','2020-02-02 19:47:33','Mongolian Beef','Sweet soy glaze, flank steak, garlic and green onion, served with a side of steamed white rice','F:\\Tiffany\\group-project/app/static/uploads/mongolian-beef.jpg',15,4,'uploads/mongolian-beef.jpg'),(27,'2020-02-02 19:48:07','2020-02-02 19:48:07','Miso Glazed Salmon','Grilled salmon, Asian mushrooms, spinach, bok choy and garlic-ginger aromatics with a miso glaze','F:\\Tiffany\\group-project/app/static/uploads/miso-glazed-salmon.jpg',15,4,'uploads/miso-glazed-salmon.jpg'),(28,'2020-02-02 19:48:35','2020-02-02 19:48:35','Ginger Chicken with Broccoli','Ginger-garlic aromatics, green onion, steamed broccoli, served with a side of steamed white rice','F:\\Tiffany\\group-project/app/static/uploads/ginger-chicken-with-broccoli.jpg',15,4,'uploads/ginger-chicken-with-broccoli.jpg'),(29,'2020-02-02 19:49:13','2020-02-02 19:49:13','Kung Pao Chicken','Lightly fried chicken in a spicy Sichuan chili sauce, peanuts, green onion, red chili peppers served with a side of steamed white rice','F:\\Tiffany\\group-project/app/static/uploads/kung-pao-chicken.jpg',15,2,'uploads/kung-pao-chicken.jpg'),(30,'2020-02-02 19:49:43','2020-02-02 19:49:43','Shrimp Fried Rice','Wok-tossed with shrimp, egg, carrots, bean sprouts, green onion and rice','F:\\Tiffany\\group-project/app/static/uploads/shrimp-rice.jpg',15,4,'uploads/shrimp-rice.jpg'),(31,'2020-02-02 19:50:04','2020-02-02 19:50:04','Chicken Lo Mein','Chicken, egg noodles, mushrooms in Asian vegetables in savory soy sauce','F:\\Tiffany\\group-project/app/static/uploads/signature-lo-mein.jpg',15,4,'uploads/signature-lo-mein.jpg');
/*!40000 ALTER TABLE `menuitems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_menuitems`
--

DROP TABLE IF EXISTS `order_menuitems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_menuitems` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `order_id` int(11) NOT NULL,
  `menuitem_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`order_id`,`menuitem_id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_orders_has_menu_items_menu_items1_idx` (`menuitem_id`),
  KEY `fk_orders_has_menu_items_orders1_idx` (`order_id`),
  CONSTRAINT `fk_orders_has_menu_items_menu_items1` FOREIGN KEY (`menuitem_id`) REFERENCES `menuitems` (`id`),
  CONSTRAINT `fk_orders_has_menu_items_orders1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_menuitems`
--

LOCK TABLES `order_menuitems` WRITE;
/*!40000 ALTER TABLE `order_menuitems` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_menuitems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `subtotal` decimal(10,0) DEFAULT NULL,
  `tax` decimal(10,0) DEFAULT NULL,
  `total` decimal(10,0) DEFAULT NULL,
  `is_delivery` tinyint(4) NOT NULL,
  `ready_by` datetime NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `payment_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_orders_users_idx` (`user_id`),
  KEY `fk_orders_payment_methods1_idx` (`payment_id`),
  CONSTRAINT `fk_orders_payment_methods1` FOREIGN KEY (`payment_id`) REFERENCES `payments` (`id`),
  CONSTRAINT `fk_orders_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` int(11) NOT NULL,
  `card_number` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_payment_users1_idx` (`user_id`),
  CONSTRAINT `fk_payment_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_addresses`
--

DROP TABLE IF EXISTS `user_addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_addresses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `address_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `address_id` (`address_id`),
  CONSTRAINT `user_addresses_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `user_addresses_ibfk_2` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_addresses`
--

LOCK TABLES `user_addresses` WRITE;
/*!40000 ALTER TABLE `user_addresses` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `column_name` tinyint(1) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (7,'2020-02-02 14:52:44','2020-02-20 20:25:36','Admin','Admin','admin@gmail.com','pbkdf2:sha256:150000$3Z9SVj8w$934fece2b4db4f3d8772abaedf62dacc1e462b1cd2b824870c5e017f8be10b9b','000-867-5309',NULL,1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'order_application'
--

--
-- Dumping routines for database 'order_application'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-20 20:28:54
