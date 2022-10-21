def delete_ver_one(list_, index=None):
    if index is None:
        index = len(list_)-1

    list_cut = list_[:len(list_)-1]
    first_half_list = list_cut[:index+1]
    second_half_list = list_cut[index+1:]
    new_half = first_half_list[:len(first_half_list)-1]

    new_half.extend(second_half_list)
    return new_half
#этот вариант функции возвращает значения, указанные изначально в комментариях около принтов
#По умолчанию удается последний элемент из списка - последний элемент удаляется всегда

def delete_ver_two(list_, index=None):
    if index is None:
        index = len(list_)-1

    first_half_list = list_[:index+1]
    second_half_list = list_[index+1:]
    new_half = first_half_list[:len(first_half_list)-1]

    new_half.extend(second_half_list)
    return new_half
#этот вариант возвращает ожидаемые в проверке значения
#По умолчанию удается последний элемент из списка - индекс удаления по умолчанию последний


print(delete_ver_two([0, 0, 1, 2], index=0))  # [0, 1]
print(delete_ver_two([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete_ver_two([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
