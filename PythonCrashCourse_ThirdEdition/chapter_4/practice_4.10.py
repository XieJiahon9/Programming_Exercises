#练习4.10 切片：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
#打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
#打印消息“Three items from the middle of the listare:”，再使用切片来打印列表中间的三个元素。
#打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
odd_numbers = [number for number in range(1,21,2)] #practice_4.6
for number in odd_numbers:
    print(number)

print("------------------------------------------------")

print("The first three items in the list are:")
for number in odd_numbers[:3]:
    print(number)

print("Three items from the middle of the listare:")
for number in odd_numbers[4:7]:
    print(number)

print("The last three items in the list are:")
for number in odd_numbers[-3:]:
    print(number)