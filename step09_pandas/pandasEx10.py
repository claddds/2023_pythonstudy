from pandas import DataFrame

df = DataFrame([
    {'name':'홍길동','b_day':'1987-10-19'},
    {'name':'일지매','b_day':'1993-08-11'},
    {'name':'장길산','b_day':'2001-04-01'},
    {'name':'임꺽정','b_day':'1996-11-05'}
])
print(df)
print('-' * 30)

def clip_year(col):
    return col.split('-')[0]

# b-day가 clip_year 함수에 적용되어서 df에 추가한다.
df['year']=df['b_day'].apply(clip_year)
print(df)

def get_age(year, c_year):
    return c_year - int(year)

df['age'] = df['year'].apply(get_age, c_year=2023)
print(df)
print('-' * 30)