#练习6.12 扩展：本章的示例足够复杂，能以很多方式进行扩展。请对本章的一个示例进行扩展：添加键和值，调整程序要解决的问题，或改进输出的格式。
favorite_languages = {   #6.2.6节示例，favorite_languages.py
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

print("--------------------------------------------")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'mike': 'C#'
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")