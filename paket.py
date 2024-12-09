maxvikt = int(input("Ange maxvikt?: "))
current_wheight = 0
amount_of_packages = 0
total_wheight = 0
while total_wheight < maxvikt:
    current_wheight = int(input("Paketets vikt (kg): "))
    if total_wheight + current_wheight > maxvikt:
        break
    else:
        total_wheight += current_wheight 
        amount_of_packages += 1


print(f'Du kan lasta {amount_of_packages} paket. Totalvikten är {total_wheight} kg')
