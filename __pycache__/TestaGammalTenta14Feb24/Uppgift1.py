timmaråkt = 0
minuteråkt = 0
def calculate_travel_time(distance):
    timmaråkt = int((distance/60))
    minuteråkt = distance - timmaråkt * 60
    return (timmaråkt, minuteråkt )

print(calculate_travel_time(int(input("Ange Distance: "))))

#GODKÄNT SJÄLV (Använde bara kalkulator)