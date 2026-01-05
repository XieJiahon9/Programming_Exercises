#练习11.1 城市和国家：编写一个函数，它接受两个形参：一个城市名和一个国家名。这个函数返回一个格式为City, Country的字符串，如Santiago, Chile。
#将这个函数存储在一个名为city_functions.py的模块中，并将这个文件存储在一个新的文件夹中，以免pytest在运行时，尝试运行之前编写的测试。

def city_country(city, country):
    """ 返回格式为City, Country的字符串 """
    return f"{city.title()}, {country.title()}"

