# Naloga5 - Klasifikacija slik
1. Izpišite koliko je vseh slik v mapi data.

2. Izrišite graf na katerem prikažete koliko je slik v posamezni kategoriji oz. koliko slik pripada posameznemu razredu.

3. Preverite kakšne slike so shranjene v obstoječih mapah, tako da izpišete po 3 primerke za vsak posamezen razred.

4. Obstoječe podatke (iz mape data) razdelite v testni in validacijski dataset, glede na naključno stanje 123. Velikost učne množice naj bo 70%. Vsem slikam spremenite velikost na 120x120. Velikost serije (batch size) naj bo 25.

5. Prikažite še 15 slik s pripadajočimi razredi iz učne množice.

6. Izpišite kakšni so izhodni razredi slik iz prve serije (batch-a).

7. Nad slikami izvedite augmentacijo tako da jih obrnete glede na vertikalno os ter jih zavrtite in približate za vrednost 0,3. Augmentacijo lahko izvedete predhodna nad slikami, ali jo vključite v model. Pazite, da jo izvedete samo enkrat.

8. Standardizirajte podatke (standardizacijo lahko izvedete neposredno nad datasetom s slikami ali pa jo vključite kot samostojno raven v model).

9. Ustvarite Sequential model, ki bo vseboval dva bloka s konvolucijskimi nevronskimi mrežami. Prvi blok naj ima vrednost filters nastavljeno na 32, drugi pa na 64. kernel_size naj bo pri obeh 3, prav tako naj imata ob aktivacijsko funkcijo 'relu', vsakemu pa naj sledi raven MaxPooling2D. Za zadnjim MaxPooling-om dodajte Dropout raven z vrednostjo 0,2. Kot zadnji dodajte še Flatten in Dense raven.

10. Delovanje optimizirajte z optimizatorjem adam, za računanje loss funkcije uporabite SparseCategoricalCrossentropy ter merite točnost napovedi.

11. Izpišite podrobnosti modela.

12. Model učite na 20 iteracijah (epoch-ah).

13. V obliki grafa izpišite kako se je spreminjala točnost tekom posameznih iteracij nad učno in validacijsko množico.

14. Za vse slike, ki niso bile uporabljene v postopku učenja modela, preverite v katere razrede in s kakšno natančnostjo jih razvrsti uporabljena klasifikacija. Glede na število pravilno in nepravilno razvrščenih slik zapišite kako točna je bila klasifikacija.

# Task5 - Image classification
1. List how many images are in the data folder.

2. Draw a graph to show how many images are in each category or how many images belong to each class.

3. Check what images are stored in the existing folders by listing 3 instances for each class.

4. Divide the existing data (from the data folder) into a test dataset and a validation dataset, according to the random state 123. Resize all images to 120x120. The batch size should be 25.

5. Display 15 more images with the corresponding classes from the training set.

6. List the output classes of the images from the first batch.

7. Perform the augmentation on the images by rotating them with respect to the vertical axis and rotating and zooming them by 0.3. Make sure that you only do it once.

8. Standardise the data (standardisation can be performed directly on top of the image dataset or included as a separate level in the model).

9. Create a Sequential model containing two blocks with convolutional neural networks. The first block should have the filters value set to 32 and the second to 64. kernel_size should be set to 3 for both, they should also have a 'relu' function at activation, and each should be followed by a MaxPooling2D level. After the last MaxPooling, add a Dropout level with a value of 0.2. Add Flatten and Dense levels last.

10. Optimise the performance with the adam optimiser, use SparseCategoricalCrossentropy to compute the loss function and measure the accuracy of the prediction.

11. Write out the details of the model.

12. Train the model on 20 iterations (epochs).

13. Graph how the accuracy changed over the iterations over the training and validation sets.

14. For all the images that were not used in the model learning process, check which classes and with what accuracy the classification used classifies them. Given the number of correctly and incorrectly classified images, record how accurate the classification was.
