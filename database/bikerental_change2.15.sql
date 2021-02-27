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

 Date: 14/02/2021 10:35:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bike_info
-- ----------------------------
DROP TABLE IF EXISTS `bike_info`;
CREATE TABLE `bike_info` (
  `bID` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'bike ID',
  `bstatus` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'bike status',
  `bGPSx` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'bike location',
  `bGPSy` varchar(255) DEFAULT NULL COMMENT 'bike location',
  `barea` varchar(100) DEFAULT NULL COMMENT 'bike area',
  `bpassword` varchar(100) DEFAULT NULL COMMENT 'bike password',
  `busage` varchar(50) DEFAULT NULL COMMENT 'bike usage',
  `bproblem` varchar(255) DEFAULT NULL COMMENT 'problem discribe',
  PRIMARY KEY (`bID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bike_info
-- ----------------------------
BEGIN;
INSERT INTO `bike_info` VALUES ('101', '2', NULL, NULL, NULL, '1224', '0', 'report');
INSERT INTO `bike_info` VALUES ('102', '2', NULL, NULL, NULL, '2345', '0', 'repair');
INSERT INTO `bike_info` VALUES ('103', '1', NULL, NULL, NULL, '2345', '0', NULL);
INSERT INTO `bike_info` VALUES ('104', '1', NULL, NULL, NULL, '4567', '0', NULL);
INSERT INTO `bike_info` VALUES ('105', '2', NULL, NULL, NULL, '3687', '0', 'geel broken');
COMMIT;

-- ----------------------------
-- Table structure for customer_info
-- ----------------------------
DROP TABLE IF EXISTS `customer_info`;
CREATE TABLE `customer_info` (
  `ID` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'userID',
  `UserName` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'username',
  `Password` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'userpassword',
  `renttime` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'total use time',
  `Tel` int DEFAULT NULL COMMENT 'telephone',
  `Bankcard` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'bankcard',
  `usertype` varchar(100) DEFAULT NULL COMMENT 'user type',
  `Balance` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'account money',
  `uGPSx` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'user location',
  `uGPSy` varchar(255) DEFAULT NULL COMMENT 'user location',
  `uarea` varchar(255) DEFAULT NULL COMMENT 'user area',
  `email` varchar(255) DEFAULT NULL COMMENT 'email',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of customer_info
-- ----------------------------
BEGIN;
INSERT INTO `customer_info` VALUES ('1001', 'lili', '123456', '500', 12345678, '234565432', '0', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `customer_info` VALUES ('1002', 'peter', '123456', '100', 2345432, '557754432', '0', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `customer_info` VALUES ('1003', 'alex', '234543', '200', 32445, '55456543', '1', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `customer_info` VALUES ('1006', 'qwerty', '123321', '300', 45464, '577578', '1', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `customer_info` VALUES ('1007', 'coco', '123456', '200', 7564, '123456', '0', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `customer_info` VALUES ('1008', 'yichen', '123456', '600', 123456, '323445', '1', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `customer_info` VALUES ('1009', 'eee', '123321', '50', 433, '12323', '1', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `customer_info` VALUES ('1010', 'zzzhh', '123123', NULL, 3435435, '5435246', NULL, NULL, NULL, NULL, NULL, NULL);
COMMIT;

-- ----------------------------
-- Table structure for pay_info
-- ----------------------------
DROP TABLE IF EXISTS `pay_info`;
CREATE TABLE `pay_info` (
  `pID` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'payment id',
  `ID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'user id',
  `bID` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'bike id',
  `starttime` varchar(100) DEFAULT NULL COMMENT 'start time',
  `endtime` varchar(100) DEFAULT NULL COMMENT 'end time',
  `duration` varchar(100) DEFAULT NULL COMMENT 'rent time',
  `oribill` varchar(100) DEFAULT NULL COMMENT 'original bill',
  `discount` varchar(100) DEFAULT NULL COMMENT 'bill after discount',
  `startGPSx` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'start gpsx',
  `startGPSy` varchar(255) DEFAULT NULL COMMENT 'start gpsy',
  `endGPSx` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'end gpsx',
  `endGPSy` varchar(255) DEFAULT NULL COMMENT 'end gpsy',
  `pstatus` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'payment status',
  PRIMARY KEY (`pID`) USING BTREE,
  KEY `bike` (`bID`),
  KEY `user` (`ID`),
  CONSTRAINT `bike` FOREIGN KEY (`bID`) REFERENCES `bike_info` (`bID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user` FOREIGN KEY (`ID`) REFERENCES `customer_info` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of pay_info
-- ----------------------------
BEGIN;
INSERT INTO `pay_info` VALUES ('1101', '1001', '102', '1245', '1315', '30min', '6', '4', NULL, NULL, NULL, NULL, '0');
INSERT INTO `pay_info` VALUES ('1102', '1002', '104', '2354', '2354', '20min', '7', '3', NULL, NULL, NULL, NULL, '0');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
