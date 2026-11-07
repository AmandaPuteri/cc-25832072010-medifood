# ADR-0001: Initial Deployment Architecture

## Status
Accepted

## Context
AWS EC2 t3.micro, sekitar 1 GB RAM, Ubuntu Server 24.04, kredit AWS Free Plan.

## Decision
Flask, Gunicorn (1 worker, 2 thread), systemd, Caddy, UFW, GitHub.

## Alternatives
1. Node.js + PM2
2. NGINX + Gunicorn
3. Docker
4. PHP-FPM

## Rationale
Python 3.12 bawaan Ubuntu, footprint kecil untuk RAM 1 GB, Caddy siap
dikembangkan menjadi HTTPS otomatis, dan container belum dibahas di M03.

## Consequences
Positif: sederhana, ringan, mudah direproduksi.
Negatif: satu server, HTTP saja, deployment masih manual.

## Review Trigger
Tinjau ulang pada M06 dan M07.
