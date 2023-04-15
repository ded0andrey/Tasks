def expectation(*args):
    list_of_num, list_of_str, list_of_bool, list_of_other = [], [], [], []
    for i in args:
        if type(i) == int:
            list_of_num.append(i)
        elif type(i) == float:
            list_of_num.append(i)
        elif type(i) == bool:
            list_of_bool.append(i)
        elif type(i) == str:
            list_of_str.append(i)

        else:
            list_of_other.append(i)

    print('List_of_num:', list_of_num, '(числа)')
    print('List_of_str:', list_of_str, '(строки)')
    print('List_of_bool:', list_of_bool, '(логический тип)')
    print('List_of_other:', list_of_other, '(кортеж)')
    print(type(False))


expectation(1, 'hi', False, 2.3, 'Yes', True, (1, 2))
