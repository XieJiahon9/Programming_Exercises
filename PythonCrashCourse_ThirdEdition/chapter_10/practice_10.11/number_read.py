#练习10.11 喜欢的数：编写一个程序，提示用户输入自己喜欢的数，并使用json.dumps()将这个数存储在文件中。
#再编写一个程序，从文件中读取这个值，并打印如下消息。
#I know your favorite number! It's _____.
import json
from pathlib import Path

path = Path("favorite_number.txt")

try:
    contents = path.read_text()
except FileNotFoundError:
    print(f"Flie {path} not found.")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")
