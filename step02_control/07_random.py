# 난수 함수
# from random import random
#import random
from random import *

# 0.0 이상 1.0 미만의 임의의 실수
print(random())
# print(random.random())

# 1.0 이상 3.0 미만
print(uniform(1.0,3.0))

# 1 이상 10 이하(포함)
print(randint(1,10))

# 1-10미만
print(randrange(1,10))

# [] 안에 존재하는 값 중 하나 선택
print(choice([1,9,56,435,77,4]))