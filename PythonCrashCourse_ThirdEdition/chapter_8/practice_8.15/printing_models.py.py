#练习8.15 打印模型：将示例printing_models.py中的函数放在一个名为printing_functions.py的文件中。
#在printing_models.py的开头编写一条import语句，并修改这个文件以使用导入的函数。

#printing_models.py
import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)