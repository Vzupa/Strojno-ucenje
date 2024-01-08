# Naloga 8 - Gručenje

Za izdelavo te naloge uporabite datoteko university_rank_no_nan.csv.

1. Naložite podatke iz datoteke v dataframe. Iz njega odstranite vse kategorične podatke. Številske podatke standardizirajte. Za nadaljnje analize boste potrebovali samo številske podatke.

2. Da dobite približen vpogled na koliko gruč bi bilo najbolj optimalno deliti instance uporabite hierarhično gručenje in izrišite dendrogram z maksimalno delitvijo na 5 nivojev.

3. Izvedite gručenje z uporabo K-means algoritma. Algoritem naj razdeli instance v dve gruči. Izpišite koliko je instanc v posamezni gruči.

4. Naredite analizo koliko je optimalno število gruč pri uporabi K-means algoritma (preizkusite delitev na do 10 gruč) in izrišite graf po metodi komolca. Zapišite na koliko gruč je po vašem mnenju najbolj smiselno razdeliti instance.

5. S pomočjo PCA transformacije naredite dva nova stolpca. Vrednosti iz teh dveh stolpcev prikažite v grafu raztrosa. Instance naj bodo obarvane glede na to, v katero gručo jih je razvrstil K-means algoritem. Uporabite rezultate k-means algoritma, ki po vašem mnenju razdeli instance v najbolj optimalno število gruč (iz 4. točke).

6. Naredite novo transformacijo številskih (še ne transformiranih podatkov) s pomočjo algoritma FastICA, s katero ustvarite dva nova stolpca . Na enak način kot v prejšnji točki izrišite graf raztrosa, le da tu uporabite vrednosti teh dveh novih stolpcev.

7. Nad transformiranimi podatki iz 5. točke (z algoritmom PCA) izvedite gručenje z dvema poljubnima algoritmoma gručenja (npr. Birch, SpectralClustering, ...). Algoritmom, ki zahtevajo predhodno določitev števila gruč, določite to število glede na najdeno optimalno vrednost iz 4. točke. Za oba izrišite graf raztrosa z obarvanimi instancami glede na pripadajočo gručo.

# Task 8 - Clustering

Use the file university_rank_no_nan.csv to complete this task.

1. Load the data from the file into a dataframe. Remove all categorical data from it. Standardise the numeric data. For further analysis you will only need the numerical data.

2. To get an approximate idea of how many clusters it would be optimal to divide the instances into, use hierarchical clustering and draw a dendrogram with a maximum division into 5 levels.

3. Perform the clustering using the K-means algorithm. The algorithm should divide the instances into two clusters. List how many instances are in each cluster.

4. Make an analysis of what is the optimal number of clusters when using the K-means algorithm (test splitting into up to 10 clusters) and draw a graph using the elbow method. Write down how many clusters you think it makes the most sense to split the instances into.

5. Using the PCA transformation, create two new columns. Plot the values from these two columns in a scatter plot. The instances should be coloured according to which cluster the K-means algorithm has grouped them into. Use the results of the k-means algorithm that you think splits the instances into the most optimal number of clusters (from point 4).

6. Make a new transformation of the numerical data (not yet transformed) using the FastICA algorithm to create two new columns. Plot the scatter plot in the same way as in the previous point, except that here you use the values of these two new columns.

7. Over the transformed data from point 5 (with the PCA algorithm), perform clustering with two arbitrary clustering algorithms (e.g. Birch, SpectralClustering, ...). For algorithms that require a predefined number of clusters, determine this number according to the optimal value found in point 4. For both of them, draw a scatter plot with the instances coloured according to the corresponding cluster.
