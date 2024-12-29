filnamn = input("Ange ett filnamn: ")
sok_ord = input("Ord att byta ut: ")
ersatt_med = input("Ersätt med: ")


try:
    with open(filnamn, "r", encoding="utf-8") as fil:
        innehall = fil.read()
    
    nytt_innehall = innehall.replace(sok_ord, ersatt_med)
    
    with open(filnamn, "w", encoding="utf-8") as fil:
        fil.write(nytt_innehall)
    
    print("Filens innehåll har uppdaterats.")
except FileNotFoundError:
    print(f"Filen '{filnamn}' hittades inte.")
except Exception as e:
    print(f"Ett fel uppstod: {e}")
