with open('C:\\Users\\Ry\\Documents\\Advent-of-code-2020\\02\\input.txt') as f:
    data=[line.split() for line in f]

result = 0
for line in data:
    count = 0
    key = line[1][0]
    test = line[2]
    first = int(line[0].split('-')[0])
    second = int(line[0].split('-')[1])
    for i in range(0,len(test)):
        if (i+1) == first and key == test[i]:
            count += 1
            
        if (i+1) == second and key == test[i]:
            count += 1
        
    if count == 1:
        result += 1
print(result)