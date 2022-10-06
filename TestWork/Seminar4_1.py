# Считайте из файла список чисел. Напишите программу, которая найдет большее и меньшее число и запишет их в отдельный файл.
# В качестве символа разделителя используйте пробел 




# mylist = []
# with open("text.txt") as f:
#     for i in f:
#         mylist.append([int(x for x in i.split())])
# print (mylist)


data = open ('PythonWork/TestWork/text.txt', 'r')
file = data.read().split(" ")
data.close()
print(file)
maxx=minn=int(file[0])
for i in range (len(file)):
    if file[i].isdigit:
        file[i]=int(file[i])
print (file)
print(min(file), max(file))
a = min(file)
b = max(file)
data = open ('PythonWork/TestWork/textNew.txt', 'w')
data.write(f'{a} {b}')
data.close()