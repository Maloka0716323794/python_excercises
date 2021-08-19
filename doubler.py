def double(numbers):
    newArr = []
    for i in range(len(numbers)):
        newArr.append(numbers[i]*2)
    return newArr
print(double(numbers=[1,2,3]))