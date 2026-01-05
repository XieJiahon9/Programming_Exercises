#练习6.4 词汇表2：现在你知道了如何遍历字典，请整理你为练习6.3编写的代码，将其中的一系列函数调用print()替换为一个遍历字典中键和值的循环。
#确保该循环正确无误后，再在词汇表中添加5个Python术语。
#当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
glossary = {
    'print':'打印/输出',
    'syntax':'句法',
    'coding':'编码',
    'error':'错误',
    'invalid':'无效',
    'input':'输入',
    'output':'输出',
    'run':'运行',
    'debug':'调试',
    'binary':'二进制',
}
for word,mean in glossary.items():
    print(f"'{word}' means {mean}")
