from season_tools import spring_start_date

def main():
    """
    Huvudprogrammet som tar in temperaturer från användaren, beräknar vårens
    ankomst och hanterar eventuella fel.
    """
    print("Välkommen! Detta program beräknar när våren börjar baserat på dina temperaturer.")
    
    try:
        # Steg 1: Läs in temperaturer från användaren
        input_temperatures = input("Ange dagliga medeltemperaturer (separerade med mellanslag): ")
        temperatures = [float(temp) for temp in input_temperatures.split()]

        # Steg 2: Beräkna vårens ankomstdatum
        spring_date = spring_start_date(temperatures)
        print(f"Vårens ankomst: {spring_date.strftime('%Y-%m-%d')}")

    except ValueError as e:
        # Hantera förväntade fel från funktionen
        print(f"Fel: {e}")

    except Exception as e:
        # Hantera oväntade fel
        print(f"Ett oväntat fel inträffade: {e}")

if __name__ == "__main__":
    main()