#练习4.8 立方：将同一个数乘三次称为立方。例如，在Python中，2的立方用2**3表示。
#创建一个列表，其中包含前10个整数（1～10）的立方，再使用一个for循环将这些立方数打印出来。
cube_number = []
for number in range(1, 11):
    cube_number.append(number**3)
    #print(number**3)
for number in cube_number:
    print(number)