#练习4.5 100万求和：创建一个包含数1～1 000 000的列表，再使用min()和max()核实该列表确实是从1开始、到1 000 000结束的。
#另外，对这个列表调用函数 sum()，看看Python将100万个数相加需要多长时间。
numbers = [number for number in range(1, 1_000_001)]
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum is {sum(numbers)}")