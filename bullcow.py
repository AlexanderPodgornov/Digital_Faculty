from random import randint


def printStats(word1, word2):
    bull = 0
    cow = 0
    for i in range(len(word1)):
        if word1[i] in word2:
            if word2[i] == word1[i]:
                bull = bull + 1
            else:
                cow = cow + 1
    print("Быков:", bull, "Коров:", cow)


words = ["python", "import", "version", "control", "main", "external", "library", "project", "console", "problem",
         "open", "save", "root", "settings", "repair", "reload"]
generatedWord = words[randint(0, len(words) - 1)]
word = ""
counter = 0
lenword = len(generatedWord)
print("Загадано слово из", lenword, "букв")
print("Попыток:", lenword * 2)
print("======")
while counter < lenword * 2:
    word = input()
    counter = counter + 1;
    printStats(word, generatedWord)
    print("Осталось попыток:", lenword * 2 - counter)
    print("=======")
    if word == generatedWord:
        print("Победа!")
        break
if counter == lenword * 2:
    print("Поражение!")
print("Сгенерированное слово:", generatedWord)
