# Naloga 2 - Pregled in vizualizacija podatkov

### 1. del
Na spletni strani Kaggle poiščite podatkovno zbirko .csv formata. To zbirko:

- naložite v notebook ali .py dokument
- izpišite koliko vrstic in stolpcev je v tej podatkovni zbirki
- prikažite katerih tipov so podatki, shranjeni v tej datoteki
- izpišite prve 4 vrstice
- izpišite zadnjih 5 vrstic
- izpišite opisno statistiko za vse številske stolpce
### 2. del
1. Naložite nasledenje podatke v nov notebook ali .py dokument: 
- university_rank_2020.csv
- university_rank_other.csv
- university_rank_students.xlsx  
Vsako datoteko naložite v svoj DataFrame. Vsaka datoteka ima svoje posebnosti. Pazite, da boste pregledali kaj je seperator v datotekah in kaj je decimalni znak pri vseh datotekah. Poskrbite, da bo index stolpec pri vseh ime univerze, da bo združevanje kasneje lažje.

2. Vse DataFrame-e združite v en DataFrame (poimenujte ga df).

3. Izpišite število vrstic in stolpcev, ki jih ima novo ustvarjeni df in preglejte kako izgleda prvih 10 vrstic.

4. Preverite koliko je manjkajočih podatkov v posameznem stolpcu.

5. Manjkajoče vrednosti za stolpec International_Outlook ročno dopolnite glede na stolpec Teaching - če je vrednost v posamezni vrstici za atribut Teaching:

  - < 20 - dopolnite stolpec International_Outlook z vrednostjo "bad"

  - \> 60  - dopolnite stolpec International_Outlook z vrednostjo "excellent"
  - vmesne vrednosti pa dopolnite z vrednostjo "good"
6. Manjkajoče vrednosti v ostalih stolpcih dopolnite s povprečjem stolpca.

7. Izpišite koliko je univerz v posamezni državi.

8. Izpišite vse univerze, ki se nahajajo v Sloveniji.

9. Ustvarite nov stolpec poimenovan Staff Skills, ki se naj izračuna kot vsota stolpcev Teaching in Research, deljeno z 2  (Teaching + Research/ 2). Izpišite prvih pet vrstic in preverite izračunane vrednosti.

10. Izbrišite stolpec Staff Skills.

11. DataFrame df shranite v csv kot "university_rank.csv" s seperatorjem ; in decimalnim znakom pika.

12. Izpišite tabelo petih univerz z največjim Rank-om, sortirano od največje vrednosti, do najmanjše.

13. Izrišite boxplot za stolpec Citations.

14. Izrišite graf, ki bo prikazal koliko univerzitet je razvrščenih v posamezno kategorijo glede na stolpec International_Outlook.

15. Izrišite vertikalni histogram brez črte, za vrednost Research.

16. Izrišite graf raztrosa za vrednost Number_students in Score_Result, ločen glede na kategorijo International_Outlook in obarvan glede na državo.

17. Izrišite graf korelacij (heatmap) vseh številskih spremenljivk.

18. Izrišite barplot, kjer prikažete povprečje Industry_Income glede na državo univerze, spremenite barve v odtenke modre.

# Task 2 - Data review and visualisation

### Part 1
On the Kaggle website, find the database in .csv format. This database:

- upload to a notebook or .py document
- list how many rows and columns are in this database
- show which types of data are stored in this file
- print out the first 4 rows
- print the last 5 rows
- print descriptive statistics for all numeric columns
### Part 2
1. Upload these files into a new notebook or .py document: 
- university_rank_2020.csv
- university_rank_other.csv
- university_rank_students.xlsx  
Upload each file to your DataFrame. Each file has its own specifics. Make sure you check what the separator is in the files and what the decimal point is in all files. Make sure that the index column in all of them is the name of the university to make merging easier later.

2. Merge all DataFrames into one DataFrame (call it df).

3. List the number of rows and columns the newly created df has and check how the first 10 rows look.

4. Check how much data is missing in each column.
5. Manually fill in the missing values for the International_Outlook column according to the Teaching column - if there is a value in each row for the Teaching attribute:
  - < 20 - complete the International_Outlook column with the value "bad"
  - \> 60 - populate the International_Outlook column with the value "excellent"
  - and the intermediate values are filled with the value "good"
6. Fill in the missing values in the other columns with the average of the column.
7. List how many universities there are in each country.

8. List all the universities located in Slovenia.

9. Create a new column called Staff Skills, which should be calculated as the sum of the columns Teaching and Research divided by 2 (Teaching + Research/ 2). Print out the first five rows and check the calculated values.

10. Delete the Staff Skills column.

11. Save the DataFrame df in csv as "university_rank.csv" with separator ; and decimal point.

12. Print a table of the five universities with the highest Rank, sorted from the highest value to the lowest.

13. Print a boxplot for the Citations column.

14. Print a graph showing how many universities are ranked in each category according to the International_Outlook column.

15. Plot a vertical histogram without a line for the value Research.

16. Draw a scatter plot for Number_students and Score_Result, separated by International_Outlook category and coloured by country.

17. Plot the correlations (heatmap) for all numeric variables.

18. Draw a barplot showing the average Industry_Income by country of the university, changing the colours to shades of blue.
