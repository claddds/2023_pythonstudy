# https://pandas.pydoto.org/
import pandas as pd
import pandasEx02 as ex02

# 한번에 value값 계산 가능
div = ex02.city / 1000000
print(div)
print('-' * 50)

# 시리즈 인덱싱 0 부터
print(ex02.city[1])
print(ex02.city['대전'])
print('-' * 50)

# 배열 인덱싱을 사용할 경우 (순서, 변경 가능)
print(ex02.city[[1,3,0]])
print('-' * 50)

print(ex02.city[['대전', '서울', '부산']])
print('-' * 50)

# 슬라이싱
print(ex02.city[1:3])   # 3은 포함 되지 않는다
print('-' * 50)

a = pd.Series(range(3), index=['가', '1', 'A'])
print(a)
print('-' * 50)
