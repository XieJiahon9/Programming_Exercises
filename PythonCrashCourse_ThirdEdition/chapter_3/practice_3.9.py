#练习3.9 晚餐嘉宾：选择你为完成练习3.4～练习3.7而编写的一个程序。
#在其中使用len()打印一条消息，指出你邀请了多少位嘉宾来共进晚餐。
person_invited = ["Joe Swanson", "Cleveland Brown", "Glenn Quagmire", "Herbert"] #from Famili Guy
print(f"Hellow {person_invited[0].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[1].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[2].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[3].title()},Would you like to go to dinner?")
print(len(person_invited))

print("-------------------------------------------------------------------")

print(f"Oh, {person_invited[-1]} can't go to the dinner!")
person_invited[-1] = "Tom Tucker"
print(f"Hellow {person_invited[0].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[1].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[2].title()},Would you like to go to dinner?")
print(f"Hellow {person_invited[3].title()},Would you like to go to dinner?")
print(len(person_invited))

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
print(len(person_invited))

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
print(len(person_invited))
print()
del person_invited[0]
del person_invited[0]
print(f"The final list of dinner:{person_invited}. The length of this list is:{len(person_invited)}.")

