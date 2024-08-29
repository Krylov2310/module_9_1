print('\033[30m\033[47mДомашнее задание по теме "Введение в функциональное программирование".\033[0m')
print('\033[30m\033[47mЗадача "Вызов разом":\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


def apply_all_func(int_list, *functions):
    results = {}
    for functions_ in functions:
        results[functions_.__name__] = functions_(int_list)
    return results


# Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print()
print(thanks)