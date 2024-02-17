from random import randint


def check_letters(char, genword):
    global mask

    for i in range(len(genword)):
        if genword[i] == char:
            mask = mask[:i] + char + mask[i + 1:]
    print(mask)


dict = {"python": ["import", "version", "control", "main", "external", "library", "project", "console", "problem",
                   "open", "save", "root", "settings", "repair", "reload"],
        "fruits": ["apple", "banana", "orange", "kiwi", "mango", "pear", "peach"],
        "countries": ["Russia", "Ukraine", "Belarus", "Latvia", "France", "Germany", "Austria", "Canada", "Turkey"],
        "chess": ["pawn", "knight", "bishop", "rook", "queen", "king", "pin", "checkmate", "fork", "draw"]}
print("Темы:")
for i in dict.keys():
    print(i)
theme = ""
while dict.get(theme) is None:
    theme = input("Выберите тему: ")
print("=====")
print("Отлично, вы выбрали тему", theme)
print("=====")
generatedWord = dict.get(theme)[randint(0, len(dict.get(theme)) - 1)]
counter = 0
lenword = len(generatedWord)
mask = "-" * lenword
print("Загадано слово из", lenword, "букв")
print("Попыток:", lenword * 2)
print("======")
while counter < lenword * 2:
    char = input()
    if char == generatedWord:
        print("Победа!")
        break
    if (len(char) > 1) and (char != generatedWord):
        print("Поражение!")
        break
    counter = counter + 1
    check_letters(char, generatedWord)
    print("Осталось попыток:", lenword * 2 - counter)
    print("=======")

    if mask == generatedWord:
        print("Победа!")
        break
if counter == lenword * 2:
    print("Поражение!")
print("Сгенерированное слово:", generatedWord)
