def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results[function.__name__] = function(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# Свое дополнение:
# Найдем сумму чисел из списка умноженных на 2
def duble_2(args):
    res = 0
    for x in args:
        res += x*2
    return res

print(apply_all_func([6, 20, 15, 9], duble_2))
