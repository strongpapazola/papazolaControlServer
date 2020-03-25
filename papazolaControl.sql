-- phpMyAdmin SQL Dump
-- version 4.9.2deb1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Waktu pembuatan: 25 Mar 2020 pada 14.53
-- Versi server: 10.3.22-MariaDB-1
-- Versi PHP: 7.3.15-3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `papazolaControl`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `info`
--

CREATE TABLE `info` (
  `id` int(11) NOT NULL,
  `type` varchar(64) NOT NULL,
  `value` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `info`
--

INSERT INTO `info` (`id`, `type`, `value`) VALUES
(1, 'Name', 'localhost'),
(2, 'IP', '127.0.0.1'),
(3, 'Status', 'Active'),
(4, 'Master', 'localhost'),
(5, 'PortSSH', '22'),
(6, 'reboot', '1');

-- --------------------------------------------------------

--
-- Struktur dari tabel `network_rule`
--

CREATE TABLE `network_rule` (
  `id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `name_val` int(1) NOT NULL COMMENT '1 = off, 2 = on',
  `execute_val` int(1) NOT NULL COMMENT '1 = belum, 2 = sudah, 3 = warrning'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `network_rule`
--

INSERT INTO `network_rule` (`id`, `name`, `name_val`, `execute_val`) VALUES
(1, 'icmp', 1, 2),
(2, 'ssh-publickey', 1, 2);

-- --------------------------------------------------------

--
-- Struktur dari tabel `services`
--

CREATE TABLE `services` (
  `id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `val` int(1) NOT NULL COMMENT '1 = off, 2 = on, 3 = error',
  `execute` int(1) NOT NULL COMMENT '1 = belum, 2 = sudah',
  `information` varchar(512) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `services`
--

INSERT INTO `services` (`id`, `name`, `val`, `execute`, `information`) VALUES
(1, 'ssh', 2, 2, 'b\'     Active: active (running) since Wed 2020-03-25 12:31:40 WIB; 2h 6min ago\\n\''),
(4, 'portsentry', 2, 2, 'b\'     Active: active (running) since Wed 2020-03-25 12:31:45 WIB; 2h 6min ago\\n\'');

-- --------------------------------------------------------

--
-- Struktur dari tabel `session`
--

CREATE TABLE `session` (
  `id` int(11) NOT NULL,
  `username` varchar(32) NOT NULL,
  `role_id` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `session`
--

INSERT INTO `session` (`id`, `username`, `role_id`) VALUES
(5, 'admin', 2);

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(16) NOT NULL,
  `password` varchar(64) NOT NULL,
  `role_id` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `role_id`) VALUES
(6, 'admin', '$2y$10$SViO6fMwP8Sui5aXcvgfB.Wfi8MYQroLZ0jRnwPRqFJmZ5a8HjEgG', 2);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `info`
--
ALTER TABLE `info`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `network_rule`
--
ALTER TABLE `network_rule`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `session`
--
ALTER TABLE `session`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `info`
--
ALTER TABLE `info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `network_rule`
--
ALTER TABLE `network_rule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `services`
--
ALTER TABLE `services`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `session`
--
ALTER TABLE `session`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
