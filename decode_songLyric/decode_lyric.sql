-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Ott 31, 2017 alle 10:51
-- Versione del server: 10.1.28-MariaDB
-- Versione PHP: 7.1.10

-- SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
-- SET AUTOCOMMIT = 0;
-- START TRANSACTION;
-- SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `decode_lyric`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `autore`
--

CREATE TABLE `autore` (
  `nome` varchar(128) COLLATE utf8_bin NOT NULL,
  `cognome` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `anno` year(4) NOT NULL,
  `id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Struttura della tabella `composizione`
--

CREATE TABLE `composizione` (
  `id_testo` int(10) UNSIGNED NOT NULL,
  `id_parola` bigint(20) UNSIGNED NOT NULL,
  `frequenza` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Struttura della tabella `parola`
--

CREATE TABLE `parola` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `word` varchar(256) COLLATE utf8_bin NOT NULL,
  `lingua` varchar(128) COLLATE utf8_bin NOT NULL,
  `len` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Struttura della tabella `raccolta`
--

CREATE TABLE `raccolta` (
  `id` int(10) UNSIGNED NOT NULL,
  `nome` varchar(256) COLLATE utf8_bin NOT NULL,
  `tipo` varchar(256) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dump dei dati per la tabella `raccolta`
--

INSERT INTO `raccolta` (`id`, `nome`, `tipo`) VALUES
(1, 'singolo', 'album');

-- --------------------------------------------------------

--
-- Struttura della tabella `testo`
--

CREATE TABLE `testo` (
  `id` int(10) UNSIGNED NOT NULL,
  `lyrics` longtext COLLATE utf8_bin,
  `anno` year(4) NOT NULL,
  `id_raccolta` int(10) UNSIGNED NOT NULL,
  `id_autore` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `autore`
--
ALTER TABLE `autore`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `composizione`
--
ALTER TABLE `composizione`
  ADD PRIMARY KEY (`id_testo`,`id_parola`),
  ADD KEY `vincolo_id_parola` (`id_parola`),
  ADD KEY `vincolo_id_testo` (`id_testo`);

--
-- Indici per le tabelle `parola`
--
ALTER TABLE `parola`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `raccolta`
--
ALTER TABLE `raccolta`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `testo`
--
ALTER TABLE `testo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vincolo_id_autore` (`id_autore`),
  ADD KEY `vincolo_id_raccolta` (`id_raccolta`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `autore`
--
ALTER TABLE `autore`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `parola`
--
ALTER TABLE `parola`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `raccolta`
--
ALTER TABLE `raccolta`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT per la tabella `testo`
--
ALTER TABLE `testo`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `composizione`
--
ALTER TABLE `composizione`
  ADD CONSTRAINT `vincolo_id_parola` FOREIGN KEY (`id_parola`) REFERENCES `parola` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `vincolo_id_testo` FOREIGN KEY (`id_testo`) REFERENCES `testo` (`id`) ON UPDATE CASCADE;

--
-- Limiti per la tabella `testo`
--
ALTER TABLE `testo`
  ADD CONSTRAINT `vincolo_id_autore` FOREIGN KEY (`id_autore`) REFERENCES `autore` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `vincolo_id_raccolta` FOREIGN KEY (`id_raccolta`) REFERENCES `raccolta` (`id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

