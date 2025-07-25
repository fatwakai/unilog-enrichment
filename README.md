# 🛠️ UniLog Enrichment

**UniLog Enrichment** adalah sebuah alat (tool) Python yang dirancang untuk memperkaya data log dengan informasi tambahan seperti lokasi IP (GeoIP), informasi ASN, dan WHOIS. Tool ini berfungsi sebagai middleware dalam sistem log management atau SIEM.

## 🔍 Fitur Utama

- 🔹 Enrichment data log berbasis JSON
- 🌍 Informasi GeoIP (negara, kota, koordinat)
- 🛰️ Informasi ASN (Autonomous System Number)
- 🕵️ WHOIS Lookup (jika diperlukan)
- 🏷️ Tagging berdasarkan kriteria tertentu
- ⚙️ Konfigurasi fleksibel via `config.yaml`

## 🧾 Prasyarat

- Python 3.10 atau lebih tinggi
- Koneksi internet (untuk lookup data publik)

## 🚀 Cara Menggunakan

1. Clone repositori:

   ```bash
   git clone https://github.com/fatwakai/unilog-enrichment.git
   cd unilog-enrichment
Install dependensi:

bash
Salin
Edit
pip install -r requirements.txt
Edit file config.yaml sesuai kebutuhan.

Jalankan tool:

bash
Salin
Edit
python main.py
📁 Struktur Folder
lua
Salin
Edit
unilog-enrichment/
├── config.yaml
├── enrichment/
│   ├── __init__.py
│   ├── enricher.py
│   └── utils.py
├── logs/
│   └── (output log files)
├── main.py
└── requirements.txt
🤝 Kontribusi
Pull request dan diskusi terbuka untuk pengembangan fitur tambahan.
