def is_satisfying(hypothesis, instance):
    if len(hypothesis) != len(instance):
        return False, -1
    for i in range(len(hypothesis)):
        if hypothesis[i] == '?' or hypothesis[i] == instance[i]:
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


# input shape
# <sky, temp, humidity, wind, water, forcast, enjoy>
examples = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Same', 'Yes']
]

hypothesis = ['!', '!', '!', '!', '!', '!']

for example in examples:
    if example[6] == 'No':
        continue
    sat = is_satisfying(hypothesis, example[:6])
    if sat[0]:
        continue
    hypothesis = coincide(hypothesis, example[:6])

print(hypothesis)
