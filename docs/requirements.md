# Requirements - Medifood Garut

## Problem Statement
Pasien diet terapeutik (diabetes, hipertensi, pasca-operasi) di Garut sulit
menemukan makanan siap saji yang sesuai pantangan medis, dan mitra katering
sehat belum memiliki cara digital untuk mengelola pesanan.

## Target Users
- Pasien atau keluarga pendamping
- Mitra katering sehat
- Administrator platform

## Functional Requirements (M03)
- FR-01 Sistem menampilkan halaman utama.
- FR-02 Sistem menyediakan endpoint /health.
- FR-03 Sistem menyediakan endpoint /api/info.
- FR-04 Sistem menampilkan daftar kategori diet.

## Non-Functional Requirements
- NFR-01 Backend hanya listen pada loopback.
- NFR-02 Aplikasi dikelola systemd.
- NFR-03 Request publik masuk melalui reverse proxy.
- NFR-04 Secret tidak disimpan pada repository.
- NFR-05 /health mengembalikan HTTP 200 saat sehat.
- NFR-06 Deployment dapat direproduksi dari repository.
- NFR-07 Arsitektur sesuai RAM sekitar 1 GB.
- NFR-08 Informasi diet bersifat edukatif dan perlu validasi tenaga medis.

## Constraints
- AWS EC2 t3.micro (2 vCPU, sekitar 1 GB RAM, 19 GB disk)
- Ubuntu Server 24.04, public IPv4

## Acceptance Criteria M03
- [x] first deployment dapat diakses
- [x] health endpoint berfungsi
