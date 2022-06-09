# Blackjack 
# Fischer Florian und Thomas Hassler 
# 1AHIF
# sehr professionell und ab 1 Juli bei Steam erhältlich (spaß)

import random

def start(einsatz, kapital,spieler, schissl):
    print("Mindesteinsatz beträgt 5 Hawi")
    print(f"Dei kapital beträgt {kapital}")
    einsatz = int(input("Wie viel möchtest du setzen: ")) 
    while (einsatz > kapital) or (einsatz < 5):
        einsatz = int(input("Wie viel möchtest du setzen: ")) # Einsatz eing 
    for i in range(2):
        kartenZahl = int(random.random()*9)+2 
        spieler += kartenZahl    # Für Spieler 2 Zufallskarten 
    for i in range(2):
        kartenZahl = int(random.random()*9)+2
        schissl += kartenZahl # Für die Schissl (Pc) 2 Zufallskarten 
    return spieler, schissl, einsatz

def ziehen_(spieler):
    # spieler zieht eine karte
    kartenZahl = int(random.random()*9)+2
    return kartenZahl

def game(): # Des is es Spiel Kumpel ge ge ge !!!! 
    nocheinmal ="ja"
    kapital = 1000
    
    while nocheinmal == "ja" and not kapital < 0:
        # jedes mal neue initialisierung
        ziehen = "na des is lei für initialisierung"
        spieler = 0
        schissl = 0
        einsatz = 0
        
        spieler, schissl, einsatz = start(einsatz, kapital, spieler, schissl)
        print(f"De Schissl hot {schissl} und du host {spieler}")
        # des if is im while weil des direkt überprüft kert
        
        while ziehen != "nein":
            ziehen = str(input("Ziehen [ja/nein]: "))
            if ziehen == "ja":
                spieler += ziehen_(spieler)
                print(f"Du hast {spieler} und des schissl hot {schissl}")
            if spieler > 21:
                break   
        # des is außerhalb für gewinn kalkulation
        
        while schissl < 17:
            kartenZahl = int(random.random()*9)+2
            schissl += kartenZahl
        print(f"De Schissl hot {schissl} du host {spieler}")
        
        if (spieler > 21) or ((schissl > spieler) and (schissl < 22)):# Überprüfung ob verloren 
            print("Hawara host nit gwunnen")
            kapital -= einsatz
        elif (spieler == schissl): # Wenn gleich dann neu anfangen
            print("Push")
            continue
        elif (schissl > 21) or ((spieler > schissl) and (spieler < 22)) or (spieler == 21): # Überprüfen ob gewonnen 
            print("Vaschwind mit deim Göld")
            kapital += einsatz
        print(f"Du host noch so viel Schilling: {kapital}")
        # nocheinmal spielen
        nocheinmal = str(input("Möchtest du nocheinmal spielen  (ja/nein): "))

game()
