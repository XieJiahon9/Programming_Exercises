#练习4.4 100万：创建一个包含数1～1 000 000的列表，再使用一个for循环将这些数打印出来。
#（如果输出的时间太、长，按Ctrl+C停止输出，或关闭输出窗口。）
numbers = list(range(1, 1_000_001))
for number in numbers:
    print(number)
