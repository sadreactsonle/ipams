-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 06, 2020 at 11:06 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_client`
--

CREATE TABLE `account_client` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `date_joined` datetime(6) NOT NULL,
  `profile_picture` varchar(100) NOT NULL,
  `verificationCode` varchar(10) NOT NULL,
  `coins` int(11) NOT NULL,
  `points` int(11) NOT NULL,
  `in_facility` tinyint(1) NOT NULL,
  `internet` int(11) NOT NULL,
  `facility_logs` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `account_client`
--

INSERT INTO `account_client` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `profile_picture`, `verificationCode`, `coins`, `points`, `in_facility`, `internet`, `facility_logs`) VALUES
(1, 'pbkdf2_sha256$180000$AskpjBFzuDs8$Vd4SeUxvvt6SBwRmwyuIc7g7Ng44J5ndkFcZXOrv4qU=', '2020-03-26 18:31:47.495866', 1, '201512006', 'Jay Vince', 'Serato', 'jayvince.serato@gmail.com', 1, 1, '2020-03-25 00:40:53.000000', '', '', 12, 0, 0, 0, ''),
(2, 'pbkdf2_sha256$180000$mmYWit8ZEgJc$yWdGclxBjrv0p9RXrLbseIcNDC6RuSRj2pDpUhiBw4I=', '2020-03-26 10:43:17.876063', 0, '201512007', 'Pinkfloyd', 'Adonay', 'padonay@gmail.com', 0, 1, '0000-00-00 00:00:00.000000', '', '', 0, 0, 0, 0, ''),
(3, 'pbkdf2_sha256$180000$bkHj9OzB1mg4$empEDYQ9Z/gOM3zO6BBJknkygngPSa4zYIg5zJZl1Ec=', '2020-03-24 16:52:54.066650', 0, '201512008', 'Ralph', 'Laviste', 'rlaviste@gmiil.acom', 0, 0, '0000-00-00 00:00:00.000000', '', '', 0, 0, 0, 0, ''),
(4, 'pbkdf2_sha256$180000$spApf1CwW5xs$abHWYX85aCvtkMX/cU3qel/Xawrv3GDGasrKhUfOIu0=', '2020-03-24 16:49:46.000627', 1, 'jdserato', 'Jay Vince', 'Serato', 'jdserato@up.edu.ph', 1, 1, '2020-03-24 16:38:45.262169', '', '', 0, 0, 0, 0, ''),
(5, 'pbkdf2_sha256$180000$IoqjUqfmqPyI$Eos/Ojc21yZSBInUOCWMIIMcHCz7zcCjoKJ1Ml6EaYA=', '2020-03-26 10:25:11.111273', 0, '201512009', 'Jurydel', 'Rama', 'jramarama@gmail.com', 0, 1, '0000-00-00 00:00:00.000000', '', '', 0, 0, 0, 0, ''),
(6, 'pbkdf2_sha256$180000$sk8ZBmXIew64$dxSz5fK9WfmeNK8HsrO+LpQkz4dKrl9IV45Q7pAXM2M=', '2020-03-26 10:26:31.647041', 0, '201512010', 'Cherry Ann', 'Sta. Romana', 'cstaromana@yahoo.com', 0, 1, '0000-00-00 00:00:00.000000', '', '', -100, 0, 0, 0, ''),
(7, 'pbkdf2_sha256$180000$G4QPtPHxoBqb$EXRWG6KoAwnv2zoRX7TsmKi20gvvH4ju6Y1smVTWbzM=', '2020-07-06 09:05:20.808340', 1, 'admin', 'admin', 'admin', 'admin@email.com', 1, 1, '2020-06-09 22:58:09.312776', '', '', 9661, 8181, 0, 0, '');

-- --------------------------------------------------------

--
-- Table structure for table `account_client_groups`
--

CREATE TABLE `account_client_groups` (
  `id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `account_client_user_permissions`
--

