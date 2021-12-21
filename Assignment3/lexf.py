#importing necessary
import itertools

#gining input: 
#symbols 
list_of_symbols = ['A','B','C','D','E','F'] 
#number of cominations 
number = 3

#combine every symbol with each other
def alphabet(n, k):
    #making sure the symbol combine also with itself and with all the symbols all the time 
    combination = itertools.product(n, repeat=k)
    #returnin result
    return combination

#printin result 
for x in alphabet(list_of_symbols, number):
    print(''.join(x))