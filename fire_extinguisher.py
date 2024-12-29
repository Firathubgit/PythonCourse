from datetime import date

# Extinguisher class
class Extinguisher:
    def __init__(self, extinguisher_type, manufacturing_date):
        """
        Initialiserar en brandsläckare med typ och tillverkningsdatum.
        """
        self.extinguisher_type = extinguisher_type
        self.manufacturing_date = date.fromisoformat(manufacturing_date)  # Använder date.fromisoformat för att skapa ett datumobjekt

    def has_expired(self):
        """
        Kontrollerar om brandsläckaren har gått ut, baserat på dess typ.
        """
        current_date = date.today()  # Använder endast datum utan tid
        if self.extinguisher_type == "water":
            lifetime = 12
        elif self.extinguisher_type == "powder":
            lifetime = 10
        elif self.extinguisher_type == "foam":
            lifetime = 5
        else:
            raise ValueError("Okänd typ av brandsläckare!")

        expiration_date = self.manufacturing_date.replace(year=self.manufacturing_date.year + lifetime)
        return current_date > expiration_date

    def get_type(self):
        """
        Returnerar typen av brandsläckare.
        """
        return self.extinguisher_type


if __name__ == '__main__':
    # Skapa instanser av Extinguisher-klassen här för att testa dess metoder
    extinguisher_type = input("Type? ").strip()
    manufacturing_date = input("Manufacturing date? ").strip()

    # Skapa en instans av Extinguisher-klassen
    extinguisher = Extinguisher(extinguisher_type, manufacturing_date)

    # Visa information om brandsläckaren
    print(f"Type? {extinguisher.get_type()}")
    print(f"Manufacturing date? {manufacturing_date}")
    if extinguisher.has_expired():
        print("Expired")
    else:
        print("Not expired")
