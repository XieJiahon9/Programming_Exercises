#练习6.5 河流：创建一个字典，在其中存储三条河流及其流经的国家。例如，一个键值对可能是'nile':'egypt'。
#使用循环为每条河流打印一条消息，如下所示。
#The Nile runs through Egypt.
#使用循环将该字典中每条河流的名字打印出来。
#使用循环将该字典包含的每个国家的名字打印出来。
rivers= {
    'Nile River': ["Egypt", "Sudan", "South Sudan", "Ethiopia", "Uganda"],
    'Amazon River': ["Brazil", "Peru", "Colombia", "Bolivia"],
    'Ganges River': ["India", "Bangladesh"],
}

for river_name,coutries in rivers.items():
    for coutry in coutries:
        print(f"The {river_name} runs through {coutry}.")
    print("---------------------------------------")