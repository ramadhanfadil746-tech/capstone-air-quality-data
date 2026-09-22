# Capstone Data Collection - Air Quality

## 1. Deskripsi Proyek

Proyek ini merupakan data collection pipeline
untuk domain Air Quality atau Kualitas Udara.

Data dikumpulkan dari dua sumber:

1. UCI Air Quality Dataset
2. Open-Meteo Air Quality REST API

Proses pengumpulan data dilakukan secara otomatis
menggunakan Python.

---

## 2. Sumber Data

### A. UCI Air Quality Dataset

Dataset:
Air Quality Dataset

Sumber:
UCI Machine Learning Repository

Jenis sumber:
CSV Dataset

Data yang digunakan berisi informasi kualitas udara
seperti CO, NMHC, Benzene, NOx, NO2, temperatur,
relative humidity, dan absolute humidity.

---

### B. Open-Meteo Air Quality API

Endpoint:

https://air-quality-api.open-meteo.com/v1/air-quality

Jenis sumber:
REST API publik

Data yang dikumpulkan meliputi:

- PM10
- PM2.5
- Carbon Monoxide
- Nitrogen Dioxide
- Sulphur Dioxide
- Ozone
- European AQI
- US AQI

---

## 3. Struktur Repository

capstone-air-quality-data/

├── data/
│   └── raw/
│       ├── AirQualityUCI.csv
│       └── air_quality_api.json
│
├── data_dictionary/
│   └── data_dictionary.csv
│
├── data_collection.py
├── requirements.txt
└── README.md

---

## 4. Instalasi

Pastikan Python sudah terinstall.

Install dependency:

pip install -r requirements.txt

---

## 5. Menjalankan Data Collection

Jalankan:

python data_collection.py

Script akan:

1. Membuat folder data/raw/
2. Mengambil dataset Air Quality dari UCI
3. Menyimpan dataset dalam format CSV
4. Mengakses Open-Meteo Air Quality REST API
5. Menyimpan hasil API dalam format JSON

---

## 6. Reproducibility

Pipeline dapat dijalankan kembali dengan:

python data_collection.py

Dengan demikian proses pengumpulan data
dapat dilakukan kembali secara otomatis
tanpa mengambil data secara manual.

---

## 7. Data Sources

UCI Machine Learning Repository:
Air Quality Dataset

Open-Meteo:
Air Quality API