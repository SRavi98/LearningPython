def even_number_check(nums):
    evens = []

    for number in range(1, len(nums)+1):
        if number % 2 == 0:
            evens.append(number)
        else:
            pass
    
    return evens


numbersList = [1,2,3,4,5,6,7,8,9,10]
print(even_number_check(numbersList))