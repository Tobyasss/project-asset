-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 20 Feb 2026 pada 08.49
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `it_asset_management`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `asset`
--

CREATE TABLE `asset` (
  `id_asset` varchar(20) NOT NULL,
  `kategori_id` int(11) DEFAULT NULL,
  `merk_id` int(11) DEFAULT NULL,
  `tipe_id` int(11) DEFAULT NULL,
  `nomor_sn` varchar(100) DEFAULT NULL,
  `spesifikasi` text DEFAULT NULL,
  `tanggal_beli` date DEFAULT NULL,
  `status` enum('Aktif','Rusak','Disimpan') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `assignment`
--

CREATE TABLE `assignment` (
  `id_transaksi` int(11) NOT NULL,
  `asset_id` varchar(20) DEFAULT NULL,
  `karyawan_id` int(11) DEFAULT NULL,
  `tanggal_serah` date DEFAULT NULL,
  `tanggal_kembali` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `karyawan`
--

CREATE TABLE `karyawan` (
  `id_karyawan` int(11) NOT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `departemen` varchar(100) DEFAULT NULL,
  `jabatan` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `kategori`
--

CREATE TABLE `kategori` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `prefix` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `kategori`
--

INSERT INTO `kategori` (`id`, `nama`, `prefix`) VALUES
(1, 'Laptop', 'LTP'),
(2, 'Printer', 'PTR'),
(3, 'Monitor', 'MNTR'),
(4, 'Mouse', 'MOU'),
(5, 'Keyboard', 'KBR'),
(6, 'Smartphone', 'HP');

-- --------------------------------------------------------

--
-- Struktur dari tabel `lisensi`
--

CREATE TABLE `lisensi` (
  `id_lisensi` int(11) NOT NULL,
  `nama_software` varchar(100) DEFAULT NULL,
  `no_sn` varchar(100) DEFAULT NULL,
  `tanggal_kadaluarsa` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `merk`
--

CREATE TABLE `merk` (
  `id` int(11) NOT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `kategori_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `merk`
--

INSERT INTO `merk` (`id`, `nama`, `kategori_id`) VALUES
(1, 'Apple', 1),
(2, 'Acer', 1),
(3, 'Asus', 1),
(4, 'Lenovo', 1),
(5, 'Hewlett Packard', 1),
(6, 'Epson', 2),
(7, 'Hewlett Packard', 2),
(8, 'Samsung', 3),
(9, 'Xiaomi', 3),
(10, 'LG', 3),
(11, 'Lenovo', 3),
(12, 'Apple', 4),
(13, 'Logitech', 4),
(14, 'Logitech', 5),
(15, 'Xiaomi', 6),
(16, 'Apple', 6),
(17, 'Samsung', 6);

-- --------------------------------------------------------

--
-- Struktur dari tabel `tipe`
--

CREATE TABLE `tipe` (
  `id` int(11) NOT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `merk_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `tipe`
--

INSERT INTO `tipe` (`id`, `nama`, `merk_id`) VALUES
(1, 'MacBook Air M1', 1),
(2, 'MacBook Air M2', 1),
(3, 'MacBook Pro M2', 1),
(4, 'MacBook Pro M4', 1),
(5, 'ROG', 3),
(6, 'A1404V', 3),
(7, 'Nitro 5', 2),
(8, 'Predator', 2),
(9, 'Aspire 5', 2),
(10, 'Aspire Lite', 2),
(11, 'Aspire 14', 2),
(12, 'Victus', 5),
(13, 'Pavilion', 5),
(14, '15-FD0888TX', 5),
(15, 'V14', 4),
(16, 'LOQ', 4),
(17, 'T47Q', 4),
(18, 'Ideapad', 4),
(19, 'Thinkpad L14', 4),
(20, 'HP DeskJet GT 5810', 7),
(21, 'L5290', 6),
(22, 'Magic Mouse', 12),
(23, 'MK220', 13),
(24, 'M220', 14),
(25, '24 Inch', 8),
(26, 'MI TV', 9),
(27, 'MI LED', 9),
(28, 'Think Vision', 11),
(29, 'iPhone 6', 16),
(30, 'iPhone 7+', 16),
(31, 'iPhone 8+', 16),
(32, 'iPhone 11', 16),
(33, 'iPhone 13', 16),
(34, 'iPhone 15', 16),
(35, 'iPhone 12', 16),
(36, 'Redmi Note 12', 15),
(37, '9C', 15),
(38, 'A04', 17),
(39, 'A05', 17),
(40, 'A04S', 17);

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `level` enum('master','admin') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `level`) VALUES
(1, 'master', 'scrypt:32768:8:1$44SYhAUlkHQMhlAs$c55fec908d4f0bf71c41dc29060f1b5cb284b09d36cd02cfe4a80a6ce6ac60a55473c4b519a2a16e1b339fc0e0ba72ab300bee69cf1e1805f1dc55bf316ef27d', 'master');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `asset`
--
ALTER TABLE `asset`
  ADD PRIMARY KEY (`id_asset`),
  ADD KEY `kategori_id` (`kategori_id`),
  ADD KEY `merk_id` (`merk_id`),
  ADD KEY `tipe_id` (`tipe_id`);

--
-- Indeks untuk tabel `assignment`
--
ALTER TABLE `assignment`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `asset_id` (`asset_id`),
  ADD KEY `karyawan_id` (`karyawan_id`);

--
-- Indeks untuk tabel `karyawan`
--
ALTER TABLE `karyawan`
  ADD PRIMARY KEY (`id_karyawan`);

--
-- Indeks untuk tabel `kategori`
--
ALTER TABLE `kategori`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `lisensi`
--
ALTER TABLE `lisensi`
  ADD PRIMARY KEY (`id_lisensi`);

--
-- Indeks untuk tabel `merk`
--
ALTER TABLE `merk`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kategori_id` (`kategori_id`);

--
-- Indeks untuk tabel `tipe`
--
ALTER TABLE `tipe`
  ADD PRIMARY KEY (`id`),
  ADD KEY `merk_id` (`merk_id`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `assignment`
--
ALTER TABLE `assignment`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `karyawan`
--
ALTER TABLE `karyawan`
  MODIFY `id_karyawan` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `kategori`
--
ALTER TABLE `kategori`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `lisensi`
--
ALTER TABLE `lisensi`
  MODIFY `id_lisensi` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `merk`
--
ALTER TABLE `merk`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT untuk tabel `tipe`
--
ALTER TABLE `tipe`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `asset`
--
ALTER TABLE `asset`
  ADD CONSTRAINT `asset_ibfk_1` FOREIGN KEY (`kategori_id`) REFERENCES `kategori` (`id`),
  ADD CONSTRAINT `asset_ibfk_2` FOREIGN KEY (`merk_id`) REFERENCES `merk` (`id`),
  ADD CONSTRAINT `asset_ibfk_3` FOREIGN KEY (`tipe_id`) REFERENCES `tipe` (`id`);

--
-- Ketidakleluasaan untuk tabel `assignment`
--
ALTER TABLE `assignment`
  ADD CONSTRAINT `assignment_ibfk_1` FOREIGN KEY (`asset_id`) REFERENCES `asset` (`id_asset`),
  ADD CONSTRAINT `assignment_ibfk_2` FOREIGN KEY (`karyawan_id`) REFERENCES `karyawan` (`id_karyawan`);

--
-- Ketidakleluasaan untuk tabel `merk`
--
ALTER TABLE `merk`
  ADD CONSTRAINT `merk_ibfk_1` FOREIGN KEY (`kategori_id`) REFERENCES `kategori` (`id`);

--
-- Ketidakleluasaan untuk tabel `tipe`
--
ALTER TABLE `tipe`
  ADD CONSTRAINT `tipe_ibfk_1` FOREIGN KEY (`merk_id`) REFERENCES `merk` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
