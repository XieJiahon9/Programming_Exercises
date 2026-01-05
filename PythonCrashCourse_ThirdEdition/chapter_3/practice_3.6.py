#练习3.6 添加嘉宾：你刚找到了一张更大的餐桌，可容纳更多的嘉宾就座。请想想你还想邀请哪三位嘉宾。
#以完成练习3.4或练习3.5时编写的程序为基础，在程序末尾添加函数调用print()，指出你找到了一张更大的餐桌。
#使用insert()将一位新嘉宾添加到名单开头。
#使用insert()将另一位新嘉宾添加到名单中间。
#使用append()将最后一位新嘉宾添加到名单末尾。
#打印一系列消息，向名单中的每位嘉宾发出邀请。
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
