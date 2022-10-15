# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

string = 'how quickly the complexity of tasks is growing for example with this absdolbanny it is just terrible'
print (string)
find = input("Введите искомый элемент: ")

jobList = string.split(' ')
# print (jobList)

reslist = [x for x in jobList if not find in x] # и так ранее использовал List Comprehensions

print (' '.join(reslist))

