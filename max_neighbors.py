def max_neighbors(values):
    if len(values) < 2:
        raise ValueError("Listan måste ha minst två element.")
    
    max_sum = values[0] + values[1]
    for i in range(1, len(values) - 1):
        current_sum = values[i] + values[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum
print(max_neighbors([9, 4, 13, 7, 8, 5]))
print(max_neighbors([8, 0, -4, 10, -12, 22, -5]))
# Enkelt input och körning
