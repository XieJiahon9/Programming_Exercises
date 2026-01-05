#练习3.8 放眼世界：想出至少5个你想去旅游的地方。
#将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
#按原始排列顺序打印该列表。不要考虑输出是否整洁，只管打印原始Python列表就好。
#使用sorted()按字母顺序打印这个列表，不要修改它。
#再次打印该列表，核实排列顺序未变。
#使用sorted()按与字母顺序相反的顺序打印这个列表，不要修改它。
#再次打印该列表，核实排列顺序未变。
#使用reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
#使用reverse()再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
#使用sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
#使用sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
places_iwant = ["Reykjavik", "New York", "Fuzhou", "Antarctica", "Las Vegas", "Sicily"]
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