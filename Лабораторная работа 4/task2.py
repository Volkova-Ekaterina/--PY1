def get_count_char(str_):
    if type(str_) is not str:
        return None
    letter_dict = {}
    low_str = str_.lower()
    for sym in low_str:
        if sym.isalpha() and sym not in letter_dict.keys():
            letter_dict.update({sym: 1})
        elif sym.isalpha() and sym in letter_dict.keys():
            letter_dict[sym] += 1
    return letter_dict


def get_percentage(dictionary):
    if type(dictionary) is not dict:
        return None
    amount_of_symbols = sum(dictionary.values())
    for keys in dictionary:
        new_value = round(dictionary[keys]*100/amount_of_symbols, 2)
        dictionary.update({keys: new_value})

    return dictionary


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_percentage(get_count_char(main_str)))
