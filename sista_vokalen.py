word = input("Skriv in ett ord: ")

vokaler = 'aouåeiyäö'

sistavokalen = ''
index_counter = 0
for i in range(len(word)):
    #får ut Bokstav med hjälpo av index
    bokstav = word[-(i + 1)]
    #Måste lower för att vokalerna är lower
    if bokstav.lower() in vokaler:
        #Om if statementet har gått igenom betyder det att vi är vid vokalen från andra sidan
        sistavokalen = bokstav
        # Converterar till posetiv index från vänster till höger
        index_counter = len(word) - (i + 1)
        break



if sistavokalen != '':
     #Fram till vokalen                              Efter
    print(word[:index_counter] + sistavokalen * 3 + word[index_counter + 1:])
else:
    print(word)