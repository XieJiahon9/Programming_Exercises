#练习11.3 雇员：编写一个名为Employee的类，其__init__()方法接受名、姓和年薪，并将它们都存储在属性中。
#编写一个名为give_raise()的方法，它默认将年薪增加5000美元，同时能够接受其他的年薪增加量。
#为Employee类编写一个测试文件，其中包含两个测试函数：test_give_default_raise()和test_give_custom_raise()。
#在不使用夹具的情况下编写这两个测试，并确保它们都通过了。然后编写一个夹具，以免在每个测试函数中都创建一个Employee对象。
#重新运行测试，确认两个测试都通过了。
from employee import Employee
import pytest

#def test_give_default_raise():
#    emp = Employee("Brian", "Griffin", 60000)
#    emp.give_raise()
#    assert emp.annual_salary == 65000

#def test_give_custom_raise():
#    emp = Employee("Brian", "Griffin", 60000)
#    emp.give_raise(30000)
#    assert emp.annual_salary == 90000

@pytest.fixture
def employee_example():
    emp = Employee("Brian", "Griffin", 60000)
    return emp

def test_give_default_raise(employee_example):
    employee_example.give_raise()
    assert employee_example.annual_salary == 65000

def test_give_custom_raise(employee_example):
    employee_example.give_raise(30000)
    assert employee_example.annual_salary == 90000