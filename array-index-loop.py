# This program was written as part of a online coding challenge

# Assignment:
#   Given a array of integers, begin at index position zero. 
#   Using the number value at index zero, travel to the position in the array that corresponds to that integer value.
#   Continue this process of indexing the array based on the number value of the indexed position.
#   Stop this process once the number value of the indexed position is -1.

#A = [1,4,-1,3,2]
A = [1,3,4,2,-1,0]

def solution(inputA):
    temp = inputA[0]
    lengthA = []
    counter = 0
    # counter variable added to prevent an infinite loop when -1 is not in the list
    while (-1 not in lengthA) and (counter < len(inputA)):
        lengthA += [temp]
        counter += 1
        temp = inputA[temp]
    #return lengthA # For Debugging
    return len(lengthA)

print solution(A)