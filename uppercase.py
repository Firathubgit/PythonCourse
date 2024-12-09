# Läs in ett par ord från användaren
user_data = input('Skriv in dina ord: ')
# Gör om till en lista
user_list = user_data.split()

for words in user_list[:]:
    if words.isupper():
        print(words)