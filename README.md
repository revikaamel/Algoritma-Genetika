## Deskripsi Proyek
Project ini merupakan implementasi **Algoritma Genetika (Genetic Algorithm)** untuk menyelesaikan permasalahan **Traveling Salesman Problem (TSP)**.

Traveling Salesman Problem adalah masalah optimasi yang bertujuan untuk mencari **rute terpendek** yang harus ditempuh oleh seorang salesman untuk mengunjungi seluruh kota **hanya satu kali** dan kembali ke kota awal.

Algoritma Genetika digunakan karena mampu mencari solusi optimal atau mendekati optimal melalui proses evolusi yang meniru mekanisme **seleksi alam**, seperti **seleksi, crossover, dan mutasi**.

Project ini dibuat sebagai bagian dari praktikum **Artificial Intelligence / Machine Learning**.

---

# Konsep Traveling Salesman Problem (TSP)

Traveling Salesman Problem adalah salah satu masalah klasik dalam bidang **optimasi kombinatorial**.

Tujuan dari TSP adalah:

- Mengunjungi seluruh kota yang ada
- Setiap kota hanya dikunjungi satu kali
- Menemukan **total jarak perjalanan paling pendek**
- Kembali ke kota awal

Permasalahan ini sering digunakan dalam berbagai bidang seperti:

- Optimasi rute logistik
- Pengiriman barang
- Perencanaan transportasi
- Penjadwalan

---

# Algoritma Genetika

Algoritma Genetika adalah algoritma pencarian berbasis **evolusi biologis**.

Algoritma ini bekerja dengan konsep:

- Populasi
- Seleksi
- Crossover
- Mutasi
- Fitness Function

Melalui beberapa generasi, solusi akan semakin baik hingga mendekati solusi optimal.

---

# Tahapan Algoritma

Proses Algoritma Genetika dalam menyelesaikan TSP:

1. **Inisialisasi Populasi**

   Membuat beberapa rute awal secara acak sebagai populasi awal.

2. **Evaluasi Fitness**

   Menghitung total jarak dari setiap rute.

   Fitness biasanya dihitung dengan rumus:

   ```
   fitness = 1 / total_jarak
   ```

   Semakin pendek jarak, semakin tinggi nilai fitness.

3. **Seleksi**

   Memilih individu terbaik dari populasi untuk menjadi induk.

4. **Crossover**

   Menggabungkan dua parent untuk menghasilkan offspring (anak).

5. **Mutasi**

   Mengubah sebagian gen untuk menjaga keberagaman populasi.

6. **Generasi Baru**

   Populasi baru dibentuk dari hasil seleksi, crossover, dan mutasi.

7. **Iterasi**

   Proses diulang hingga mencapai jumlah generasi tertentu atau solusi terbaik ditemukan.

---

# Representasi Solusi

Setiap solusi direpresentasikan sebagai **urutan kota**.

Contoh kromosom:

```
[A, C, B, D, E]
```

Artinya:

Salesman akan mengunjungi kota:

```
A → C → B → D → E → kembali ke A
```

---

# Parameter Algoritma

Beberapa parameter penting dalam Algoritma Genetika:

| Parameter | Nilai |
|----------|------|
| Population Size | 100 |
| Mutation Rate | 0.01 |
| Crossover Rate | 0.8 |
| Generations | 500 |

Parameter ini dapat diubah untuk mendapatkan performa yang lebih baik.

---

# Alur Sistem

Alur kerja program:

```
Inisialisasi Populasi
        ↓
Hitung Fitness
        ↓
Seleksi Parent
        ↓
Crossover
        ↓
Mutasi
        ↓
Populasi Baru
        ↓
Evaluasi Generasi
        ↓
Solusi Rute Terbaik
```

---

# Hasil yang Diharapkan

Setelah proses evolusi selesai, algoritma akan menghasilkan:

- Rute perjalanan terbaik
- Total jarak minimum
- Visualisasi rute antar kota

Contoh output:

```
Best Route:
A → C → D → B → E → A

Total Distance:
215 km
```

---

# Kesimpulan

Algoritma Genetika dapat digunakan untuk menyelesaikan **Traveling Salesman Problem** dengan pendekatan optimasi berbasis evolusi.

Melalui proses seleksi, crossover, dan mutasi, algoritma mampu menghasilkan rute perjalanan yang mendekati optimal dalam jumlah generasi tertentu.

Pendekatan ini efektif digunakan untuk masalah optimasi yang memiliki **ruang pencarian yang sangat besar**.

3. Russell & Norvig (2010). Artificial Intelligence: A Modern Approach
