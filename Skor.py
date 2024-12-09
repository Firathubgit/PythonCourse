# Alla mina skor har samma färg, storlek och modell. Varje högersko kan alltså
# paras ihop med vilken vänstersko som helst och vice versa. Skriv ett program
# som läser in antalet vänsterskor och antalet högerskor från användaren.

# Programmet ska skriva ut resultatet på följande format:
# "Det finns m par och n överblivna skor."
# med värden på m och n beroende på antalet höger- och vänsterskor som
# användaren angett.


# Läs in antal vänsterskor och gör om till heltal         13
vänstersko = int(input("Ange antalet vänster skor "))

# Läs in antal högerskor och gör om till heltal           9
högersko = int(input("Ange antalet höger skor "))

# Beräkna antal kompletta par                             9
totalskor = vänstersko + högersko
if vänstersko < högersko:
    m = vänstersko
else:
    m = högersko

n =  (m * 2) - totalskor
print(f'Det finns {abs(m)} par och {abs(n)} överblivna skor')
# Beräkna antal överblivna skor                           4

# Skriv ut resultatet                                     'Det finns 9 par och 4 överblivna skor.'
