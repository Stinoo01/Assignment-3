#importing permutation
from itertools import permutations

#defining the function
def permutation(input):

    #defining count and permutation 
    count = 0
    number = list(permutations(range(1, input + 1)))

    #printing the total number of permutations
    for x in number:
        count+=1
    print(count)

    #printing the possible permutation with a space
    for x in number:
        print(' '.join(map(str,x)))

#giving input
a = 5
#executing the programme 
permutation(a)