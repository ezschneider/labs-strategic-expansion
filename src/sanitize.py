import pandas as pd
import re

def extract_zip_from_id(id_str):
    match = re.search(r'(\d{5})$', str(id_str))
    return int(match.group(1)) if match else None

def clean_geocode(df: pd.DataFrame) -> pd.DataFrame:
    df['Zipcode'] = pd.to_numeric(df['Zipcode'], errors='coerce')
    df['Zipcode'] = df.apply(
        lambda row: row['Zipcode'] if not pd.isna(row['Zipcode']) else extract_zip_from_id(row['Address']),
        axis=1
    )
    df = df[df['Zipcode'].notna()]
    df = df[df['Address'] != 'Unavailable']
    df['Zipcode'] = df['Zipcode'].astype(int)
    return df

def clean_exams_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset='CodItem')
    df = df[df['Testing Cost'] > 0]
    p99 = df['Testing Cost'].quantile(0.99)
    df['Testing Cost'] = df['Testing Cost'].clip(upper=p99)
    return df

def clean_demographic_data(df: pd.DataFrame) -> pd.DataFrame:
    df['SexRatio(males per 100 females)'] = pd.to_numeric(df['SexRatio(males per 100 females)'], errors='coerce')
    df.loc[df['SexRatio(males per 100 females)'] > 150, 'SexRatio(males per 100 females)'] = None
    df['SexRatio(males per 100 females)'] = df['SexRatio(males per 100 females)'].fillna(
        df['SexRatio(males per 100 females)'].median()
    )
    df['MedianAgeInYears'] = df['MedianAgeInYears'].fillna(
        df['MedianAgeInYears'].median()
    )
    df = df[df['TotalPopulation'] > 0]
    df = df.drop_duplicates(subset='Id')
    return df

def clean_transactional_data(df: pd.DataFrame) -> pd.DataFrame:
    df['Testing Cost'] = (
        df['Testing Cost']
        .astype(str)
        .str.replace(',', '.', regex=False)
        .pipe(pd.to_numeric, errors='coerce')
    )
    df['Date of birth'] = pd.to_datetime(df['Date of birth'], errors='coerce')
    df['Date of service'] = pd.to_datetime(df['Date of service'], errors='coerce')
    df = df.dropna(subset=['Date of birth'])

    # Classifica tipo de Patient Id
    df.loc[:, 'id_tipo'] = df['Patient Id'].astype(str).apply(
        lambda x: (
            'completo' if re.match(r'^\d{6,}-\d$', x) else
            'com_bio' if re.match(r'^\d+-BIO\d+$', x) else
            'outro'
        )
    )
    # Mantém apenas os IDs válidos
    df = df[df['id_tipo'].isin(['completo', 'com_bio'])]
    df = df.drop_duplicates()

    return df

def clean_economic_data(df: pd.DataFrame) -> pd.DataFrame:
    rename_map = {
        'TotalHouseholds_LessThan$10.000': 'Households_<10k',
        'TotalHouseholds_$10.000to$14.999': 'Households_10k_14k',
        'TotalHouseholds_$15.000to$24.999': 'Households_15k_24k',
        'TotalHouseholds_$25.000to$34.999': 'Households_25k_34k',
        'TotalHouseholds_$35.000to$49.999': 'Households_35k_49k',
        'TotalHouseholds_$50.000to$74.999': 'Households_50k_74k',
        'TotalHouseholds_$75.000to$99.999': 'Households_75k_99k',
        'TotalHouseholds_$100.000to$149.999': 'Households_100k_149k',
        'TotalHouseholds_$150.000to$199.999': 'Households_150k_199k',
        'TotalHouseholds_$200.000OrMore': 'Households_200k_plus'
    }
    df = df.rename(columns=rename_map)
    df['Zipcode'] = df['id'].apply(extract_zip_from_id)
    df = df.groupby('Zipcode', as_index=False).sum(numeric_only=True)
    return df

def sanitize_all(data: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    return {
        'geocode': clean_geocode(data['geocode']),
        'exams': clean_exams_data(data['exams']),
        'demographic': clean_demographic_data(data['demographic']),
        'transactional': clean_transactional_data(data['transactional']),
        'economic': clean_economic_data(data['economic'])
    }
