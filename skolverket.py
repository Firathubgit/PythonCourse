import requests
Komunnamn = str(input("Komun Namn: "))
def hitta_kommunkod(str):
    response =  requests.get('https://api.skolverket.se/skolenhetsregistret/v1/kommun')
    data = response.json()
    if response.status_code == 200:
        print("Found 200")
    else:
        return "Did not find api server zib"
    
    for kommun in data["Kommuner"]:
        senaste_kommunkod = kommun.get("Kommunkod", "Ingen kod")
        if kommun.get("Namn", "").lower() == str.lower():
            print(f"kommunkod är: {senaste_kommunkod}")
        else:
            return "Kommunen hittades inte, dubbelkolla stavningen!"
        
    
        
hitta_kommunkod(Komunnamn)