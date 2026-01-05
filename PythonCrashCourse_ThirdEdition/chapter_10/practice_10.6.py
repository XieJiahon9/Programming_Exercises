#练习10.6 加法运算：在提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数。
#在这种情况下，当你尝试将输入转换为整数时，将引发ValueError异常。
#编写一个程序，提示用户输入两个数，再将它们相加并打印结果。
#在用户输入的任意一个值不是数时都捕获ValueError异常，并打印一条友好的错误消息。
#对你编写的程序进行测试：先输入两个数，再输入一些文本而不是数。
try:
    dividend = float(input("Please enter the dividend: ")) #被除数
    divisor = float(input("Please enter the dividend: ")) #除数
except ValueError:
    print("Please enter the correct content!")
else:
    result = dividend / divisor
    print(result)