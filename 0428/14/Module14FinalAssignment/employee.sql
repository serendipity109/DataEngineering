CREATE DATABASE IF NOT EXISTS employeedb;
 
USE employeedb;
 
DROP TABLE IF EXISTS `employee`;
 
CREATE TABLE `employee` (
   `id` int not null,
   `FirstName` varchar(255) default null,
   `LastName` varchar(255) default null,
   `MobileNumber` varchar(255) default null,
   `email` varchar(255) default null,
   PRIMARY KEY (`id`)
);
 
INSERT INTO employeedb.employee VALUES (1, "John", "Doe", "1112223333", "john@doe.com");