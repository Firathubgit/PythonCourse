# Läs in ett ord från användaren
word = input("Ange ett ord: ")

# Loopa över varje index i ordet
for i in range(len(word)):
    # Hämta motsvarande bokstäver
    forward_letter = word[i]          # Bokstav framlänges
    backward_letter = word[-(i + 1)]  # Bokstav baklänges
    # Skriv ut bokstäverna med bindestreck emellan
    print(f"{forward_letter} - {backward_letter}")