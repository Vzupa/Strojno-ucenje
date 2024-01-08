# Projekt
Pri analizi vremenskih podatkov z ARSO sem začel z zapisi iz leta 2001, ki zajemajo temperaturo, tlak, vlažnost in veter. Začetna faza mojega projekta je vključevala strogo čiščenje podatkov, ki je vključevalo odstranitev vrstic z vsemi ničelnimi vrednostmi in interpolacijo manjkajočih podatkov za ohranitev celovitosti podatkov.

S poudarkom na predobdelavi sem svoj pristop prilagodil tako, da sem posebej obravnaval nianse podatkov o temperaturi, vlažnosti, tlaku in padavinah. Pri modeliranju sem uporabil linearno regresijo, regresijo odločitvenega drevesa in Random Forest regressor, pri čemer sem poudaril ključno vlogo različnih značilnosti pri napovedovanju temperature.

Nabor podatkov sem spremenil tako, da sem na podlagi preteklih podatkov napovedal temperaturo, in podatke združil v različne časovne intervale - 6-urne, 12-urne in 24-urne - da bi analiziral vpliv časa na napovedovanje temperature. Uspešnost teh modelov je bila ocenjena z matrikami, kot so R², MSE in RMSE. 

Modela 12-urnega in 24-urnega intervala sta se izkazala za najučinkovitejša, medtem ko je model odločitvenega drevesa pokazal slabo učinkovitost, kar je pokazala negativna ocena R². Moj projekt ponazarja podroben in sistematičen pristop k napovedovanju temperature z uporabo podatkov o časovnih vrstah.
# Project
In my analysis of weather data from ARSO, I started with records dating back to 2001, encompassing temperature, pressure, humidity, and wind parameters. The initial phase of my project involved rigorous data cleaning, which included the removal of rows with all null values and interpolating missing data to maintain data integrity.

Focusing on preprocessing, I tailored my approach to specifically address the nuances of temperature, humidity, pressure, and precipitation data. For the modeling aspect, I employed Linear Regression, Decision Tree Regression, and Random Forest Regressor, highlighting the critical role of various features in predicting temperature.

I modified the dataset to specifically predict temperature based on historical data and aggregated the data into different time intervals - 6-hour, 12-hour, and 24-hour - to analyze the impact of time on temperature prediction. The performance of these models was evaluated using metrics such as R², MSE, and RMSE. The 12-hour and 24-hour interval models emerged as the most effective, while the decision tree model showed poor performance, indicated by a negative R² score. My project exemplifies a detailed and systematic approach to temperature prediction using time-series data.
