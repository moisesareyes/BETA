-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-02-2024 a las 15:15:05
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `test`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `billetera`
--

CREATE TABLE `billetera` (
  `id` int(11) NOT NULL,
  `poseedor` text NOT NULL,
  `tipo` text NOT NULL,
  `cantidad` float NOT NULL,
  `billeteraID` text NOT NULL,
  `act` text NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `billetera`
--

INSERT INTO `billetera` (`id`, `poseedor`, `tipo`, `cantidad`, `billeteraID`, `act`) VALUES
(1, 'ZRO-42111', 'Bs.D', 95.65, 'ZRO-42111-BSD', '2024-02-09 17:22:25'),
(2, 'ZRO-42111', 'USD', 55, 'ZRO-42111-USD', '2024-02-09 17:22:25'),
(3, 'ZRO-42111', 'CRYPTO', 1.11199, 'ZRO-42111-CRYPTO', '2024-02-07 14:10:11'),
(4, 'EZr-24018', 'Bs.D', 0, 'EZr-24018-BSD', '2024-02-14 13:03:25'),
(5, 'EZr-24018', 'USD', 0, 'EZr-24018-USD', '2024-02-14 13:04:01'),
(6, 'EZr-24018', 'CRYPTO', 0, 'EZr-24018-CRYPTO', '2024-02-14 13:04:07');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial`
--

CREATE TABLE `historial` (
  `ID` int(11) NOT NULL,
  `servidor` text NOT NULL,
  `recep` text NOT NULL,
  `tipo` text NOT NULL,
  `moneda` text NOT NULL,
  `status` text NOT NULL,
  `cantidad` text NOT NULL,
  `billetera1` text NOT NULL,
  `billetera2` text NOT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recarga`
--

CREATE TABLE `recarga` (
  `ID` int(11) NOT NULL,
  `usuario` text NOT NULL,
  `tipo` text NOT NULL,
  `doc` text NOT NULL,
  `banco` text NOT NULL,
  `telefono` text NOT NULL,
  `cantidad` text NOT NULL,
  `operacion` text NOT NULL,
  `status` text NOT NULL,
  `fecha_tra` date NOT NULL,
  `reg` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `recarga`
--

INSERT INTO `recarga` (`ID`, `usuario`, `tipo`, `doc`, `banco`, `telefono`, `cantidad`, `operacion`, `status`, `fecha_tra`, `reg`) VALUES
(1, 'EZr-24018', 'Bs.D', '300', '0102', '300', '2000', '20000000', 'Pendiente', '2024-02-14', '2024-02-14 14:14:19');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `test`
--

CREATE TABLE `test` (
  `user` text NOT NULL,
  `pass` text NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `test`
--

INSERT INTO `test` (`user`, `pass`, `id`) VALUES
('admin', '1234', 1),
('admin', '1234', 2),
('admin', '1234', 3),
('admin', 'sql', 4),
('admin', 'sql', 5),
('admin', 'sql', 6),
('admin', 'sql', 7),
('try', 'test', 8),
('Prueba', 'test', 11),
('funciona', 'si', 12);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `ID` int(11) NOT NULL,
  `UserID` text NOT NULL,
  `Nombre` text NOT NULL,
  `Apellido` text NOT NULL,
  `User_name` text NOT NULL,
  `Email` text NOT NULL,
  `Pass` text NOT NULL,
  `Tlf` text NOT NULL,
  `Reg` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`ID`, `UserID`, `Nombre`, `Apellido`, `User_name`, `Email`, `Pass`, `Tlf`, `Reg`) VALUES
(1, 'Ede002', 'a', 'a', 'a', 'a', 'a', 'a', '2024-01-31 09:24:49'),
(2, 'EDE-2', 'Juan Roman', 'Riquelme', 'JRM10', 'jrm1@gm.com', 'password', '0424', '2024-01-31 09:59:21'),
(3, '', 'Juan Roman', 'Riquelme', 'JRM', 'jrm2@gm.com', 'password', '0424', '2024-01-31 09:59:41'),
(4, '', 'Juan Roman', 'Riquelme', 'b', 'jrm3@gm.com', 'password', '0424', '2024-01-31 10:00:00'),
(5, '', 'b', 'b', 'try', 'try', 'try', 'try', '2024-01-31 10:36:33'),
(6, 'EDE-1', 'Moises', 'Reyes', 'MReyes', 'moises@gmail.com', '223', '0424-1', '2024-01-31 13:29:20'),
(7, '', 'Trent', 'Alexander Arnold', 'TAA10L', 'taa@gm.com', 'trentalexander', '04241', '2024-01-31 13:45:56'),
(8, 'EDE-002', 'A', 'A', 'AMultiplicado', 'Am@gmail.com', 'Guns1110', '0421', '2024-01-31 15:22:23'),
(9, 'EZr-24018', 'Alejandro', 'De la Torre', 'ElZorro', 'elzrro@gm.com', 'zoRRo25555', '042417018', '2024-02-01 11:14:27'),
(10, 'ZRO-42111', 'Diego', 'De la vega', 'Zorro25', 'diaaaa@', 'zoRRo25555', '024211111', '2024-02-01 11:16:14');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `billetera`
--
ALTER TABLE `billetera`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `historial`
--
ALTER TABLE `historial`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `recarga`
--
ALTER TABLE `recarga`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `billetera`
--
ALTER TABLE `billetera`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `historial`
--
ALTER TABLE `historial`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `recarga`
--
ALTER TABLE `recarga`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
