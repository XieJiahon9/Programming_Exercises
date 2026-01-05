#练习10.12 记住喜欢的数：将你在完成练习10.11时编写的两个程序合而为一。
#如果存储了用户喜欢的数，就向用户显示它，否则提示用户输入自己喜欢的数并将其存储在文件中。运行这个程序两次，看看它是否像预期的那样工作。
import json
from pathlib import Path

def number_write(path):
    """ 写入用户最喜爱数字 """
    try:
        number = int(input("Please enter your favorite number: "))
    except ValueError:
        print("Enter the correct content!")
    else:
        contents = json.dumps(number)
        path.write_text(contents)

def number_read(path):
    """ 读出用户最喜爱数字 """
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Flie {path} not found.")
    else:
        number = json.loads(contents)
        print(f"I know your favorite number! It's {number}.")


path = Path("favorite_number.txt")
if path.exists():
    number_read(path)
else:
    number_write(path)