CREATE TABLE `account_client_user_permissions` (
  `id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `account_startupteam`
--

CREATE TABLE `account_startupteam` (
  `id` int(11) NOT NULL,
  `team_image` varchar(100) NOT NULL,
  `startup_name` varchar(20) NOT NULL,
  `company_name` varchar(40) NOT NULL,
  `founders` longtext NOT NULL,
  `main_address` varchar(500) NOT NULL,
  `parent_company` varchar(100) NOT NULL,
  `partner_company` varchar(350) NOT NULL,
  `contact_number` varchar(11) NOT NULL,
  `email` varchar(35) NOT NULL,
  `type_of_business` varchar(50) NOT NULL,
  `industry` varchar(30) NOT NULL,
  `business_system` varchar(50) NOT NULL,
  `operating_start` time(6) NOT NULL,
  `operating_end` time(6) NOT NULL,
  `accelerators` longtext NOT NULL,
  `mission` longtext NOT NULL,
  `vision` longtext NOT NULL,
  `tagline` longtext NOT NULL,
  `employee_list` longtext NOT NULL,
  `internet` int(11) NOT NULL,
  `coins` int(11) NOT NULL,
  `points` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `account_technoteam`
--

CREATE TABLE `account_technoteam` (
  `id` int(11) NOT NULL,
  `project_name` varchar(20) NOT NULL,
  `group_name` varchar(40) NOT NULL,
  `contact_number` varchar(11) NOT NULL,
  `email` varchar(35) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `type_of_business` varchar(50) NOT NULL,
  `industry` varchar(30) NOT NULL,
  `business_system` varchar(50) NOT NULL,
  `instructor` varchar(30) NOT NULL,
  `mentors` varchar(50) NOT NULL,
  `mission` longtext NOT NULL,
  `vision` longtext NOT NULL,
  `tagline` longtext NOT NULL,
  `members` longtext NOT NULL,
  `coins` int(11) NOT NULL,
  `internet` int(11) NOT NULL,
  `points` int(11) NOT NULL,
  `team_image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add user', 1, 'add_client'),
(2, 'Can change user', 1, 'change_client'),
(3, 'Can delete user', 1, 'delete_client'),
(4, 'Can view user', 1, 'view_client'),
(5, 'Can add booking', 2, 'add_booking'),
(6, 'Can change booking', 2, 'change_booking'),
(7, 'Can delete booking', 2, 'delete_booking'),
(8, 'Can view booking', 2, 'view_booking'),
(9, 'Can add venue', 3, 'add_venue'),
(10, 'Can change venue', 3, 'change_venue'),
(11, 'Can delete venue', 3, 'delete_venue'),
(12, 'Can view venue', 3, 'view_venue'),
(13, 'Can add log entry', 4, 'add_logentry'),
(14, 'Can change log entry', 4, 'change_logentry'),
(15, 'Can delete log entry', 4, 'delete_logentry'),
(16, 'Can view log entry', 4, 'view_logentry'),
(17, 'Can add permission', 5, 'add_permission'),
(18, 'Can change permission', 5, 'change_permission'),
(19, 'Can delete permission', 5, 'delete_permission'),
(20, 'Can view permission', 5, 'view_permission'),
(21, 'Can add group', 6, 'add_group'),
(22, 'Can change group', 6, 'change_group'),
(23, 'Can delete group', 6, 'delete_group'),
(24, 'Can view group', 6, 'view_group'),
(25, 'Can add content type', 7, 'add_contenttype'),
(26, 'Can change content type', 7, 'change_contenttype'),
(27, 'Can delete content type', 7, 'delete_contenttype'),
(28, 'Can view content type', 7, 'view_contenttype'),
(29, 'Can add session', 8, 'add_session'),
(30, 'Can change session', 8, 'change_session'),
(31, 'Can delete session', 8, 'delete_session'),
(32, 'Can view session', 8, 'view_session'),
(33, 'Can add techno team', 9, 'add_technoteam'),
(34, 'Can change techno team', 9, 'change_technoteam'),
(35, 'Can delete techno team', 9, 'delete_technoteam'),
(36, 'Can view techno team', 9, 'view_technoteam'),
(37, 'Can add start up team', 10, 'add_startupteam'),
(38, 'Can change start up team', 10, 'change_startupteam'),
(39, 'Can delete start up team', 10, 'delete_startupteam'),
(40, 'Can view start up team', 10, 'view_startupteam'),
(41, 'Can add review', 11, 'add_review'),
(42, 'Can change review', 11, 'change_review'),
(43, 'Can delete review', 11, 'delete_review'),
(44, 'Can view review', 11, 'view_review'),
(45, 'Can add max days of booking', 12, 'add_maxdaysofbooking'),
(46, 'Can change max days of booking', 12, 'change_maxdaysofbooking'),
(47, 'Can delete max days of booking', 12, 'delete_maxdaysofbooking'),
(48, 'Can view max days of booking', 12, 'view_maxdaysofbooking');

-- --------------------------------------------------------

--
-- Table structure for table `booking_booking`
--

CREATE TABLE `booking_booking` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `startDate` date NOT NULL,
  `endDate` date NOT NULL,
  `startTime` time(6) NOT NULL,
  `endTime` time(6) NOT NULL,
  `purpose` varchar(30) NOT NULL,
  `referenceNo` int(11) NOT NULL,
  `cost` int(11) NOT NULL,
  `venue` varchar(30) NOT NULL,
  `attendee` varchar(30) NOT NULL,
  `computers` int(11) NOT NULL,
  `book_date` datetime(6) NOT NULL,
  `time_stay` int(11) NOT NULL,
  `status` varchar(30) NOT NULL,
  `booker` varchar(30) NOT NULL,
  `payment_method` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `booking_booking`
--

INSERT INTO `booking_booking` (`id`, `title`, `startDate`, `endDate`, `startTime`, `endTime`, `purpose`, `referenceNo`, `cost`, `venue`, `attendee`, `computers`, `book_date`, `time_stay`, `status`, `booker`, `payment_method`) VALUES
(430, '', '2020-06-13', '2020-06-13', '09:30:00.000000', '10:00:00.000000', 'Studying', 216200, 50, 'Coworking Space', 'admin', 0, '2020-06-13 07:58:36.908631', 0, 'Booked', 'admin', 'Points'),
(431, '', '2020-06-13', '2020-06-13', '10:00:00.000000', '10:30:00.000000', 'Studying', 216200, 50, 'Coworking Space', 'admin', 0, '2020-06-13 07:58:36.908631', 0, 'Booked', 'admin', 'Points'),
(432, '', '2020-06-13', '2020-06-13', '09:30:00.000000', '10:00:00.000000', 'Studying', 216200, 50, 'Coworking Space', 'admin', 0, '2020-06-13 07:58:36.908631', 0, 'Booked', 'admin', 'Points'),
(433, '', '2020-06-13', '2020-06-13', '10:00:00.000000', '10:30:00.000000', 'Studying', 216200, 50, 'Coworking Space', 'admin', 0, '2020-06-13 07:58:36.908631', 0, 'Booked', 'admin', 'Points'),
(434, '', '2020-06-13', '2020-06-13', '12:00:00.000000', '12:30:00.000000', 'Studying', 336948, 140, 'Conference Room A', 'admin', 0, '2020-06-13 07:58:36.908631', 0, 'Booked', 'admin', 'Points'),
(435, '', '2020-06-13', '2020-06-13', '12:30:00.000000', '13:00:00.000000', 'Studying', 336948, 140, 'Conference Room A', 'admin', 0, '2020-06-13 07:58:36.908631', 0, 'Booked', 'admin', 'Points'),
(436, '', '2020-06-13', '2020-06-13', '12:00:00.000000', '12:30:00.000000', 'Studying', 336948, 140, 'Conference Room A', 'admin', 0, '2020-06-13 07:58:36.908631', 0, 'Booked', 'admin', 'Points'),
(437, '', '2020-06-13', '2020-06-13', '12:30:00.000000', '13:00:00.000000', 'Studying', 336948, 140, 'Conference Room A', 'admin', 0, '2020-06-13 07:58:36.908631', 0, 'Booked', 'admin', 'Points');

-- --------------------------------------------------------

--
-- Table structure for table `booking_maxdaysofbooking`
--

CREATE TABLE `booking_maxdaysofbooking` (
  `id` int(11) NOT NULL,
  `max_days` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `booking_review`
--

CREATE TABLE `booking_review` (
  `id` int(11) NOT NULL,
  `submit_date` datetime(6) NOT NULL,
  `stars` int(11) NOT NULL,
  `comment` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `booking_venue`
--

CREATE TABLE `booking_venue` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `cap` int(11) NOT NULL,
  `computers` int(11) NOT NULL,
  `has_computers` tinyint(1) NOT NULL,
  `cost` int(11) NOT NULL,
  `computer_fee` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `booking_venue`
--

INSERT INTO `booking_venue` (`id`, `name`, `cap`, `computers`, `has_computers`, `cost`, `computer_fee`) VALUES
(1, 'Coworking Space', 6, 8, 1, 25, 10),
(2, 'Conference Room A', 7, 0, 0, 70, 10),
(3, 'Conference Room B', 7, 0, 0, 70, 10),
(4, 'Joined Conference Room', 14, 0, 0, 120, 10);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'account', 'client'),
(10, 'account', 'startupteam'),
(9, 'account', 'technoteam'),
(4, 'admin', 'logentry'),
(6, 'auth', 'group'),
(5, 'auth', 'permission'),
(2, 'booking', 'booking'),
(12, 'booking', 'maxdaysofbooking'),
(11, 'booking', 'review'),
(3, 'booking', 'venue'),
(7, 'contenttypes', 'contenttype'),
(8, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-03-24 08:21:36.843406'),
(2, 'contenttypes', '0002_remove_content_type_name', '2020-03-24 08:21:36.905891'),
(3, 'auth', '0001_initial', '2020-03-24 08:21:36.984000'),
(4, 'auth', '0002_alter_permission_name_max_length', '2020-03-24 08:21:37.218342'),
(5, 'auth', '0003_alter_user_email_max_length', '2020-03-24 08:21:37.218342'),
(6, 'auth', '0004_alter_user_username_opts', '2020-03-24 08:21:37.218342'),
(7, 'auth', '0005_alter_user_last_login_null', '2020-03-24 08:21:37.218342'),
(8, 'auth', '0006_require_contenttypes_0002', '2020-03-24 08:21:37.233939'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2020-03-24 08:21:37.233939'),
(10, 'auth', '0008_alter_user_username_max_length', '2020-03-24 08:21:37.233939'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2020-03-24 08:21:37.233939'),
(12, 'auth', '0010_alter_group_name_max_length', '2020-03-24 08:21:37.296425'),
(13, 'auth', '0011_update_proxy_permissions', '2020-03-24 08:21:37.312046'),
(14, 'account', '0001_initial', '2020-03-24 08:21:37.390153'),
(15, 'account', '0002_client_balance', '2020-03-24 08:21:37.624472'),
(16, 'admin', '0001_initial', '2020-03-24 08:21:37.655716'),
(17, 'admin', '0002_logentry_remove_auto_add', '2020-03-24 08:21:37.811950'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2020-03-24 08:21:37.827580'),
(19, 'booking', '0001_initial', '2020-03-24 08:21:37.890036'),
(20, 'booking', '0002_booking_venue', '2020-03-24 08:21:37.905656'),
(21, 'booking', '0003_booking_attendee', '2020-03-24 08:21:37.921302'),
(22, 'booking', '0004_auto_20200229_1713', '2020-03-24 08:21:37.983764'),
(23, 'booking', '0005_auto_20200302_1723', '2020-03-24 08:21:37.983764'),
(24, 'booking', '0006_venue_cost', '2020-03-24 08:21:37.999384'),
(25, 'booking', '0007_auto_20200303_1456', '2020-03-24 08:21:38.015006'),
(26, 'booking', '0008_auto_20200303_1533', '2020-03-24 08:21:38.015006'),
(27, 'booking', '0009_auto_20200303_1538', '2020-03-24 08:21:38.030666'),
(28, 'booking', '0010_booking_computers', '2020-03-24 08:21:38.046249'),
(29, 'booking', '0011_auto_20200313_1531', '2020-03-24 08:21:38.061870'),
(30, 'booking', '0012_auto_20200313_1534', '2020-03-24 08:21:38.077492'),
(31, 'booking', '0013_auto_20200313_1536', '2020-03-24 08:21:38.077492'),
(32, 'booking', '0014_auto_20200313_1538', '2020-03-24 08:21:39.546394'),
(33, 'booking', '0015_auto_20200321_2304', '2020-03-24 08:21:39.562016'),
(34, 'booking', '0016_auto_20200324_1621', '2020-03-24 08:21:39.577637'),
(35, 'sessions', '0001_initial', '2020-03-24 08:21:39.593259'),
(36, 'account', '0003_client_points', '2020-03-26 17:31:39.841612'),
(37, 'booking', '0017_auto_20200327_0131', '2020-03-26 17:31:40.015715'),
(38, 'account', '0004_client_in_facility', '2020-06-09 22:57:21.904227'),
(39, 'account', '0005_technoteam', '2020-06-09 22:57:22.158292'),
(40, 'account', '0006_auto_20200401_1920', '2020-06-09 22:57:22.824410'),
(41, 'account', '0007_auto_20200401_1930', '2020-06-09 22:57:25.152288'),
(42, 'account', '0008_auto_20200403_1812', '2020-06-09 22:57:26.622021'),
(43, 'booking', '0018_auto_20200327_1323', '2020-06-09 22:57:26.848438'),
(44, 'booking', '0019_auto_20200327_1329', '2020-06-09 22:57:27.941122'),
(45, 'booking', '0020_auto_20200327_1335', '2020-06-09 22:57:27.981563'),
(46, 'booking', '0021_auto_20200327_1351', '2020-06-09 22:57:28.079940'),
(47, 'booking', '0022_auto_20200327_1400', '2020-06-09 22:57:28.140988'),
(48, 'booking', '0023_auto_20200327_1407', '2020-06-09 22:57:28.189782'),
(49, 'booking', '0024_auto_20200327_1410', '2020-06-09 22:57:28.786082'),
(50, 'booking', '0025_auto_20200327_1411', '2020-06-09 22:57:28.885761'),
(51, 'booking', '0026_auto_20200327_1413', '2020-06-09 22:57:28.928906'),
(52, 'booking', '0027_auto_20200327_1414', '2020-06-09 22:57:29.463148'),
(53, 'booking', '0028_auto_20200327_1417', '2020-06-09 22:57:29.532334'),
(54, 'booking', '0029_auto_20200401_1501', '2020-06-09 22:57:29.782613'),
(55, 'booking', '0030_auto_20200401_1529', '2020-06-09 22:57:30.196555'),
(56, 'booking', '0031_auto_20200401_1914', '2020-06-09 22:57:30.235946'),
(57, 'booking', '0032_auto_20200401_1920', '2020-06-09 22:57:30.276588'),
(58, 'booking', '0033_auto_20200401_1930', '2020-06-09 22:57:30.304407'),
(59, 'booking', '0034_auto_20200401_2315', '2020-06-09 22:57:30.806026'),
(60, 'booking', '0035_auto_20200403_1812', '2020-06-09 22:57:30.867812'),
(61, 'booking', '0036_auto_20200610_0657', '2020-06-09 22:57:30.911038');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('37yrnhumc9z4d89tuyovullyj89tot8m', 'ZWNlNmEwNzJlZjRiYjlmYWNmMzFmZmY2OThiNWIyMmMyMzY4MjVmNTp7ImlkTm8iOiJhZG1pbiIsIl9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNTkxOWYxY2JlZmFjZmNiMzEzOGEzMDQzMmU1MzgyOWNhNjBkMTg3In0=', '2020-07-20 09:05:20.866298'),
('6kije5uhp7c8zu3yq96wj2wmekshsfm2', 'ZTdjYjE1Y2MwY2UxNDExM2VlODc5OGFjZDU4YTc0YTJmZjdhNWNhZDp7ImlkTm8iOiJhZG1pbiIsIl9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNTkxOWYxY2JlZmFjZmNiMzEzOGEzMDQzMmU1MzgyOWNhNjBkMTg3Iiwic3RhcnRfZGF5cyI6WyIyMDIwLTA2LTEzIiwiMjAyMC0wNi0xMyIsIjIwMjAtMDYtMTMiLCIyMDIwLTA2LTEzIl0sImVuZF9kYXlzIjpbIjIwMjAtMDYtMTMiLCIyMDIwLTA2LTEzIiwiMjAyMC0wNi0xMyIsIjIwMjAtMDYtMTMiXSwic3RhcnRfdGltZXMiOlsiMTI6MDAiLCIxMjozMCIsIjEyOjAwIiwiMTI6MzAiXSwiZW5kX3RpbWVzIjpbIjEyOjMwIiwiMTM6MDAiLCIxMjozMCIsIjEzOjAwIl0sInZlbnVlIjoiQ29uZmVyZW5jZSBSb29tIEEiLCJ0b3RUaW1lIjoyLjAsInJlZk51bSI6MzM2OTQ4LCJzcGFjZSI6NywiY29tcHMiOjAsInB1cnBvc2UiOiJTdHVkeWluZyIsImF0dGVuZGVlcyI6ImFkbWluIGFkbWluIFthZG1pbl0sICIsImF0dGVuZGVlc19pZCI6ImFkbWluLCAiLCJjb21wdXRlcnMiOjAsImNvc3QiOjE0MC4wLCJ1bml0X2Nvc3QiOjE0MC4wfQ==', '2020-06-27 09:23:57.692944'),
('bt3wmriulutklmfee3muqozitm0bc0g7', 'M2Y1OGVmYTQ5MmVjNDIwY2RhN2QxNmNiZmNmN2UzZjBhOTczMTc2ZTp7ImlkTm8iOiJhZG1pbiIsIl9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNTkxOWYxY2JlZmFjZmNiMzEzOGEzMDQzMmU1MzgyOWNhNjBkMTg3Iiwic3RhcnRfZGF5cyI6WyIyMDIwLTA2LTEwIiwiMjAyMC0wNi0xMCIsIjIwMjAtMDYtMTAiLCIyMDIwLTA2LTEwIiwiMjAyMC0wNi0xMCIsIjIwMjAtMDYtMTAiLCIyMDIwLTA2LTEwIiwiMjAyMC0wNi0xMCIsIjIwMjAtMDYtMTAiLCIyMDIwLTA2LTEwIiwiMjAyMC0wNi0xMCJdLCJlbmRfZGF5cyI6WyIyMDIwLTA2LTEwIiwiMjAyMC0wNi0xMCIsIjIwMjAtMDYtMTAiLCIyMDIwLTA2LTEwIiwiMjAyMC0wNi0xMCIsIjIwMjAtMDYtMTAiLCIyMDIwLTA2LTEwIiwiMjAyMC0wNi0xMCIsIjIwMjAtMDYtMTAiLCIyMDIwLTA2LTEwIiwiMjAyMC0wNi0xMCJdLCJzdGFydF90aW1lcyI6WyIwOTozMCIsIjA5OjMwIiwiMDk6MzAiLCIxMDozMCIsIjEwOjAwIiwiMTA6MzAiLCIxMTowMCIsIjEwOjAwIiwiMTA6MzAiLCIxMTowMCIsIjExOjMwIl0sImVuZF90aW1lcyI6WyIxMDowMCIsIjEwOjAwIiwiMTA6MDAiLCIxMTowMCIsIjEwOjMwIiwiMTE6MDAiLCIxMTozMCIsIjEwOjMwIiwiMTE6MDAiLCIxMTozMCIsIjEyOjAwIl0sInZlbnVlIjoiQ293b3JraW5nIFNwYWNlIiwidG90VGltZSI6NS41LCJyZWZOdW0iOjcyNzIzOCwic3BhY2UiOjYsImNvbXBzIjo4LCJwdXJwb3NlIjoiU3R1ZHlpbmciLCJhdHRlbmRlZXMiOiJhZG1pbiBhZG1pbiBbYWRtaW5dLCBKYXkgVmluY2UgU2VyYXRvIFsyMDE1MTIwMDZdLCBKYXkgVmluY2UgU2VyYXRvIFtqZHNlcmF0b10sICIsImF0dGVuZGVlc19pZCI6ImFkbWluLCAyMDE1MTIwMDYsIGpkc2VyYXRvLCAiLCJjb21wdXRlcnMiOjAsImNvc3QiOjQxMi41LCJ1bml0X2Nvc3QiOjEzNy41fQ==', '2020-06-24 06:57:44.895183'),
('z8qm1pksgemjz33tenngsyxbzipiivyh', 'ZTcyZDBiYjVhZTVhMTgzY2I5YTc0MDVlNGUyNzM2MzFlOGJlMWYzNDp7ImlkTm8iOiIyMDE1MTIwMDYiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODk4MGY0MmIzNDEyNjQyYmY3NmVkZjNiZDZmZmI5NzQwMWFkNWVlNCJ9', '2020-04-09 18:31:47.503475');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_client`
--
ALTER TABLE `account_client`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `account_client_groups`
--
ALTER TABLE `account_client_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_client_groups_client_id_group_id_c11fcb23_uniq` (`client_id`,`group_id`),
  ADD KEY `account_client_groups_group_id_68213f09_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `account_client_user_permissions`
--
ALTER TABLE `account_client_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_client_user_perm_client_id_permission_id_c2152324_uniq` (`client_id`,`permission_id`),
  ADD KEY `account_client_user__permission_id_8852aa72_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `account_startupteam`
--
ALTER TABLE `account_startupteam`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `account_technoteam`
--
ALTER TABLE `account_technoteam`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `booking_booking`
--
ALTER TABLE `booking_booking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `booking_maxdaysofbooking`
--
ALTER TABLE `booking_maxdaysofbooking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `booking_review`
--
ALTER TABLE `booking_review`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `booking_venue`
--
ALTER TABLE `booking_venue`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_account_client_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account_client`
--
ALTER TABLE `account_client`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `account_client_groups`
--
ALTER TABLE `account_client_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `account_client_user_permissions`
--
ALTER TABLE `account_client_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `account_startupteam`
--
ALTER TABLE `account_startupteam`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `account_technoteam`
--
ALTER TABLE `account_technoteam`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `booking_booking`
--
ALTER TABLE `booking_booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=438;

--
-- AUTO_INCREMENT for table `booking_maxdaysofbooking`
--
ALTER TABLE `booking_maxdaysofbooking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `booking_review`
--
ALTER TABLE `booking_review`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `booking_venue`
--
ALTER TABLE `booking_venue`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account_client_groups`
--
ALTER TABLE `account_client_groups`
  ADD CONSTRAINT `account_client_groups_client_id_228dd8b2_fk_account_client_id` FOREIGN KEY (`client_id`) REFERENCES `account_client` (`id`),
  ADD CONSTRAINT `account_client_groups_group_id_68213f09_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `account_client_user_permissions`
--
ALTER TABLE `account_client_user_permissions`
  ADD CONSTRAINT `account_client_user__client_id_d4484046_fk_account_c` FOREIGN KEY (`client_id`) REFERENCES `account_client` (`id`),
  ADD CONSTRAINT `account_client_user__permission_id_8852aa72_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_account_client_id` FOREIGN KEY (`user_id`) REFERENCES `account_client` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
