import random


def check_combinations(deck):
    # deck = [['Трефы', '10'], ['Трефы', 'валет'], ['Трефы', 'дама'], ['Трефы', 'король'], ['Трефы', 'туз']]        test flash_royal +
    # deck = [['Трефы', '5'], ['Трефы', '6'], ['Трефы', '7'], ['Трефы', '8'], ['Трефы', '9']]                       test street_flash +
    # deck = [['Трефы', '10'], ['Черви', '10'], ['Бубны', '10'], ['Пики', '10'], ['Трефы', 'туз']]                  test care +
    # deck = [['Трефы', '4'], ['Черви', '4'], ['Трефы', '6'], ['Черви', '6'], ['Пики', '6']]                        test full house +
    # deck = [['Трефы', '10'], ['Трефы', '7'], ['Трефы', 'дама'], ['Трефы', 'король'], ['Трефы', 'туз']]            test flash +
    # deck = [['Пики', '5'], ['Трефы', '6'], ['Бубны', '7'], ['Черви', '8'], ['Трефы', '9']]                        test street +
    # deck = [['Пики', '5'], ['Трефы', '5'], ['Бубны', '5'], ['Черви', '6'], ['Трефы', '9']]                        test set +
    # deck = [['Пики', '5'], ['Трефы', '5'], ['Бубны', 'валет'], ['Черви', 'валет'], ['Трефы', '9']]                test two_pairs +
    # deck = [['Пики', '5'], ['Трефы', '5'], ['Бубны', '6'], ['Черви', 'валет'], ['Трефы', '9']]                    test pair +
    flash_royal = False
    street_flash = False
    care = False
    full_house = False
    flash = False
    street = False
    set = False
    two_pairs = False
    pair = False
    elder_card = False

    max_count_mast = 0
    max_count_number = 0

    counter_mast = {'Бубны': 0, 'Черви': 0, 'Пики': 0, 'Трефы': 0}
    for i in range(5):
        if deck[i][0] == 'Трефы':
            counter_mast['Трефы'] += 1
        if deck[i][0] == 'Бубны':
            counter_mast['Бубны'] += 1
        if deck[i][0] == 'Черви':
            counter_mast['Черви'] += 1
        if deck[i][0] == 'Пики':
            counter_mast['Пики'] += 1
    # print(counter_mast)

    counter_number = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'валет': 0, 'дама': 0,
                      'король': 0, 'туз': 0}
    for i in range(5):
        if deck[i][1] == '2':
            counter_number['2'] += 1
        if deck[i][1] == '3':
            counter_number['3'] += 1
        if deck[i][1] == '4':
            counter_number['4'] += 1
        if deck[i][1] == '5':
            counter_number['5'] += 1
        if deck[i][1] == '6':
            counter_number['6'] += 1
        if deck[i][1] == '7':
            counter_number['7'] += 1
        if deck[i][1] == '8':
            counter_number['8'] += 1
        if deck[i][1] == '9':
            counter_number['9'] += 1
        if deck[i][1] == '10':
            counter_number['10'] += 1
        if deck[i][1] == 'валет':
            counter_number['валет'] += 1
        if deck[i][1] == 'дама':
            counter_number['дама'] += 1
        if deck[i][1] == 'король':
            counter_number['король'] += 1
        if deck[i][1] == 'туз':
            counter_number['туз'] += 1

    max_count_mast = max(counter_mast.values())  # максимальное кол-во карт одной масти
    max_count_number = max(counter_number.values())  # максимальное кол-во карт одного значения

    if max_count_mast == 5:
        if (deck[0][1] == '10') and (deck[1][1] == 'валет') and (deck[2][1] == 'дама') and (
                deck[3][1] == 'король') and (deck[4][1] == 'туз'):
            flash_royal = True
        elif ((deck[0][1] == '2') and (deck[1][1] == '3') and (deck[2][1] == '4') and (deck[3][1] == '5') and (
                deck[4][1] == '6')) or \
                ((deck[0][1] == '3') and (deck[1][1] == '4') and (deck[2][1] == '5') and (deck[3][1] == '6') and (
                        deck[4][1] == '7')) or \
                ((deck[0][1] == '4') and (deck[1][1] == '5') and (deck[2][1] == '6') and (deck[3][1] == '7') and (
                        deck[4][1] == '8')) or \
                ((deck[0][1] == '5') and (deck[1][1] == '6') and (deck[2][1] == '7') and (deck[3][1] == '8') and (
                        deck[4][1] == '9')) or \
                ((deck[0][1] == '6') and (deck[1][1] == '7') and (deck[2][1] == '8') and (deck[3][1] == '9') and (
                        deck[4][1] == '10')) or \
                ((deck[0][1] == '7') and (deck[1][1] == '8') and (deck[2][1] == '9') and (deck[3][1] == '10') and (
                        deck[4][1] == 'валет')) or \
                ((deck[0][1] == '8') and (deck[1][1] == '9') and (deck[2][1] == '10') and (deck[3][1] == 'валет') and (
                        deck[4][1] == 'дама')) or \
                ((deck[0][1] == '9') and (deck[1][1] == '10') and (deck[2][1] == 'валет') and (
                        deck[3][1] == 'дама') and (deck[4][1] == 'король')):
            street_flash = True

    if ((deck[0][1] == '2') and (deck[1][1] == '3') and (deck[2][1] == '4') and (deck[3][1] == '5') and (
            deck[4][1] == '6')) or \
            ((deck[0][1] == '3') and (deck[1][1] == '4') and (deck[2][1] == '5') and (deck[3][1] == '6') and (
                    deck[4][1] == '7')) or \
            ((deck[0][1] == '4') and (deck[1][1] == '5') and (deck[2][1] == '6') and (deck[3][1] == '7') and (
                    deck[4][1] == '8')) or \
            ((deck[0][1] == '5') and (deck[1][1] == '6') and (deck[2][1] == '7') and (deck[3][1] == '8') and (
                    deck[4][1] == '9')) or \
            ((deck[0][1] == '6') and (deck[1][1] == '7') and (deck[2][1] == '8') and (deck[3][1] == '9') and (
                    deck[4][1] == '10')) or \
            ((deck[0][1] == '7') and (deck[1][1] == '8') and (deck[2][1] == '9') and (deck[3][1] == '10') and (
                    deck[4][1] == 'валет')) or \
            ((deck[0][1] == '8') and (deck[1][1] == '9') and (deck[2][1] == '10') and (deck[3][1] == 'валет') and (
                    deck[4][1] == 'дама')) or \
            ((deck[0][1] == '9') and (deck[1][1] == '10') and (deck[2][1] == 'валет') and (deck[3][1] == 'дама') and (
                    deck[4][1] == 'король')) or \
            ((deck[0][1] == '10') and (deck[1][1] == 'валет') and (deck[2][1] == 'дама') and (
                    deck[3][1] == 'король') and (
                     deck[4][1] == 'туз')):
        street = True

    if max_count_number == 4:
        care = True
    if max_count_number == 3:
        set = True

    for i in range(len(counter_number)):
        if ((2 in list(counter_number.values())) + (3 in list(counter_number.values()))) == 2:
            full_house = True
    for i in range(len(counter_number)):
        if list(counter_number.values()).count(2) == 2:
            two_pairs = True
    for i in range(len(counter_number)):
        if list(counter_number.values()).count(2) == 1:
            pair = True
    if flash_royal == street_flash == care == full_house == flash == street == set == two_pairs == pair == False:
        elder_card = True
    # print('flash_royal', flash_royal)
    # print('street_flash', street_flash)
    # print('care', care)
    # print('full_house', full_house)
    # print('flash', flash)
    # print('street', street)
    # print('set', set)
    # print('two_pairs', two_pairs)
    # print('pair', pair)
    # print('elder_card', elder_card)
    # print("=====")
    # print(counter_mast)
    # print(counter_number)
    # print(max_count_mast)
    # print(max_count_number)
    if flash_royal:
        print("FLASH ROYAL")
    if street_flash:
        print("STREET FLASH")
    if care:
        print("CARE")
    if full_house:
        print("FULL HOUSE")
    if flash:
        print("FLASH")
    if street:
        print("STREET")
    if set:
        print("SET")
    if two_pairs:
        print("TWO PAIRS")
    if pair:
        print("PAIR")
    if elder_card:
        print("ELDER CARD")


cards = {'Бубны': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз'],
         'Черви': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз'],
         'Пики': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз'],
         'Трефы': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']}

deck = []
selected_cards = set()

for i in range(5):
    key = random.choice(list(cards.keys()))
    value = random.choice(cards[key])

    while (key, value) in selected_cards:
        key = random.choice(list(cards.keys()))
        value = random.choice(cards[key])

    selected_cards.add((key, value))
    deck.append([key, value])

deck_sorted = sorted(deck, key=lambda x: x[1])
deck = deck_sorted

print(deck)
print('=======')
check_combinations(deck)
