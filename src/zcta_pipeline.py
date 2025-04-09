import pandas as pd


def preparar_dados_geocode(geocode_df):
    geocode_df['ZCTA'] = geocode_df['Zipcode'].astype(str).str.split('.').str[0].str.zfill(5)
    return geocode_df[['Lab Id', 'ZCTA']]

def preparar_dados_transactional(transactional_df, geocode_df):
    transactional_df = transactional_df.copy()

    transactional_df['Testing Cost'] = (
        transactional_df['Testing Cost']
        .astype(str).str.replace(',', '.', regex=False)
        .pipe(pd.to_numeric, errors='coerce')
    )
    transactional_df['Date of service'] = pd.to_datetime(transactional_df['Date of service'], errors='coerce')
    transactional_df = transactional_df.merge(geocode_df, on='Lab Id', how='left')
    transactional_df['ZCTA'] = transactional_df['ZCTA'].astype(str).str.split('.').str[0].str.zfill(5)
    return transactional_df

def calcular_exames_por_zcta(transactional_df):
    return transactional_df.groupby('ZCTA').size().reset_index(name='num_exames')

def calcular_diversidade_exames(transactional_df):
    return transactional_df.groupby('ZCTA')['CodItem'].nunique().reset_index(name='num_tipos_exames')

def calcular_fidelizacao(transactional_df):
    transactional_df['ano'] = transactional_df['Date of service'].dt.year

    anos_por_paciente = transactional_df.groupby('Patient Id')['ano'].nunique().reset_index(name='anos_distintos')
    zcta_por_paciente = (
        transactional_df.groupby(['Patient Id', 'ZCTA']).size().reset_index(name='freq')
        .sort_values(['Patient Id', 'freq'], ascending=[True, False])
        .drop_duplicates('Patient Id')
    )
    paciente_fidelidade = pd.merge(anos_por_paciente, zcta_por_paciente[['Patient Id', 'ZCTA']], on='Patient Id')
    media_anos = paciente_fidelidade.groupby('ZCTA')['anos_distintos'].mean().reset_index(name='media_anos_por_paciente')
    prop_fieis = (
        paciente_fidelidade.assign(is_fiel=lambda x: x['anos_distintos'] >= 2)
        .groupby('ZCTA')['is_fiel'].mean().reset_index(name='proporcao_fieis')
    )
    return pd.merge(media_anos, prop_fieis, on='ZCTA')

def calcular_crescimento(transactional_df):
    transactional_df['YearMonth'] = transactional_df['Date of service'].dt.to_period('M').astype(str)
    monthly = transactional_df.groupby(['ZCTA', 'YearMonth']).size().reset_index(name='num_exames')
    meses = monthly.groupby('ZCTA').size().reset_index(name='meses_crescimento')
    return meses

def preparar_demografia(demographic_df):
    demographic_df['ZCTA'] = demographic_df['GeographicAreaName'].str.extract(r'(\d{5})')
    demographic_df['ZCTA'] = demographic_df['ZCTA'].astype(str).str.zfill(5)
    demographic_df['perc_idosos'] = (
        demographic_df['Population_65to74Years'] +
        demographic_df['Population_75to84Years'] +
        demographic_df['Population_85YearsAndOver']
    ) / demographic_df['TotalPopulation']
    demographic_df['perc_mulheres'] = 1 / (1 + demographic_df['SexRatio(males per 100 females)'] / 100)
    return demographic_df[['ZCTA', 'TotalPopulation', 'perc_idosos', 'perc_mulheres']]

def contar_labs_por_zcta(geocode_df):
    return geocode_df.groupby('ZCTA').size().reset_index(name='Labs na ZCTA')

def gerar_tabela_final(
    exames_df, diversidade_df, fidelizacao_df,
    crescimento_df, demografia_df, labs_df
):
    df = exames_df.merge(diversidade_df, on='ZCTA') \
                  .merge(demografia_df, on='ZCTA') \
                  .merge(fidelizacao_df, on='ZCTA') \
                  .merge(crescimento_df, on='ZCTA', how='left') \
                  .merge(labs_df, on='ZCTA', how='left')

    df.rename(columns={
        'num_exames': 'Total Exames',
        'num_tipos_exames': 'Tipos de Exames',
        'media_anos_por_paciente': 'Fidelização Média',
        'proporcao_fieis': 'Fidelização (%)',
        'meses_crescimento': 'Meses com Crescimento'
    }, inplace=True)

    return df[['ZCTA', 'Total Exames', 'Tipos de Exames', 'TotalPopulation', 'perc_idosos',
               'perc_mulheres', 'Labs na ZCTA', 'Meses com Crescimento',
               'Fidelização Média', 'Fidelização (%)']].sort_values(by='Total Exames', ascending=False)
