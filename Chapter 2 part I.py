with open('skyphrases') as f:
    data = [x.split() for x in f]

print(data)
x = 0
for elem in data:
    if len(elem) == len(set(elem)):
        x += 1
print(x)
