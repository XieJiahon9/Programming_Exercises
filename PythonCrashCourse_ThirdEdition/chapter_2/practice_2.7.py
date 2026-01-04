#练习2.7 删除人名中的空白：用变量表示一个人的名字，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和 "\n" 各一次。
#打印这个人名，显示其开头和末尾的空白。然后，分别使用函数lstrip()、rstrip() 和 strip() 对人名进行处理，并将结果打印出来。
name = "   Peter Griffin   "
print(name.lstrip())
print(name.rstrip())
print(name.strip())
print(name)