'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It's guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

'''

'''
def find_uniq(list):
    for i in list:
        counter = 0
        for j in list:
           if i == j:
               counter = counter + 1
        if counter == 1:
          return i
'''

def find_uniq(arr):
    arr.sort()
    
    # Compare to the first 2 positions
    # If equals the unique numeber is in the final
    # Else the unique number is first
    if arr[0] != arr[1]:
        return arr[0]
    else:
        return arr[-1]


def basic_test_cases():
    assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    
    assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

basic_test_cases()    