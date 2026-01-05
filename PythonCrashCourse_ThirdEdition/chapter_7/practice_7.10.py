#练习7.10 梦想中的度假胜地：编写一个程序，调查用户梦想中的度假胜地。
#使用类似于“If you could visit one place in the world, where would you go?”的提示，并编写一个打印调查结果的代码块。
Vacation_destinations = {}
while True:
    name = input("What is your name?(Enter 'quit' to quit.) ")
    place = input("If you could visit one place in the world, where would you go?(Enter 'quit' to quit.) ")

    if name == 'quit' or place == 'quit':
        break
    else:
        Vacation_destinations[name] = place

    repeat = input("Would u like to let another person respond?(yes/no)")
    if repeat == 'no':
        break


print("--------Poll Results--------")
for name,place in Vacation_destinations.items():
    print(f"{name}'s favorite vacation destination is {place}.")