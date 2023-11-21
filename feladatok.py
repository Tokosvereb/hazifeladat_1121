"""Vizsgáld meg hogy egy adott szám prímszám-e!"""

def elsofeladat():
    szam =int(input("Kérlek adj meg egy prím számot:"))
    
    if szam < 2:
         szam =int(input("Rossz számot adtál meg, adj meg egy prím számot:"))
    
    i = 2
    while i * i <= szam:
        if szam % i == 0:
            print(f"A megadott szám({szam}) prím szám")
        i += 1   
        #A KÓD MŰKÖDIK, VISZONT NEMTUDOM HOGY MIÉRT TÖBBSZÖR ÍRJA KI AZ EREDMÉNYT ABBAN AZ ESETBEN, HA PRÍM SZÁMOT ADOK MEG


"""Keresd meg, hogya hány 7-el osztható szám van 1-1000 között!"""

def masodikfeladat():
    szam = int(input("Kérlek adj meg egy számot [1-1000] között:"))

    i = 0
    while szam <= 1000:
        if szam % 7 == 0:
            print(szam)
    i += 1












    """röviden prímnek nevezzük azokat a természetes számokat, amelyeknek pontosan két osztójuk van a természetes számok között (az 1 és önmaguk)."""
