with open('C:/Users/Krystian/PycharmProjects/TEST2/skyphrases') as f:
    data = [x.split() for x in f]

print(data)
x = 0
for elem in data:
    if len(elem) == len(set(elem)):
        x += 1
print(x)
