import matplotlib.pyplot as plt
import os

def plot_route(coords, route, save_path=None):
    xs = [coords[i][0] for i in route] + [coords[route[0]][0]]
    ys = [coords[i][1] for i in route] + [coords[route[0]][1]]

    plt.figure(figsize=(8, 6))
    
    # Titik kota
    for i, (x, y) in enumerate(coords):
        plt.scatter(x, y)
        plt.text(x + 0.015, y + 0.015, str(i), fontsize=9)

    # Garis rute
    plt.plot(xs, ys, linewidth=1.5)

    plt.title("Visualisasi Rute TSP")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    # === SAVE GAMBAR JIKA DIMINTA ===
    if save_path:
        folder = os.path.dirname(save_path)
        if folder != "" and not os.path.exists(folder):
            os.makedirs(folder)
        plt.savefig(save_path, dpi=300)
        print(f"Gambar berhasil disimpan: {save_path}")

    # Tampilkan grafik
    plt.show()
