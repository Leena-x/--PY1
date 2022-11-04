dict_ = {}


def get_count_char(str_):
    str_ = "".join(str_.split()).lower()
    for b in str_:
        if b.isalpha() == True:
            if b in dict_:
                dict_[b] += 1
            else:
                dict_[b] = 1
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
print(get_count_char(main_str))

dict_p = {}
all_symbols = sum(dict_.values())


def procent(dict_):
    for b in dict_:
        dict_p[b] = round(dict_.get(b) * 100 / all_symbols, 2)
    return dict_p
print(procent(dict_))

