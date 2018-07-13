# 用双向队列可以很轻松解决 判断回文问题
# 先将字符串以普通队列方式入队，之后不断迭代判断首尾元素是否相等

from pythonds.basic.deque import Deque
def palchecker(aString):
    chardeque = deQue()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
