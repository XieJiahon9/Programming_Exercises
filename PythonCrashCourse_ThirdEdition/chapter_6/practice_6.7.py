#练习6.7 人们：在为练习6.1编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people的列表中。
#遍历这个列表，将其中每个人的所有信息都打印出来。
personal_information = {'first_name':'Griffin', 'last_name':'Peter', 'age':45, 'city':'Quahog'}  #6.1代码
print(personal_information,"\n")
for information in personal_information:
    print(f"{information} : {personal_information[information]}")

print("----------------------------------------------"
      "\n----------------------------------------------")

#本节任务代码
personal_information1 = {'first_name':'Griffin', 'last_name':'Lois', 'age':45, 'city':'Quahog'}
personal_information2 = {'first_name':'Griffin', 'last_name':'Brian', 'age':7, 'city':'Quahog'}

people = [personal_information, personal_information1, personal_information2]
for informations_list in people:
    for attribute, content in informations_list.items():
        print(f"{attribute}:{content}")
    print("------------------------------------")
