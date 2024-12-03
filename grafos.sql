-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 30-11-2024 a las 08:02:17
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `grafos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Conexion`
--

CREATE TABLE `Conexion` (
  `id_Conexion` int(11) NOT NULL,
  `origen_id` int(11) NOT NULL,
  `destino_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `Conexion`
--

INSERT INTO `Conexion` (`id_Conexion`, `origen_id`, `destino_id`) VALUES
(1, 0, 1),
(2, 0, 2),
(3, 0, 3),
(4, 0, 4),
(5, 0, 5),
(6, 0, 6),
(7, 0, 8),
(8, 0, 9),
(9, 0, 10),
(10, 1, 0),
(11, 1, 2),
(12, 1, 7),
(13, 1, 8),
(14, 1, 9),
(15, 1, 10),
(16, 1, 12),
(17, 2, 0),
(18, 2, 1),
(19, 2, 8),
(20, 2, 9),
(21, 2, 10),
(22, 2, 11),
(23, 2, 12),
(24, 2, 13),
(25, 2, 14),
(26, 3, 0),
(27, 4, 0),
(28, 5, 0),
(29, 6, 0),
(30, 7, 1),
(31, 7, 10),
(32, 8, 0),
(33, 8, 1),
(34, 8, 2),
(35, 8, 10),
(36, 9, 0),
(37, 9, 1),
(38, 9, 2),
(39, 10, 0),
(40, 10, 1),
(41, 10, 2),
(42, 10, 7),
(43, 10, 8),
(44, 11, 2),
(45, 12, 2),
(46, 13, 2),
(47, 14, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Nodo`
--

CREATE TABLE `Nodo` (
  `id_nodo` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `Nodo`
--

INSERT INTO `Nodo` (`id_nodo`, `nombre`) VALUES
(0, 'Manizales'),
(1, 'Pereira'),
(2, 'Armenia'),
(3, 'Chinchina'),
(4, 'Villamaria'),
(5, 'Palestina'),
(6, 'Neira'),
(7, 'La Virginia'),
(8, 'Dosquebradas'),
(9, 'Santa Rosa de Cabal'),
(10, 'Cartago'),
(11, 'Calarca'),
(12, 'Ciscasia'),
(13, 'La Tebaida'),
(14, 'Montenegro');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Conexion`
--
ALTER TABLE `Conexion`
  ADD PRIMARY KEY (`id_Conexion`),
  ADD KEY `origen_id` (`origen_id`),
  ADD KEY `destino_id` (`destino_id`);

--
-- Indices de la tabla `Nodo`
--
ALTER TABLE `Nodo`
  ADD PRIMARY KEY (`id_nodo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Conexion`
--
ALTER TABLE `Conexion`
  MODIFY `id_Conexion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Conexion`
--
ALTER TABLE `Conexion`
  ADD CONSTRAINT `Conexion_ibfk_1` FOREIGN KEY (`origen_id`) REFERENCES `Nodo` (`id_nodo`),
  ADD CONSTRAINT `Conexion_ibfk_2` FOREIGN KEY (`destino_id`) REFERENCES `Nodo` (`id_nodo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
