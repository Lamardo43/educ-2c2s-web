-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: std-mysql
-- Время создания: Май 30 2024 г., 15:57
-- Версия сервера: 5.7.26-0ubuntu0.16.04.1
-- Версия PHP: 8.1.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `std_2408_course`
--

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `route_id` int(11) NOT NULL,
  `person_count` int(11) NOT NULL,
  `total_price` int(11) NOT NULL,
  `order_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `duration` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `orders`
--

INSERT INTO `orders` (`id`, `user_id`, `route_id`, `person_count`, `total_price`, `order_date`, `duration`) VALUES
(1, 14, 65, 9, 34480, '2024-05-21 23:30:47', 5),
(2, 14, 93, 4, 5316, '2024-11-01 16:48:00', 4),
(3, 18, 42, 3, 31044, '2024-05-21 23:30:47', 6),
(4, 12, 78, 3, 26172, '2024-05-21 23:30:47', 6),
(7, 26, 23, 15, 6801, '2024-05-21 23:30:47', 3),
(8, 19, 69, 5, 23994, '2024-05-21 23:30:47', 3),
(9, 12, 48, 4, 53502, '2024-05-21 23:30:47', 6),
(10, 27, 6, 1, 4357, '2024-11-26 17:19:00', 1),
(11, 1, 36, 20, 658680, '2024-05-22 04:30:47', 6),
(12, 27, 53, 11, 16473, '2024-05-21 23:30:47', 3),
(13, 25, 13, 14, 36075, '2024-05-21 23:30:47', 5),
(14, 5, 70, 8, 18392, '2024-05-21 23:30:47', 2),
(16, 14, 29, 15, 17091, '2024-05-21 23:30:47', 3),
(17, 28, 6, 12, 26142, '2024-05-21 23:30:47', 6),
(18, 28, 3, 15, 10146, '2024-05-21 23:30:47', 6),
(19, 19, 84, 14, 14796, '2024-05-21 23:30:47', 2),
(20, 14, 94, 10, 52794, '2024-05-21 23:30:47', 6),
(21, 19, 34, 12, 18640, '2024-05-21 23:30:47', 5),
(22, 18, 55, 11, 20485, '2024-05-21 23:30:47', 5),
(23, 24, 30, 15, 33410, '2024-05-21 23:30:47', 5),
(24, 25, 68, 1, 3754, '2024-05-21 23:30:47', 2),
(25, 11, 4, 17, 31204, '2024-05-21 23:30:47', 4),
(26, 26, 6, 15, 21785, '2024-05-21 23:30:47', 5),
(27, 11, 4, 9, 15602, '2024-05-21 23:30:47', 2),
(28, 28, 79, 4, 28544, '2024-11-18 13:18:00', 4),
(29, 12, 63, 10, 8542, '2024-05-21 23:30:47', 1),
(33, 1, 2, 20, 302400, '2024-05-23 09:32:00', 6);

-- --------------------------------------------------------

--
-- Структура таблицы `routes`
--

CREATE TABLE `routes` (
  `id` int(11) NOT NULL,
  `route` text NOT NULL,
  `guide_id` int(11) NOT NULL,
  `price_per_person` decimal(10,0) NOT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `routes`
--

INSERT INTO `routes` (`id`, `route`, `guide_id`, `price_per_person`, `name`) VALUES
(1, 'Парк Горького&Московский музей архитектуры&Музей-квартира Федора Шаляпина&Новодевичий монастырь&Музей Москвы&Музей Победы&Музей физической культуры и спорта России&Московский Кремль&Большой театр&Музей-квартира Федора Шаляпина&Музей железных дорог России&Сад музеон&Музей истории Москвы&Сад музеон', 7, 2147, 'Экскурсия по Москве 988'),
(2, 'Сад музеон&Красная площадь&Новодевичий монастырь&Московский зоомузей&Музей-заповедник «Царицыно»&Московский зоопарк&Новодевичий монастырь&Третьяковская галерея&Собор Василия Блаженного&Московский областной краеведческий музей&Сад музеон', 20, 2520, 'Экскурсия по Москве 245'),
(3, 'Московский музей ретроавтомобилей&Московский зоопарк&Музей Москвы&Храм Христа Спасителя&Музей-заповедник «Царицыно»', 3, 1691, 'Экскурсия по Москве 258'),
(4, 'Московский государственный академический театр детей и молодежи на Таганке&Третьяковская галерея&Московский музей кукол и детских книг&Музей народного искусства&Музей Пушкина на Арбате&Музей советских игровых автоматов&Третьяковская галерея&Музей Востока&Московский зоопарк', 11, 7801, 'Экскурсия по Москве 555'),
(5, 'Московский зоопарк&Музей космонавтики&Собор Василия Блаженного&Собор Василия Блаженного&Московский зоомузей&Коломенское&ВДНХ&Музей кино и мультимедиа&Московский государственный академический театр детей и молодежи на Таганке&Музей кукол', 15, 1037, 'Экскурсия по Москве 3'),
(6, 'Собор Василия Блаженного&Красная площадь&Собор Василия Блаженного&Музей изобразительных искусств имени Пушкина&Московский музей медицины&Храм Христа Спасителя&Кремль&Новодевичий монастырь&ВДНХ&Музей Исаакиевского собора&Музей изобразительных искусств имени Пушкина&Московский музей естественной истории&Московский метрополитен', 4, 4357, 'Экскурсия по Москве 349'),
(7, 'Московский музей миниатюр&Московский музей миниатюр&Кремль&Музей хоккея&Московский областной музей изобразительных искусств имени И.Н. Крамского&Собор Василия Блаженного', 7, 8455, 'Экскурсия по Москве 734'),
(8, 'Музей космонавтики и ракетных войск РФ&Музей-квартира Федора Шаляпина&Музей археологии&Музей-квартира А.М. Васнецова&Третьяковская галерея&Музей-квартира А.М. Васнецова&Музей кукол&Московский зоопарк&Музей космонавтики и ракетных войск РФ&Музей Исаакиевского собора&Сад музеон', 2, 5172, 'Экскурсия по Москве 625'),
(9, 'Московский музей ретроавтомобилей&Московский Кремль&Собор Василия Блаженного&Музей истории литературы&Коломенское&Музей истории Москвы&Музей советских игровых автоматов', 20, 5874, 'Экскурсия по Москве 922'),
(10, 'Музей космонавтики&Московская детская художественная галерея&Московская государственная консерватория им. П.И. Чайковского&ВДНХ&Московский областной художественный музей имени И.В. Сурикова&Музей истории Москвы&Парк Лосиный остров&Московский музей миниатюр&Музей-заповедник «Царицыно»&Центральный дом художника&Парк Патриот&Московский международный Дом Музыки&Парк Зарядье&Большой театр&Музей городского транспорта', 9, 2081, 'Экскурсия по Москве 734'),
(11, 'Московский музей современного искусства на Эрарте&Парк Зарядье&Музей животных&Московский метрополитен&Московский музей кукол и детских книг&Крымская набережная', 20, 4331, 'Экскурсия по Москве 902'),
(12, 'Музей кино и мультимедиа&Коломенское&Парк Патриот&Московский музей кукол и детских книг&Государственный музей изобразительных искусств имени А.С. Пушкина&Строгинский парк&Московский музей декоративно-прикладного искусства&Коломенское&Сад музеон&Музей археологии&Храм Христа Спасителя&Крымская набережная', 20, 4680, 'Экскурсия по Москве 310'),
(13, 'Большой театр&Крымская набережная&Третьяковская галерея&Музей физической культуры и спорта России&Московский планетарий&Музей Москвы&Московский музей архитектуры&Большой театр&Московский метрополитен&Музей детства&Музей военной техники', 7, 7215, 'Экскурсия по Москве 843'),
(14, 'Третьяковская галерея&Музей кукол&Храм Христа Спасителя&Московская детская художественная галерея&Московский Кремль&ВДНХ&Московский музей миниатюр', 2, 7506, 'Экскурсия по Москве 282'),
(15, 'ВДНХ&Московская детская художественная галерея&Московский музей декоративно-прикладного искусства&Большой театр&Музей животных&Государственный музей изобразительных искусств имени А.С. Пушкина&Музей космонавтики&Храм Христа Спасителя&Московский музей кино&Музей изобразительных искусств имени Пушкина&Кремль&Музей Пушкина на Арбате&Московский зоомузей&Музей-квартира Федора Шаляпина', 2, 2772, 'Экскурсия по Москве 882'),
(16, 'Музей изобразительных искусств имени Пушкина&Московский музей архитектуры&Музей советских игровых автоматов&Музей Исаакиевского собора&Кремль&Музей космонавтики&Новодевичий монастырь&Сад музеон&Московский музей садово-паркового искусства&Музей кукол&Большой театр&Музей Востока&Парк Лосиный остров&Красная площадь', 8, 8189, 'Экскурсия по Москве 564'),
(17, 'Московский Кремль&Музей кино и мультимедиа&Кремль&Строгинский парк&Музей советских игровых автоматов&Музей современного искусства «Гараж»&Московский музей медицины&Музей-квартира Федора Шаляпина&Музей Москвы&Строгинский парк&Музей кукол&Московский музей медицины&Сад музеон&Парк Горького', 20, 8076, 'Экскурсия по Москве 175'),
(18, 'Государственный музей изобразительных искусств имени А.С. Пушкина&Музей Исаакиевского собора&Московский Кремль&Музей-заповедник «Царицыно»&Центральный дом художника&Музей истории Москвы&Московский метрополитен&Новодевичий монастырь&Храм Христа Спасителя&Центральный дом художника&Московский музей кино&Музей Москвы&Кремль&Музей животных&Государственный музей изобразительных искусств имени А.С. Пушкина', 20, 2367, 'Экскурсия по Москве 180'),
(19, 'Музей космонавтики и ракетных войск РФ&Московский музей ретроавтомобилей&Московский зоопарк&Музей современного искусства «Гараж»&Парк Горького&Музей современного искусства «Гараж»&Музей Москвы&Музей военной техники&Музей Востока&Московский зоопарк&Музей физической культуры и спорта России&Музей космонавтики', 10, 8120, 'Экскурсия по Москве 377'),
(20, 'Московская детская художественная галерея&Сад музеон&Парк Патриот&Московская государственная консерватория им. П.И. Чайковского&Сад музеон&Московский государственный академический театр детей и молодежи на Таганке&Киностудия Мосфильм&Собор Василия Блаженного&Московский зоомузей', 17, 9597, 'Экскурсия по Москве 345'),
(21, 'Московский музей кино&Кремль&Парк Зарядье&Московский музей архитектуры&Музей истории Москвы&Новодевичий монастырь&Московский музей естественной истории&Сад музеон&Московский зоомузей&Московский метрополитен&Московский областной краеведческий музей', 3, 9614, 'Экскурсия по Москве 594'),
(22, 'Музей Победы&Кремль&Музей космонавтики&Музей космонавтики&Музей Востока&Московский музей архитектуры&Музей военной техники', 6, 5962, 'Экскурсия по Москве 932'),
(23, 'Музей советских игровых автоматов&Большой театр&ВДНХ&Музей космонавтики&ВДНХ&Красная площадь&Музей физической культуры и спорта России&Московский музей естественной истории', 9, 2267, 'Экскурсия по Москве 878'),
(24, 'Московский метрополитен&Музей Пушкина на Арбате&Музей истории Москвы&Музей космонавтики и ракетных войск РФ&Московский музей современного искусства на Эрарте&Музей Москвы&Московский музей кукол и детских книг&Музей Победы&Московский областной краеведческий музей&Красная площадь&Московский музей садово-паркового искусства&Собор Василия Блаженного', 13, 2287, 'Экскурсия по Москве 595'),
(25, 'Музей физической культуры и спорта России&Музей животных&Московский международный Дом Музыки&Музей кукол&Большой театр', 7, 6781, 'Экскурсия по Москве 339'),
(26, 'Московский музей декоративно-прикладного искусства&Музей Москвы&Московский музей архитектуры&Музей-квартира Федора Шаляпина&Московский метрополитен&Красная площадь&Музей железных дорог России&Московский зоопарк&Московский областной художественный музей имени И.В. Сурикова&Музей истории Москвы&Храм Христа Спасителя&Музей животных&Московский музей кино&Большой театр', 13, 5733, 'Экскурсия по Москве 911'),
(27, 'Московский музей садово-паркового искусства&Собор Василия Блаженного&Музей космонавтики&Музей Востока&Парк Горького&Музей Востока', 13, 9860, 'Экскурсия по Москве 536'),
(28, 'Музей военной техники&Музей Пушкина на Арбате&Музей детства&Красная площадь&Строгинский парк&Храм Христа Спасителя&Музей городского транспорта&Сад музеон&Музей детства&Парк Горького&Музей кино и мультимедиа&Музей железных дорог России&Московский областной краеведческий музей', 20, 4380, 'Экскурсия по Москве 948'),
(29, 'Московский музей архитектуры&Музей животных&Музей Исаакиевского собора&Храм Христа Спасителя&Музей народного искусства&Государственный музей изобразительных искусств имени А.С. Пушкина&Музей Победы&Музей Победы&Московский музей истории московского футбола', 10, 5697, 'Экскурсия по Москве 132'),
(30, 'Музей изобразительных искусств имени Пушкина&Музей космонавтики&Музей авиации&Московский международный Дом Музыки&Красная площадь', 9, 6682, 'Экскурсия по Москве 816'),
(31, 'Московский метрополитен&Московский музей кукол и детских книг&Московский музей медицины&Парк Коломенское&Парк Патриот&Музей Исаакиевского собора', 2, 9753, 'Экскурсия по Москве 681'),
(32, 'Московский музей кукол и детских книг&Московский зоопарк&Парк культуры и отдыха имени Горького&Музей Московского метрополитена&Музей-квартира Федора Шаляпина&Парк Горького&Московский метрополитен&Московский областной музей изобразительных искусств имени И.Н. Крамского&Московский зоопарк&Музей изобразительных искусств имени Пушкина&Парк Патриот&Новодевичий монастырь&Центральный дом художника&Московский музей современного искусства на Эрарте', 11, 6586, 'Экскурсия по Москве 955'),
(33, 'Третьяковская галерея&Строгинский парк&Музей железных дорог России&Третьяковская галерея&Музей физической культуры и спорта России&Музей животных&Третьяковская галерея&Московский планетарий&Московский зоомузей&Московский Кремль&Московский государственный академический театр детей и молодежи на Таганке&Парк культуры и отдыха имени Горького&Музей военной техники&Крымская набережная&Парк Патриот', 8, 5827, 'Экскурсия по Москве 735'),
(34, 'Московский музей ретроавтомобилей&Парк Горького&Музей физической культуры и спорта России&Храм Христа Спасителя&Московский областной краеведческий музей&Московский музей современного искусства на Эрарте', 2, 3728, 'Экскурсия по Москве 810'),
(35, 'ВДНХ&Музей изобразительных искусств имени Пушкина&Музей Москвы&Музей военной техники&Московский государственный академический театр детей и молодежи на Таганке&Музей Исаакиевского собора&Музей-заповедник «Царицыно»', 4, 4193, 'Экскурсия по Москве 843'),
(36, 'Парк Коломенское&Московский музей медицины&Музей Победы&Музей истории литературы&Третьяковская галерея&Московский зоопарк&Государственный музей изобразительных искусств имени А.С. Пушкина', 4, 5489, 'Экскурсия по Москве 787'),
(37, 'Музей Исаакиевского собора&Красная площадь&Коломенское&Московский музей садово-паркового искусства&Музей изобразительных искусств имени Пушкина&Музей хоккея&Третьяковская галерея&Большой театр', 6, 4735, 'Экскурсия по Москве 403'),
(38, 'Музей изобразительных искусств имени Пушкина&ВДНХ&Московский планетарий&Московский зоопарк&Московский музей кино&Музей истории литературы', 17, 2379, 'Экскурсия по Москве 656'),
(39, 'Московский музей архитектуры&Музей Исаакиевского собора&Музей хоккея&Московский музей архитектуры&Парк культуры и отдыха имени Горького', 10, 6584, 'Экскурсия по Москве 67'),
(40, 'Музей физической культуры и спорта России&Крымская набережная&Коломенское&Музей Москвы&Музей Победы&Московский музей архитектуры&Музей Москвы&Музей Москвы&Коломенское&Центральный дом художника', 20, 2222, 'Экскурсия по Москве 370'),
(41, 'Московская детская художественная галерея&Сад музеон&Третьяковская галерея&Коломенское&Московский музей архитектуры', 6, 1110, 'Экскурсия по Москве 646'),
(42, 'Музей современного искусства «Гараж»&Музей изобразительных искусств имени Пушкина&Московский зоопарк&Музей железных дорог России&Красная площадь&Московский метрополитен&Кремль&Музей Москвы&Московский музей естественной истории&Третьяковская галерея&Парк Лосиный остров&Сад музеон', 7, 5174, 'Экскурсия по Москве 122'),
(43, 'Парк Коломенское&Собор Василия Блаженного&Большой театр&Третьяковская галерея&Музей истории Москвы&Сад музеон', 16, 5445, 'Экскурсия по Москве 669'),
(44, 'Парк Горького&Строгинский парк&Большой театр&Парк Горького&Музей советских игровых автоматов&Парк Горького&Музей истории Москвы&Московский музей декоративно-прикладного искусства&Парк культуры и отдыха имени Горького&Красная площадь&Московский международный Дом Музыки&Музей археологии&Московский музей ретроавтомобилей&Строгинский парк', 6, 8293, 'Экскурсия по Москве 979'),
(45, 'Парк Лосиный остров&Московский зоопарк&Музей-квартира Федора Шаляпина&Крымская набережная&ВДНХ&Московский музей ретроавтомобилей&Музей Исаакиевского собора&Музей космонавтики и ракетных войск РФ&Музей животных&Собор Василия Блаженного&Парк культуры и отдыха имени Горького&Музей Исаакиевского собора', 20, 8661, 'Экскурсия по Москве 889'),
(46, 'Кремль&Московский зоопарк&Парк Лосиный остров&Парк Коломенское&Музей городского транспорта&Музей хоккея&Музей советских игровых автоматов&Московский метрополитен&Музей военной техники&Музей детства&Музей физической культуры и спорта России&Парк Горького', 8, 9044, 'Экскурсия по Москве 506'),
(47, 'Парк Коломенское&Музей изобразительных искусств имени Пушкина&Московский музей миниатюр&Новодевичий монастырь&Московский метрополитен&Музей кукол&Московский областной художественный музей имени И.В. Сурикова', 7, 2204, 'Экскурсия по Москве 864'),
(48, 'Киностудия Мосфильм&Сад музеон&Парк Лосиный остров&Музей космонавтики&Крымская набережная&Крымская набережная&Московский музей садово-паркового искусства&Музей бронетехники&Строгинский парк', 17, 8917, 'Экскурсия по Москве 803'),
(49, 'Московский музей садово-паркового искусства&Строгинский парк&Московский международный Дом Музыки&Музей Московского метрополитена&ВДНХ&Государственный музей изобразительных искусств имени А.С. Пушкина&Кремль&Музей Победы&Музей железных дорог России&Московский планетарий&Парк культуры и отдыха имени Горького&Парк культуры и отдыха имени Горького&Большой театр&Парк культуры и отдыха имени Горького', 6, 1396, 'Экскурсия по Москве 420'),
(50, 'Московский музей истории московского футбола&Музей истории Москвы&Музей городского транспорта&Строгинский парк&Музей Исаакиевского собора&Музей-заповедник «Царицыно»&Московский зоопарк&Московский планетарий&Музей кино и мультимедиа', 15, 2826, 'Экскурсия по Москве 691'),
(51, 'Музей бронетехники&Парк культуры и отдыха имени Горького&Музей физической культуры и спорта России&Новодевичий монастырь&Музей военной техники&Собор Василия Блаженного&Музей Исаакиевского собора&Музей изобразительных искусств имени Пушкина&Красная площадь&Московский международный Дом Музыки&Храм Христа Спасителя&Московский зоомузей&Московская детская художественная галерея&Московский музей истории московского футбола', 17, 9891, 'Экскурсия по Москве 193'),
(52, 'Большой театр&Музей космонавтики&Новодевичий монастырь&Московский зоопарк&Храм Христа Спасителя&Московский музей миниатюр&Музей изобразительных искусств имени Пушкина&Московский международный Дом Музыки&Музей советских игровых автоматов&Строгинский парк&Музей Исаакиевского собора', 6, 3816, 'Экскурсия по Москве 892'),
(53, 'Московский Кремль&Московская государственная консерватория им. П.И. Чайковского&Музей археологии&Московский метрополитен&Музей Востока&Кремль&Музей-квартира Федора Шаляпина&Московский зоопарк&ВДНХ', 7, 5491, 'Экскурсия по Москве 881'),
(54, 'Музей Москвы&Кремль&Музей современного искусства «Гараж»&Парк культуры и отдыха имени Горького&Новодевичий монастырь', 8, 6311, 'Экскурсия по Москве 727'),
(55, 'Московский международный Дом Музыки&Музей Исаакиевского собора&Музей кино и мультимедиа&Московский музей естественной истории&Московский музей медицины', 17, 4097, 'Экскурсия по Москве 991'),
(56, 'Музей детства&Музей Исаакиевского собора&Московский музей современного искусства на Эрарте&Парк Лосиный остров&Киностудия Мосфильм&Музей авиации&Московский областной художественный музей имени И.В. Сурикова&Музей истории Москвы&Строгинский парк&Московский музей садово-паркового искусства&Парк Горького&Парк культуры и отдыха имени Горького', 13, 2805, 'Экскурсия по Москве 775'),
(57, 'ВДНХ&Музей Пушкина на Арбате&Музей Пушкина на Арбате&Музей Востока&Московский музей современного искусства на Эрарте&Музей-заповедник «Царицыно»&Третьяковская галерея&Крымская набережная&Собор Василия Блаженного&Строгинский парк&Московский музей миниатюр&Московский музей медицины', 17, 5273, 'Экскурсия по Москве 899'),
(58, 'Собор Василия Блаженного&Московский музей архитектуры&Строгинский парк&Московский зоопарк&Московский метрополитен', 16, 6710, 'Экскурсия по Москве 173'),
(59, 'Московский зоомузей&Третьяковская галерея&Музей Востока&Собор Василия Блаженного&Музей современного искусства «Гараж»&Музей Востока&Музей Пушкина на Арбате&Московский государственный академический театр детей и молодежи на Таганке&Московский музей кино&Московский музей архитектуры&Крымская набережная&Музей-квартира Федора Шаляпина&Новодевичий монастырь&Московский зоопарк&Московский зоопарк', 3, 2946, 'Экскурсия по Москве 165'),
(60, 'Музей хоккея&Московский метрополитен&Музей хоккея&Центральный дом художника&Музей изобразительных искусств имени Пушкина&Московский областной краеведческий музей&Государственный музей изобразительных искусств имени А.С. Пушкина&Московский международный Дом Музыки', 10, 6587, 'Экскурсия по Москве 307'),
(61, 'Московский музей садово-паркового искусства&Музей Московского метрополитена&Музей Пушкина на Арбате&Третьяковская галерея&Музей Исаакиевского собора&Музей-заповедник «Царицыно»&Московский государственный академический театр детей и молодежи на Таганке&Музей археологии&Московский музей архитектуры&Музей Пушкина на Арбате&Московский музей ретроавтомобилей&Музей Востока&Музей Исаакиевского собора', 20, 9243, 'Экскурсия по Москве 39'),
(62, 'Московский музей естественной истории&Строгинский парк&Киностудия Мосфильм&Музей-заповедник «Царицыно»&Собор Василия Блаженного&Красная площадь&Парк культуры и отдыха имени Горького&Строгинский парк&ВДНХ&Музей археологии&Крымская набережная', 13, 6506, 'Экскурсия по Москве 272'),
(63, 'Музей истории Москвы&Строгинский парк&Музей изобразительных искусств имени Пушкина&Музей Московского метрополитена&Парк Зарядье&Музей-заповедник «Царицыно»&Парк культуры и отдыха имени Горького&Музей Пушкина на Арбате&Собор Василия Блаженного&Музей истории литературы&Музей-квартира Федора Шаляпина&Большой театр&Большой театр&Кремль&Музей военной техники', 9, 8542, 'Экскурсия по Москве 246'),
(64, 'Московский музей декоративно-прикладного искусства&Московский музей миниатюр&Московский зоопарк&Московский музей естественной истории&Музей Москвы&Музей изобразительных искусств имени Пушкина', 9, 6087, 'Экскурсия по Москве 410'),
(65, 'Музей-квартира Федора Шаляпина&Музей кукол&Московский музей декоративно-прикладного искусства&Третьяковская галерея&Московский Кремль', 3, 6896, 'Экскурсия по Москве 314'),
(66, 'Музей железных дорог России&Кремль&Парк Патриот&Коломенское&Новодевичий монастырь&Музей космонавтики&Парк Патриот&Музей городского транспорта&Музей бронетехники&Музей изобразительных искусств имени Пушкина&Музей советских игровых автоматов&Музей кино и мультимедиа&Московский музей естественной истории&Музей изобразительных искусств имени Пушкина&Сад музеон', 2, 5695, 'Экскурсия по Москве 340'),
(67, 'Московский Кремль&Московский зоопарк&ВДНХ&Собор Василия Блаженного&Музей Московского метрополитена&Музей Исаакиевского собора&Московский Кремль&Музей народного искусства&Киностудия Мосфильм&Музей военной техники', 2, 8602, 'Экскурсия по Москве 758'),
(68, 'Музей Пушкина на Арбате&Музей народного искусства&Музей кукол&Московский музей архитектуры&ВДНХ&Третьяковская галерея&Музей Победы&ВДНХ', 13, 1877, 'Экскурсия по Москве 769'),
(69, 'Музей современного искусства «Гараж»&Коломенское&Музей истории литературы&Красная площадь&Музей истории литературы&Московский государственный академический театр детей и молодежи на Таганке&Московский музей миниатюр&Кремль&Парк Горького&Музей кукол&Парк культуры и отдыха имени Горького&Киностудия Мосфильм&Новодевичий монастырь', 13, 7998, 'Экскурсия по Москве 572'),
(70, 'Музей Востока&Сад музеон&Большой театр&Музей космонавтики&Музей истории Москвы&Музей кино и мультимедиа&Большой театр&Строгинский парк&Музей-квартира Федора Шаляпина&Музей современного искусства «Гараж»&Музей современного искусства «Гараж»&Собор Василия Блаженного&Музей физической культуры и спорта России', 13, 9196, 'Экскурсия по Москве 550'),
(71, 'Красная площадь&Красная площадь&Московский зоопарк&Крымская набережная&Музей Пушкина на Арбате&Музей кино и мультимедиа&Парк Лосиный остров&Московский музей кино&Московский Кремль&Московская детская художественная галерея&Музей кино и мультимедиа&Третьяковская галерея&Московский зоомузей&Музей космонавтики', 17, 8602, 'Экскурсия по Москве 35'),
(72, 'Сад музеон&Музей космонавтики&Музей истории литературы&Музей Победы&Парк Горького&Музей-квартира А.М. Васнецова&Музей военной техники&Музей кино и мультимедиа&Московский зоопарк&Музей-заповедник «Царицыно»&Московский музей медицины&Парк Зарядье&Московский Кремль&Музей истории литературы&Московский музей медицины', 3, 8593, 'Экскурсия по Москве 525'),
(73, 'Музей детства&Музей Исаакиевского собора&Музей Московского метрополитена&Московский зоопарк&Музей военной техники&Музей истории литературы&Крымская набережная&Московский музей кукол и детских книг&Парк Патриот&Московский музей медицины&Большой театр', 2, 6768, 'Экскурсия по Москве 519'),
(74, 'Московский областной краеведческий музей&Музей космонавтики&Собор Василия Блаженного&Музей хоккея&Музей-квартира Федора Шаляпина&Музей Москвы&Музей Исаакиевского собора&Коломенское&ВДНХ&Красная площадь&Музей истории Москвы&Музей физической культуры и спорта России', 11, 9334, 'Экскурсия по Москве 18'),
(75, 'Кремль&Музей Москвы&Музей Москвы&Музей-заповедник «Царицыно»&Московский государственный академический театр детей и молодежи на Таганке&Новодевичий монастырь', 10, 6770, 'Экскурсия по Москве 535'),
(76, 'Кремль&Музей авиации&Музей Пушкина на Арбате&Музей Победы&Крымская набережная&Музей физической культуры и спорта России&Музей изобразительных искусств имени Пушкина&Музей железных дорог России&Музей-квартира Федора Шаляпина&Музей народного искусства&ВДНХ&Музей военной техники&Музей Исаакиевского собора&Московский зоопарк', 4, 4584, 'Экскурсия по Москве 619'),
(77, 'Новодевичий монастырь&Сад музеон&Музей детства&Московский областной художественный музей имени И.В. Сурикова&Музей-квартира Федора Шаляпина&Московский зоопарк&Московский музей миниатюр&Красная площадь&Московский Кремль&Сад музеон&Кремль&Парк Горького&Московский музей кино&Музей Московского метрополитена', 3, 9288, 'Экскурсия по Москве 491'),
(78, 'Московский международный Дом Музыки&Большой театр&Большой театр&Московский зоопарк&Парк Коломенское&Музей истории литературы&Коломенское&Музей Исаакиевского собора&Московский музей естественной истории', 15, 4362, 'Экскурсия по Москве 595'),
(79, 'Музей Исаакиевского собора&Московский международный Дом Музыки&Московский музей миниатюр&Музей космонавтики&Парк Зарядье&Новодевичий монастырь&Кремль&Музей военной техники&Музей-заповедник «Царицыно»&Храм Христа Спасителя&Музей-квартира Федора Шаляпина&Московский метрополитен', 10, 7136, 'Экскурсия по Москве 505'),
(80, 'Кремль&Музей городского транспорта&Московский метрополитен&Московский планетарий&Музей Москвы&Музей Исаакиевского собора&Московский музей архитектуры&Музей кино и мультимедиа&Музей бронетехники&Музей космонавтики', 8, 5118, 'Экскурсия по Москве 736'),
(81, 'Московский международный Дом Музыки&Большой театр&Парк Коломенское&Третьяковская галерея&Парк культуры и отдыха имени Горького&Московский музей кукол и детских книг&Киностудия Мосфильм&Кремль&Кремль&Музей космонавтики&Кремль&Музей космонавтики&Музей военной техники&Московская детская художественная галерея', 15, 2571, 'Экскурсия по Москве 166'),
(82, 'Новодевичий монастырь&Музей Пушкина на Арбате&Музей Московского метрополитена&Московский областной музей изобразительных искусств имени И.Н. Крамского&Московский государственный академический театр детей и молодежи на Таганке&Московский музей кукол и детских книг&Московский государственный академический театр детей и молодежи на Таганке&Новодевичий монастырь&Красная площадь&Музей бронетехники', 11, 6055, 'Экскурсия по Москве 623'),
(83, 'Собор Василия Блаженного&Музей истории Москвы&Московский музей истории московского футбола&ВДНХ&Московский музей архитектуры&Музей городского транспорта', 8, 3349, 'Экскурсия по Москве 617'),
(84, 'Парк культуры и отдыха имени Горького&Московский международный Дом Музыки&Музей физической культуры и спорта России&Музей изобразительных искусств имени Пушкина&Собор Василия Блаженного&Музей-квартира Федора Шаляпина&Московский государственный академический театр детей и молодежи на Таганке&Музей советских игровых автоматов', 13, 7398, 'Экскурсия по Москве 216'),
(85, 'Музей Пушкина на Арбате&Музей детства&Московский музей миниатюр&Музей детства&Московский музей архитектуры', 4, 8345, 'Экскурсия по Москве 229'),
(86, 'Московский музей ретроавтомобилей&Московский зоопарк&Музей изобразительных искусств имени Пушкина&Московский международный Дом Музыки&Московский Кремль&Московский музей кукол и детских книг&Московский зоопарк&Музей Москвы&Московский музей садово-паркового искусства&Московский международный Дом Музыки&Музей советских игровых автоматов&Государственный музей изобразительных искусств имени А.С. Пушкина&Большой театр&Музей кино и мультимедиа&Музей Востока', 4, 5036, 'Экскурсия по Москве 497'),
(87, 'Музей Москвы&Музей военной техники&Музей Исаакиевского собора&Музей военной техники&Московский музей ретроавтомобилей&Строгинский парк&Московский музей садово-паркового искусства&Музей советских игровых автоматов', 2, 2336, 'Экскурсия по Москве 795'),
(88, 'Московский Кремль&Московский зоомузей&Музей Москвы&Московский музей архитектуры&Музей Пушкина на Арбате&Строгинский парк&Киностудия Мосфильм&Московский музей ретроавтомобилей&Строгинский парк&Московский метрополитен', 8, 9999, 'Экскурсия по Москве 485'),
(89, 'ВДНХ&Музей Пушкина на Арбате&Музей археологии&ВДНХ&Московский международный Дом Музыки&Сад музеон&Московский государственный академический театр детей и молодежи на Таганке', 8, 2815, 'Экскурсия по Москве 37'),
(90, 'Сад музеон&Московский музей естественной истории&Кремль&ВДНХ&Московский музей естественной истории&Музей Исаакиевского собора&Третьяковская галерея&Московский музей ретроавтомобилей&Кремль&Московский музей садово-паркового искусства', 4, 3361, 'Экскурсия по Москве 732'),
(91, 'Московский музей садово-паркового искусства&Московский зоопарк&Большой театр&Музей Исаакиевского собора&Московский музей ретроавтомобилей&Московский зоопарк&Московский музей кино&Музей космонавтики и ракетных войск РФ&Парк культуры и отдыха имени Горького&Московский зоопарк&Строгинский парк&Московский международный Дом Музыки&Музей Исаакиевского собора&Музей-квартира Федора Шаляпина&Собор Василия Блаженного', 7, 1627, 'Экскурсия по Москве 546'),
(92, 'Московский музей садово-паркового искусства&Храм Христа Спасителя&Крымская набережная&Музей космонавтики&Крымская набережная&Парк Зарядье&Большой театр', 3, 4563, 'Экскурсия по Москве 535'),
(93, 'Московский областной краеведческий музей&Крымская набережная&Музей изобразительных искусств имени Пушкина&Московский метрополитен&Сад музеон&Третьяковская галерея', 13, 1329, 'Экскурсия по Москве 37'),
(94, 'Московский музей естественной истории&Музей изобразительных искусств имени Пушкина&Музей-заповедник «Царицыно»&Музей изобразительных искусств имени Пушкина&Сад музеон&Музей-заповедник «Царицыно»&Парк Горького&Храм Христа Спасителя', 10, 8799, 'Экскурсия по Москве 578'),
(95, 'Московский зоопарк&Музей Москвы&Крымская набережная&Крымская набережная&Музей физической культуры и спорта России&Музей космонавтики&Московский музей естественной истории&Московский зоопарк&Музей Москвы&Коломенское&Московский музей декоративно-прикладного искусства&Крымская набережная', 3, 7914, 'Экскурсия по Москве 780'),
(96, 'Московский государственный академический театр детей и молодежи на Таганке&Парк культуры и отдыха имени Горького&Крымская набережная&Московский зоопарк&Парк Патриот&Центральный дом художника&Музей военной техники', 9, 3684, 'Экскурсия по Москве 165'),
(97, 'Музей-квартира А.М. Васнецова&Московский музей ретроавтомобилей&Государственный музей изобразительных искусств имени А.С. Пушкина&Московская детская художественная галерея&Государственный музей изобразительных искусств имени А.С. Пушкина&Музей космонавтики', 4, 2743, 'Экскурсия по Москве 485'),
(98, 'Московский музей истории московского футбола&Музей Востока&Музей кукол&Московский музей архитектуры&Третьяковская галерея&Московский областной музей изобразительных искусств имени И.Н. Крамского&Музей изобразительных искусств имени Пушкина&Музей физической культуры и спорта России', 3, 4036, 'Экскурсия по Москве 929'),
(99, 'Музей хоккея&Храм Христа Спасителя&Музей Победы&Московский планетарий&Новодевичий монастырь&Музей Востока&Московский зоопарк&Московский Кремль', 3, 5053, 'Экскурсия по Москве 191');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `role` enum('tourist','guide') NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `middlename` varchar(100) DEFAULT NULL,
  `login` varchar(100) NOT NULL,
  `password_hash` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `role`, `firstname`, `lastname`, `middlename`, `login`, `password_hash`) VALUES
(1, 'tourist', 'user1_firstname', 'user1_lastname', 'user1_middlename', 'user1', '0a041b9462caa4a31bac3567e0b6e6fd9100787db2ab433d96f6d178cabfce90'),
(2, 'guide', 'user2_firstname', 'user2_lastname', 'user2_middlename', 'user2', '6025d18fe48abd45168528f18a82e265dd98d421a7084aa09f61b341703901a3'),
(3, 'guide', 'user3_firstname', 'user3_lastname', 'user3_middlename', 'user3', '5860faf02b6bc6222ba5aca523560f0e364ccd8b67bee486fe8bf7c01d492ccb'),
(4, 'guide', 'user4_firstname', 'user4_lastname', 'user4_middlename', 'user4', '5269ef980de47819ba3d14340f4665262c41e933dc92c1a27dd5d01b047ac80e'),
(5, 'tourist', 'user5_firstname', 'user5_lastname', 'user5_middlename', 'user5', '5a39bead318f306939acb1d016647be2e38c6501c58367fdb3e9f52542aa2442'),
(6, 'guide', 'user6_firstname', 'user6_lastname', 'user6_middlename', 'user6', 'ecb48a1cc94f951252ec462fe9ecc55c3ef123fadfe935661396c26a45a5809d'),
(7, 'guide', 'user7_firstname', 'user7_lastname', 'user7_middlename', 'user7', '3268151e52d97b4cacf97f5b46a5c76c8416e928e137e3b3dc447696a29afbaa'),
(8, 'guide', 'user8_firstname', 'user8_lastname', 'user8_middlename', 'user8', 'f60afa4989a7db13314a2ab9881372634b5402c30ba7257448b13fa388de1b78'),
(9, 'guide', 'user9_firstname', 'user9_lastname', 'user9_middlename', 'user9', '0fb8d3c5dfaf81a387bf0ba439ab40e6343d2155fb4ddf6978a52d9b9ea8d0f8'),
(10, 'guide', 'user10_firstname', 'user10_lastname', 'user10_middlename', 'user10', '5bbf1a9e0de062225a1bb7df8d8b3719591527b74950810f16b1a6bc6d7bd29b'),
(11, 'guide', 'user11_firstname', 'user11_lastname', 'user11_middlename', 'user11', '81115e31e22a5801b197750ec12d7a51ad693aa017ecc8bca033cbd500a928b6'),
(12, 'tourist', 'user12_firstname', 'user12_lastname', 'user12_middlename', 'user12', 'bd35283fe8fcfd77d7c05a8bf2adb85c773281927e12c9829c72a9462092f7c4'),
(13, 'guide', 'user13_firstname', 'user13_lastname', 'user13_middlename', 'user13', '1834e148b518a43a37e04a4e4fbcee1eb845de6ee5a3f04fe9fb749f9695be42'),
(14, 'tourist', 'user14_firstname', 'user14_lastname', 'user14_middlename', 'user14', 'daf7996f88742675acb3d0f85a8069d02fdf1c4dc2026de7f01a0ba7e65922fb'),
(15, 'guide', 'user15_firstname', 'user15_lastname', 'user15_middlename', 'user15', '2b8b66f64b605318593982b059a08dae101c0bdf5d8cb882a0891241a704f46c'),
(16, 'guide', 'user16_firstname', 'user16_lastname', 'user16_middlename', 'user16', '4de4153595c0977d2389d0880547bd3aa60871e906ce52a26648d8ca0a157e5c'),
(17, 'guide', 'user17_firstname', 'user17_lastname', 'user17_middlename', 'user17', '2a60ff641c890283b1d070f827cf9c0cce004769c2a2dc7136bc6d290477275c'),
(18, 'tourist', 'user18_firstname', 'user18_lastname', 'user18_middlename', 'user18', 'ebc835d1b43e63d1ba35af810da3a23e4f8a04cf680f1718c2fefb1ee77fcecf'),
(19, 'tourist', 'user19_firstname', 'user19_lastname', 'user19_middlename', 'user19', '0b6ecb3aa9b23589fb9e314b46c832d977e597228c1e358fcc564bd8ba733195'),
(20, 'guide', 'user20_firstname', 'user20_lastname', 'user20_middlename', 'user20', '7febe54e79096749ac43dc6c2e3e5d4dc768993d1f3102889257c9cab7934ec7'),
(24, 'tourist', 'user21_firstname', 'user21_lastname', 'user21_middlename', 'user21', '8fab3a60577befd765cde83f2737cd1a9f25a72356c94052c2194e816829b331'),
(25, 'tourist', 'user22_firstname', 'user22_lastname', 'user22_middlename', 'user22', 'b999205cdacd2c4516598d99b420d29786443e9908556a65f583a6fd4765ee4a'),
(26, 'tourist', 'user23_firstname', 'user23_lastname', 'user23_middlename', 'user23', '2a0fff6e36fbc6a21f7b065f24a3ffb40de209ea8cfc15d76cf786f74dd6f115'),
(27, 'tourist', 'user24_firstname', 'user24_lastname', 'user24_middlename', 'user24', '65303a0ec5984ab62d102031a5c9be89ca21812816af34a8e13c8104be240ab2'),
(28, 'tourist', 'user25_firstname', 'user25_lastname', 'user25_middlename', 'user25', 'dab53605c85e2eff2f2192e08b772cbc06af317d217d09e161215901339300e0');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `route_id` (`route_id`);

--
-- Индексы таблицы `routes`
--
ALTER TABLE `routes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `guide_id` (`guide_id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login` (`login`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT для таблицы `routes`
--
ALTER TABLE `routes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`route_id`) REFERENCES `routes` (`id`);

--
-- Ограничения внешнего ключа таблицы `routes`
--
ALTER TABLE `routes`
  ADD CONSTRAINT `routes_ibfk_1` FOREIGN KEY (`guide_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
