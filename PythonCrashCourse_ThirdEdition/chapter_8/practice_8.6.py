#练习8.6 城市名：编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。
#这个函数应返回一个格式类似于下面的字符串：
#"Santiago, Chile"
def city_coutry(city, country):
    """ 城市描述 """
    return f'"{city}, {country}"'

print(city_coutry('FuZhou', 'China'))
print(city_coutry(city='Santiago', country='Chile'))
print(city_coutry(country='Island', city='Reykjavik'))
