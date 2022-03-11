def calc(n):
    sum = 0
    for i in range(0, 4):
        sum += int(input())
    return sum

print ("Insert Number : ")
count = int(input())
while count <= 0:
    count = int(input())
print("Sum = ", calc(count))