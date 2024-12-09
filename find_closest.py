# Läs in en serie heltal från användaren
user_input = input("Ange en serie heltal, åtskilda av mellanslag: ")

# Omvandla inmatningen till en lista av heltal
numbers = list(map(int, user_input.split()))

# Läs in målvärdet
target = int(input("Ange ett målvärde: "))

# Variabler för att spåra närmaste talet och dess avstånd till målvärdet
closest_number = None
smallest_difference = float('inf')  # Börja med ett mycket stort värde

# Loopa igenom talen för att hitta det närmaste
for number in numbers:
    difference = abs(number - target)  # Beräkna avståndet till målvärdet
    if difference < smallest_difference:
        closest_number = number
        smallest_difference = difference

# Skriv ut det närmaste talet
print(f"Närmast: {closest_number}")
