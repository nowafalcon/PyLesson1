# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать
# функцию input().
my_list = ["a", "b", "c", "d", "e", "x"]
i = 0
while i < len(my_list):
    if i != len(my_list)-1:
        my_list[i], my_list[i + 1] = my_list[i + 1],my_list[i]
        i += 2
    else:
        break
print(my_list)
