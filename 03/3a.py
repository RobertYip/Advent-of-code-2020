with open('C:\\Users\\Ry\\Documents\\Advent-of-code-2020\\03\\input.txt') as f:
    data = [line.split() for line in f]

vlength = len(data)-1
hlength = len(data[1][0])-1


count=0
i=0
j=0
while (i < vlength):
    i += 1
    j += 3
    if j >= hlength:
        j = j - hlength - 1
    if data[i][0][j] == "#":
        count += 1
print(count)
