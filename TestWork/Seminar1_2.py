list = [1, 3, 2, 0, -5, 8, 3, 15]
print (list)

#print (min(list))
#print (max(list))
max = list[0]
min = list[0]
for i in range (len(list)):
    if list[i] > max:
        max = list[i]
    if list[i] < min:
        min = list[i]
print (max , min)
