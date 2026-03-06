import pandas as pd
import ast

def load_tsp_dataset(path):
    df = pd.read_csv(path)

    # Ambil 1 instance saja
    row = df.iloc[0]

    num_cities = int(row["num_cities"])
    coords = ast.literal_eval(row["city_coordinates"])
    distance_matrix = ast.literal_eval(row["distance_matrix"])

    return num_cities, coords, distance_matrix
