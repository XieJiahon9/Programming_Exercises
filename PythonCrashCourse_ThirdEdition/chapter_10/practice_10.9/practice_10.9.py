#练习10.9 静默的猫和狗：修改你在练习 10.8 中编写的except代码块，让程序在文件不存在时静默失败。
from pathlib import Path

def read(path_name):
    """ 阅读文件_遇错静默失败 """
    try:
        name = path_name.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"{name}\n")

path_cats = Path("cats.txt")
path_dogs = Path("dogs.txt")

read(path_cats)
read(path_dogs)