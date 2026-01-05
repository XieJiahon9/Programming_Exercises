#练习8.15 打印模型：将示例printing_models.py中的函数放在一个名为printing_functions.py的文件中。
#在printing_models.py的开头编写一条import语句，并修改这个文件以使用导入的函数。

#printing_functions.py
def print_models(unprinted_designs, completed_models):
    """ 模拟打印每个设计，直到没有未打印的设计为止打印每个设计后，都将其移到列表completed_models中 """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """ 显示打印好的所有模型 """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)