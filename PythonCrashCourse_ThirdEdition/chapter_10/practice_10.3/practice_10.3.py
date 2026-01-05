#练习10.3 简化代码：本节前面的程序file_reader.py中使用了一个临时变量lines，来说明splitlines()的工作原理。
#可省略这个临时变量，直接遍历splitlines()返回的列表：for line in contents.splitlines():
#对于本节的每个程序，都删除其中的临时变量，让代码更简洁。

#file_reader.py
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)