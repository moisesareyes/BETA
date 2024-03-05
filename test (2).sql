-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-03-2024 a las 13:42:09
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
(1, 'ZRO-42111', 'Bs.D', 7661.4, 'ZRO-42111-BSD', '2024-02-26 13:21:19'),
(2, 'ZRO-42111', 'USD', 385, 'ZRO-42111-USD', '2024-02-26 13:15:58'),
(4, 'EZr-24018', 'Bs.D', 400, 'EZr-24018-BSD', '2024-02-23 09:29:22'),
(5, 'EZr-24018', 'USD', 30, 'EZr-24018-USD', '2024-02-23 09:30:05'),
(7, 'Eai-47325', 'Bs.D', 1100, 'Eai-47325-BSD', '2024-02-23 09:29:22'),
(8, 'Eai-47325', 'USD', 10, 'Eai-47325-USD', '2024-02-23 09:30:05'),
(9, 'To2-47789', 'Bs.D', 0, 'To2-47789-BSD', '2024-02-23 09:40:04'),
(10, 'To2-47789', 'USD', 0, 'To2-47789-USD', '2024-02-23 09:40:04'),
(11, 'RMN-11111', 'Bs.D', 0, 'RMN-11111-BSD', '2024-02-23 09:43:24'),
(12, 'RMN-11111', 'USD', 0, 'RMN-11111-USD', '2024-02-23 09:43:24'),
(13, 'Sny-25874', 'Bs.D', 0, 'Sny-25874-BSD', '2024-02-23 09:44:24'),
(14, 'Sny-25874', 'USD', 0, 'Sny-25874-USD', '2024-02-23 09:44:24'),
(15, 'RIN-11111', 'Bs.D', 10000, 'RIN-11111-BSD', '2024-02-26 13:21:19'),
(16, 'RIN-11111', 'USD', 0, 'RIN-11111-USD', '2024-02-23 09:47:35');

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

--
-- Volcado de datos para la tabla `historial`
--

INSERT INTO `historial` (`ID`, `servidor`, `recep`, `tipo`, `moneda`, `status`, `cantidad`, `billetera1`, `billetera2`, `fecha`) VALUES
(2, 'ZRO-42111', 'Servidor', 'Recarga', 'Bs.D', 'Pendiente', '1000000', '', '', '2024-02-26 16:48:49'),
(3, 'ZRO-42111', 'ZRO-42111', 'converse', 'USD to Bs.D', 'confirmado', '31088.7', 'ZRO-42111-BSD', 'ZRO-42111-USD', '2024-02-26 17:00:13'),
(4, 'ZRO-42111', 'ZRO-42111', 'converse', 'USD to Bs.D', 'confirmado', '31451.600000000002', 'ZRO-42111-BSD', 'ZRO-42111-USD', '2024-02-26 17:00:50'),
(5, 'ZRO-42111', 'ZRO-42111', 'converse', 'Bs.D to USD', 'confirmado', '505.0', 'ZRO-42111-USD', 'ZRO-42111-BSD', '2024-02-26 17:01:21'),
(6, 'ZRO-42111', 'ZRO-42111', 'converse', 'USD to Bs.D', 'confirmado', '14032.4', 'ZRO-42111-BSD', 'ZRO-42111-USD', '2024-02-26 17:13:59'),
(7, 'ZRO-42111', 'ZRO-42111', 'converse', 'USD to Bs.D', 'confirmado', '3629.0', 'ZRO-42111-BSD', 'ZRO-42111-USD', '2024-02-26 17:15:58'),
(8, 'ZRO-42111', 'RIN-11111', 'transferencia', 'Bs.D', 'confirmado', '10000', 'RIN-11111-BSD', 'ZRO-42111-BSD', '2024-02-26 17:21:19');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recarga`
--

CREATE TABLE `recarga` (
  `ID` int(11) NOT NULL,
  `usuario` text NOT NULL,
  `tipo` text NOT NULL,
  `doc` text NOT NULL,
  `formato` text NOT NULL,
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

INSERT INTO `recarga` (`ID`, `usuario`, `tipo`, `doc`, `formato`, `telefono`, `cantidad`, `operacion`, `status`, `fecha_tra`, `reg`) VALUES
(1, 'EZr-24018', 'Bs.D', '300', '0', '300', '2000', '20000000', 'Pendiente', '2024-02-14', '2024-02-14 14:14:19'),
(2, 'ZRO-42111', 'Bs.D', '30', 'PAGO MOVIL', '30', '', '30', 'Pendiente', '2024-02-22', '2024-02-21 16:35:26'),
(3, 'ZRO-42111', 'Bs.D', '30', 'PAGO MOVIL', '30', '30', '30', 'Pendiente', '2024-02-21', '2024-02-21 16:44:11'),
(4, 'ZRO-42111', 'Bs.D', '302', 'PAGO MOVIL', '30', '302', '30', 'Pendiente', '2024-02-21', '2024-02-21 16:44:25'),
(5, 'ZRO-42111', 'USD', '111', 'PAYPAL', '', '200', '112', 'Pendiente', '2024-02-21', '2024-02-21 17:22:42'),
(6, 'ZRO-42111', 'Bs.D', '555', 'PAGO MOVIL', '55555', '010110', '55585', 'Pendiente', '2024-02-22', '2024-02-21 17:25:13'),
(7, 'ZRO-42111', 'Bs.D', '20000', 'PAGO MOVIL', '0424244', '100', '50101011', 'Pendiente', '2024-02-27', '2024-02-26 16:47:13'),
(8, 'ZRO-42111', 'Bs.D', '1000', 'PAGO MOVIL', '100000', '1000000', '1000000', 'Pendiente', '2024-02-27', '2024-02-26 16:48:49');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `retiros`
--

CREATE TABLE `retiros` (
  `id` int(11) NOT NULL,
  `usuario` text NOT NULL,
  `banco` text NOT NULL,
  `documento` text NOT NULL,
  `cantidad` text NOT NULL,
  `tlf` text NOT NULL,
  `status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `retiros`
