# Naloga 4 - Pretvorba podatkov in optimizacija parametrov
Za izdelavo te naloge uporabite podatke iz prejšnje naloge, ki ste jim odstranili manjkajoče vrednosti (university_rank_no_nan.csv). Preverite, da ima ta datoteka pravilne vrednosti (so bili DataFrami pravilno združeni, in so bile vse manjkajoče vrednosti dopolnjene).

1. Ustvarite nov stolpec Status. Vse univerzitete, ki imajo Rank:

- manjši od 200, naj imajo status prestigious (prestižne),
- večji od 200 in manjši od 300, naj imajo status reputable (ugledne),
- večji od 300 in manjši od 430, naj imajo status average (povprečne),
- večji od 430, naj imajo status badReputation (slab sloves).  
Pazite da zajamete tudi mejne vrednosti. Na koncu preverite, da ne obstajajo nobene manjkajoče vrednosti. Izpišite prvih 5 vrstic.

2. Izrišite graf, ki bo prikazoval, koliko je univerz s posameznim statusom.

3. Preverite kakšen status sta dobili slovenski univerzi.

4. Izdelajte klasifikacijo, ki bo napovedovala Status univerze. Postopek klasifikacije ponovite dvakrat. 

- Pri prvi izvedbi:

  - Ustvarite kopijo df in jo poimenujte df1.
  - Kategorične (nominalne) podatke iz df1 pretvorite v številske s pomočjo LabelEncoder. Pazite da ne pretvorite tudi podatkov izhodnega razreda.
  - Številske podatke standardizirajte.
  - Uporabite klasifikacijski algoritem nad prilagojenimi podatki iz df1.
  - Izpišite točnost klasifikacije.
- Pri drugi izvedbi:

  - Ustvarite kopijo df in jo poimenujte df2.
  - Kategorične (nominalne) podatke iz df2 pretvorite v indikacijske parametre (dummy variable). Pazite da ne pretvorite tudi podatkov izhodnega razreda.
  - Številske podatke standardizirajte.
  - Uporabite klasifikacijski algoritem nad prilagojenimi podatki iz df2.
  - Izpišite točnost klasifikacije.  
- V obeh primerih za vhodne podatke uporabite vse podatke razen izhodnega razreda, Rank in Score_Result.
  - Uporabite algoritem naključnega gozda, sestavljen iz 50 dreves.
  - Za testno množico uporabite 25% podatkov, naključno stanje pa naj bo 789.  
Primerjajte točnosti obeh izvedb.
5. Poiščite najboljše nastavitve parametrov za algoritem naključnega gozda s pomočjo naključnega iskanja. Pri tem upoštevajte naslednje:

- Uporabljena mora biti navzkrižna validacija s petimi rezi. 
- Za ocenjevanje naj bo uporabljena metrika točnosti.
- Uporabljeni naj bodo enaki vhodni in izhodni podatki kot pri 4. točki.
- Za podatke uporabite tisti df, ki namesto kategoričnih vrednosti vsebuje indikacijske parametre.
- Iskanje omejite na 50 iteracij.
- Pri tem iskanju preizkusite naslednje vrednosti parametrov:
  - n_estimators = naključne diskretne vrednosti iz uniformne porazdelitve med 2 in 1500,
  - max_depth = naključne diskretne vrednosti iz uniformne porazdelitve med 2 in 50,
  - criterion = gini, entropy,
  - max_features = auto, sqrt, log2
6. Izpišite najboljše vrednosti parametrov, najboljši rezultat in kodo za najboljšo kombinacijo parametrov.

# Task 4 - Data conversion and parameter optimisation
To complete this task, use the data from the previous task with the missing values removed (university_rank_no_nan.csv). Check that this file has the correct values (the DataFrames have been merged correctly, and any missing values have been filled in).

1. Create a new Status column. All universities that have Rank:

- less than 200 should have a status of prestigious,
- greater than 200 and less than 300 should have the status Reputable,
- greater than 300 and less than 430 should have a status of average,
- greater than 430, should have badReputation status.  
Be sure to capture the thresholds as well. Finally, check that there are no missing values. Write out the first 5 rows.

2. Draw a graph showing how many universities have each status.

3. Check what status the two Slovenian universities have been given.

4. Make a classification that predicts the status of the university. Repeat the classification process twice. 

- The first time:

  - Create a copy of df and name it df1.
  - Convert the categorical (nominal) data from df1 into numeric data using LabelEncoder. Be careful not to convert the output class data as well.
  - Standardise the numeric data.
  - Apply the classification algorithm over the adjusted data from df1.
  - Write out the classification accuracy.
- For the second implementation:

  - Create a copy of df and name it df2.
  - Convert the categorical (nominal) data from df2 to dummy variable parameters. Be careful not to convert the output class data as well.
  - Standardise the numeric data.
  - Apply the classification algorithm over the adjusted df2 data.
  - Write down the classification accuracy.  
- In both cases, use all data except the output class, Rank and Score_Result as input data.
  - Use a random forest algorithm consisting of 50 trees.
  - Use 25% of the data as the test set and the random state should be 789.  
Compare the accuracies of the two implementations.
5. Find the best parameter settings for the random forest algorithm using random search. Consider the following:

- Five-cut cross-validation should be used. 
- The accuracy metric should be used for the evaluation.
- The same input and output data should be used as for point 4.
- For the data, use a df that contains indicator parameters instead of categorical values.
- Limit the search to 50 iterations.
- For this search, test the following parameter values:
  - n_estimators = random discrete values from a uniform distribution between 2 and 1500,
  - max_depth = random discrete values from a uniform distribution between 2 and 50,
  - criterion = gini, entropy,
  - max_features = auto, sqrt, log2
6. Write down the best values of the parameters, the best result and the code for the best combination of the parameters.
