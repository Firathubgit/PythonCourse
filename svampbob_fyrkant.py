# Läs in ett ord från användaren
word = input('Ange ett ord: ')

# Variabel för att hålla resultatet
current_word = ''

# Loopa genom varje bokstav och växla mellan liten och stor
for i in range(len(word)):
    if i % 2 == 0:
        current_word += word[i].lower()  # Varannan liten
    else:
        current_word += word[i].upper()  # Varannan stor

# Skriv ut resultatet
print(current_word)
