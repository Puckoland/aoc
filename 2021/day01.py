lines = open('input.txt', 'r').read().splitlines()

increments = -1
last = 0
for line in lines:
    if line > last:
        last = line
        increments += 1

print(increments)
