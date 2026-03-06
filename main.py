from src.loader import load_tsp_dataset
from src.ga_tsp import GeneticAlgorithmTSP
from src.visualize import plot_route

def main():
    # Load dataset
    num_cities, coords, dist_matrix = load_tsp_dataset("data/tsp_dataset.csv")

    print("Jumlah kota:", num_cities)
    print("Menjalankan Genetic Algorithm...\n")

    # Jalankan GA
    ga = GeneticAlgorithmTSP(
        dist_matrix=dist_matrix,
        population_size=60,
        mutation_rate=0.02,
        generations=200
    )

    best_route, best_distance = ga.run()

    print("\n====================")
    print("      HASIL AKHIR   ")
    print("====================")
    print("Best Route:", best_route)
    print(f"Total Distance: {best_distance:.4f}")

    # Visualisasi rute
    #print("\nMenampilkan visualisasi rute...")
    #plot_route(coords, best_route)
    # Visualisasi + simpan
    print("\nMenyimpan dan menampilkan visualisasi rute...")
    plot_route(coords, best_route, save_path="output/best_route.png")


if __name__ == "__main__":
    main()
