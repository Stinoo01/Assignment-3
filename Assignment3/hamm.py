def Distance(first, second):
    #seqences of same length
    long  = 0

    #compare two sequences
    for x, y in zip(first, second):

        #If nucleotides not same, distance + 1
        if x != y:
            long += 1

    #retunring the result 
    return long

#must open the folder before, with this document inside 
f = open("dati.txt", "r").readlines()
f = list(map(lambda x: x.replace("\n", ""), f))
    
#giving result 
print(Distance(f[0], f[1]))