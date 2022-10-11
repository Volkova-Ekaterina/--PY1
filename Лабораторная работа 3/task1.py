src = not False and True or False and not True

# result = True and True or False and False # избавляемся от отрицаний
# result = True or False # выполняем логические умножения
# result = True # выполняем логическое сложение
result = True

print(src == result)
