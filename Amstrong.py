num = input('Enter a number : ')
length = len(num)
sum = 0
print(length)
for i in num:
   sum=int(i)**length+sum
if sum==int(num):
   print(num,'is an amstrong number')
else:
   print(num,'is not an amstrong number')   