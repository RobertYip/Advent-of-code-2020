#to read single column
#data = open('C:\\Users\\Ry\\Documents\\advent\\01\\input.txt').read().split()

with open('C:\\Users\\Ry\\Documents\\advent\\02\\input2.txt') as f:
    data=[line.split() for line in f]

result = 0
for password in data:
    count = 0
    numrange = password[0]
    key = password[1][0]
    test = password[2]
    min = int(numrange.split('-')[0])
    max = int(numrange.split('-')[1])
    for i in test:
        if i == key:
            count += 1;
    if min <= count and count <= max:
        result +=1;
print(result)