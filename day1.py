digits = [ ('one', '1'), ('two', '2'), ('three', '3')
         , ('four', '4'), ('five', '5'), ('six', '6')
         , ('seven', '7'), ('eight', '8'), ('nine', '9')
         ]

def modify(line):
    for (text, digit) in digits:
        line = line.replace(text, text + digit + text)
    return line

def get_digits(line):
    allDigits = list(filter(str.isdigit, line))
    return int(allDigits[0] + allDigits[-1])

with open('input1.txt', 'r') as f:
    lines = f.readlines()

# part 1
print(sum(map(get_digits, lines)))

# part 2
lines = map(modify, lines)
print(sum(map(get_digits, lines)))
