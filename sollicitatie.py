dierenDressuur = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?"))
jongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren?"))
acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek?"))
diploma = input("Bezit u in bezit van een Diploma MBO-4 ondernemen?")
vrachtwagenRijbewijs = input("Bent u in bezit van een geldig vrachtwagen rijbewijs?")
hogeHoed = input("Bezit u een hoge hoed?")
geslacht = input("Bent u een man of vrouw?")

if geslacht == "man":
    snor = input("Heeft u een snor?")
    if snor == "ja":
        moustacheWidth = int(input("Hoelang is uw snor?"))
    else:
        moustacheWidth = 0 

else: 
    roodKrulhaar = input("Heeft u rood krulhaar?")
    if roodKrulhaar == "ja":
        KrulhaarWidth = int(input("Hoelang is uw krulhaar?"))
    else:
        KrulhaarWidth = 0
lengte = int(input("Hoe lang bent u in?"))
gewicht = int(input("Hoe zwaar bent u?"))
certificaat = input("Heeft u een certificaat 'Overleven met gevaarlijk personeel'?")
naam = input("Wat is uw naam:")
Italiaans = input("Spreekt u Italiaans?")
Huisdieren = int(input("Hoeveel huisdieren heeft u?"))
handstand = input("Kunt u de handstand?")

Aangenomen = (dierenDressuur > 4 or jongleren > 5 or acrobatiek > 3)and(diploma == "ja")and(vrachtwagenRijbewijs == "ja")and(hogeHoed == "ja")and(geslacht == "man" or geslacht == "vrouw")and(snor == "ja" and moustacheWidth > 10)or(roodKrulhaar == "ja" and KrulhaarWidth > 20)and(lengte > 150)and(gewicht > 90)and(certificaat == "ja")

if Aangenomen == True:
    print("U bent aangenomen!!!")
else:
    print("Helaas bent u niet aangenomen")