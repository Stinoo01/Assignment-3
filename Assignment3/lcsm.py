#import 
from Bio import SeqIO      

#opening file                           
f = open('dati.txt', 'r')
#store sequences
sequences = []    
#fixing fasta format    
for line in SeqIO.parse(f, 'fasta'):              
    seq = ''                               
    for x in line.seq:                  
        #write sequence
        seq += x
    #append them                           
    sequences.append(seq)                  

#defining function for finding nucleotides 
def function(input):

    inp_set = set()
    last = input.pop()

    for x in range(len(last)):
        common = True
        y = x
        while common is True:
            y += 1
            for k in input:
                if last[x:y] not in k:
                    common = False
                    y -= 1
                    break
            if common is False or y > len(last):
                break
            inp_set.add(last[x:y])

    inp_set = list(inp_set)

    #returning result 
    return max(inp_set, key=len)

#printing result 
print(function(sequences))
