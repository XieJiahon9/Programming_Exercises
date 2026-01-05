#练习7.3 10的整数倍：让用户输入一个数，并指出这个数是否是 10 的整数倍。
number = int(input("Please enter a number: "))
if (number % 10) == 0:
    print("This number is multiple of 10!")
else:
    print("This number isn't multiple of 10!")