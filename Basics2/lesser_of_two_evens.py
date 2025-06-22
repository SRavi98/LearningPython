def lesser_of_two_evens(a,b):
    if a%2 == 0 == b%2:
        return a if a<b else b
    else:
        return b if b%2 != 0 else a
    

print(lesser_of_two_evens(2, 6))
print(lesser_of_two_evens(2, 5))