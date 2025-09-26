numbers=[]
enumber=[]
oddnumber=[]
Divnumber=[]
for i in range(101):
    if i < 100:
        numbers.append(i+1)
print("          First 100 Numbers")
print(numbers)
 #Even numbers
for i in numbers:
    if i % 2 == 0:
        enumber.append(i)
print('                      Even Numbers')
print(enumber)        
#odd number
for i in numbers:
    if i % 2 != 0:
        oddnumber.append(i)
print('                              Odd number')
print(oddnumber)
for i in numbers:
    if i % 3 ==0 and i % 5 ==0:
        Divnumber.append(i) 
print('                      Multiples of 3and 5')        
print(Divnumber)
