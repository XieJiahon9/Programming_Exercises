#练习11.2 人口数量：修改前面的函数，使其包含第三个必不可少的形参population，并返回一个格式为City,Country - population xxx的字符串，
#如Santiago,Chile - population 5000000。运行测试，确认test_city_country()未通过。
#修改上述函数，将形参population设置为可选的。再次运行测试，确认test_city_country()又通过了。
#再编写一个名为test_city_country_population()的测试，核实可以使用类似于 'santiago'、'chile' 和'population=5000000' 这样的值来调用这个函数。
#再次运行测试，确认test_city_country_population()通过了。

#def city_country(city, country, population_number):
#    """ 返回格式为City, Country - population xxx的字符串 """
#    return f"{city.title()}, {country.title()} - population {population_number}"

def city_country(city, country, population_number):
    """ 返回格式为City, Country - population xxx的字符串 """
    return f"{city.title()}, {country.title()} - population {population_number}"

