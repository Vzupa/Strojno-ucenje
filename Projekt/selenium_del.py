import os
import time
from datetime import datetime, timedelta

from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
import pandas as pd

import xpathData


zacetek_datum = '2023-11-23'
# zacetek_datum = '2001-05-03'
koliko_dni_naprej = 29

# podatki = [xpathData.xpath_spremenljivke, xpathData.headers, "podatki_vreme_1_1.csv"]
podatki = [xpathData.xpath_spremenljivke2, xpathData.headers2, "podatki_vreme_2.csv"]


def izracunaj_datum(zacetni_datum, plus_dni):
    prvi_date = datetime.strptime(zacetni_datum, '%Y-%m-%d')
    drugi_date = prvi_date + timedelta(days=plus_dni)

    comparison_date = datetime.strptime("2023-12-22", '%Y-%m-%d')
    if drugi_date > comparison_date:
        drugi_date = comparison_date

    return drugi_date.strftime('%Y-%m-%d')


def klikni(kaj_klikno, xpath, cas_spanje):
    time.sleep(cas_spanje)
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    button.click()
    print(f"Kliknil {kaj_klikno}")


def poklikaj(items, cas_spanje):
    for item in items:
        klikni(item["ime"], item["xpath"], cas_spanje)


def vnesi_datum(xpath, datum):
    input_datum = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )

    input_datum.clear()
    input_datum.send_keys(datum)
    print(f"Vnesel {datum}")


def vnesi_datume():
    global zacetek_datum
    konec_datum = izracunaj_datum(zacetek_datum, koliko_dni_naprej)

    vnesi_datum(xpathData.xpath_inputi[0], zacetek_datum)
    vnesi_datum(xpathData.xpath_inputi[1], konec_datum)
    klikni("Poizvedi", xpathData.xpath_poizvedi, 0)

    zacetek_datum = izracunaj_datum(zacetek_datum, koliko_dni_naprej + 1)


def obdelaj_shrani(rows):
    cleaned_data_list = [item.replace('\xa0', '') for item in rows]
    # print(cleaned_data_list)

    data_chunks = [cleaned_data_list[i:i+8] for i in range(0, len(cleaned_data_list), 8)]
    data_chunks = [chunk for chunk in data_chunks if any(item.strip() for item in chunk)]
    print(data_chunks[-5:])

    df = pd.DataFrame(data_chunks, columns=podatki[1])

    file_exists = os.path.isfile(podatki[2])
    df.to_csv(podatki[2], mode='a' if file_exists else 'w', index=False, header=not file_exists)
    time.sleep(60)


def preberi_podatke():
    time.sleep(20)
    html_content = driver.page_source
    selector = Selector(text=html_content)

    obdelaj_shrani(selector.xpath(xpathData.xpath_tabela).xpath('.//td/text()').getall()[4:])

    print("Prebral podatke")


def glavni_loop():
    poklikaj(xpathData.xpath_postaje, 2)

    preberi_podatke()
    klikni("nazaj", xpathData.xpath_nazaj, 2)
    vnesi_datume()


def pridi_do_podatkov():
    poklikaj(xpathData.gumbi_zacetek, 2)
    vnesi_datume()
    poklikaj(podatki[0], 0)
    while True:
        try:
            glavni_loop()
        except UnexpectedAlertPresentException as e:
            input("VLADA NECE DAT PODATKOV")
            time.sleep(30)
            glavni_loop()


chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

url = 'https://meteo.arso.gov.si/met/sl/app/webmet/'
driver.get(url)
try:
    pridi_do_podatkov()
    input("Konec?")
finally:
    driver.quit()
