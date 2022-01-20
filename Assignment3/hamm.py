#function
def distances(first, second):
    #seqences of same length
    distance  = 0

    #compare two sequences
    for x, y in zip(first, second):

        #If nucleotides not same, distance + 1
        if x != y:
            distance += 1

    #retunring the result 
    return distance

#open file 
f = open("dati.txt", "r").readlines()
#extract sequence 
seq = [line.strip('\n') for line in f]

#giving result 
print(distances(seq[0], seq[1])) #are two sequences, the first and the second
