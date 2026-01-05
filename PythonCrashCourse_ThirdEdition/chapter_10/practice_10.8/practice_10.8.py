#练习10.8 猫和狗：创建文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
#编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。
#将这些代码放在一个try-except代码块中，以便在文件不存在时捕获FileNotFoundError异常，并显示一条友好的消息。
#将任意一个文件移到另一个地方，并确认except代码块中的代码将正确地执行。
from pathlib import Path

path_cats = Path("cats.txt")
path_dogs = Path("dogs.txt")

try:
    cats = path_cats.read_text()
    dogs = path_dogs.read_text()
except FileNotFoundError:
    print("Some file not found.")
else:
    print(f"cats:\n{cats}\n")
    print(f"dogs:\n{dogs}\n")


