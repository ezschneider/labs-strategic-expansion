from pathlib import Path
from src.zcta_pipeline import (
    preparar_dados_geocode,
    preparar_dados_transactional,
    calcular_exames_por_zcta,
    calcular_diversidade_exames,
    calcular_fidelizacao,
    calcular_crescimento,
    preparar_demografia,
    contar_labs_por_zcta,
    gerar_tabela_final
)
from src.utils import load_all_csvs

def main():
    dfs = load_all_csvs(Path.cwd() / "data")

    # 1. Pré-processa dados brutos
    geocode_df = preparar_dados_geocode(dfs['geocode'])
    transactional_df = preparar_dados_transactional(dfs['transactional'], geocode_df)
    demographic_df = preparar_demografia(dfs['demographic'])

    # 2. Calcula métricas intermediárias
    exames_df = calcular_exames_por_zcta(transactional_df)
    diversidade_df = calcular_diversidade_exames(transactional_df)
    fidelizacao_df = calcular_fidelizacao(transactional_df)
    crescimento_df = calcular_crescimento(transactional_df)
    labs_df = contar_labs_por_zcta(geocode_df)

    # 3. Junta tudo em tabela final
    zcta_final_df = gerar_tabela_final(
        exames_df, diversidade_df, fidelizacao_df,
        crescimento_df, demographic_df, labs_df
    )

    # 4. Visualiza os Top 10 ZCTAs mais relevantes
    print(zcta_final_df.head(10))

if __name__ == "__main__":
    main()