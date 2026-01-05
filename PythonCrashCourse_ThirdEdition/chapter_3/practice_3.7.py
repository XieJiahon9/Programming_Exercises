#练习3.7 缩短名单：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
#以完成练习3.6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
#使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知道你很抱歉，无法邀请他来共进晚餐。
#对于余下两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀之列。
#使用del将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实名单在程序结束时确实是空的。
person_invited = ["Joe Swanson", "Cleveland Brown", "Glenn Quagmire", "Herbert"] #from Famili Guy
print(f"Hellow {person_invited[0].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[1].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[2].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[3].title()},Would you like to go to dinner?")

print("-------------------------------------------------------------------")

print(f"Oh, {person_invited[-1]} can't go to the dinner!")
person_invited[-1] = "Tom Tucker"
print(f"Hellow {person_invited[0].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[1].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[2].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[3].title()},Would you like to go to dinner?")

print("-------------------------------------------------------------------")

print("Guys, I found a bigger table!")
person_invited.insert(0,"Bonnie Swanson")
person_invited.insert(3, "Loretta Brown")
person_invited.append("Jake Tucker")
print(f"Hellow {person_invited[0].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[1].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[2].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[3].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[4].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[5].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[6].title()},Would you like to go to dinner?")

print("-------------------------------------------------------------------")

print("Oh sorry, I can only invite two people to dinner!")
print(f"{person_invited.pop(5)}, I'm sorry that i can't invite you come to dinner!")
print(f"{person_invited.pop(4)}, I'm sorry that i can't invite you come to dinner!")
print(f"{person_invited.pop(3)}, I'm sorry that i can't invite you come to dinner!")
print(f"{person_invited.pop(2)}, I'm sorry that i can't invite you come to dinner!")
print(f"{person_invited.pop( )}, I'm sorry that i can't invite you come to dinner!")
print()
print(f"Hi {person_invited[0]}, you are still on the list for the dinner!")
print(f"Hi {person_invited[1]}, you are still on the list for the dinner!")
print()
del person_invited[0]
del person_invited[0]
print("The final list of dinner: ",person_invited)