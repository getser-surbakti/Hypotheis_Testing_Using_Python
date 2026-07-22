import pandas as pd

def load_data():
    control = pd.read_csv("../data/raw/control_group.csv")
    treatment = pd.read_csv("../data/raw/treatment_group.csv")
    return control, treatment

def clean_data(control, treatment):
    # 1. Drop missing values
    control = control.dropna()
    treatment = treatment.dropna()

    # 2. Pastikan tipe data sesuai
    control["Age"] = control["Age"].astype(int)
    treatment["Age"] = treatment["Age"].astype(int)

    control["Infected"] = control["Infected"].astype(int)
    treatment["Infected"] = treatment["Infected"].astype(int)

    # 3. Hapus duplikat
    control = control.drop_duplicates()
    treatment = treatment.drop_duplicates()

    # 4. Validasi kolom Infected hanya berisi 0/1
    assert set(control["Infected"].unique()).issubset({0,1}), "Kontrol: nilai Infected tidak valid"
    assert set(treatment["Infected"].unique()).issubset({0,1}), "Perlakuan: nilai Infected tidak valid"

    return control, treatment

def save_processed(control, treatment, control_path="../data/processed/control_group_clean.csv", treatment_path="../data/processed/treatment_group_clean.csv"):
    control.to_csv(control_path, index=False)
    treatment.to_csv(treatment_path, index=False)
    print("Data processed berhasil disimpan ke folder 'data/processed/'")

