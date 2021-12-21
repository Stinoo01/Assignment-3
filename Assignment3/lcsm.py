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
    return max(inp_set,key=len)

#opening file
with open('dati.txt', 'r') as file:
    content = file.read()

#fixing fasta format
"""
for the fasta format I didn't install biopython yet (my python has some problems and I hope to fix them asap)
so I searched on the interned for some solutions 
and I come up with this one improving and fixing something
"""
DNAs_number = content.count('>')
lines = content.splitlines()
line_number = 0 
DNAs = []
#skipping lines starting with > and returning all the nucleotides on the variable 
for x in range(DNAs_number):
    DNA = ''
    line_number += 1
    while lines[line_number][0] != '>':
        DNA += lines[line_number]
        line_number += 1
        if line_number+1 > len(lines):
            break
    DNAs.append(DNA)

#printing result 
print(function(DNAs))