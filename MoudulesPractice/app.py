import converters
from converters import kg_to_lbs
#可以单独导入一个 Modules 当中的函数

print(kg_to_lbs(60))  #当单独导入一个函数的时候，可以直接调用此函数
print(converters.kg_to_lbs(70))