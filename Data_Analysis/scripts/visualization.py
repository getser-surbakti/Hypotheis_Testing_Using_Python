import matplotlib.pyplot as plt
import seaborn as sns
import os

# Helper untuk simpan plot
def save_plot(fig, filename):
    os.makedirs("../results/plots", exist_ok=True)  # pastikan folder ada
    fig.savefig(os.path.join("../results/plots", filename), bbox_inches="tight")
    plt.close(fig)  # tutup figure supaya tidak bentrok dengan plot berikutnya

def plot_age_distribution(control, treatment):
    fig = plt.figure()
    plt.hist(control["Age"], alpha=0.5, label="Control")
    plt.hist(treatment["Age"], alpha=0.5, label="Treatment")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.legend()
    plt.title("Age Distribution")
    save_plot(fig, "age_distribution.png")

def plot_infection_rate(control, treatment):
    fig = plt.figure()
    rates = [control["Infected"].mean(), treatment["Infected"].mean()]
    plt.bar(["Control", "Treatment"], rates, color=["blue", "orange"])
    plt.ylabel("Proportion Infected")
    plt.title("Comparison of Infection Rates")
    save_plot(fig, "infection_rate_comparison.png")

def plot_gender_distribution(control, treatment):
    fig, axes = plt.subplots(1, 2, figsize=(10,5))
    sns.countplot(x="Gender", data=control, ax=axes[0])
    axes[0].set_title("Control Group Gender")
    sns.countplot(x="Gender", data=treatment, ax=axes[1])
    axes[1].set_title("Treatment Group Gender")
    save_plot(fig, "gender_distribution.png")
