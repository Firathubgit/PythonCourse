# Läs in ett positivt heltal från användaren
tal = int(input('Ange ett positivt heltal: '))
# Ange om talet är jämnt eller udda.
if tal < 0:
    print("Talet är Negativ")
elif tal % 2 == 0:
    print("Talet är jämnt")
elif tal % 2 == 1:
    print("Talet är udda")
    