#练习6.1 人：使用一个字典来存储一个人的信息，包括名、姓、年龄和居住的城市。
#该字典应包含键 first_name、last_name、age 和 city。将存储在该字典中的每项信息都打印出来。
personal_information = {'first_name':'Griffin', 'last_name':'Peter', 'age':45, 'city':'Quahog'}
print(personal_information,"\n")
for information in personal_information:
    print(f"{information} : {personal_information[information]}")
