import io
from pathlib import Path
import pandas as pd
from IPython.display import display, HTML


def load_all_csvs(folder: Path) -> dict[pd.DataFrame]:
    csv_files = list(folder.glob("*.csv"))
    dfs = {f.stem: pd.read_csv(f, sep=None, engine="python") for f in csv_files}
    return dfs

def quick_overview(df: pd.DataFrame, name: str ="DataFrame") -> None:
    display(HTML(f"<h3 style='color:#333;font-weight:bold;'>📋 Overview de <code>{name}</code></h3>"))
    
    display(HTML("<hr>"))

    display(HTML("<b>🔹 Shape:</b>"))
    print(df.shape)

    display(HTML("<b>🔹 Primeiras linhas:</b>"))
    display(df.head())

    display(HTML("<b>🔹 Info:</b>"))
    buffer = io.StringIO()
    df.info(buf=buffer)
    print(buffer.getvalue())

    display(HTML("<b>🔹 Estatísticas descritivas:</b>"))
    display(df.describe(include='all').transpose())

    display(HTML("<b>🔹 Valores nulos:</b>"))
    display(df.isnull().sum())
    display(HTML("<hr>"))
