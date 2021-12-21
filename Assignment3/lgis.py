#longest increasing sequence
def increasing(numbers, n):
    #storing values
    #int
    int_ = []   
    #list
    list_ = [] 

    #searching all numbers
    for x in range(n):
        int_.append(1)
        #writing numbers in the list
        list_.append([numbers[x]])
        for y in range(x):
            #algorithm for che increaisng order 
            if numbers[y] < numbers[x]:
                int_[x] = max(int_[x], int_[y] + 1)
                if len(list_[x]) <= len(list_[y]):
                    list_[x] = list_[y] + [numbers[x]]
    #print result fixing output 
    print(str(list_[int_.index(max(int_))]).replace(',','').replace('[','').replace(']',''))

#longest decreasing sequence
#same to the other but change >
def decreasing(numbers, n):
    int_ = [] 
    list_ = [] 

    for x in range(n):
        int_.append(1)
        list_.append([numbers[x]])
        for y in range(x):
            #here the only change
            if numbers[y] > numbers[x]:
                int_[x] = max(int_[x], int_[y] + 1)
                if len(list_[x]) <= len(list_[y]):
                    list_[x] = list_[y] + [numbers[x]]
    #print result fixing output 
    print(str(list_[int_.index(max(int_))]).replace(',','').replace('[','').replace(']',''))


#open file and read in the proper way
f = open("dati.txt", "r")
f_ =  int(f.readline().strip())
num = [int(i) for i in f.readline().strip().split(" ")]

#executing, first ascending then decrescending 
increasing(num, f_)
decreasing(num, f_)