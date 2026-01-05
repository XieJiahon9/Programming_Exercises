#练习9.14 彩票：创建一个列表或元素，其中包含10个数和5个字母。
#从这个列表或元组中随机选择4个数或字母，并打印一条消息，指出只要彩票上是这4个数或字母，就中大奖了。
from contextlib import nullcontext
from random import choice

lottery = ['3', '9', '4', 'n', '5', 'i', 'l', '2', '1', '7', 'w', '0', '8', 'e', '6']
result = ''

times = 4
while times > 0:
    result += choice(lottery)
    times -= 1

print(f"The result is {result}.")
if result == 'win7':
    print("You win the Grand Prize!")
else:
    print("You don't win the prize.")
