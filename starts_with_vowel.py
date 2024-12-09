# Läs in ord från användaren
user_input = input('Ange en serie ord, åtskilda av mellanslag: ')

# Omvandla strängen till en lista av ord
words = user_input.split()

# Definiera vokaler
vokaler = 'aouåeiyäö'

# Lista för att lagra ord som börjar med vokal
resultat = []

# Iterera genom varje ord
for word in words:
    if word[0].lower() in vokaler:  # Kontrollera om första bokstaven (liten eller stor) är en vokal
        resultat.append(word)       # Lägg till ordet i resultatlistan

# Skriv ut alla ord som börjar med vokal, åtskilda av mellanslag
print(' '.join(resultat))
