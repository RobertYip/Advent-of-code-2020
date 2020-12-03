with open('C:\\Users\\Ry\\Documents\\Advent-of-code-2020\\03\\input.txt') as f:
    data = [line.split() for line in f]

vlength = len(data)-1
hlength = len(data[1][0])-1

slopes = [(1, 1),
          (1, 3),
          (1, 5),
          (1, 7),
          (2, 1)]

totalcount = 1

for s in slopes:
    i = 0
    j = 0
    count = 0
    while (i < vlength):
        i += s[0]
        j += s[1]
        if j >= hlength:
            j = j - hlength - 1
        if data[i][0][j] == "#":
            count += 1
    totalcount *= count
print(totalcount)
