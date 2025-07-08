-- Adminer 5.3.0 MySQL 9.3.0 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `cgvbot` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cgvbot`;

DROP TABLE IF EXISTS `echanges`;
CREATE TABLE `echanges` (
  `id` int NOT NULL AUTO_INCREMENT,
  `prompt` text NOT NULL,
  `reponse` text NOT NULL,
  `date` datetime NOT NULL,
  `statut` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `statut` (`statut`),
  CONSTRAINT `echanges_ibfk_1` FOREIGN KEY (`statut`) REFERENCES `statuts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `statuts`;
CREATE TABLE `statuts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `libelle` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `libelle` (`libelle`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `statuts` (`id`, `libelle`) VALUES
(2,	'erreur'),
(1,	'succes');

-- 2025-07-08 12:55:52 UTC