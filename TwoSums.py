def two_sum(arr, objetive):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i]+ arr[j] == objetive:
                return [i,j]
                    
print(two_sum([1, 2, 3], 4))
