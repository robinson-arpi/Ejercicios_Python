def two_sum(numbers, tarjet):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i]+ numbers[j] == tarjet:
                return [i,j]
                    
print(two_sum([1, 2, 3], 4))
