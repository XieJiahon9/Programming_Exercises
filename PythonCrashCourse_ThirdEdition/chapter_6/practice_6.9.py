#练习6.9 喜欢的地方：创建一个名为favorite_places的字典。
#在这个字典中，将三个人的名字用作键，并存储每个人喜欢的1～3个地方。
#为让这个练习更有趣些，让一些朋友说出他们喜欢的几个地方。
#遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
favorite_places = {
    "Hong" : ["Reykjavik", "Beijing", "New York"],
    "Zhang" : ["Japan", "UK"],
    "Hao" : ["Fuzhou"],
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"{name}'s favorite places:")
    else:
        print(f"{name}'s favorite place:")

    for place in places:
        print({place})

    print("------------------------------")