currentInches = 0
currentFeet = 0

def feet_inches(inches):
   currentFeet = inches / 12
   totalRightFeet = int(currentFeet) * 12
   leftoverInches = inches - totalRightFeet
   return [int(currentFeet), leftoverInches]
print(feet_inches(93))

def season(mounth, day):
   totalmounthdays = mounth * 30
   totaldays = totalmounthdays + day
   if 355 <= totaldays <= 365:
      return "Vinter"
   elif 0 <= totaldays <= 79:
      return"Vinter"
   elif 80 <= totaldays <= 200:
      return"Vår"
   elif 201 <= totaldays <= 291:
      return"Sommar"
   elif 292<= totaldays <= 354:
      return"Höst"
print(season(9,21))



def center_list(lst):
    # Initialize the sum
    total = 0
    # Loop through the list to calculate the total
    for val in lst:
        total += val
    # Calculate the average
    medelvärde = total / len(lst)
    return medelvärde


   




Values = [12, 5, 9, 13, 11]
print(center_list(Values))