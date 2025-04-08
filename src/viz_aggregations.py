import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="whitegrid", palette="viridis")

def plot_exam_volume_by_zip(series: pd.Series, top_n: int = 15):
    """Plots the top ZCTAs by exam volume."""
    top_series = series.head(top_n)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_series.values, y=top_series.index)
    plt.title(f"Top {top_n} ZCTAs by Exam Volume")
    plt.xlabel("Exam Volume")
    plt.ylabel("ZCTA")
    plt.tight_layout()
    plt.show()

def plot_avg_cost_by_zip(series: pd.Series, top_n: int = 15):
    """Plots the top ZCTAs by average testing cost."""
    top_series = series.head(top_n)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_series.values, y=top_series.index)
    plt.title(f"Top {top_n} ZCTAs by Average Testing Cost")
    plt.xlabel("Average Cost")
    plt.ylabel("ZCTA")
    plt.tight_layout()
    plt.show()

def plot_exam_volume_by_age_group(series: pd.Series):
    """Plots exam volume per age group."""
    plt.figure(figsize=(8, 5))
    sns.barplot(x=series.index, y=series.values)
    plt.title("Exam Volume by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Exam Volume")
    plt.tight_layout()
    plt.show()

def plot_top_coditems(df: pd.DataFrame):
    """Plots top CodItems by exam volume and total cost."""
    fig, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=df.index.astype(str), y=df['volume'], ax=ax1, color="skyblue", label='Volume')

    ax2 = ax1.twinx()
    sns.lineplot(x=df.index.astype(str), y=df['custo_total'], ax=ax2, color="orange", marker='o', label='Total Cost')

    ax1.set_title("Top Exams by Volume and Total Cost")
    ax1.set_xlabel("CodItem")
    ax1.set_ylabel("Volume")
    ax2.set_ylabel("Total Cost")
    ax1.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    plt.show()
