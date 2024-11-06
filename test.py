print("Vcházíš do obchodního domu IKEA, tvým úkolem není nic jednoduššího než najít sedačku Strandmon.")
print("Z mně neznámých důvodů ses rozhodl, že půjdeš na nákup 8 minut před zavíračkou...")
print("Proto nezapomeň, zbloudilé duše, které nestihnou utéct před zavřením hlavních dveří se stanou zaměstnanci! Hodně štěstí...")

tahy = 8  # Počet zbývajících tahů
lokace = "vstup"  # Hráčova aktuální pozice
nalezeno = False  # Zda hráč nalezl sedačku

# Sledování instrukcí, které hráč zadal
instrukce = []  # Uchovává instrukce, aby je hráč musel dodržet v daném pořadí

# Hlavní hra
while tahy > 0 and not nalezeno:
    print(f"\nZbývající tahy: {tahy}")
    
    if lokace == "vstup":
        odpoved = input("Zaměstnanec se vás ptá: 'Potřebujete s něčím poradit?' (ano/ne): ").strip().lower()
        if odpoved == "ano":
            # Pokud hráč odpoví ano, dostane pomoc
            print("Zaměstnanec: 'Co hledáte?'")
            hledane = input("Vyberte: 1) strandmon sedačka 2) židle Ingolf 3) skleničky IKEA365+: ").strip()
            
            if hledane == "1":
                print("Zaměstnanec: 'Na sedačku Strandmon musíte jít 1x doprava, 2x doleva a pak 2x rovně.'")
                instrukce = ["doprava", "doleva", "doleva", "rovne", "rovne"]  # Správná sekvence k nalezení sedačky
                lokace = "sedačky"
                tahy -= 1
            elif hledane == "2":
                print("Zaměstnanec: 'Na židli Ingolf jděte 3x doprava, 4x doleva a pak 2x rovně.'")
                tahy -= 5
            elif hledane == "3":
                print("Zaměstnanec: 'Na skleničky IKEA365+ jděte 3x rovně, 4x vlevo a pak 3x vpravo.'")
                tahy -= 5
            else:
                print("Zaměstnanec: 'Nevím, co hledáte, zkusím vám poradit.'")
                tahy -= 1
            
        elif odpoved == "ne":
            print("Odmítl jste pomoc a pokračujete sami do oddělení sedaček.")
            lokace = "sedačky"
            tahy -= 1
        else:
            print("Neplatná odpověď. Prosím, napište 'ano' nebo 'ne'.")
            continue

    elif lokace == "sedačky":
        smer = input("Jste v oddělení sedaček. Kam se chcete vydat? (doprava/doleva/rovne): ").strip().lower()
        
        if smer not in ["doprava", "doleva", "rovne"]:
            print("Neplatný směr. Zadejte 'doprava', 'doleva' nebo 'rovne'.")
            continue
        
        instrukce.append(smer)  # Přidává tah hráče do seznamu instrukcí
        tahy -= 1

        # Kontrola, zda hráč dodržuje správnou sekvenci
        if instrukce == ["doprava", "doleva", "doleva", "rovne", "rovne"]:
            print("Gratuluji! Našli jste sedačku Strandmon.")
            nalezeno = True
        elif len(instrukce) > len(["doprava", "doleva", "doleva", "rovne", "rovne"]):
            print("Ztratili jste se a instrukce neodpovídají. Zkusili jste to špatně.")
            break

# Výsledek hry
if nalezeno:
    print("Našli jste sedačku Strandmon a můžete IKEA opustit jako spokojený zákazník!")
else:
    print("Bohužel jste sedačku Strandmon nenašli včas.")
    print("Z IKEA se už nevrátíte jako zákazník... stáváte se zaměstnancem. Vítejte v týmu!")
