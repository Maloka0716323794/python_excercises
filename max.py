def fizz_buzz(max):
    nums = []
    for i in range(0, max):
        if((i % 4 == 0 or i % 6 == 0) and  (i % 4 != 0 or  i % 6 != 0)):
            nums.append(i)

            i += 1
    return nums
print(fizz_buzz(20))