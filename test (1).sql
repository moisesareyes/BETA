-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-03-2024 a las 14:16:57
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
(2, 'ZRO-42111', 'USD', 235, 'ZRO-42111-USD', '2024-03-04 09:34:57'),
(4, 'EZr-24018', 'Bs.D', 400, 'EZr-24018-BSD', '2024-02-23 09:29:22'),
(5, 'EZr-24018', 'USD', 30, 'EZr-24018-USD', '2024-02-23 09:30:05'),
(7, 'Eai-47325', 'Bs.D', 1100, 'Eai-47325-BSD', '2024-03-12 12:47:14'),
(8, 'Eai-47325', 'USD', 10, 'Eai-47325-USD', '2024-02-23 09:30:05'),
(9, 'To2-47789', 'Bs.D', 0, 'To2-47789-BSD', '2024-02-23 09:40:04'),
(10, 'To2-47789', 'USD', 0, 'To2-47789-USD', '2024-02-23 09:40:04'),
(11, 'RMN-11111', 'Bs.D', 150, 'RMN-11111-BSD', '2024-03-12 12:44:25'),
(12, 'RMN-11111', 'USD', 0, 'RMN-11111-USD', '2024-02-23 09:43:24'),
(13, 'Sny-25874', 'Bs.D', 650, 'Sny-25874-BSD', '2024-03-13 13:17:45'),
(14, 'Sny-25874', 'USD', 498, 'Sny-25874-USD', '2024-03-13 13:17:45'),
(15, 'RIN-11111', 'Bs.D', 756.05, 'RIN-11111-BSD', '2024-03-11 13:34:18'),
(16, 'RIN-11111', 'USD', 405, 'RIN-11111-USD', '2024-03-06 13:09:00'),
(17, 'PEE-35141', 'Bs.D', 0, 'PEE-35141-BSD', '2024-03-08 09:00:52'),
(18, 'PEE-35141', 'USD', 0, 'PEE-35141-USD', '2024-03-08 09:00:52'),
(19, 'Iai-47896', 'Bs.D', 0, 'Iai-47896-BSD', '2024-03-15 13:26:46'),
(20, 'Iai-47896', 'USD', 0, 'Iai-47896-USD', '2024-03-15 13:26:46');

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
(3, 'ZRO-42111', 'ZRO-42111', 'converse', 'USD to Bs.D', 'confirmado', '31088.7', 'ZRO-42111-BSD', 'ZRO-42111-USD', '2024-02-26 17:00:13'),
(4, 'ZRO-42111', 'ZRO-42111', 'converse', 'USD to Bs.D', 'confirmado', '31451.600000000002', 'ZRO-42111-BSD', 'ZRO-42111-USD', '2024-02-26 17:00:50'),
(5, 'ZRO-42111', 'ZRO-42111', 'converse', 'Bs.D to USD', 'confirmado', '505.0', 'ZRO-42111-USD', 'ZRO-42111-BSD', '2024-02-26 17:01:21'),
(6, 'ZRO-42111', 'ZRO-42111', 'converse', 'USD to Bs.D', 'confirmado', '14032.4', 'ZRO-42111-BSD', 'ZRO-42111-USD', '2024-02-26 17:13:59'),
(7, 'ZRO-42111', 'ZRO-42111', 'converse', 'USD to Bs.D', 'confirmado', '3629.0', 'ZRO-42111-BSD', 'ZRO-42111-USD', '2024-02-26 17:15:58'),
(8, 'ZRO-42111', 'RIN-11111', 'transferencia', 'Bs.D', 'confirmado', '10000', 'RIN-11111-BSD', 'ZRO-42111-BSD', '2024-02-26 17:21:19'),
(9, 'ZRO-42111', 'RIN-11111', 'transferencia', 'USD', 'confirmado', '150', 'RIN-11111-USD', 'ZRO-42111-USD', '2024-03-04 13:34:57'),
(10, 'RIN-11111', 'RIN-11111', 'converse', 'Bs.D to USD', 'confirmado', '3629.0', 'RIN-11111-USD', 'RIN-11111-BSD', '2024-03-06 13:17:34'),
(11, 'RIN-11111', 'RIN-11111', 'converse', 'Bs.D to USD', 'confirmado', '1814.5', 'RIN-11111-USD', 'RIN-11111-BSD', '2024-03-06 13:30:14'),
(12, 'RIN-11111', 'RIN-11111', 'converse', 'Bs.D to USD', 'confirmado', '725.8', 'RIN-11111-USD', 'RIN-11111-BSD', '2024-03-06 13:33:25'),
(13, 'RIN-11111', 'RIN-11111', 'converse', 'Bs.D to USD', 'confirmado', '544.35', 'RIN-11111-USD', 'RIN-11111-BSD', '2024-03-06 14:00:33'),
(14, 'RIN-11111', 'RIN-11111', 'converse', 'Bs.D to USD', 'confirmado', '1814.5', 'RIN-11111-USD', 'RIN-11111-BSD', '2024-03-06 16:59:03'),
(15, 'RIN-11111', 'RIN-11111', 'converse', 'Bs.D to USD', 'confirmado', '725.8', 'RIN-11111-USD', 'RIN-11111-BSD', '2024-03-06 17:09:00'),
(16, 'Sny-25874', 'RIN-11111', 'transferencia', 'Bs.D', 'confirmado', '10', 'RIN-11111-BSD', 'Sny-25874-BSD', '2024-03-11 17:34:18'),
(17, 'Sny-25874', 'Sny-25874', 'converse', 'USD to Bs.D', 'confirmado', '362.9', 'Sny-25874-BSD', 'Sny-25874-USD', '2024-03-11 17:34:42'),
(18, 'Sny-25874', 'Sny-25874', 'converse', 'USD to Bs.D', 'confirmado', '362.9', 'Sny-25874-BSD', 'Sny-25874-USD', '2024-03-11 17:35:10'),
(19, 'Sny-25874', 'RMN-11111', 'transferencia', 'Bs.D', 'confirmado', '150', 'RMN-11111-BSD', 'Sny-25874-BSD', '2024-03-12 16:44:25'),
(20, 'Sny-25874', 'Eai-47325', 'transferencia', 'Bs.D', 'confirmado', '500', 'Eai-47325-BSD', 'Sny-25874-BSD', '2024-03-12 16:45:02'),
(21, 'Eai-47325', 'Sny-25874', 'transferencia', 'Bs.D', 'confirmado', '500', 'Sny-25874-BSD', 'Eai-47325-BSD', '2024-03-12 16:47:14'),
(22, 'Sny-25874', 'Servidor', 'Recarga', 'Bs.D', 'Pendiente', '111', '', '', '2024-03-13 17:17:12'),
(23, 'Sny-25874', 'Sny-25874', 'converse', 'Bs.D to USD', 'confirmado', '362.9', 'Sny-25874-USD', 'Sny-25874-BSD', '2024-03-13 17:17:45'),
(24, 'Sny-25874', 'Servidor', 'Recarga', 'Bs.D', 'Pendiente', '100', '', '', '2024-03-13 17:27:22'),
(25, 'Sny-25874', 'Servidor', 'Recarga', 'Bs.D', 'Pendiente', '5555555', '', '', '2024-03-13 17:30:13'),
(26, 'Sny-25874', 'Paypal', 'Retiro', 'usd', 'Pendiente', '520', '', '', '2024-03-14 13:16:50'),
(27, 'Sny-25874', 'Servidor', 'Recarga', 'Bs.D', 'Pendiente', '1111111', '', '', '2024-03-14 16:02:38');

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
(3, 'ZRO-42111', 'Bs.D', '30', 'PAGO MOVIL', '30', '30', '30', 'Pendiente', '2024-02-21', '2024-03-17 07:11:26'),
(7, 'ZRO-42111', 'Bs.D', '20000', 'PAGO MOVIL', '0424244', '100', '50101011', 'Pendiente', '2024-02-27', '2024-03-17 07:16:00'),
(11, 'Sny-25874', 'Bs.D', '55555', 'PAGO MOVIL', '55555555', '5555555', '5555555555', 'Pendiente', '2024-03-13', '2024-03-17 07:11:20');

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
(3, 'ZRO-42111', '0102 Banco de Venezuela, S.A.C.A.', '5000', '5005', '0555', 'pendiente'),
(4, 'Sny-25874', 'Paypal', '', '122', 'tta10@gm.com', 'pendiente'),
(5, 'Sny-25874', 'Paypal', '', '520', 'elm@gm.com', 'pendiente');

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
(10, 'ZRO-42111', 'Diego', 'De la vega', 'Dzroo', 'diaaaa@', 'zoRRo25555', '024211111', '2024-02-01 11:16:14'),
(11, 'Eai-47325', 'Eladio', 'Carrion', 'Eladio123', 'ela123@gm', 'Ela123456', '0147896325', '2024-02-15 14:22:12'),
(14, 'To2-47789', 'Teo', 'Eo', 'Teo123', 'teo@gm.', 'TEO123teo', '0147814789', '2024-02-23 09:40:04'),
(15, 'RMN-11111', 'Roman', 'Reigns', 'ROMAN1', 'Reings@233.com', 'Roman2231', '1111111111', '2024-02-23 09:43:24'),
(16, 'Sny-25874', 'Sunny', 'Adams', 'Sunny', 'sunny@.com', 'Sunny111', '1425369874', '2024-02-23 09:44:23'),
(17, 'RIN-11111', 'Roman', 'Reigns', 'REIGNS11', 'reigns@gm.com', 'REigns223', '1111111111111', '2024-02-23 09:47:35'),
(18, 'PEE-35141', 'PREDETERMINADO', 'PREDETERMINADO', 'PREDETERMINADO', 'PREDETERMINADO', 'Predeterminado1', '7535731414141', '2024-03-08 09:00:52'),
(19, 'Iai-47896', 'imayin', 'one', 'Imayin', 'imayin@gm.com', 'Imayin1223', '0147111896', '2024-03-15 13:26:46');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `web`
--

CREATE TABLE `web` (
  `cargo` text NOT NULL,
  `user` varchar(50) NOT NULL,
  `pass` varchar(255) NOT NULL,
  `nom` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `web`
--

INSERT INTO `web` (`cargo`, `user`, `pass`, `nom`) VALUES
('CEO', 'itsArtu', '$2y$10$.DRgYv/0hknwnKtLuq4AreMgvnyfAgy/LVegbqhlzZPRZgnv8j93S', 'Arturo Pérez'),
('CEO', 'Imagine', '$2y$10$V4i2Zl/NCaNorerF3NRQXuJu2h5vX37qrqVgD4KhI5uhXBCcYbAFe', 'Moisés Reyes');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `historial`
--
ALTER TABLE `historial`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `recarga`
--
ALTER TABLE `recarga`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `retiros`
--
ALTER TABLE `retiros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
