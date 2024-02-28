from functools import reduce


def sq(fl) -> float:
    return round(fl ** 2, 3)


my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
print(list(map(sq, my_floats)))


def less7(string) -> bool:
    return len(string) <= 7


my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
print(list(filter(less7, my_names)))

my_numbers = [4, 6, 9, 23, 5]
print(reduce(lambda a, b: a * b, my_numbers))


def st(string) -> str:
    if "1" in string and "4" in string:
        string = "jazzjoker"
    elif "1" in string:
        string = "joker"
    elif "4" in string:
        string = "jazz"
    return string


array = ["array1", "array4", "array41", "array"]
print(list(map(st, array)))


def cnt(string):
    k = 0
    for i in string:
        if i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            k = k + 1
    return k


print(reduce(lambda a, b: a if cnt(a) > cnt(b) else b, ["qwertyuiop", "asdfghjkl", "zxcvbnm", "aaaaaa", "bbbbbbbbbb"]))
