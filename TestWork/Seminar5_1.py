n = int(input('Введите число 1: '))
m = int(input('Введите число 2: '))

# if m%n==0 and n%n==0:
#     print (f'наименьшее общее кратное {n}')
# elif n%m==0 and m%m==0:
#     print (f'наименьшее общее кратное {m}')
# else:
#     print ('хз')

k = max(m,n)
print (k)

while True:
    if k % m ==0 and k % n == 0:
        z = k
        break
    k+=1

print (z)