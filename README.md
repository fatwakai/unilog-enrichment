# 🛡️ Unilog Enrichment

Middleware enrichment tool untuk memperkaya log JSON dengan data GeoIP dan penandaan logtype (tagging).

## ✨ Fitur
- Enrichment berdasarkan IP publik (GeoIP API)
- Penambahan tag `logtype` otomatis
- Dukungan input dari file JSON, syslog, atau Elasticsearch (coming soon)
- Output ke file atau Elasticsearch

## 🛠️ Instalasi

```bash
git clone https://github.com/username/unilog-enrichment.git
cd unilog-enrichment
pip install .
