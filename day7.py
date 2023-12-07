with open('input7.txt', 'r') as f:
    lines = f.readlines()

def hand_type(cards):
    max_count = max(map(lambda c: cards.count(c), cards))
    l = len(set(cards))
    if l == 1 or l==2: return max_count+2
    elif l == 3: return max_count+1
    else: return max_count

def joker_type(cards):
    if 'J' not in cards: return hand_type(cards)
    js = cards.count('J')
    max_count = max(map(lambda c: cards.count(c) if c != 'J' else 0, cards))
    l = len(set(cards))
    if l == 1 or l == 2: return 7
    elif l == 3:
        if js == 3 or js == 2 or max_count == 3: return 6
        return 5
    elif l == 4: return 4
    return 2

def run(cardbids, type_function, alphabet):
    func = lambda cardbid: (type_function(cardbid[0]), cardbid[0], cardbid[1])
    cardbids = list(map(func, cardbids))
    cardbids.sort(key=lambda card: (card[0], [alphabet.index(c) for c in card[1]]))
    return sum([(i+1)*cardbid[2] for i, cardbid in enumerate(cardbids)])

func = lambda line: (line.split()[0], int(line.split()[1]))
cardbids = list(map(func, lines))

# part 1
print(run(cardbids, hand_type, '123456789TJQKA'))

# part 2
print(run(cardbids, joker_type, 'J123456789TQKA'))
