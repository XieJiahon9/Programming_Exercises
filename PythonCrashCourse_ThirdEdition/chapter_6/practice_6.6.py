#练习6.6 调查：在6.3.1节编写的程序favorite_languages.py中执行以下操作。
#创建一个应该会接受调查的人的名单，其中有些人已在字典中，而其他人不在字典中。
#遍历这个名单。对于已参与调查的人，打印一条消息表示感谢；对于还未参与调查的人，打印一条邀请参加调查的消息。
favorite_languages = {    #6.3.1代码
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("----------------------------------------")

#本节任务代码
servey_respondents = ["sarah",  "peter", "mike"]
print(f"The list of servey_respondents :{servey_respondents}")
for name in servey_respondents:
    if name in favorite_languages:
        print(f"{name.title()}, thank u for taking our poll!")
    else:
        print(f"{name.title()}, please take our poll!")