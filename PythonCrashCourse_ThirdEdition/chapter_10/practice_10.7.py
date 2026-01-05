#练习10.7 加法计算器：将为练习10.6编写的代码放在一个while循环中，让用户在犯错（输入的是文本而不是数）后能够继续输入数。
while True:
        dividend = input("Please enter the dividend(enter 'q' to quit.): ")  #被除数
        if (dividend == 'q'):
            break

        divisor = input("Please enter the dividend(enter 'q' to quit.): ")  #除数
        if (divisor == 'q'):
            break

        try:
            result = float(dividend) / float(divisor)
        except ValueError:
            print("Please enter the correct content!")
            continue
        else:
            print(result)