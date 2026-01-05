#练习10.10 常见单词：访问古登堡计划，找一些你想分析的图书。下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
#可以使用方法count()来确定特定的单词或短语在字符串中出现了多少次。例如，下面的代码计算'row'在一个字符串中出现了多少次：
#   >>> line = "Row, row, row your boat"
#   >>> line.count('row')
#   >>> line.lower().count('row')
#请注意，通过使用lower()将字符串转换为全小写的，可捕捉要查找的单词的各种格式，而不管其大小写如何。
#编写一个程序，读取你在古登堡计划中获取的文件，并计算单词'the' 在每个文件中分别出现了多少次。
#这里计算得到的结果并不准确，因为诸如'then'和'there'等单词也被计算在内了。
#请尝试计算'the'（包含空格）出现的次数，看看结果相差多少。
from pathlib import Path

path = Path("Romeo and Juliet.txt")
content = path.read_text(encoding='utf-8')  #encoding='utf-8',系统的默认编码与要读取的文件的编码不一致，参数encoding必不可少

words = content.split()
print(f"The Romeo and Juliet has about {len(words)} woeds.\n")

num_the = content.count("the")
num_the_space = content.count("the ")

print(f"The number of 'the..' is {num_the}.(may include 'then'、'there' and so on.) \n The number of 'the ' is {num_the_space}.")