#defining the function
def rabit(n,k):

    m = [0]
    for x in range(1,n+1,1):
        if x <= 2:
            f = 1
        else: 
            f = m[x-1] + k*m[x-2]
        m.append(f)
    return m[n]

#taking inputs and printing results
a = 33
b = 4
print(rabit(a,b))