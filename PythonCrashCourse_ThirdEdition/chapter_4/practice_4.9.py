#练习4.9 立方推导式：使用列表推导式生成一个列表，其中包含前10个整数的立方。
cube_number = [value**3 for value in range(10)] #列表推导式，前十个数为0~9
print(cube_number)
