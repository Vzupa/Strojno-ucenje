# Naloga3 - Klasifikacija (strukturirani podatki)
Za izdelavo te naloge uporabite podatke iz prejšnje naloge (university_rank_2020.csv, university_rank_other.csv, university_rank_students.xlsx). Vse podatke iz teh datotek ponovno naložite in jih nato združite v en DataFrame, poimenovan df, z indeks stolpcem University.

1. Izpišite:
- koliko vrstic in stolpcev ima ta združen df,
- kakšnega tipa so posamezni stolpci,
- prvih 5 vrstic in
- koliko je manjkajočih podatkov v posameznem stolpcu.
2. Vse manjkajoče vrednosti v številskih stolpcih nadomestite s povprečjem stolpca (pri tem si pomagajte s knjižnico sklearn). Ponovno izpišite koliko je manjkajočih podatkov v posameznem stolpcu.

3. Kategorične oz. nominalne vrednosti nadomestite z najpogostejšimi vrednostmi stolpca (pri tem si pomagajte s knjižnico sklearn). Ponovno izpišite koliko je manjkajočih podatkov v posameznem stolpcu.

4. Podatke brez manjkajočih vrednosti shranite v .csv datoteko poimenovano university_rank_no_nan.csv. Stolpci naj bodo ločeni z vejico, decimalna števila pa zapisana s piko.

5. Podatke razdelite na učno in testno množico. Vhod v vaš klasifikacijski algoritem naj predstavljajo vsi številski stolpci. Napovedovali boste vrednost International_Outlook. Testna množica naj bo velikosti 25%, random_state pa 123.

6. Kot klasifikacijski algoritem uporabite odločitveno drevo, ki ga naučite na učnimi podatki in nato napovejte rezultat za testno množico. Izpišite prve štiri napovedane vrednosti in točnost napovedi. 

7. Da preverite kako dobre napovedi je podal zgrajen model izpišite še vsaj tri druge metrike s katerimi lahko ovrednotimo rezultate. K vsaki uporabljeni metriki dodajte tudi komentar, v katerem zapišete kaj nam ta metrika pove.

8. Izrišite graf, ki bo prikazoval v kakšnem razmerju so si vrednosti International_Outlook in Teaching (namig: catplot).

9. Ponovite cel postopek klasifikacije, le da zdaj kot vhod uporabite številske podatke brez stolpca Teaching. Izpišite kakšna je v tem primeru točnost klasifikacije.

10. S pomočjo navzkrižne validacije z osmimi rezi, z optimizacijo metrike točnosti, preizkusite naslednje klasifikatorje:

- Odločitveno drevo
- Logistična regresija
- Linearna metoda podpornih vektorjev
- K najbližjih sosedov
- Naivni Bayes z gaussovo porazdelitvijo
- Naključni gozd (Random forest)
- Ekstremni gozd (Extra trees)
- AdaBoost
- Gradient tree boosting  
Vhod naj predstavljajo vsi številski podatki, napovedujte pa vrednost International_Outlook.

11. Za vsak klasifikator rezultate izpišite v konzolo.

12. Izrišite stolpični graf v katerem prikažete rezultate točnosti vsakega klasifikatorja posebej. Pazite da bo graf pregleden (bodo vidna imena vseh klasifikatorjev, ...).

# Task3 - Classification (structured data)
To complete this task, use the data from the previous task (university_rank_2020.csv, university_rank_other.csv, university_rank_students.xlsx). Reload all the data from these files and then merge them into one DataFrame, named df, with the index column University.
1. Print:
- How many rows and columns does this merged df have,
- what type each column is,
- the first 5 rows and
- how much data is missing in each column.
2. Replace all missing values in the numeric columns by the column average (using the sklearn library). Write out again how many missing data are in each column.

3. Replace the categorical or nominal values by the most frequent values of the column (using the sklearn library). Write again how much data is missing in each column.

4. Save the data without missing values in a .csv file named university_rank_no_nan.csv. Columns should be separated by a comma and decimal numbers should be written as dots.

5. Split the data into training and test sets. All numeric columns should be input to your classification algorithm. You will predict the value of International_Outlook. The size of the test set should be 25% and the size of the random_state should be 123.

6. Use the decision tree learned from the training data as a classification algorithm and then predict the result for the test set. Write down the first four predicted values and the accuracy of the prediction.
7. To check how well the model has predicted, write down at least three other metrics that can be used to evaluate the results. For each metric used, add a commentary to say what the metric tells us.

8. Draw a graph showing the relationship between International_Outlook and Teaching (hint: catplot).

9. Repeat the whole classification process, but now using numerical data as input without the Teaching column. Write down what the classification accuracy is in this case.

10. Test the following classifiers using eight-cut cross-validation, optimising the accuracy metric:

- Decision tree
- Logistic regression
- Linear support vector method
- K nearest neighbours
- Naive Bayes with Gaussian distribution
- Random forest
- Extra trees
- AdaBoost
- Gradient tree boosting  
The input should be all numerical data and the prediction should be the International_Outlook value.

11. For each classifier, output the results to the console.

12. Plot a bar graph showing the accuracy results for each classifier separately. Make sure that the graph is clear (names of all classifiers are visible, etc.).
