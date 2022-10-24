num_array = [int(i) for i in input('Введите числа через пробел: ').split()]

lenghtArray = len(num_array)

count=0

for run in range(lenghtArray-1):
    for i in range(lenghtArray-1):
        if num_array[i]>num_array[i+1]:
            count+=1
            num_array[i],num_array[i+1] = num_array[i+1], num_array[i]


print(num_array)