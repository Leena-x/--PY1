dict_ = {}
def get_count_char(str_):
    str_split = "".join(str_.split())
    str_lower = str_split.lower().replace(".", '').replace(",", '').replace("!",'')
    for b in str_lower:
        if b in dict_ :
            dict_[b] += 1
        else:
            dict_[b] = 1
    print(dict_)

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
print(get_count_char(main_str))
