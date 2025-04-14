import utils

numbers = input("Enter numbers separated by spaces: ")
output = list(map(int, numbers.split()))
#list()函数是用于创建列表对象，将可迭代对象转换为列表
# map()函数是将一个函数应用到一个序列的每个元素上，map 返回一个迭代器，然后 list()函数将其转换为列表
# 这里是将 int()函数应用到 numbers 当中的每个元素上，将其转换为整数。
#又要 python比较字符串是通过 ASCII 码值来比较的，所以需要将其转换为整数，才能比较不同位数数字的大小
print(utils.find_max(output))