'''
+ 더하기
- 뺄셈
* 곱셈
/ 나누기
** 제곱
% 나머지
// 몫
a > b b보다 a가 크다.
a < b a보다 b가 크다.
a >= b b보다 a가 크거나 같다.
a <= b a보다 b가 크거나 같다.
a == b a와 b는 똑같다'''

print(1+1) # 2
print(5-1) # 4
print(8*7) # 56
print(9/3) # 3

print(3**3) # 27
print(5%3) # 2
print(10%5) # 0
print(5//2) # 2

print (10 > 7) # true
print (13 > 15) # false
print (7 < 19) # true
print (27 < 12) # false

print (10 >= 10) # true
print (13 >= 15) # false
print (7 <= 8) # true
print (27 <= 12) # false

print (99 == 99) # true
print (17 + 3 == 20) # true
print (2 == 3) # false
print (1 + 1 == 3) # false

'''
a != b a 와 b는 같지 않다.
not(a != 3) a와 b는 같지 않지 않다
and = & 둘 다 맞으면 true 둘 중 하나가 틀리다면 false
or = | 둘 다 맞거나 둘 중 하나가 틀려도 ture 둘 다 틀리다면 false
'''

print (1 !=3) # true
print (not(1 != 3)) # false

print ((3 > 0 ) and (3 < 5)) # true
print ((3 > 0) & (3 < 5)) # true
print ((3 < 0) and (3 < 5)) # false 
print ((3 < 0) & (3 > 5)) # false

print ((3 > 0 ) or (3 < 5)) # true
print ((3 > 0) | (3 > 5)) # true
print ((3 < 0) or (3 > 5)) # false
print ((3 < 0) | (3 > 5)) # false

print (7 > 5 > 1) # true
print (3 > 2 > 7) # false

print (1 + 5 * 7) # 36
print ((1 + 5) * 7) # 42

'''
number = number + x
number += x = number + x
.
.
.
'''

number = 7 + 9 * 8 # 79
print (number)
number = number + 1 # 80
print (number)
number += 2 # 82
print (number)
number *= 2 # 164
print (number)
number /= 4 # 41
print (number)
number -= 1 # 40
print (number)

number %= 2 # 0
print (number)

'''
abs(a) = a의 절대값
pow(a, b) a의 b제곱
max(a, b) a와 b 중에 제일 큰 값을 출력
min(a, b) a와 b 중에 제일 작은 값을 출력
round(a) a를 반올림 또는 내림
'''

print (abs(-7)) # 7
print (pow(9 , 2)) # 9^2 = 9*9 = 81
print (max(1 , 5 , 7 , 9)) # 9
print (min(2 , 4 , 6 , 8)) # 2
print (round(1.15))
print (round(9.99))

'''
from math import *
floor(x) x를 반올림
ceil(x) x를 반버림
sprt(x) x의 제곱근 출력

from random improt *
print (random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print (random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print (int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성 
print (randrange(a, b)) # a ~ b 미만의 임의의 값 생성
print (randint(a, b)) # a ~ b 이하의 임의의 값 생성
'''
from math import *
print (floor(10.99)) # 반올림
print (ceil(4.15)) # 내림
print (sqrt(9)) # 제곱근

from random import *
print (random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print (random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print (int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성 
print (int(random() * 10) + 1) # 0 ~ 10 이하의 임의의 값 생성

print ("-" * 50)

print (int(random() * 100) + 1) # 0 ~ 100 이하의 임의의 값 생성
print (int(random() * 100) + 1) # 0 ~ 100 이하의 임의의 값 생성
print (int(random() * 100) + 1) # 0 ~ 100 이하의 임의의 값 생성
print (int(random() * 100) + 1) # 0 ~ 100 이하의 임의의 값 생성
print (int(random() * 100) + 1) # 0 ~ 100 이하의 임의의 값 생성

print ("-" * 50)

print (randrange(1, 101)) # 1 ~ 101 미만의 임의의 값 생성
print (randrange(1, 101)) # 1 ~ 101 미만의 임의의 값 생성
print (randrange(1, 101)) # 1 ~ 101 미만의 임의의 값 생성
print (randrange(1, 101)) # 1 ~ 101 미만의 임의의 값 생성
print (randrange(1, 101)) # 1 ~ 101 미만의 임의의 값 생성

print ("-" * 50)

print (randint(1, 100)) # 1 ~ 100 이하의 임의의 값 생성
print (randint(1, 100)) # 1 ~ 100 이하의 임의의 값 생성
print (randint(1, 100)) # 1 ~ 100 이하의 임의의 값 생성
print (randint(1, 100)) # 1 ~ 100 이하의 임의의 값 생성
print (randint(1, 100)) # 1 ~ 100 이하의 임의의 값 생성

