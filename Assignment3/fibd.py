#defing function 
def rabbits(n, k):
    #n = month
    #k = life of a rbbit
    
    rabbit = []
    #in the first month, the n of rabbit is 1. 
    rabbit.append(0)
    rabbit.append(1)

    #range between minimun number of rabbits (1) and the input 
    for x in range(1, n):
        
        if x < k:
            rabbit.append(rabbit[x] + rabbit[x-1])
        if x == k:
            rabbit.append(rabbit[x] + rabbit[x-1] - rabbit[x-k+1])
        if x > k:
            rabbit.append(rabbit[x] + rabbit[x-1] - rabbit[x-k])

    #returning the result 
    return rabbit[n]

#printing result taking the inputs (100 & 17)
print(rabbits(100,17))