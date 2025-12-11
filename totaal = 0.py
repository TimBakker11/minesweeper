def vraag_bedrag(prompt):
    #dit vraagt het bedrag
    while True:
        invoer = input(prompt).replace(",", ".")
        try:
            bedrag = float(invoer)
            return bedrag
        except ValueError:
            print("Ongeldige invoer! Voer een geldig bedrag in.\n")


#Bedragen opvragen
totaal = 0.0
print("Voer 0 in om te stoppen.\n")

while True:
    bedrag = vraag_bedrag("Bedrag: ")
    if bedrag <= 0:
        break
    totaal += bedrag

print(f"\nTotaal te betalen: € {totaal:.2f}\n")

#Betalen
betaald = 0.0
while betaald < totaal:
    betaling = vraag_bedrag("Betaalbedrag: ")
    if betaling <= 0:
        print("Voer een bedrag groter dan 0 in.\n")
        continue
    betaald += betaling
    if betaald < totaal:
        print(f"Nog te betalen: € {totaal - betaald:.2f}\n")

#Wisselgeld
verschil = betaald - totaal

if verschil > 0:
    print(f"\nWisselgeld: € {verschil:.2f}")
else:
    print("\nBedrag is betaald. Bedankt!")
    if verschil > -1: 
        print("\nFBI komt je halen")
    else:
        print("\nGoed Zo")