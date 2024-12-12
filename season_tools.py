from datetime import date, timedelta

def spring_start_date(temperatures):
    """
    Bestämmer datumet för vårens ankomst baserat på temperaturen.

    Parametrar:
    - temperatures: En lista med dagliga medeltemperaturer.

    Returnerar:
    - Ett datum (datetime.date) för vårens ankomst.

    Kastar:
    - ValueError om något av följande är sant:
      1. Listan innehåller färre än 7 temperaturer.
      2. Vårens ankomst är senare än 31 juli.
      3. Det inte finns 7 dagar i rad över 0°C.
    """
    if len(temperatures) < 7:
        raise ValueError("Minst sju dygnsmedeltemperaturer behövs!")

    # Startdatum för temperaturerna
    start_date = date(2024, 2, 15)

    # Kontrollera varje grupp av 7 dagar
    for i in range(len(temperatures) - 6):  # -6 för att undvika IndexError
        if all(temp > 0 for temp in temperatures[i:i + 7]):
            arrival_date = start_date + timedelta(days=i)

            # Kontrollera om datumet är för sent
            if arrival_date > date(2024, 7, 31):
                raise ValueError("Vårens ankomst kan inte vara senare än 31 juli!")
            
            return arrival_date  # Returnera vårens ankomstdatum

    # Om ingen vår hittas, kasta ett fel
    raise ValueError("Våren är inte här än!")

print(spring_start_date([-1.4, 0.3, -0.5, 0.3, 0.0, 1.7, 1.6, 0.9, 0.2, 0.3, 1.2, 1.4, 0.9, -0.2]))