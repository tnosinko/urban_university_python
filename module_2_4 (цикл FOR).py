# numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# primes=[]
# not_primes=[]
#
# for i in numbers:
#     print(numbers)
#
#
# new_ = int(input('введите число n:'))
#
# for i in range(len(numbers)):
#     is_primes = True
#     n = numbers[i]
#     if n < 2:
#         print(n)
#         continue
#     else:
#         f = n ** (1 / 2)
#         for a in range(2, int(f + 1)):
#             if n % a == 0:
#                 is_primes = False
#                 break
#         print(i, end='')

#
# import math
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
#
# for digits in numbers:
#     is_prime = True
#
#     if digits < 2:
#         is_prime = False
#         continue
#
#     for  divider in range(2, int(math.sqrt(digits)) + 1):
#         if digits % divider == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         primes.append(digits)
#     else:
#         not_primes.append(digits)
#
# print(f"Исходный код:\nnumbers = {numbers}")
# print(f"Primes: {primes}")
# print(f"Not Primes: {not_primes}")


name = "Irina"
age = 25
new_age = age + 1

print(f"Вас зовут {name}, вам {age}, \nв следующем году вам будет {new_age}")