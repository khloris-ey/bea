-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 13, 2024 at 02:21 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `khloris_ecommerce`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(2, 'admin', '$2y$10$UCKnmHQ9IBQB57.mDohFlO1Ml/ZPFI4fCEkmQwgASWdo.kPILyk7.');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `price` int(10) DEFAULT NULL,
  `quantity` int(10) DEFAULT NULL,
  `image_url` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`cart_id`, `user_id`, `name`, `price`, `quantity`, `image_url`) VALUES
(1, 17, 'wwwww', 100, 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`) VALUES
(1, 'flower'),
(2, 'occasion'),
(3, 'customize');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `address` varchar(80) NOT NULL,
  `phone_num` varchar(15) NOT NULL,
  `delivery_option` varchar(15) NOT NULL,
  `qty` int(3) NOT NULL DEFAULT 1,
  `total` decimal(10,2) NOT NULL,
  `order_date` date DEFAULT curdate(),
  `delivery` date NOT NULL,
  `order_status` enum('Ordered','Pending','Completed') DEFAULT 'Ordered'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `description`, `price`, `quantity`, `image_url`, `category_id`, `type_id`) VALUES
(11, 'Sunflower Bouquet', '', 12000.00, 50, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725509898/images/sunflower/fwso4b9f6wjmuqwwkrmb.jpg', 1, 2),
(12, 'White Tulips Bouquet', '', 15000.00, 100, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725509904/images/sunflower/xb69l4rl7ou1zrf1q7ji.jpg', 1, 2),
(13, 'Golden Sunshine Bliss', '', 10000.00, 90, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725509919/images/sunflower/muadbqi0e7c45vft7jpr.jpg', 1, 2),
(14, 'Sunshine Serenade', '', 7000.00, 70, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725509926/images/sunflower/ldqdudh7gtzpzch5ssx4.jpg', 1, 2),
(15, 'Sunflower Delight', '', 20000.00, 10, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725509933/images/sunflower/xrw5gybjrj6vlisynhi3.jpg', 1, 2),
(16, 'Golden Glow Harmony', '', 5000.00, 40, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725509998/images/sunflower/fe7bc7ootsfe3kns2mdo.jpg', 1, 2),
(17, 'Tulip Elegance', '', 3500.00, 65, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725510132/images/tulips/euxenjxze3amuu6q7zfh.webp', 1, 4),
(18, 'Tulip Garden Delight', '', 8600.00, 60, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725510139/images/tulips/sem08xxrgexfn9p9czul.webp', 1, 4),
(19, 'Peach and White Bouquet', '', 15000.00, 50, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725510157/images/tulips/nt46g1smhnl5le1qarrh.jpg', 1, 4),
(20, 'Blue Tulips Bouquet', '', 5500.00, 35, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725510207/images/tulips/eoy2rjygcebsvqjcht1v.jpg', 1, 4),
(21, 'Orange Tulip Bouquet', '', 1200.00, 100, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725510234/images/tulips/zaym6mrpavpkesggvudf.webp', 1, 4),
(22, 'Peachy Tulip Bouquet', '', 2600.00, 45, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725510249/images/tulips/foyikbwklbc6hxpwlbnj.jpg', 1, 4),
(23, 'Blissful Blossoms', '', 5800.00, 35, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725510354/images/rose/lcbyvmogxq4wyjrrnneo.jpg', 1, 1),
(24, 'Timeless Romance', '', 25000.00, 90, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725510372/images/rose/ubn1zoyojxbift2yr2ta.webp', 1, 1),
(25, 'Velvet Embrace', '', 4999.00, 40, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725510440/images/rose/jfzpre2mhpbrukgvy6kr.jpg', 1, 1),
(26, 'Elegant Affair', '', 8500.00, 20, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725510446/images/rose/f2qmdjlksxi6cx7fu5p4.jpg', 1, 1),
(27, 'Passionate Charm', '', 9000.00, 55, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725510414/images/rose/ewvk6nzfeskumx3nxn51.jpg', 1, 1),
(28, 'Enchanted Garden', '', 3000.00, 10, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725510429/images/rose/wxbwjfkvmzloa8h9w0lj.jpg', 1, 1),
(29, 'Lily Serenity', '', 6999.00, 60, 'https://res.cloudinary.com/dzvd6o0og/image/upload/v1725527225/HB-3893_r640-1824x2384_wqs4ce.jpg', 1, 3),
(30, 'Majestic Bloom', '', 10500.00, 90, 'https://res.cloudinary.com/dzvd6o0og/image/upload/v1725527224/FTD-PCV_fpvsst.webp', 1, 3),
(31, 'Pure Radiance', '', 9000.00, 35, 'https://res.cloudinary.com/dzvd6o0og/image/upload/v1725527225/beautiful-lilies-bouquet_3_tdc4m7.jpg', 1, 3),
(32, 'Luminous Garden', '', 12000.00, 55, 'https://res.cloudinary.com/dzvd6o0og/image/upload/v1725527227/4665b4d2ec0b4b236dbea1ebd68bfa70_gdlzuw.jpg', 1, 3),
(33, 'Elegant Harmony', '', 2500.00, 10, 'https://res.cloudinary.com/dzvd6o0og/image/upload/v1725527226/lily35b1-scaled_cevi14.jpg', 1, 3),
(34, 'Opulent Splendor', '', 3500.00, 25, 'https://res.cloudinary.com/dzvd6o0og/image/upload/v1725527224/34198900b2d5482ceef4fcceadec0985_uvgewp.jpg', 1, 3),
(35, 'Red Rose', 'rose stem', 100.00, 50, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1723270009/flowers/lbxdapwfesoogo1tbi8s.png', 3, 11),
(36, 'White Rose', 'white rose stem', 100.00, 50, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1723359130/flowers/whiterose.png', 3, 11),
(37, 'Red Tulip', 'red tulips stem', 70.00, 60, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1723359191/flowers/ms9xtemytwlhyyhqeabb.png', 3, 11),
(38, 'Yellow Tulip', 'tulip stem', 70.00, 60, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1723359199/flowers/yellowtulips.png', 3, 11),
(39, 'White Tulip', 'tulip stem', 70.00, 60, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1723359203/flowers/whitetulips.png', 3, 11),
(40, 'Red Carnaion', 'carnation stem', 70.00, 50, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1723880362/flowers/redcarnation.png', 3, 11),
(41, 'White Carnation', 'carnation stem', 70.00, 70, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1723880362/flowers/stm3btzql1daz3mobly5.png', 3, 11),
(42, 'Pink Carnation', 'carnation stem', 70.00, 60, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1723880363/flowers/vsu5tp0qduzpnt6c4wjd.png', 3, 11),
(43, 'White Lily', 'Lily stem', 60.00, 100, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725817506/flowers/emj9un5g1kt7fwhh0ogx.png', 3, 11),
(44, 'Pink Lily', 'lily stem', 60.00, 90, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725820010/flowers/lily.png', 3, 11),
(45, 'Orange Dahlia', 'dahlia stem', 100.00, 50, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725824085/flowers/rttpojbctuub3nssek3n.png', 3, 11),
(46, 'White Dahlia', 'dahlia stem', 100.00, 50, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725824085/flowers/qvjekv39v4g04idwwyu8.png', 3, 11),
(47, 'Pink Dahlia', 'dahlia stem', 100.00, 50, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725824086/flowers/uywfmvp2mlxuonwgdesh.png', 3, 11),
(48, 'Violet Iris', 'iris stem', 70.00, 70, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725824294/flowers/j52tsqq0xfvt1z4kgzwe.png', 3, 11),
(49, 'Blue Iris', 'iris stem', 70.00, 80, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725824294/flowers/fjublfznvmpfabnxkhyu.png', 3, 11),
(50, 'Pink Hydrangea', 'hydrangea stem', 150.00, 40, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725826061/flowers/imdgxzj7aakq1d4cpxso.png', 3, 11),
(51, 'Blue Hydrangea', 'hydrangea stem', 150.00, 40, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725826067/flowers/h4v3aali5jdaw1qlhokj.png', 3, 11),
(52, 'Purple Anemone', 'anemone stem', 100.00, 50, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725826062/flowers/y82usejj2ac2i90jldzc.png', 3, 11),
(53, 'Red Anemone', 'anemone stem', 100.00, 50, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725826753/flowers/voikv1769whr33lkm645.png', 3, 11),
(54, 'Iris', 'iris stem', 70.00, 70, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725826744/flowers/wzqu2frxrdh8e4uiu6j2.png', 3, 11),
(55, 'Peach Peony', 'peony stem', 100.00, 60, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725826062/flowers/jfmqz2y1dbifiulcvbdk.png', 3, 11),
(56, 'Pink Peony', 'peony stem', 100.00, 65, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1725826752/flowers/bvbnyqmudbkqh0bd5zjj.png', 3, 11),
(57, 'Sunflower', 'sunflower stem', 50.00, 100, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1726073109/flowers/ms3vruapnyhspj8hbejv.png', 3, 11),
(58, 'Daisy', 'daisy stem', 30.00, 70, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1726072396/flowers/xaggp9utttrbdasstll8.png', 3, 11),
(59, 'Simple Brown Wrapper', 'brown wrapper', 50.00, 100, 'https://res.cloudinary.com/dsfcl09md/image/upload/v1723359520/flowers/kjy5hmwbf14bxt0c4qox.png', 3, 9),
(60, 'Pixie Dream', 'hydrangea bday', 12000.00, 20, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725509168/images/BIRTHDAYFLOWERS/br21gmyop5xo1f3ip4mo.jpg', 2, 5),
(61, 'Petal Poetry', 'birthday', 13000.00, 30, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725509186/images/BIRTHDAYFLOWERS/rjiv8evs1l0tcafoavxf.jpg', 2, 5),
(62, 'Crimson Kiss', 'bday', 11000.00, 20, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725509196/images/BIRTHDAYFLOWERS/b3ik1hj0ujq0ongymvgs.jpg', 2, 5),
(63, 'Blossom Granduer', 'bday', 10000.00, 30, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725509294/images/BIRTHDAYFLOWERS/hyxfzseaxhtpjhn5talu.webp', 2, 5),
(64, 'Blushing Dreamscape', 'bday', 11500.00, 24, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725509311/images/BIRTHDAYFLOWERS/xnksmff0umawglcuqwoz.jpg', 2, 5),
(65, 'Springtime Fantasy', 'bday', 12000.00, 12, 'https://res.cloudinary.com/dogrgo15f/image/upload/v1725509319/images/BIRTHDAYFLOWERS/vryvirl13wmuilttqjos.jpg', 2, 5);

-- --------------------------------------------------------

--
-- Table structure for table `types`
--

CREATE TABLE `types` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `category_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `types`
--

INSERT INTO `types` (`id`, `name`, `category_id`) VALUES
(1, 'Rose', 1),
(2, 'Sunflower', 1),
(3, 'Lily', 1),
(4, 'Tulip', 1),
(5, 'Birthday', 2),
(6, 'Valentine', 2),
(7, 'Funeral', 2),
(9, 'wrappers', 3),
(10, 'ribbons', 3),
(11, 'flower', 3);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `name`, `username`, `email`, `password`) VALUES
(6, 'ss', 'ssss', 'ss', 'ssss'),
(12, 'ayheca', 'ayheca', 'ayheca', 'ayheca'),
(13, '', 'ss', 'sss', 'rrr'),
(14, 'louise', 'louise', 'louise', 'louise'),
(16, 'qqqq', 'qqqq', 'qqqq', 'qqqq'),
(17, 'new', 'new', 'new', 'new'),
(18, 'qq', 'qq', 'qq', 'qq');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`cart_id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`),
  ADD KEY `type_id` (`type_id`);

--
-- Indexes for table `types`
--
ALTER TABLE `types`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `cart_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT for table `types`
--
ALTER TABLE `types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`ID`);

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  ADD CONSTRAINT `products_ibfk_2` FOREIGN KEY (`type_id`) REFERENCES `types` (`id`);

--
-- Constraints for table `types`
--
ALTER TABLE `types`
  ADD CONSTRAINT `types_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