--

INSERT INTO `retiros` (`id`, `usuario`, `banco`, `documento`, `cantidad`, `tlf`, `status`) VALUES
(1, 'ZRO-42111', '0104 Venezolano de Crédito', '5500', '500', '755', 'pendiente'),
(2, 'ZRO-42111', '0102 Banco de Venezuela, S.A.C.A.', '300', '25255252', '5255', 'pendiente'),
(3, 'ZRO-42111', '0102 Banco de Venezuela, S.A.C.A.', '5000', '5005', '0555', 'pendiente');

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
(9, 'EZr-24018', 'Alejandro', 'De la Torre', 'ElZorro', 'elzrro@gm.com', 'zoRRo25555', '042417018', '2024-02-01 11:14:27'),
(10, 'ZRO-42111', 'Diego', 'De la vega', 'Diego de la Vega', 'diaaaa@', 'zoRRo25555', '024211111', '2024-02-01 11:16:14'),
(11, 'Eai-47325', 'Eladio', 'Carrion', 'Eladio123', 'ela123@gm', 'Ela123456', '0147896325', '2024-02-15 14:22:12'),
(12, 'Buo-34901', 'Bruno ', 'Mars', 'Bruno12', 'mars@124', 'A1234567a', '12345678901', '2024-02-15 14:35:12'),
(13, 'mla-24614', 'Melvis', 'Soto', 'melrafa84', 'melrafa84@gmail.com', 'Dana2022', '04242770614', '2024-02-15 14:51:58'),
(14, 'To2-47789', 'Teo', 'Eo', 'Teo123', 'teo@gm.', 'TEO123teo', '0147814789', '2024-02-23 09:40:04'),
(15, 'RMN-11111', 'Roman', 'Reigns', 'ROMAN1', 'Reings@233.com', 'Roman2231', '1111111111', '2024-02-23 09:43:24'),
(16, 'Sny-25874', 'Sunny', 'Adams', 'Sunny', 'sunny@.com', 'Sunny111', '1425369874', '2024-02-23 09:44:23'),
(17, 'RIN-11111', 'Roman', 'Reigns', 'REIGNS11', 'reigns@gm.com', 'REigns223', '1111111111111', '2024-02-23 09:47:35');

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
-- Indices de la tabla `retiros`
--
ALTER TABLE `retiros`
  ADD PRIMARY KEY (`id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `historial`
--
ALTER TABLE `historial`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `recarga`
--
ALTER TABLE `recarga`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `retiros`
--
ALTER TABLE `retiros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
