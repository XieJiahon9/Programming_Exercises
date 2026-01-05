#练习9.12 多个模块：将User类存储在一个模块中，并将Privileges类和Admin类存储在另一个模块中。
#再创建一个文件，在其中创建一个Admin实例并对其调用show_privileges()方法，以确认一切依然能够正确地运行。
from privileges_and_admin import Admin

admin = Admin('Xie', 'Jiahong', 21, 'male')
admin.privileges.show_privileges()