#练习3.5 修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
#以完成练习3.4时编写的程序为基础，在程序末尾添加函数调用print()，指出哪位嘉宾无法赴约。
#修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
#再次打印一系列消息，向名单中的每位嘉宾发出邀请。
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