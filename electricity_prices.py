def cheapest_3h(prices):
    min_avg_price = float('inf')  #Starta högt så man kan sänka. Loopens logic funkar inte då lol
    print(min_avg_price)
    min_index = 0 
    
    for i in range(len(prices) - 2):  # Iterera fram till sista möjliga starttimme 3 sammanhängande timmar
        # Beräkna medelvärdet för tre sammanhängande timmar: i, i+1, och i+2
        avg_price = (prices[i] + prices[i+1] + prices[i+2]) / 3
        
        # Kontrollera om denna period är billigare än tidigare
        if avg_price < min_avg_price:
            min_avg_price = avg_price
            min_index = i
    
    return min_index #starten av perioden index count 0 först
print(cheapest_3h([143, 167, 124, 112, 96, 102, 129, 190]))