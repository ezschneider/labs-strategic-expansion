import geopandas as gpd
import pandas as pd
from sanitize import clean_demographic_data

def generate_geojson_file():
    demographic_df = pd.read_csv("../data/demographic.csv")
    demographic_df = clean_demographic_data(demographic_df)
    demographic_df['ZCTA'] = demographic_df['GeographicAreaName'].str.extract(r'ZCTA5 (\d{5})')

    zcta_gdf = gpd.read_file("../data/tl_2024_us_zcta520/tl_2024_us_zcta520.shp")
    zcta_gdf = zcta_gdf[['ZCTA5CE20', 'geometry']]
    zcta_gdf = zcta_gdf[zcta_gdf['ZCTA5CE20'].isin(demographic_df['ZCTA'].unique())]
    zcta_gdf['geometry'] = zcta_gdf['geometry'].simplify(0.01, preserve_topology=True)
    zcta_gdf.to_file("../data/zcta_subset.geojson", driver="GeoJSON")

if __name__ == "__main__":
    generate_geojson_file()
    print("GeoJSON file generated successfully.")