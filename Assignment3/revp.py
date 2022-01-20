#function
def count(dna):
	DNA=""
	for x in range(len(dna)):
		if(dna[x]=='A'):
			DNA+='T'
		elif(dna[x]=='T'):
			DNA+='A'
		elif(dna[x]=='C'):
			DNA+='G'
		elif(dna[x]=='G'):
			DNA+='C'
	return DNA

def reverse(dnas):
	return dnas[len(dnas)::-1] #reverse the string 

#i have to write on the consol the imput from rosalind
#first input is the fasta format
fasta=input() #skip
#second input is the file. make sure that the file has no spaces.
DNA_string=input()
for k in range(len(DNA_string)):
	#palindrome sequence between 4 and 12
	for j in range(4,12):
		if (DNA_string[k:k+j]==reverse(count(DNA_string[k:k+j]))and k+j<=len(DNA_string)):
			#output
			print(k+1, j)
