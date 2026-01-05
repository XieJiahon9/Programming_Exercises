#练习4.6 奇数：通过给range()函数指定第三个参数来创建一个列表，其中包含1～20的奇数，再使用一个for循环将这些数打印出来。
odd_numbers = [number for number in range(1,21,2)]
for number in odd_numbers:
    print(number)