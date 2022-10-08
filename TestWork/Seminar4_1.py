# Считайте из файла список чисел. Напишите программу, которая найдет большее и меньшее число и запишет их в отдельный файл.
# В качестве символа разделителя используйте пробел 

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

# pathRead = r"text.txt"
# pathWrite = r"file2.txt"

# try:
# with open (pathRead) as data:
# file = data.read().split(" ")
# except:
# print("Файл не найден")

# listInt = []

# for elem in file:
# if elem.isdigit():
# listInt.append(int(elem))

# try:
# with open (pathWrite, 'w') as data:
# data.write(str(min(listInt)))
# data.write('\n')
# data.write(str(max(listInt)))
# except:
# print("Ошибка работы с файлом")