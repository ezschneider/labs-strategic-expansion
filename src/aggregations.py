import pandas as pd

def add_age_column(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['Age'] = (df['Date of service'] - df['Date of birth']).dt.days // 365
    return df

def exam_volume_by_zip(transactional: pd.DataFrame, geocode: pd.DataFrame) -> pd.Series:
    merged = transactional.merge(geocode[['Lab Id', 'Zipcode']], on='Lab Id', how='left')
    return merged.groupby('Zipcode')['Patient Id'].count().sort_values(ascending=False)

def avg_cost_by_zip(transactional: pd.DataFrame, geocode: pd.DataFrame) -> pd.Series:
    merged = transactional.merge(geocode[['Lab Id', 'Zipcode']], on='Lab Id', how='left')
    return merged.groupby('Zipcode')['Testing Cost'].mean().sort_values(ascending=False)

def exam_volume_by_age_group(transactional: pd.DataFrame) -> pd.Series:
    df = add_age_column(transactional)
    faixa = pd.cut(df['Age'], bins=[0, 18, 35, 50, 65, 80, 100], right=False,
                   labels=['0-17', '18-34', '35-49', '50-64', '65-79', '80+'])
    return df.groupby(faixa)['Patient Id'].count()

def top_coditems(transactional: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    return transactional.groupby('CodItem').agg(
        volume=('Patient Id', 'count'),
        custo_total=('Testing Cost', 'sum')
    ).sort_values(by='volume', ascending=False).head(top_n)

