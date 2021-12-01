lines = open('input.txt', 'r').read().splitlines()
lines = list(map(lambda x: int(x), lines))

increments = -1
last = 0
for line in lines:
    if line > last:
        last = line
        increments += 1

print(increments)
