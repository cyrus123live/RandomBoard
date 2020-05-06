import random

randomNums = []

def print2DArray (array):
    for i in range(10):
        for j in range(10):
            numberAsString = str(randomNums[i][j])
            print(numberAsString, end=" ")
        print(" ")

def findSum (array):
    sum = 0
    for i in range(10):
        for j in range(10):
            sum = sum + randomNums[i][j]
    print("-" * 25)
    print("The sum is " + str(sum))
    print("-" * 25)

for i in range(10):
    list = []
    for j in range(10):
        list.append(round(random.random() * 10))
    randomNums.append(list)

print2DArray(randomNums)

findSum(randomNums)
