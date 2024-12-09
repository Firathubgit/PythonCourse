# Som ni redan vet har alla mina skor samma färg, storlek och modell. Varje högersko kan
# alltså paras ihop med vilken vänstersko som helst och vice versa. I förra laborationen
# skrev ni ett program som läser in antalet vänsterskor och antalet högerskor från
# användaren. Programmet beräknade och skrev ut antalet kompletta par och antalet
# överblivna skor. Dessvärre kunde den utskrivna texten bli lite konstig, med fel former
# av vissa ord.

# I den här uppgiften ska utskriften snyggas till så att programmet
#   * väljer rätt form: överbliven/överblivna, sko/skor
#   * anger om de överblivna skorna är högerskor eller vänsterskor
#   * anpassar texten om inga skor blivit över
vänsterskor = int(input("Hur många vänster skor finns det?: "))
högerskor = int(input("Hur många höger skor finns det?: "))
totala_skor = vänsterskor + högerskor
par = 0
skor_left = 0
if vänsterskor == högerskor:
    par = vänsterskor
    print(f'finns {par} par och inga överblivna skor')
elif vänsterskor > högerskor:
    par = högerskor
    skor_left = totala_skor - (par * 2)
    if skor_left <= 1:
        print(f'Det finns {par} par och {skor_left} överbliven vänstersko.')
    else:
        print(f'Det finns {par} par och {skor_left} överblivna vänsterskor.')
else:
    par = vänsterskor
    skor_left = totala_skor - (par * 2)
    if skor_left <= 1:
        print(f'Det finns {par} par och {skor_left} överbliven högersko.')
    else:
        print(f'Det finns {par} par och {skor_left} överblivna högerskor.')


        


# Exempel 1: (Talen 8 och 5 anges av användaren)
# Hur många vänsterskor finns det? 8
# Hur många högerskor finns det? 5
# Det finns 5 par och 3 överblivna vänsterskor.

# Exempel 2: (Talen 1 och 32 anges av användaren)
# Hur många vänsterskor finns det? 25
# Hur många högerskor finns det? 26
# Det finns 25 par och 1 överbliven högersko.

# Exempel 3: (Talen 17 och 17 anges av användaren)
# Hur många vänsterskor finns det? 17
# Hur många högerskor finns det? 17
# Det finns 17 par och inga överblivna skor.


# Läs in antal vänsterskor och gör om till heltal

# Läs in antal högerskor och gör om till heltal

# Beräkna antal kompletta par

# Beräkna antal överblivna skor

# Skriv ut resultatet på rätt form
