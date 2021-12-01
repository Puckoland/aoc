lines = open('input.txt', 'r').read().splitlines()
lines = list(map(lambda x: int(x), lines))

increments = 0
last = lines[0]
for line in lines:
    if line > last:
        increments += 1
    last = line

print(increments)
