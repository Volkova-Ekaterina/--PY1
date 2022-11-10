import random


def get_unique_list_numbers() -> list[int]:
    list_of_rnd = []
    while len(list_of_rnd) < 16:
        x = random.randint(-10, 10)
        if x not in list_of_rnd:
            list_of_rnd.append(x)
    return list_of_rnd


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
