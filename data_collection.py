import os
import json
import zipfile
import requests
import pandas as pd
from io import BytesIO


# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RAW_DIR = os.path.join(
    BASE_DIR,
    "data",
    "raw"
)


UCI_DATASET_URL = (
    "https://archive.ics.uci.edu/static/public/360/"
    "air%2Bquality.zip"
)


OPEN_METEO_API_URL = (
    "https://air-quality-api.open-meteo.com/v1/air-quality"
)


# Jakarta
LATITUDE = -6.2088
LONGITUDE = 106.8456


# ============================================================
# CREATE DIRECTORY
# ============================================================

def create_directories():

    os.makedirs(
        RAW_DIR,
        exist_ok=True
    )

    print("Folder data/raw/ berhasil disiapkan.")


# ============================================================
# DOWNLOAD UCI DATASET
# ============================================================

def download_uci_dataset():

    print("\n[1] Mengambil dataset Air Quality dari UCI...")

    csv_path = os.path.join(
        RAW_DIR,
        "AirQualityUCI.csv"
    )

    try:

        response = requests.get(
            UCI_DATASET_URL,
            timeout=60
        )

        response.raise_for_status()

        with zipfile.ZipFile(
            BytesIO(response.content)
        ) as zip_file:

            csv_files = [
                file_name
                for file_name in zip_file.namelist()
                if file_name.lower().endswith(".csv")
            ]

            if not csv_files:

                raise FileNotFoundError(
                    "File CSV tidak ditemukan di dalam ZIP."
                )

            csv_file_name = csv_files[0]

            with zip_file.open(
                csv_file_name
            ) as file:

                df = pd.read_csv(
                    file,
                    sep=";",
                    decimal=","
                )

        df.to_csv(
            csv_path,
            index=False
        )

        print(
            "Dataset UCI berhasil diambil."
        )

        print(
            f"Jumlah baris: {len(df):,}"
        )

        print(
            f"Jumlah kolom: {len(df.columns)}"
        )

        print(
            f"File disimpan: {csv_path}"
        )

    except Exception as error:

        print(
            "Gagal mengambil dataset UCI."
        )

        raise error


# ============================================================
# DOWNLOAD OPEN-METEO API
# ============================================================

def download_air_quality_api():

    print(
        "\n[2] Mengambil data dari "
        "Open-Meteo Air Quality API..."
    )

    json_path = os.path.join(
        RAW_DIR,
        "air_quality_api.json"
    )

    params = {

        "latitude": LATITUDE,

        "longitude": LONGITUDE,

        "hourly": (
            "pm10,"
            "pm2_5,"
            "carbon_monoxide,"
            "nitrogen_dioxide,"
            "sulphur_dioxide,"
            "ozone,"
            "european_aqi,"
            "us_aqi"
        ),

        "forecast_days": 5,

        "timezone": "Asia/Jakarta"
    }

    try:

        response = requests.get(
            OPEN_METEO_API_URL,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        with open(
            json_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        hourly_data = data.get(
            "hourly",
            {}
        )

        time_data = hourly_data.get(
            "time",
            []
        )

        print(
            "Data Open-Meteo berhasil diambil."
        )

        print(
            f"Jumlah observasi hourly: "
            f"{len(time_data)}"
        )

        print(
            f"File disimpan: {json_path}"
        )

    except requests.exceptions.RequestException as error:

        print(
            "Gagal mengakses Open-Meteo API."
        )

        raise error


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 60)

    print(
        "DATA COLLECTION - AIR QUALITY"
    )

    print("=" * 60)

    try:

        create_directories()

        download_uci_dataset()

        download_air_quality_api()

        print(
            "\n" + "=" * 60
        )

        print(
            "DATA COLLECTION SELESAI"
        )

        print(
            "=" * 60
        )

    except Exception as error:

        print(
            "\n" + "=" * 60
        )

        print(
            "DATA COLLECTION GAGAL"
        )

        print(
            f"Error: {error}"
        )

        print(
            "=" * 60
        )


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":

    main()