list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

maxn = max(list_numbers)
idxmax = list_numbers.index(maxn)
list_numbers[-1], list_numbers[idxmax] = list_numbers[idxmax], list_numbers[-1]
print(list_numbers)
