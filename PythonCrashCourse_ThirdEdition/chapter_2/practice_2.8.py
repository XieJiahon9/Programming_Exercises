#练习2.8 文件扩展名：Python 提供了removesuffix()方法，其工作原理与removeprefix()很像。
#请将值'python_notes.txt'赋给变量filename，再使用removesuffix()方法来显示不包含扩展名的文件名，就像文件浏览器所做的那样。
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))
