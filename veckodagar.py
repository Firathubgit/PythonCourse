    # Läs in ett serie av dagar från användaren
user_data = input('Skriv in dagar (0-6): ')
#1 2 4
user_data_split = user_data.split()

dagar = [int(i) for i in user_data_split]


veckodagarna = ['måndag', 'tisdag', 'onsdag','torsdag','fredag']
    # Gör om till en lista av heltal

for dag in dagar:
    print(veckodagarna[dag])


