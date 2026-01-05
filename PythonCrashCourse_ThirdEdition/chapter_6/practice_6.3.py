#练习6.3 词汇表1：Python字典可用于模拟现实生活中的字典。为避免混淆，我们将后者称为词汇表。
#想出你在前面学过的5个编程术语，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。以整洁的方式打印每个术语及其含义。
#为此，既可以先打印术语，在它后面加上一个冒号，再打印其含义；
#也可以先在一行里打印术语，再使用换行符（\n）插入一个空行，然后在下一行里以缩进的方式打印其含义。
glossary = {'print':'打印/输出', 'syntax':'句法', 'coding':'编码', 'error':'错误', 'invalid':'无效'}
for word in glossary:
    print(f"'{word}' means {glossary.get(word, 'No this word in this glossary')}")
    #print(f"{word}: {glossary[word]}") #先打印术语，在它后面加上一个冒号，再打印其含义
    #print(f"{word}\n{glossary[word]}\n") #先在一行里打印术语，再使用换行符插入一个空行，然后在下一行里以缩进的方式打印其含义。
#print(glossary.get('hello', 'No this word in this glossary')) #测试不在字典中时候的情况

#这道题想让我们用五个print()函数分别打出五个词，可参考fpr循环中的print()函数逐个输出