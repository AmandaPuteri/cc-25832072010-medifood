# Medifood Garut

Cloud Computing - PTI 2802 - Pertemuan 3 (Project Inception)

## Author
Nisrina Amanda Puteri - NIM 25832072010 - Kelas: (isi kelasmu)

## Problem
Pasien dengan kebutuhan diet terapeutik (diabetes, hipertensi, pasca-operasi)
dan keluarganya di Garut kesulitan menemukan makanan siap saji yang sesuai
pantangan medis, sementara mitra katering sehat belum punya cara digital
untuk mengelola pesanan. Medifood Garut menyediakan katalog menu yang dapat
difilter menurut kondisi medis, kalkulasi nutrisi otomatis, dan dasbor
pesanan untuk katering.

## Target Users
- Pasien atau keluarga pendamping
- Mitra katering sehat
- Administrator platform

## Features M03
- Halaman utama dengan daftar kategori diet
- Endpoint kesehatan: `GET /health`
- Endpoint info aplikasi: `GET /api/info`
- Endpoint kategori diet: `GET /api/diet-categories`
- Deployment pada AWS EC2 (Ubuntu Server 24.04)

## Architecture

```mermaid
flowchart LR
    U[User] -->|HTTP :80| C[Caddy]
    C --> G[Gunicorn 127.0.0.1:8000]
    G --> F[Flask]
```

## Infrastructure
- AWS EC2 t3.micro, region Singapore (ap-southeast-1)
- Ubuntu Server 24.04 LTS, 2 vCPU, sekitar 1 GB RAM, disk 19 GB, swap 1 GB
- Python 3.12, Flask, Gunicorn (1 worker, 2 thread), systemd, Caddy, UFW

## Public Endpoint
`http://<PUBLIC_IP>/` (IP publik dapat berubah jika instance dihentikan)

## Health Check
`GET /health`

## Deployment
Lihat `docs/deployment.md`.

## Security
- SSH hanya dengan key, login root dan password dinonaktifkan
- Hanya user `cloudstudent` yang diizinkan SSH
- UFW aktif, backend hanya listen di 127.0.0.1
- Tidak ada secret di repository

## Current Limitations
- HTTP saja, belum HTTPS
- Belum ada database, container, atau CI/CD
- Informasi diet bersifat edukatif dan perlu divalidasi ahli gizi atau tenaga medis

## Roadmap
M04 DNS dan HTTPS, M05 Data, M06 Container, M07 IaC, M09 CI/CD
