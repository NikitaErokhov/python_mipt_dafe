# print('Введите последова','тельность чисел:', end=" ", sep='А')
# var = input()
# print(type(var))
# print(var)

# l = 16
# k = bin(0)[2:].zfill(l)
# while k != '1'*l:
#     print(k)
#     k = bin(int(k,2)+1)[2:].zfill(l)

# flag = True
# print(flag, type(flag))
# flag &= True
# print(flag, type(flag))

# k = -1
# only_chet = True
# listik = list()
# while k < 11:
#     k+=1
#     if only_chet and k%2:
#         continue
#     listik.append(k)
#     print(listik)
# else:
#     print(listik+[11])

# k = 10
# condition = eval('k>9')
# while [condition]:
#     k+=1
#     print(k)
#     if condition:
#         break

# while True:
#     print(eval(input('Введите выражение: ')))

# k = 1
# n = 5
# while n != 0:
#     divs = set()
#     for d in range(1,round(k**0.5)+1):
#         if k%d==0:
#             divs.add(d)
#             divs.add(k//d)
#     if sum(divs) == k*2:
#         print(f'{5-n+1}. {k}')
#         n-=1
#     k+=1

k = 2
n = 0
stop = 64
summa = 0
while n<=stop:
    summa+=k**n
    n+=1
print(summa)