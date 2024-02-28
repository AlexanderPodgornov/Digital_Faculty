import random


def fib():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b


fb = fib()  # без fb не работает
print(next(fb))
print(next(fb))
print(next(fb))
print(next(fb))
print(next(fb))


def gen_card():
    cards = {'Бубны': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз'],
             'Черви': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз'],
             'Пики': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз'],
             'Трефы': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']}
    while True:
        yield str(random.choice(random.choice(list(cards.values())))) + " " + str(random.choice(list(cards.keys())))


card = gen_card()
print(next(card))
print(next(card))
print(next(card))
print(next(card))
