import ecommerce.shipping
from ecommerce.shipping import calc_shipping # 直接导入 ecommerce.shipping 模块
from ecommerce import shipping #  # 导入 ecommerce 包当中的shipping 模块
#三种调用方式



ecommerce.shipping.calc_shipping()
#调用 ecommerce Package 当中shipping.py 模块的 calc_shipping 函数

calc_shipping()
shipping.calc_shipping() 
