#练习10.2 C语言学习笔记：可使用replace()方法将字符串中的特定单词替换为另一个单词。
#下面是一个简单的示例，演示了如何将句子中的'dog'替换为'cat'：
#   >>> message = "I really like dogs."
#   >>> message.replace('dog', 'cat')  !!! replace()方法返回一个新的字符串，而不会修改原始字符串。 !!!
#   'I really like cats.'
#读取你刚创建的文件learning_python.txt中的每一行，将其中的Python都替换为另一门语言的名称，如C。将修改后的各行都打印到屏幕上。
from pathlib import Path

path = Path('learning_python.txt')
learning_pythons = path.read_text()

lines = learning_pythons.splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)

print("------------------------------------------------------------------------------------------------------")

print(lines)