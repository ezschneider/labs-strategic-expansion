import pandas as pd
import folium
from folium import Choropleth, CircleMarker
from branca.colormap import LinearColormap


def generate_exam_location_map(transactional: pd.DataFrame, geocode: pd.DataFrame, output_path: str = "exames_por_local.html"):
    """
    Gera um mapa interativo com círculos coloridos e escalados de acordo com volume e custo médio dos exames.
    
    - Cor: custo médio
    - Tamanho: volume de exames
    
    Parameters:
    - transactional: DataFrame com colunas ['Lab Id', 'Patient Id', 'Testing Cost']
    - geocode: DataFrame com colunas ['Lab Id', 'Location'] no formato "lat,lon"
    - output_path: caminho para salvar o HTML com o mapa
    """
    geocode = geocode.copy()
    geocode[['lat', 'lon']] = geocode['Location'].str.split(',', expand=True).astype(float)

    exames_por_lab = transactional.groupby('Lab Id').agg(
        volume=('Patient Id', 'count'),
        custo_total=('Testing Cost', 'sum'),
        custo_medio=('Testing Cost', 'mean')
    ).reset_index()

    df_map = geocode.merge(exames_por_lab, on='Lab Id', how='left')
    m = folium.Map(location=[39.5, -98.35], zoom_start=5)

    colormap = LinearColormap(
        colors=['#440154', '#482878', '#3e4989', '#31688e', '#26828e', '#1f9e89', '#35b779', '#6ece58', '#b5de2b', '#fde725'],
        vmin=df_map['custo_medio'].min(),
        vmax=df_map['custo_medio'].max(),
    )
    colormap.caption = 'Custo Médio por Laboratório (Cor)'
    colormap.add_to(m)

    max_volume = df_map['volume'].max()
    min_volume = df_map['volume'].min()

    for _, row in df_map.iterrows():
        if pd.notna(row['volume']) and pd.notna(row['custo_medio']):
            radius = 5 + 15 * (row['volume'] - min_volume) / (max_volume - min_volume)

            folium.CircleMarker(
                location=(row['lat'], row['lon']),
                radius=radius,
                color=colormap(row['custo_medio']),
                fill=True,
                fill_opacity=0.8,
                popup=folium.Popup(
                    f"<b>Lab:</b> {row['Lab Id']}<br>"
                    f"<b>Volume:</b> {int(row['volume'])}<br>"
                    f"<b>Custo Médio:</b> ${row['custo_medio']:.2f}",
                    max_width=300
                )
            ).add_to(m)

    # Legenda de tamanho (manual)
    legend_html = '''
     <div style="position: fixed; 
                 bottom: 40px; left: 40px; width: 230px; height: 100px; 
                 background-color: white; z-index:9999; font-size:14px;
                 border:2px solid grey; padding: 10px;">
     <b>Tamanho do círculo</b><br>
     🔘 Pequeno: baixo volume<br>
     🔘 Grande: alto volume<br>
     </div>'''
    m.get_root().html.add_child(folium.Element(legend_html))

    m.save(output_path)
    print(f"✅ Mapa salvo em: {output_path}")
