vokaler = 'aouåeiyäö'
ett_ord = input("Skriv ett ord: ")
resultat = ''

for bokstaver in ett_ord:
    if bokstaver.lower() in vokaler:
        resultat += bokstaver

print(resultat)