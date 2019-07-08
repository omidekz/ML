def is_satisfying(hypothesis, instance):
    if len(instance) < len(hypothesis):
        return False, -1
    for i in range(len(hypothesis)):
        if hypothesis[i] == instance[i] or hypothesis[i] == '?':
            continue
        return False, i
    return True, ''


def coincide(hypothesis, instance):
    for i in range(len(hypothesis)):
        if hypothesis[i] == instance[i]:
            continue
        elif hypothesis[i] == '!':
            hypothesis[i] = instance[i]
        else:
            hypothesis[i] = '?'
    return hypothesis


def is_positive(instance):
    return instance[6] == 'Yes'


def more_specific_general(general, instance, expected: bool):
    counter = 0
    while True:
        if counter >= len(general):
            break
        if is_satisfying(general[counter], instance)[0] is not expected:
            general.pop(counter)
        else:
            counter += 1


# data shape:
# <sky, temp, humidity, wind, water, forcast, enjoy>
examples = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

specific = ['!', '!', '!', '!', '!', '!']
generals = [['?', '?', '?', '?', '?', '?']]

for example in examples:
    if is_positive(example):
        specific = coincide(specific, example)
        more_specific_general(generals, example, expected=True)
    else:
        more_specific_general(generals, example, expected=False)
        for i in range(len(specific)):
            now = ['?', '?', '?', '?', '?', '?']
            if specific[i] == example[i] or specific[i] == '?':
                continue
            now[i] = specific[i]
            generals.append(now)

print('specific:', specific)
print('\ngenerals:')
for g in generals:
    print(g)
