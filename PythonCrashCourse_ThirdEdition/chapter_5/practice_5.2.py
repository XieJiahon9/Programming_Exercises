#练习5.2 更多条件测试：你并非只能创建10个条件测试。如果想尝试做更多的比较，可再编写一些条件测试，并将它们加入conditional_tests.py。
#对于下面列出的各种情况，至少编写两个条件测试，结果分别为True和False。
#检查两个字符串是否相等和不等。
str = "Python"
print("Python?", str == "Python")
print("JAVA?", str == "JAVA")

#使用lower()方法的条件测试。
print("\npython?(Case insensitive)", str.lower() == "python")
print("PYTHON?(Case insensitive)", str.lower() == "PYTHON".lower())
print("JAVA?(Case insensitive)", str.lower() == "JAVA".lower())

#涉及相等、不等、大于、小于、大于等于和小于等于的数值比较。
number = 8
print("\n>2?", number > 2)
print("<2?", number < 2)
print(">=2?", number >= 2)
print("<=2?", number <= 2)
print("==2?", number == 2)
print("\n>8?", number > 8)
print("<8?", number < 8)
print(">=8?", number >= 8)
print("<=8?", number <= 8)
print("==8?", number == 8)
print("\n>13?", number > 13)
print("<13?", number < 13)
print(">=13?", number >= 13)
print("<=13?", number <= 13)
print("==13?", number == 13)

#使用关键字and和or的条件测试。
age1 = 18
age2 = 22
print("\nAll ages bigger than 16?(include 16)", (age1 >= 16) and (age2 >= 16))
print("All ages bigger than 20?(include 20)", (age1 >= 20) and (age2 >= 20))
print("Any ages bigger than 20?(include 20)", (age1 >= 20) or (age2 >= 20))
print("Any ages small than 13?(include 13)", (age1 <= 13) or (age2 <= 13))

#测试特定的值是否在列表中。
number_list = [9, 6, 7, 2, 0, 3]
print("\nIs number 6 in the list?", 6 in number_list)
print("Is number 5 in the list?", 5 in number_list)

#测试特定的值是否不在列表中。
print("\nIs number 6 not in the list?", 6 not in number_list)
print("Is number 5 not in the list?", 5 not in number_list)
