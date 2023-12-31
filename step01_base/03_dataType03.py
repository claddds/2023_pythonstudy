# 리스트(list): 배열과 같은 의미
#               리스트내에는 어떠한 자료형도 포함 시킬수도 있다.
# su1 = [10,20,30]
# su2 = ["홍길동","이길동","박길동"]
# su3 = [10, "홍길동", 127.6]
# su4 = [10, ["홍길동", 24, 76.1],172.6]

su1 = [10,20,30]
print(su1[0])
print(su1)
print(su1[0]+su1[1])
print(su1[-1])

# 이중 리스트 구조
su2 = [10,20,30,["ab","cd","df"]]

print(su2[3])   #["ab", "cd", "ef]
print(su2[3][1])    # "cd"
print(su2[-1][1])   # "cd"
print(su2[-1][-1])  # "ef"

# 삼중 리스트 구조
su3 = [10,20,['aa','bb','cc',["오펜하이머","무빙","명량"]]]
print(su3[2][3][1]) # 무빙

# 리스트 슬라이싱
su4 = [1,10,100,1000,10000]
print(su4[2:3]) #[100]
print(su4[:3])  #[1,10,100]


su5 = [1,10,100,["ab","cd","ef"],1000,10000]
print(su5[2:5]) # [100, ['ab', 'cd', 'ef'], 1000]
print(su5[3][1:])   # ['cd', 'ef']

# 리스트 연산(+,*:반복)
k1 = [10,20]
k2 = [100,200,300]

print(k1+k2)    #[10, 20, 100, 200, 300]
print(k1*2) #[10, 20, 10, 20]
print(k2 * 5)   #[100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300, 100, 200, 300]

# 리스트 값 변경하기
# 문자열, 튜플의 요소값은 변경(수정, 삭제, 생성)할 수 없다
# 리스트의 요소값은 변경(수정, 삭제, 생성)할 수 있다

k3 = [100,200,300]
k3[1] = 20000
print(k3)   # [100, 20000, 300]

k3[2:] = ["국제시장", "명량"]
print(k3)   #[100, 20000, '국제시장', '명량']

k3[1:3] = ["백", "천", "만","백만"]
print(k3)   #[100, '백', '천', '만', '백만', '명량']

k3[2:3] = []    #요소삭제   [100, '백', '만', '백만', '명량']
print(k3)

del k3[3]   # [100, '백', '만', '명량']
print(k3)