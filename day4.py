from collections import defaultdict

with open('input4.txt', 'r') as f:
    cards = f.readlines()

# part 1
def points_card(card):
    id, all_numbers = card.split(':')
    winning, numbers = map(str.split, all_numbers.split('|'))
    winning = set(winning)

    points = 0
    for number in numbers:
        if number in winning:
            if points == 0: points = 1
            else: points = points*2

    return points

print(sum(map(points_card, cards)))

# part 2
id_cards = defaultdict(lambda: 1)
def matching_cards(card):
    card_id, all_numbers = card.split(':')
    card_id = int(card_id.split()[1])
    winning, numbers = map(str.split, all_numbers.split('|'))
    winning = set(winning)

    number_of_card = id_cards[card_id]
    id_to_increase = card_id + 1
    for number in numbers:
        if number in winning:
            id_cards[id_to_increase] += number_of_card
            id_to_increase += 1

list(map(matching_cards, cards))
print(sum(id_cards.values()))
