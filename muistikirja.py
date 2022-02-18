
import time

def startti(aloitus='muistio.txt'):
    try:
        eka_muistio = open(aloitus)
        eka_muistio.close
        print("Käytetään muistiota: ", aloitus)
    except OSError:
        eka_muistio = open(aloitus, "w")
        eka_muistio.close
        print("Oletusmuistioa ei löydy, luodaan tiedosto.\nKäytetään muistiota: ", aloitus)
		
def vaihto(uusi_nimi):
    try:
        tiedosto = open(uusi_nimi, "r")
        tiedosto.close
        print("Käytetään muistiota: ", uusi_nimi)
    except IOError:
        tiedosto = open(uusi_nimi, "w")
        tiedosto.close
        print("Tiedostoa ei löydy, luodaan tiedosto.\nKäytetään muistiota: ",uusi_nimi)
		
def main():
    startti()
    valinta = 0
    vaihtuva_nimi = "muistio.txt"
    while valinta < 6:
        print("""(1) Lue muistikirjaa
        (2) Lisää merkintä
        (3) Tyhjennä muistikirja
        (4) Vaihda muistiota
        (5) Lopeta""")
        valinta = int(input("Mitä haluat tehdä?: "))
        if valinta == 1:
            muistikirja = open(vaihtuva_nimi,"r")
            sisalto = muistikirja.read()
            print(sisalto+"\nKäytetään muistiota: ",vaihtuva_nimi)
            muistikirja.close()
        elif valinta == 2:
            muistikirja = open(vaihtuva_nimi,"a")
            teksti = input("Kirjoita uusi merkintä: ")
            muistikirja.write(teksti + ':::' + time.strftime("%X %x") + '\n')
            print("Käytetään muistiota: ",vaihtuva_nimi)
            muistikirja.close()
        elif valinta == 3:
            muistikirja = open(vaihtuva_nimi,"w")
            muistikirja.close()
            print("Muistio tyhjennetty.")
            print("Käytetään muistiota: ",vaihtuva_nimi)
        elif valinta == 4:
            vaihtuva_nimi = str(input("Anna tiedoston nimi: "))
            muistikirja = vaihto(vaihtuva_nimi)
        elif valinta == 5:	
            print("Lopetetaan.")
            break

if __name__ == "__main__":
    main()
