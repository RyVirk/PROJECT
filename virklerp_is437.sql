-- phpMyAdmin SQL Dump
-- version 4.0.10deb1ubuntu0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 03, 2020 at 05:08 PM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `virklerp_is437`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE IF NOT EXISTS `customers` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `subscribed` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `fname`, `lname`, `email`, `password`, `subscribed`) VALUES
(12, 'Admin', 'Ryan', 'v@v.com', '1234', 'True'),
(13, 'User', 'Ryan', 'r@r.com', '123', 'True');

-- --------------------------------------------------------

--
-- Table structure for table `games`
--

CREATE TABLE IF NOT EXISTS `games` (
  `gid` int(5) NOT NULL AUTO_INCREMENT,
  `gname` varchar(100) NOT NULL,
  `gdate` date DEFAULT NULL,
  `team1` varchar(100) DEFAULT NULL,
  `team2` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`gid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `games`
--

INSERT INTO `games` (`gid`, `gname`, `gdate`, `team1`, `team2`) VALUES
(1, 'Test', '2020-04-07', '1', '2'),
(2, 'Test2', '2020-05-01', '3', '4'),
(5, 'Game B', '2020-06-06', '2', '1'),
(6, 'Test3', '2020-06-12', '15', '5'),
(7, 'Test4', '2020-06-26', '6', '9'),
(8, 'Test7', '2020-06-27', '11', '10');

-- --------------------------------------------------------

--
-- Table structure for table `matchEvents`
--

CREATE TABLE IF NOT EXISTS `matchEvents` (
  `eid` int(5) NOT NULL AUTO_INCREMENT,
  `ename` varchar(100) NOT NULL,
  `estat` float NOT NULL,
  `etime` varchar(20) NOT NULL,
  `pid` int(5) NOT NULL,
  `gid` int(5) NOT NULL,
  `tid` int(5) NOT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `matchEvents`
--

INSERT INTO `matchEvents` (`eid`, `ename`, `estat`, `etime`, `pid`, `gid`, `tid`) VALUES
(1, 'Goal', 1, '6', 1, 1, 1),
(2, 'Assist', 1, '19', 3, 1, 2),
(3, 'Goal', 1, '70', 6, 1, 2),
(4, 'Own Goal', 1, '44', 2, 2, 4),
(5, 'Goal', 1, '74', 5, 2, 3),
(6, 'Assist ', 1, '87', 1, 1, 1),
(7, 'Goal', 1, '79', 11, 7, 6),
(8, 'Tackles', 7, '90', 16, 5, 1),
(9, 'Goal', 1, '32', 15, 8, 11);

-- --------------------------------------------------------

--
-- Table structure for table `players`
--

CREATE TABLE IF NOT EXISTS `players` (
  `pid` int(5) NOT NULL AUTO_INCREMENT,
  `pname` varchar(100) NOT NULL,
  `age` int(2) NOT NULL,
  `position` varchar(50) NOT NULL,
  `tid` int(5) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=17 ;

--
-- Dumping data for table `players`
--

INSERT INTO `players` (`pid`, `pname`, `age`, `position`, `tid`) VALUES
(1, 'Nicolas Pepe', 24, 'RW', 1),
(2, 'Jadon Sancho', 20, 'LW', 4),
(3, 'Lionel Messi', 32, 'RW', 2),
(4, 'Mesut Ozil', 31, 'CAM', 1),
(5, 'Virgil Van Dijk', 28, 'CB', 3),
(6, 'Luis Suarez', 33, 'ST', 2),
(7, 'Frenkie De Jong', 22, 'CM', 2),
(8, 'Marcus Rashford', 22, 'LW', 5),
(9, 'Anthony Martial ', 24, 'ST', 5),
(10, 'Toni Kroos', 30, 'CM', 6),
(11, 'Vinicius Junior', 19, 'LW', 6),
(12, 'Neymar', 28, 'LW', 15),
(13, 'Brahim Diaz ', 20, 'CAM', 6),
(14, 'Sadio Mane', 28, 'LW', 3),
(15, 'Kai Havertz', 20, 'CAM', 11),
(16, 'Lucas Torreira', 24, 'CDM', 1);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE IF NOT EXISTS `products` (
  `pid` int(25) NOT NULL AUTO_INCREMENT,
  `sku` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` decimal(5,2) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`pid`, `sku`, `name`, `price`) VALUES
(1, '123', 'Ball', 9.00),
(2, '123', 'Ball', 0.00),
(3, '123', 'Ball', 0.00);

-- --------------------------------------------------------

--
-- Table structure for table `teams`
--

CREATE TABLE IF NOT EXISTS `teams` (
  `tid` int(5) NOT NULL AUTO_INCREMENT,
  `tname` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `groupnum` char(1) NOT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=18 ;

--
-- Dumping data for table `teams`
--

INSERT INTO `teams` (`tid`, `tname`, `country`, `groupnum`) VALUES
(1, 'Arsenal', 'England', '1'),
(2, 'Barcelona', 'Spain', '1'),
(3, 'Liverpool', 'England', '2'),
(4, 'Borussia Dortmund', 'Germany', '2'),
(5, 'Machester United', 'England ', '3'),
(6, 'Real Madrid', 'Spain', '4'),
(7, 'Bayern Munich', 'Germany ', '1'),
(8, 'Monaco ', 'France', '1'),
(9, 'RC Strasbourg Alsace', 'France', '4'),
(10, 'Chelsea', 'England', '4'),
(11, 'Bayer Leverkusen', 'Germany', '4'),
(12, 'Valencia', 'Spain', '2'),
(13, 'Olympique Lyonnais', 'France', '2'),
(14, 'FC Zenit Saint Petersburg', 'Russia', '3'),
(15, 'Paris Saint Germain', 'France', '3'),
(16, 'S.L. Benfica ', 'Portugal', '3');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
