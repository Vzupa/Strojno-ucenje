# Naloga 7 - Regresija

Za to nalogo uporabite podatke iz že ustvarjene datoteke university_rank_no_nan.csv.

1. V tej datoteki naj ne bi bilo več manjkajočih podatkov, jih je pa potrebno še prilagoditi. Zato kategorične podatke zamenjajte z indikacijskimi parametri (dummy vrednostmi), številske stolpce (razen Score_Result) pa standardizirajte. Score_Result bomo kasneje uporabili kot izhodni razred.

2. Množico razdelite na učno in testno tako, da bo testna množica velika 30%, ostali podatki pa naj bodo uporabljeni za učno množico. Naključno stanje naj bo 789. Napovedovali bomo podatek Score_Result. Za vhodne podatke uporabite vse stolpce razen izhodnega razreda in stolpca Rank. Za algoritem uporabite linearno regresijo.

3. Ustvarite dataframe, katerega prvi stolpec bodo predstavljale dejanske vrednosti, drugi stolpec pa napovedane vrednosti modela. Izpišite prvih 5 vrstic tega datafram-a.

4. Podatke iz datafram-a izrišite v obliki grafa z dvema krivuljama - ena krivulja naj predstavlja dejanske vrednosti, druga krivulja pa napovedane vrednosti.

5. Kako dobro model napove vrednosti preverite še s tremi metrikami: srednjo absolutno napako, srednjo kvadratno napako in odstotkom razložene variance. Poleg vsake metrike v komentar na kratko zapišite kaj z njo merimo in kakšna mora biti njena vrednost (čim višja/čim manjša), da vemo da je naučeni model dober.

6. Ponovite regresijo iz 2. točke, le da zdaj za vhodne podatke uporabite vse stolpce razen izhodnega razreda ter stolpcev Rank, Teaching, Research in Citations. Primerjajte v katerem primeru dobite boljše rezultate.

7. Podatke razdelite na učno in testno množico s pomočjo navzkrižne validacije (KFold) s petimi rezi. Še vedno napovedujete Score_Result, kot vhodne podatke pa uporabite tisto kombinacijo, ki je prej dala boljše rezultate. Merite srednjo absolutno napako. S pomočjo te navzkrižne validacije preizkusite naslednje regresijske algoritme: 

- linearno regresijo, 
- regresijsko drevo,
- regresijo z linearno metodo podpornih vektorjev, 
- regresor naključnega gozda in 
- ExtraTreesRegressor.
8. Izrišite graf, ki bo prikazal srednjo absolutno napako za vse uporabljene algoritme.

9. S pomočjo iskanja po mreži poiščite najboljše nastavitve parametrov za regresor naključnega gozda. Pri iskanju naj preizkusi naslednje kombinacije vrednosti parametrov: n_estimators ={50, 100, 200}, criterion = {“se”, “ae”}, max_depth = {5, 10, 15} in max_features = {"None", “sqrt”, “log2”}. Pri deljenju na folde uporabite 10 rezov, meri pa se naj R^2 score. Izpišite najboljše nastavitve parametrov in najboljši rezultat.

# Task 7 - Regression

For this task, use the data from the already created file university_rank_no_nan.csv.

1. There should be no more missing data in this file, but it still needs to be adjusted. Therefore, replace the categorical data with indicator parameters (dummy values) and standardise the numeric columns (except Score_Result). Score_Result will be used as an output class later.

2. Divide the training set and the test set so that the test set is 30% large and the rest of the data should be used for the training set. The random state should be 789. We will predict the Score_Result data. Use all columns except the output class and the Rank column as input data. Use linear regression for the algorithm.

3. Create a dataframe with the first column representing the actual values and the second column representing the predicted values of the model. Print out the first 5 rows of this dataframe.

4. Plot the data from the dataframe as a graph with two curves - one curve should represent the actual values and the other curve should represent the predicted values.

5. Check how well the model predicts the values using three more metrics: mean absolute error, root mean square error and percentage of explained variance. Next to each metric, write briefly in the commentary what it measures and what its value should be (as high/as low as possible) to know that the learned model is good.

6. Repeat the regression from point 2, but now using all columns as inputs except the output class and the columns Rank, Teaching, Research and Citations. Compare in which case you get better results.

7. Split the data into training and test sets using five-slice cross-validation (KFold). You are still predicting Score_Result, but use as input the combination that gave better results earlier. Measure the mean absolute error. Using this cross-validation, test the following regression algorithms: 

- linear regression, 
- regression tree,
- regression with the linear support vector method, 
- random forest regressor, and 
- ExtraTreesRegressor.
8. Plot a graph showing the mean absolute error for all the algorithms used.

9. Using grid search, find the best parameter settings for the Random Forest Regressor. Try the following combinations of parameter values: n_estimators = {50, 100, 200}, criterion = {"se", "ae"}, max_depth = {5, 10, 15} and max_features = {"None", "sqrt", "log2"}. When dividing into folds, use 10 cuts and the R^2 score should be measured. Write down the best parameter settings and the best score.
