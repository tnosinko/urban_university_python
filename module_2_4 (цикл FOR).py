numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes=[]
not_primes=[]

for i in range(len(numbers)):
     is_primes = True
     n = numbers[i]
     if n < 2:
         continue
     else:
         f = n ** (1 / 2)
         for a in range(2, int(f + 1)):
             if n % a == 0:
                 is_primes = False
                 break
         print(i, end='')


