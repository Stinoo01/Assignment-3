import string


def writing(dna):
	DNA=""
	for i in range(len(dna)):
		if(dna[i]=='A'):
			DNA+='T'
		elif(dna[i]=='T'):
			DNA+='A'
		elif(dna[i]=='C'):
			DNA+='G'
		elif(dna[i]=='G'):
			DNA+='C'
	return DNA

def reverse(dnas):
	return dnas[len(dnas)::-1]
#first input is the fasta format: skip 
fasta=input()
#second input is the file. make sure tht the file has no spaces.
DNA_string=input()
for i in range(len(DNA_string)):
	for j in range(4,14):
		if (DNA_string[i:i+j]==reverse(writing(DNA_string[i:i+j]))and i+j<=len(DNA_string)):
			print(i+1, end=" ")
			print(j)