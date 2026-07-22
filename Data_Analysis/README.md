# 🧪 Data Analytics Using Python

Proyek ini bertujuan untuk menganalisis data eksperimen **kontrol vs perlakuan** dalam konteks infeksi, menggunakan Python, Pandas, Seaborn, dan Matplotlib.  
Workflow mencakup **data cleaning, exploratory data analysis (EDA), visualisasi, dan hypothesis testing**.  
Hasil akhir disimpan di folder `results/` dalam bentuk **summary.csv** dan grafik di `plots/`.

---

## 📂 Struktur Project

```text
Data_Analytics_Using_Python/
│
├── data/
│   ├── raw/                # Dataset mentah
│   └── processed/          # Dataset hasil cleaning
│
├── notebooks/
│   ├── analysis.ipynb      # Workflow cleaning + EDA
│   ├── visualization.ipynb # Visualisasi hasil analisis
│   └── hypothesis_testing.ipynb # Uji hipotesis proporsi infeksi
│
├── scripts/
│   ├── __init__.py
│   ├── analysis.py         # Fungsi modular untuk cleaning
│   └── visualization.py    # Fungsi modular untuk visualisasi
│
├── results/
│   ├── summary.csv         # Ringkasan hasil uji hipotesis
│   └── plots/              # Grafik utama (usia, gender, infeksi)
│       ├── age_distribution.png
│       ├── gender_distribution.png
│       └── infection_rate_comparison.png
│
└── README.md               # Dokumentasi project
