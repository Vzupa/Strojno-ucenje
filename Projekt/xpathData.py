gumbi_zacetek = [
    {
        "xpath": "//td[normalize-space(.)='Arhiv']",
        "ime": "arhiv"
     },
    {
        "xpath": "//td[@class='link-table']//p[contains(text(), 'Sprejmem')]",
        "ime": "sprejem"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr"
                 "/td/div/table/tbody/tr[5]/td/div/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td[1]"
                 "/fieldset/div/table/tbody/tr[2]/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td/img[5]",
        "ime": "obdobje"
    }
]

xpath_poizvedi = ("/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                  "div/table/tbody/tr[5]/td/div/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td[2]/table/"
                  "tbody/tr/td/div")

xpath_inputi = [
    '/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/'
    'tbody/tr/td/div/table/tbody/tr[5]/td/div/div[1]/table/tbody/tr[2]/td/div/table/tbody/'
    'tr[3]/td[1]/fieldset/div/table/tbody/tr[2]/td[2]/div/input',
    '/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody'
    '/tr/td/div/table/tbody/tr[5]/td/div/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td[1]'
    '/fieldset/div/table/tbody/tr[2]/td[4]/div/input'
]

xpath_spremenljivke = [
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/img[5]",
        "ime": "meteoroloske spremenljivke"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "povprecen zracni tlak"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[4]/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "terminska temperatura zraka na 2m"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[5]/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "povprecna temperatura zraka na 2m"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[8]/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "terminska relativna vlaga"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[9]/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "povprecna relativna vlaga"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "kolicina padavin"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "povprecna hitrost vetra"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "povprecna smer vetra"
    }
]

xpath_spremenljivke2 = [
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/img[5]",
        "ime": "meteoroloske spremenljivke"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/div"
                 "/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/div/"
                 "table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "minimalen zracni tlak"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "maksimalen zracni tlak"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[6]/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "minimalna temperatura zraka na 2m"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[7]/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "maksimalna temperatura zraka na 2m"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "minimalna relativna vlaga"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "maksimalna relativna vlaga"
    },
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/"
                 "div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td/div/fieldset/"
                 "div/table/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td/img[1]",
        "ime": "maksimalna hitrost vetra"
    }
]

xpath_postaje = [
    {
        "xpath": "/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/"
                 "td/div/table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[1]/td/table/"
                 "tbody/tr/td[4]",
        "ime": "postaje"
    },
    {
        "xpath": "//*[contains(text(), 'LETALIŠČE EDVARDA RUSJANA MARIBOR')]",
        "ime": "LETALIŠČE EDVARDA RUSJANA MARIBOR"
    }
]

xpath_nazaj = ("/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/div/"
               "table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/"
               "div")

xpath_tabela = ("/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td/div/"
                "table/tbody/tr[5]/td/div/div[2]/table/tbody/tr[2]/td/div/table[2]/tbody/tr[7]/td/div/div/table/tbody/"
                "tr/td/table")

headers = ["date", "povp. tlak [hPa]", "T [°C]", "povp. T [°C]", "rel. vla. [%]", "povp. rel. vla. [%]",
           "količina padavin [mm]", "hitrost vetra [m/s]", "smer vetra [°]"]

headers2 = ["date", "min. tlak [hPa]", "max. tlak [hpa]", "min. T [°C]", "max. T [°C]", "min. vla. [%]",
            "max. vla. [%]", "max. hitrost vetra [m/s]"]
