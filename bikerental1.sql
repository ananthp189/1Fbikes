/*
 Navicat Premium Data Transfer

 Source Server         : mysql3
 Source Server Type    : MySQL
 Source Server Version : 80020
 Source Host           : localhost:3306
 Source Schema         : bikerental

 Target Server Type    : MySQL
 Target Server Version : 80020
 File Encoding         : 65001

 Date: 01/02/2021 10:36:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Bike
-- ----------------------------
DROP TABLE IF EXISTS `Bike`;
CREATE TABLE `Bike` (
  `bid` int NOT NULL COMMENT 'bike ID',
  `bstatus` int NOT NULL COMMENT 'bike status',
  `bGPS` varchar(255) DEFAULT NULL COMMENT 'bike location',
  `barea` varchar(100) DEFAULT NULL COMMENT 'bike area',
  `bpassword` varchar(100) DEFAULT NULL COMMENT 'bike password',
  `busage` varchar(50) DEFAULT NULL COMMENT 'bike usage',
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Bike
-- ----------------------------
BEGIN;
INSERT INTO `Bike` VALUES (101, 2, NULL, NULL, '1224', '0');
INSERT INTO `Bike` VALUES (102, 2, NULL, NULL, '2345', '1');
COMMIT;

-- ----------------------------
-- Table structure for Payment
-- ----------------------------
DROP TABLE IF EXISTS `Payment`;
CREATE TABLE `Payment` (
  `pid` int NOT NULL COMMENT 'payment id',
  `pstatus` varchar(100) DEFAULT NULL COMMENT 'payment status',
  `starttime` varchar(100) DEFAULT NULL COMMENT 'start time',
  `endtime` varchar(100) DEFAULT NULL COMMENT 'end time',
  `duration` varchar(100) DEFAULT NULL COMMENT 'rent time',
  `oribill` varchar(100) DEFAULT NULL COMMENT 'original bill',
  `discount` varchar(100) DEFAULT NULL COMMENT 'bill after discount',
  `startGPS` varchar(255) DEFAULT NULL COMMENT 'start gps',
  `endGPS` varchar(255) DEFAULT NULL COMMENT 'end gps',
  `uid` int DEFAULT NULL COMMENT 'user id',
  `bid` int DEFAULT NULL COMMENT 'bike id',
  PRIMARY KEY (`pid`),
  KEY `u_payment` (`uid`),
  KEY `b_payment2` (`bid`),
  CONSTRAINT `b_payment2` FOREIGN KEY (`bid`) REFERENCES `Bike` (`bid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `u_payment` FOREIGN KEY (`uid`) REFERENCES `Users` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Payment
-- ----------------------------
BEGIN;
INSERT INTO `Payment` VALUES (1101, '0', '12:45', '13:15', '30min', '6', '4', NULL, NULL, 1001, 102);
COMMIT;

-- ----------------------------
-- Table structure for Users
-- ----------------------------
DROP TABLE IF EXISTS `Users`;
CREATE TABLE `Users` (
  `uid` int NOT NULL COMMENT 'userID',
  `upassword` varchar(100) NOT NULL COMMENT 'userpassword',
  `uname` varchar(100) NOT NULL COMMENT 'username',
  `Tel` int DEFAULT NULL COMMENT 'telephone',
  `bankcard` varchar(100) DEFAULT NULL COMMENT 'bankcard',
  `usertype` varchar(100) DEFAULT NULL COMMENT 'user type',
  `uGPS` varchar(255) DEFAULT NULL COMMENT 'user location',
  `uarea` varchar(255) DEFAULT NULL COMMENT 'user area',
  `totaltime` varchar(255) DEFAULT NULL COMMENT 'total use time',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Users
-- ----------------------------
BEGIN;
INSERT INTO `Users` VALUES (1001, '123456', 'lili', 12345678, '234565432', '0', NULL, NULL, NULL);
INSERT INTO `Users` VALUES (1002, '123456', 'peter', 2345432, '557754432', '0', NULL, NULL, NULL);
INSERT INTO `Users` VALUES (1003, '234543', 'alex', 32445, '55456543', '1', NULL, NULL, NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
