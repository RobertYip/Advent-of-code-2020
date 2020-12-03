with open('C:\\Users\\Ry\\Documents\\Advent-of-code-2020\\02\\input.txt') as f:
    data=[line.split() for line in f]

result = 0
for line in data:
    count = 0
    key = line[1][0]
    test = line[2]
    min = int(line[0].split('-')[0])
    max = int(line[0].split('-')[1])
    for i in test:
        if i == key:
            count += 1;
    if min <= count <= max:
        result += 1;
print(result)