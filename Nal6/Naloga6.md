# Naloga 6 - Tekstovna klasifikacija
V datoteki wineReviews.csv so objavljena ocene posameznih vin iz različnih držav. Namen te naloge je ugotoviti ali lahko glede na oceno vina, določimo iz katere države prihaja.

1. Preberite datoteko wineReviews.csv in izpišite prve tri ocene vin.

2. Izpišite iz katerih držav prihajajo ocenjena vina in koliko jih prihaja iz posamezne države.

3. Združite ocene vseh slovenskih vin v skupno besedilo. To besedilo:

- tokeniziraje in izpišite 8 tokenov, ki imajo najvišjo frekvenco pojavitve,
- izrišite graf, ki bo ponazoril, katerih 15 tokenov se največkrat pojavi v oceni slovenskih vin,
- iz besedila odstranite vse "stop words" (besede brez pomena in ločila) ter izmed preostalih tokenov izpišite 5 takšnih, ki imajo najvišjo frekvenco pojavitve,
- iz tako prečiščenega besedila izpišite 5 najpogostejših bigramov in trigramov.
4. V datafram-u ustvarite nov stolpec poimenovan processed, kamor shranite besedilo ocen (description), ki je:

- v celoti zapisano z malimi črkami,
- brez "stop words" (besede brez pomena in ločila),
- besede morajo biti krnjene (nad njimi uporabite stemming).
5. S pomočjo TfidfVectorizer razdelite predprocesirana besedila ocen (iz stolpca processed) na unigrame in izpišite koliko je vseh nastalih tokenov (features).

6. Nad tako pripravljenimi podatki uporabite klasifikacijski algoritem Support Vector Classification, s katerim napoveste v katero državo sodi vino glede na besedilo podane ocene. Učna množica naj zajema 70% vseh podatkov, naključno stanje pa naj bo 789. Izpišite točnost klasifikacije.

7. Enak postopek klasifikacije ponovite še nad bigrami in trigrami. Primerjajte točnosti klasifikacije.

8. Za konec vzemite še neprečiščeno besedilo ocen iz stolpca description. Predprocesirajte ga z uporabo TfidfVectorizer in ga razdelite na unigrame. Nad njim izvedite klasifikacijo z enakim algoritmom, enako delitvijo učnih/testih podatkov, in enakim izhodnim razredom kot v prejšnjih točkah. Točnost klasifikacije primerjajte s tisto iz 6. točke.

# Task 6 - Text classification
The wineReviews.csv file contains ratings of individual wines from different countries. The purpose of this task is to see if we can determine which country a wine comes from based on its rating.

1. Read the wineReviews.csv file and list the first three wine ratings.

2. List which countries the rated wines come from and how many wines come from each country.

3. Combine the ratings of all Slovenian wines into a common text. This text:

- tokenize and list the 8 tokens that have the highest frequency of occurrence,
- draw a graph to illustrate which 15 tokens appear most frequently in the rating of Slovenian wines,
- remove all "stop words" (words with no meaning or punctuation) from the text, and out of the remaining tokens, list the 5 that have the highest frequency of occurrence,
- extract the 5 most frequent bigrams and trigrams from the text thus refined.
4. In the dataframe, create a new column called processed, where you store the text of the evaluation (description), which is:

- in full lower case,
- without "stop words" (words without meaning and punctuation),
- the words must be contracted (use stemming above them).
5. Using TfidfVectorizer, split the preprocessed text of the ratings (from the processed column) into unigrams and print out how many of the resulting tokens (features) there are.

6. Over this data, use the Support Vector Classification algorithm to predict which country the wine belongs to, given the text of the given rating. The training set should cover 70% of the data and the random state should be 789. Write down the classification accuracy.

7. Repeat the same classification procedure on bigrams and trigrams. Compare the classification accuracies.

8. Finally, take the raw text of the estimates from the description column. Preprocess it using TfidfVectorizer and split it into unigrams. Over it, perform classification with the same algorithm, the same splitting of training/test data, and the same output class as in the previous sections. Compare the accuracy of the classification with that of point 6.



