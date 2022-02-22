-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 24, 2019 at 01:29 PM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `djangoprojectdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admintable`
--

CREATE TABLE `admintable` (
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `admintype` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `admintable`
--

INSERT INTO `admintable` (`email`, `password`, `admintype`) VALUES
('mehak@gmail.com', 'mehak', 'superadmin'),
('neha@gmail.com', '1234', 'subadmin');

-- --------------------------------------------------------

--
-- Table structure for table `amenities`
--

CREATE TABLE `amenities` (
  `id` int(11) NOT NULL,
  `name` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `icon` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `amenities`
--

INSERT INTO `amenities` (`id`, `name`, `icon`) VALUES
(3, 'Pet Friendly', 'static/uploadimages/A_pets%20allowed.png'),
(4, 'Garage', 'static/uploadimages/A_garage.png'),
(5, 'Air Conditioned', 'static/uploadimages/A_airc.png'),
(6, 'Swimming Pool', 'static/uploadimages/A_swimmingpool.png'),
(7, 'Wireless Internet Access', 'static/uploadimages/A_internetaccess.png'),
(8, 'Balcony', 'static/uploadimages/A_balcony.png'),
(9, 'Dishwasher', 'static/uploadimages/A_dishwasher.png'),
(10, 'Laundry Facility', 'static/uploadimages/A_Laundry_Dryer.png'),
(11, 'Fitness Center', 'static/uploadimages/A_finesscenter.png'),
(12, 'Furnished', 'static/uploadimages/A_fullyfurnished.png'),
(13, 'Lift', 'static/uploadimages/iconlift.png');

-- --------------------------------------------------------

--
-- Table structure for table `bookingdetail`
--

CREATE TABLE `bookingdetail` (
  `id` int(100) NOT NULL,
  `bookingid` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `roomid` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `date1` date DEFAULT NULL,
  `price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `bookingdetail`
--

INSERT INTO `bookingdetail` (`id`, `bookingid`, `roomid`, `date1`, `price`) VALUES
(32, '25', '11', '2019-03-17', 399),
(33, '25', '11', '2019-03-18', 399),
(34, '25', '11', '2019-03-19', 399),
(35, '25', '11', '2019-03-20', 399),
(36, '25', '11', '2019-03-21', 399),
(37, '26', '14', '2019-03-28', 455),
(38, '26', '14', '2019-03-29', 455),
(39, '26', '14', '2019-03-30', 455),
(40, '26', '14', '2019-03-31', 455),
(41, '26', '14', '2019-04-01', 455),
(42, '26', '14', '2019-04-02', 455),
(43, '26', '14', '2019-04-03', 455),
(44, '27', '7', '2019-03-18', 500),
(45, '27', '7', '2019-03-19', 500),
(46, '27', '7', '2019-03-20', 500),
(47, '27', '7', '2019-03-21', 500),
(48, '28', '11', '2019-05-14', 399),
(49, '28', '11', '2019-05-15', 399),
(50, '28', '11', '2019-05-16', 399),
(51, '28', '11', '2019-05-17', 399),
(52, '28', '11', '2019-05-18', 399),
(53, '28', '11', '2019-05-19', 399),
(54, '28', '11', '2019-05-20', 399),
(55, '28', '11', '2019-05-21', 399),
(56, '28', '11', '2019-05-22', 399),
(57, '28', '11', '2019-05-23', 399),
(58, '28', '11', '2019-05-24', 399),
(59, '29', '11', '2019-05-08', 399),
(60, '29', '11', '2019-05-09', 399),
(61, '30', '11', '2019-05-25', 399),
(62, '30', '11', '2019-05-26', 399),
(63, '30', '11', '2019-05-27', 399),
(64, '31', '13', '2019-05-09', 678),
(65, '31', '13', '2019-05-10', 678),
(66, '31', '13', '2019-05-11', 678),
(67, '31', '13', '2019-05-12', 678),
(68, '31', '13', '2019-05-13', 678),
(69, '31', '13', '2019-05-14', 678),
(70, '31', '13', '2019-05-15', 678);

-- --------------------------------------------------------

--
-- Table structure for table `bookingtable`
--

CREATE TABLE `bookingtable` (
  `bid` int(100) NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mobileno` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `noofperson` int(50) DEFAULT NULL,
  `totalcost` float DEFAULT NULL,
  `dateofbooking` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `bookingtable`
--

INSERT INTO `bookingtable` (`bid`, `email`, `name`, `mobileno`, `noofperson`, `totalcost`, `dateofbooking`) VALUES
(25, 'sujata@gmail.com', 'Sujata', '7485968574', 2, 1596, '2019-03-14'),
(26, 'manisha@gmail.com', 'Manisha', '7485968574', 3, 2730, '2019-03-14'),
(27, 'sujata@gmail.com', 'Sjata', '7485748574', 2, 1500, '2019-03-16'),
(28, 'manisha@gmail.com', 'twinkle', '9882768681', 2, 3990, '2019-04-30'),
(29, 'manisha@gmail.com', 'twin', '9877876854', 3, 399, '2019-04-30'),
(30, 'sujata@gmail.com', 'neha', '890790779', 4, 798, '2019-04-30'),
(31, 'sujata@gmail.com', 'sujatak', '9789876766', 3, 4068, '2019-05-01');

-- --------------------------------------------------------

--
-- Table structure for table `categorytable`
--

CREATE TABLE `categorytable` (
  `categoryname` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `description` text COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `categorytable`
--

INSERT INTO `categorytable` (`categoryname`, `description`) VALUES
('abc', 'abcnfbdjjuygbuynuhn\r\n'),
('def', 'hello world');

-- --------------------------------------------------------

--
-- Table structure for table `roomphotos`
--

CREATE TABLE `roomphotos` (
  `id` int(50) NOT NULL,
  `title` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `photo` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `roomid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `roomphotos`
--

INSERT INTO `roomphotos` (`id`, `title`, `photo`, `roomid`) VALUES
(6, 'bathroom', 'static/uploadimages/room3_M1LA3Hl.jpg', 1),
(10, 'kitchen', 'static/uploadimages/kitchen_2PfpbRR.jpg', 2),
(11, 'bathroom', 'static/uploadimages/bathroom.jpg', 2),
(12, 'Balcony', 'static/uploadimages/balcony1.jpg', 2),
(13, 'kitchen', 'static/uploadimages/kitchen3.jpg', 3),
(14, 'bathroom', 'static/uploadimages/bathroom2.jpeg', 3),
(15, 'Balcony', 'static/uploadimages/balcony4.jpg', 3),
(16, 'kitchen', 'static/uploadimages/kitchen2.jpg', 1),
(17, 'Balcony', 'static/uploadimages/balcony5.jpg', 1),
(21, 'living room', 'static/uploadimages/living3.jpg', 5),
(24, 'Bathroom', 'static/uploadimages/bathroom3.jpg', 17);

-- --------------------------------------------------------

--
-- Table structure for table `roomtable`
--

CREATE TABLE `roomtable` (
  `roomid` int(11) NOT NULL,
  `title` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `priceperday` float DEFAULT NULL,
  `description` text COLLATE utf8_unicode_ci DEFAULT NULL,
  `photo` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `city` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `roomtable`
--

INSERT INTO `roomtable` (`roomid`, `title`, `priceperday`, `description`, `photo`, `email`, `city`) VALUES
(1, 'delux', 200.99, 'We have economy rooms available for solo travelers or those wishing to have their own privacy. These are comfortable with a smaller double bed and have their own en suites. (One room has a single bed though!) All have plenty of light and windows and are nicely furnished. As a single person you will be very comfortable!.', 'static/uploadimages/balcony1_taCl3b0.jpg', 'sujata@gmail.com', 'Amritsar'),
(2, 'Portico', 90, 'Standard rooms have a standard double bed and en suite. Twin rooms have 2 separate beds and are very comfortable. The rooms have nice new bathrooms.All rooms have a minimum of 2 opening windows some rooms as many as 5 windows. Some of our double rooms have a small sitting area, Some rooms have a glimpse of the sea or village street views.', 'static/uploadimages/room5_ZJjW61s.jpg', 'sujata@gmail.com', 'Delhi'),
(3, 'Luxary room', 800, 'Our Family suites have a separate entry sitting room opening to a bedroom with queen size bed and a divan. The family suite has a large shower room. It is ideal for people who want a large room and who do not wish to use stairs. Also for people with children it is ideal. It can sleep up to 4 persons so is great for a family.', 'static/uploadimages/room2_DlvB3LN.jpg', 'sujata@gmail.com', 'Banglore'),
(5, 'Cottage King', 300, 'Double rooms have a standard double bed and en suite. Twin rooms have 2 separate beds and are very comfortable. The rooms have nıce new bathrooms.All rooms have a minimum of 2 opening windows some rooms as many as 5 windows. Some of our double rooms have a small sitting area, Some rooms have a glimpse of the sea or village street views.', 'static/uploadimages/room4_1S3zlIy.jpg', 'sujata@gmail.com', 'Chennai'),
(7, 'Delux', 500, 'Each of the 40 Canopy Deluxe rooms is 63 square metres in size and offer luxury accommodation with an outdoor balcony overlooking the rainforest.\r\n\r\nThey have a combined bedroom and living room with a king-size or twin bed dressed in Egyptian cotton linen, writing desk, vanity table, and cosy day-beds. There is a complimentary minibar (excluding spirits), tea- and coffee-making facilities, personal safe, Wi-Fi, multi-purpose charging ports, and an IPTV.\r\n\r\nThe spacious bathroom and dressing room features a separate shower and WC area, twin-basin vanity, bathtub, and luxury tailor-made amenities. These rooms are located in the main building and provide easy access to The Lobby.', 'static/uploadimages/balcony_CcdjMvf.jpg', 'manisha@gmail.com', 'Amritsar'),
(8, 'Portico', 499.99, 'The 11 Canopy Suites, located in the main building, are sized between 109 to 125 square metres and have spacious verandas looking out into the rainforest.\r\n\r\nThe Canopy Suites feature a large bedroom, with a king-size bed dressed in Egyptian cotton linen, and a spacious, separate living and dining area. Each has an oversized daybed, writing desk, vanity table, complimentary minibar (excluding spirits), tea- and coffee-making facilities, personal safe, Wi-Fi, multi-purpose charging ports, and IPTV.', 'static/uploadimages/kitchen4.jpg', 'manisha@gmail.com', 'Delhi'),
(9, 'Cottage', 300.89, 'The spacious bathroom and dressing room feature twin wardrobes, a separate shower and WC area, twin-basin vanity, bathtub and luxury tailor-made amenities in keeping with overall resort sustainability. There is also a guest bathroom.', 'static/uploadimages/living2.jpg', 'manisha@gmail.com', 'Chennai'),
(10, 'Luxary room', 200.98, 'Executive deluxe rooms are a luxurious choice of accommodation, with twin bed and Deluxe en-suite bathrooms with towelling bathrobes. If you’re travelling with a family or in a group, you can book an interconnecting room or you can get an extra bed a third person can sleep.', 'static/uploadimages/living4.jpg', 'manisha@gmail.com', 'Banglore'),
(11, 'Twin Room', 399, 'Executive deluxe rooms are a luxurious choice of accommodation, with twin bed and Deluxe en-suite bathrooms with towelling bathrobes. If you’re travelling with a family or in a group, you can book an interconnecting room or you can get an extra bed a third person can sleep.', 'static/uploadimages/balcony4_tfRlTX0.jpg', 'manisha@gmail.com', 'Amritsar'),
(12, 'Delux Twin', 799, 'With their spacious feel and choice of double, king or twin beds, Suite are perfect if you like to stretch out and relax. All have comfortable seating areas and air conditioning, along with luxurious bedding that will guarantee you a great night’s sleep. If you’re travelling with a family or in a group of three, you can book an interconnecting room or get an extra bed.', 'static/uploadimages/balcony5_VllM8BJ.jpg', 'manisha@gmail.com', 'Amritsar'),
(13, 'Portico Twin', 678, 'Our Deluxe  Rooms  has a  large bed,private bathroom  , shower products,TV with satellite channels,Tea / Coffee makers, Mini bar with refreshments*, free high speed  wireless internet.\r\n\r\n \r\n\r\nRoom Size:360sq ft\r\nBed Size: 78 x 78 inches for King Rooms and 78 x 55 inches for Queen Rooms(twin beds)', 'static/uploadimages/kitchen_19PBy8B.jpg', 'manisha@gmail.com', 'Amritsar'),
(14, 'Delux', 455, 'with garage', 'static/uploadimages/balcony4_ICzjhF0.jpg', 'manisha@gmail.com', 'Delhi'),
(15, 'Cottage King', 788, 'Lawn Avl.', 'static/uploadimages/bathroom2_o1aeAoN.jpeg', 'manisha@gmail.com', 'Delhi'),
(16, 'Portico', 899, 'Swimming Pool', 'static/uploadimages/living1_HlSBXs7.jpeg', 'manisha@gmail.com', 'Delhi'),
(17, 'Standard Room', 199, 'Feel the morning mist pass by your windows, so close you can almost reach out the clouds. We have well appointed deluxe rooms each with a view that is breathtaking.What better place to refresh yourself after a long day\r\n\r\n \r\n\r\nOur Deluxe  Rooms  has a  large bed,private bathroom  , shower products,TV with satellite channels,Tea / Coffee makers, Mini bar with refreshments*, free high speed  wireless internet.', 'static/uploadimages/1.jpg', 'sujata@gmail.com', 'Dehradun');

-- --------------------------------------------------------

--
-- Table structure for table `usersignup`
--

CREATE TABLE `usersignup` (
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `fullname` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `mobileno` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `photo` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `usertype` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `city` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `usersignup`
--

INSERT INTO `usersignup` (`email`, `password`, `fullname`, `mobileno`, `address`, `photo`, `status`, `usertype`, `city`) VALUES
('komal@gmail.com', '123', 'komal gupta', '98628662 ', 'amritsar ', 'static/uploadimages/IMG_20171019_182713.jpg', 'Pending', 'Buyer', 'Amritsar'),
('laxmi@gmail.com', 'laxmi', 'Laxmi Rana', '7836345472 ', 'kathmandu ', 'static/uploadimages/IMG_20171019_184401.jpg', 'Pending', 'Buyer', 'KAthmandu'),
('manisha@gmail.com', 'manisha', 'Manisha Bhaskar', '8766746768', 'Amritsar,Punjab,India', 'static/uploadimages/loki.jpg', 'Approved', 'Seller', 'Amritsar'),
('sudhira@gmail.com', 'sudhira', 'Sudhira Mandal', '9868757870', 'Nepal', 'static/uploadimages/loki_CNzfcLo.jpg', 'Pending', 'Buyer', 'Janakpur'),
('sujata@gmail.com', 'sujata', 'Sujata Magar', '7485968574', 'punjab ,india', 'static/uploadimages/20160209_153839_ZnTwtpP.jpg', 'Approved', 'Seller', 'Amritsar');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admintable`
--
ALTER TABLE `admintable`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `amenities`
--
ALTER TABLE `amenities`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bookingdetail`
--
ALTER TABLE `bookingdetail`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bookingtable`
--
ALTER TABLE `bookingtable`
  ADD PRIMARY KEY (`bid`),
  ADD KEY `bookingemail_idx` (`email`);

--
-- Indexes for table `categorytable`
--
ALTER TABLE `categorytable`
  ADD PRIMARY KEY (`categoryname`);

--
-- Indexes for table `roomphotos`
--
ALTER TABLE `roomphotos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `roomid_idx` (`roomid`);

--
-- Indexes for table `roomtable`
--
ALTER TABLE `roomtable`
  ADD PRIMARY KEY (`roomid`),
  ADD KEY `fk_email_idx` (`email`);

--
-- Indexes for table `usersignup`
--
ALTER TABLE `usersignup`
  ADD PRIMARY KEY (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `amenities`
--
ALTER TABLE `amenities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `bookingdetail`
--
ALTER TABLE `bookingdetail`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- AUTO_INCREMENT for table `bookingtable`
--
ALTER TABLE `bookingtable`
  MODIFY `bid` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `roomphotos`
--
ALTER TABLE `roomphotos`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `roomtable`
--
ALTER TABLE `roomtable`
  MODIFY `roomid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bookingtable`
--
ALTER TABLE `bookingtable`
  ADD CONSTRAINT `bookingemail` FOREIGN KEY (`email`) REFERENCES `usersignup` (`email`);

--
-- Constraints for table `roomphotos`
--
ALTER TABLE `roomphotos`
  ADD CONSTRAINT `roomid` FOREIGN KEY (`roomid`) REFERENCES `roomtable` (`roomid`);

--
-- Constraints for table `roomtable`
--
ALTER TABLE `roomtable`
  ADD CONSTRAINT `email` FOREIGN KEY (`email`) REFERENCES `usersignup` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
