# 🛠️ UniLog Enrichment

**UniLog Enrichment** adalah alat (tool) berbasis Python yang dirancang untuk memperkaya data log dengan informasi tambahan seperti lokasi IP (GeoIP), ASN, dan WHOIS. Tool ini bekerja sebagai middleware dalam sistem log management atau SIEM untuk memberikan konteks tambahan terhadap data log mentah.

---

## 🔍 Fitur Utama

- 📦 **Enrichment log JSON** secara otomatis
- 🌍 Tambahan informasi GeoIP (negara, kota, koordinat)
- 🛰️ Informasi ASN (Autonomous System Number)
- 🕵️ WHOIS Lookup (opsional)
- 🏷️ Tagging berbasis kriteria tertentu
- ⚙️ Konfigurasi fleksibel melalui `config.yaml`

---

## 🧾 Prasyarat

- Python **3.10** atau lebih tinggi
- Koneksi internet (untuk data publik seperti GeoIP, ASN, dan WHOIS)

---

## 🚀 Cara Menggunakan

1. **Clone repositori:**

   ```bash
   git clone https://github.com/fatwakai/unilog-enrichment.git
   cd unilog-enrichment
Install dependensi:
pip install -r requirements.txt
Sesuaikan konfigurasi di file config.yaml sesuai kebutuhan.

Jalankan tool:
python main.py

🤝 Kontribusi
Kontribusi sangat terbuka! Silakan buat issue, pull request, atau diskusi fitur tambahan untuk pengembangan lebih lanjut.
