n = []
with open('C:\\Users\\Ry\\Documents\\Advent-of-code-2020\\01\\input.txt', 'r') as my_file:
    for line in my_file:
        n.append(int(line.strip('\n')))

for i in range(len(n)-1):
    for j in range(i+1, len(n)):
        if n[i]+n[j]==2020:
            print("Part1:", n[i]*n[j])

for i in range(len(n)-1):
    for j in range(i+1, len(n)):
        for k in range(j+1, len(n)):
            if n[i]+n[j]+n[k]==2020:
                print("Part2:",n[i]*n[j]*n[k])