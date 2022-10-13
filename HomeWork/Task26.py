# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc


Eq1 = r'PythonWork/HomeWork/Text26_1.txt'
Eq2 = r'PythonWork/HomeWork/Text26_2.txt'

try:
    with open (Eq1) as data:
        file1 = data.read()
except:
    print ('Ошибка чтения')

print (file1)

def rle (file1):
    count = 1
    resfile = ''
    for i in range (len(file1)-1):
        if file1[i] == file1[i+1]:
            count+=1
        else:
            resfile = resfile + str(count) + file1[i]
            count = 1
    if count > 1 or (file1[len(file1)- 2] != file1 [-1]):
        resfile = resfile + str(count) + file1[-1]
    return resfile

resfile = rle(file1)
print (resfile)

def outRle (resfile):
    num = ''
    newresfile = ''
    for i in range (len(resfile)):
        if not resfile[i].isalpha():
            num+=resfile[i]
        else:
            newresfile = newresfile + resfile[i] * int(num)
            num = ''
    return newresfile

newresfile = outRle(resfile)
print (newresfile)

try:
    with open (Eq2, 'w') as data:
        data.write(resfile)
except:
    print("Ошибка обработки файла")