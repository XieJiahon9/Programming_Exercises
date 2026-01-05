#创建一个名为test_cities.py的程序，对刚编写的函数进行测试。
#编写一个名为test_city_country()的函数，核实在使用类似于'santiago'和'chile'这样的值来调用该函数时，得到的字符串是正确的。
#运行测试，确认test_city_country() 通过了。
from city_functions import city_country

def test_city_coutry():
    cc_str = city_country("santiago", "chile")
    assert cc_str == "Santiago, Chile"