import io
from pandas import DataFrame
from IPython.display import display, HTML

def quick_overview(df, name="DataFrame"):
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