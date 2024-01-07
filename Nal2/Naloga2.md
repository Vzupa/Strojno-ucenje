# Naloga 2 - Pregled in vizualizacija podatkov

### 1. del
Na spletni strani Kaggle poiščite podatkovno zbirko .csv formata. To zbirko:

naložite v notebook ali .py dokument
izpišite koliko vrstic in stolpcev je v tej podatkovni zbirki
prikažite katerih tipov so podatki, shranjeni v tej datoteki
izpišite prve 4 vrstice
izpišite zadnjih 5 vrstic
izpišite opisno statistiko za vse številske stolpce
### 2. del
1. Naložite nasledenje podatke v nov notebook ali .py dokument: 

university_rank_2020.csv
university_rank_other.csv
university_rank_students.xlsx
Vsako datoteko naložite v svoj DataFrame. Vsaka datoteka ima svoje posebnosti. Pazite, da boste pregledali kaj je seperator v datotekah in kaj je decimalni znak pri vseh datotekah. Poskrbite, da bo index stolpec pri vseh ime univerze, da bo združevanje kasneje lažje.

2. Vse DataFrame-e združite v en DataFrame (poimenujte ga df).

3. Izpišite število vrstic in stolpcev, ki jih ima novo ustvarjeni df in preglejte kako izgleda prvih 10 vrstic.

4. Preverite koliko je manjkajočih podatkov v posameznem stolpcu.

5. Manjkajoče vrednosti za stolpec International_Outlook ročno dopolnite glede na stolpec Teaching - če je vrednost v posamezni vrstici za atribut Teaching:

  - < 20 - dopolnite stolpec International_Outlook z vrednostjo "bad"

  - \> 60  - dopolnite stolpec International_Outlook z vrednostjo "excellent"
vmesne vrednosti pa dopolnite z vrednostjo "good"
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
