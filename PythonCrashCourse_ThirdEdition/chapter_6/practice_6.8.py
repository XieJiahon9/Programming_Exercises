#练习6.8 宠物：创建多个表示宠物的字典，每个字典都包含宠物的类型及其主人的名字。
#将这些字典存储在一个名为pets的列表中，再遍历该列表，并将有关每个宠物的所有信息打印出来。
pet1 = {'name':'Brian', 'category':'dog', 'master':'Peter'}
pet2 = {'name':'Tom', 'category':'cat', 'master':'a lady'}
pet3 = {'name':'Pochi', 'category':'dog', 'master':'Shin'}

pets = [pet1, pet2, pet3]
for pet_info in pets:
    for attribute, info in pet_info.items():
        print(f"{attribute}:{info}")
    print("----------------------------")
