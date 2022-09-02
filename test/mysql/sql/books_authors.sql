USE books_authors;
--
-- Base de datos: `books_authors`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `authors`
--

CREATE TABLE `authors` (
  `AuthorID` int(11) NOT NULL,
  `AuthorName` varchar(255) NOT NULL,
  `AuthorCity` varchar(255) NOT NULL,
  `Genre` varchar(255) NOT NULL,
  `BookTitle` varchar(255) NOT NULL,
  `ReleaseYear` int(11) NOT NULL,
  `NumberOfPages` int(11) NOT NULL,
  `PiecesSold` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `authors`
--

INSERT INTO `authors` (`AuthorID`, `AuthorName`, `AuthorCity`, `Genre`, `BookTitle`, `ReleaseYear`, `NumberOfPages`, `PiecesSold`) VALUES
(1, 'Miguel De Cervantes', 'Madrid', 'Ficción', 'Don Quijote', 1950, 225, 1000),
(2, 'Marqués De Sade', 'Nueva York', 'Ficción', 'Justine de Sade', 1960, 200, 5000),
(3, 'Albert Camus', 'París', 'Terror', 'Mamá se ha muerto hoy. O puede que ayer, no lo sé', 1970, 150, 7000),
(4, 'Carlos Fuentes', 'Ciudad de México', 'Detective', 'El naranjo', 1980, 170, 1050),
(5, 'Isaiah Berlin', 'Berlín', 'Psicología', 'Sobre la libertad y la igualdad', 1990, 180, 1200),
(6, 'Federico García Lorca', 'Madrid', 'Romance', 'Romancero Gitano', 2000, 250, 1800),
(7, 'Octavio Paz', 'Ciudad de México', 'Detective', 'El laberinto de la Soledad', 2005, 300, 1540),
(8, 'Frank Sinatra', 'Nueva York', 'Psicología', 'En busca del tiempo perdido', 2015, 180, 1070),
(9, 'Virgilio', 'Moscú', 'Terror', 'La Eneida', 2020, 225, 5800),
(10, 'William Shakespeare', 'Berlín', 'Ficción', 'Hamlet', 2022, 225, 7580);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `authors`
--
ALTER TABLE `authors`
  ADD PRIMARY KEY (`AuthorID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `authors`
--
ALTER TABLE `authors`
  MODIFY `AuthorID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;
