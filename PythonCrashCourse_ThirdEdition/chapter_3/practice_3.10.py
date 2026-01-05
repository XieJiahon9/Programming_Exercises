#练习3.10 尝试使用各个函数：想想可存储到列表中的东西，如山川、河流、国家、城市、语言或你喜欢的任何东西。
#编写一个程序，在其中创建一个包含这些元素的列表。然后，至少把本章介绍的每个函数都使用一次来处理这个列表。
from pydoc import plain

places_iwant = ["Reykjavik", "New York", "Fuzhou", "Antarctica", "Las Vegas", "Sicily"]
#访问列表
print(places_iwant)
print(places_iwant[0].title())
print(places_iwant[3].upper())
print(places_iwant[5].lower())
#使用列表值
message = f"I would like to go to {places_iwant[0]}"
print(message)
#添加
places_iwant.append("AAAAA")
places_iwant.insert(0, "BBBBB")
print(places_iwant)
#修改
places_iwant[0] = "CCCCC"
print(places_iwant)
#删除
del places_iwant[0]
print(places_iwant)
place_pop1 = places_iwant.pop()
place_pop2 = places_iwant.pop(3)
print(places_iwant)
print(f"Eliminated places are {place_pop1} and {place_pop2}")
place_removed = "New York"
places_iwant.remove(place_removed)
print(places_iwant)
print(f"Removed places are {place_removed}")
#管理
print(places_iwant)
print(sorted(places_iwant))
print(places_iwant)
print(sorted(places_iwant, reverse=True))
print(places_iwant)
places_iwant.reverse()
print(places_iwant)
places_iwant.reverse()
print(places_iwant)
places_iwant.sort()
print(places_iwant)
places_iwant.sort(reverse=True)
print(places_iwant)
print(f"The length of the list is {len(places_iwant)}")