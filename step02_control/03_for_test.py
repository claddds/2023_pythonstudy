# 1-10까지의 합, 홀수의 합, 짝수의 합

sum_0 = 0;
for i in range(11):
    sum_0 = sum_0+i

print(sum_0)

sum_1 = 0;
for i in range(11):
    if i%2 == 1:
        sum_1 = sum_1 + i

print(sum_1)

sum_2 = 0;
for i in range(11):
    if i%2 == 0:
        sum_2 = sum_2 + i

print(sum_2)

print("범위(range): ", sum(range(11)))