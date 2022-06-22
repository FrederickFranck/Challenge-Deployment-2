CREATE DATABASE `steamdb`;

USE steamdb;

CREATE TABLE `Categories`  (
  `ID` int NOT NULL,
  `Description` text NULL,
  PRIMARY KEY (`ID`)
);

CREATE TABLE `Game-Categories`  (
  `ID` int NOT NULL,
  `Game_ID` int NULL,
  `Category_ID` int NULL,
  PRIMARY KEY (`ID`)
);

CREATE TABLE `Game-Genres`  (
  `ID` int NOT NULL,
  `Game_ID` int NULL,
  `Genre_ID` int NULL,
  PRIMARY KEY (`ID`)
);

CREATE TABLE `Games`  (
  `ID` int NOT NULL,
  `Name` varchar(255) NULL,
  `Description` text NULL,
  `Price` decimal(10, 2) NULL,
  `Developer` varchar(255) NULL,
  `Win_Support` boolean,
  `Mac_Support` boolean,
  `Linux_Support` boolean,
  `Pos_Review` int NULL,
  `Neg_Review` int NULL,
  PRIMARY KEY (`ID`)
);

CREATE TABLE `Genres`  (
  `ID` int NOT NULL,
  `Description` varchar(255) NULL,
  PRIMARY KEY (`ID`)
);

CREATE TABLE `Languages`  (
  `ID` int NOT NULL,
  `Name` varchar(255) NULL,
  PRIMARY KEY (`ID`)
);

CREATE TABLE `Supported-Languages`  (
  `ID` int NOT NULL,
  `Game_ID` int NULL,
  `Language_ID` int NULL,
  PRIMARY KEY (`ID`)
);

ALTER TABLE `Game-Categories` ADD CONSTRAINT `Game_ID` FOREIGN KEY (`Game_ID`) REFERENCES `Games` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Game-Categories` ADD CONSTRAINT `Category_ID` FOREIGN KEY (`Category_ID`) REFERENCES `Categories` (`ID`) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE `Game-Genres` ADD CONSTRAINT `Game_ID` FOREIGN KEY (`Game_ID`) REFERENCES `Games` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Game-Genres` ADD FOREIGN KEY (`Genre_ID`) REFERENCES `Genres` (`ID`) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE `Supported-Languages` ADD CONSTRAINT `Game_ID` FOREIGN KEY (`Game_ID`) REFERENCES `Games` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Supported-Languages` ADD CONSTRAINT `Language_ID` FOREIGN KEY (`Language_ID`) REFERENCES `Languages` (`ID`) ON DELETE SET NULL ON UPDATE CASCADE;

