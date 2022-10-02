
num = input('Введите вещественное число: ')
def digit_after_dot_counter (num:float):
    count = 0
    div = 1
    while True:
        if not (num*div == int(num*div)):
            count+=1
            div*=10
        else: break
    return count
print (digit_after_dot_counter(num))

# abs - число по модулю