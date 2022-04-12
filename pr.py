
from calendar import c


jumin = "990120-1234567"

print ("성별 : " + jumin[7])
print ("연 : " + jumin[0:2]) # 0 ~ 2 직전까지 (0, 1)
print ("월 : " + jumin[2:4])
print ("일 : " + jumin[4:6])

print ("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print ("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지
print ("뒤 7자리 : " + jumin[-7:]) # 7부터 끝까지

python = "Python is Amazing"
print (python.lower()) # 변수의 문자를 소문자로 출력
print (python.upper()) # 변수의 문자를 대문자로 출력
print (python[0].isupper()) # 변수의 x번째의 문자가 대문자면 true 소문자면 false
print (len(python)) # 변수의 문자의 갯수 (띄어쓰기 포함)
print (python.replace("Python", " Java")) # 변수에서의 문자를 다른 문자로 변경하여 출력

index = python.index("n") # 변수에 어떤 문자가 몇 번째에 있는지 숫자로 출력
print (index)
index = python.index("n", index + 1) # 변수에 어떤 문자가 첫 번째에 나오는 것에 x 번째 다음 그 문자가 있는지 숫자로 출력
print (index)

print (python.find("Java")) # find는 원하는 문자가 없다면 -1
#print (python.index(Java)) # index는 원하는 문자가 없다면 실행이 안됌
print("hi")

print (python.count("n")) # 변수 내에서 원하는 문자가 몇 번 나왔는지 출력

# print ("a" + "b")
# print ("a" , "b")

# 방법 1
print ("나는 %d살입니다." % 20 ) # "%d" % x x의 값을 d에 적용하여 출력
print ("나는 %s을 좋아해요" % "파이썬") # "%s" % "X" X인 문자를 s에 적용하여 출력
print("Apple 은 %c로 시작해요" % "A") # %c는 위와 다르게 한 글자만 출력 가능

print ("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # "%s %s" % ("a" , "b") a와 b를 s에 순서대로 적용하여 출력

print ("-"*50)

# 방법 2
print ("나는 {}살입니다.".format(20)) # "{}".format(x) {}안에 x를 적용하여 출력
print ("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) # "{} {}".format("a", "b") {}들에 a와 b를 순서대로 적용하여 출력
print ("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # "{} {}".format("a", "b") {}들 안에 0~ 숫자를 넣어 그에 해당하는 문자를 적용하여 출력
print ("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

print ("-"*50)

# 방법 3
print ("나는 {age}살이며, {color}색을 좋아해요.".format(age = 17, color = "검정색"))
print ("나는 {age}살이며, {color}색을 좋아해요.".format(color = "검정색", age = 17))

print ("-"*50)

# 방법 4 (파이썬 v3.6 이상~)
age = 17
color = "검정색"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # f"" f는 포맷인 듯

print ("-"*50)

# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "KGM입니다."
# print ('저는 "KGM"입니다')
print ("저는 \"KGM\"입니다.")
print ("저는 \'KGM\'입니다.")

# \\ : 문장 내에서 \
print ("C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python310-32\\python.exe c:\\kg/JH\\pr.py")
# \r : 커서를 맨 앞으로 이동
print ("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print ("Redd\bApple")

# \t : 탭
print ("Red\tApple")

print ("-"*50)

# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10 , 20, 30]
print (subway)

subway = ["유재석", "조세호", "박명수"]
print (subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print (subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print (subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print (subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print (subway.pop())
print (subway)

# print (subway.pop())
# print (subway)

# print (subway.pop())
# print (subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print (subway)
print (subway.count("유재석"))

# insert : 리스트에 추가
# pop : 뒤에서 부터 하나씩 제거

print ("-"*50)

# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print (num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print (num_list)

# # 모두 지우기
# num_list.clear()
# print (num_list)

# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
# print (mix_list)

# 리스트 확장
num_list.extend(mix_list)
print (num_list)

# sort : 리스트 정렬
# reverse : 리스트 뒤에서부터 정렬
# clear : 모두 지우기
# A.extend(B) : 리스트 결합

print ("-"*50)

# cabinet = {3:"유재석" , 100:"김태호"}
# print (cabinet[3])
# print (cabinet[100])

# print (cabinet[5]) # 안됌
# print (cabinet.get(5, "사용 가능")) 

# print (3 in cabinet) # True
# print (5 in cabinet) # False

cabinet = {"A-3":"유재석" , "B-100":"김태호"}
print (cabinet["A-3"])
print (cabinet["B-100"])

# 새 손님
print (cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print (cabinet)

# 간 손님
del cabinet["A-3"]
print (cabinet)

# key 들만 출력
print (cabinet.keys())

# value 들만 출력
print (cabinet.values())

# key, value 쌍으로 출력
print (cabinet.items())

# 목용탕 폐점
cabinet.clear()
print (cabinet)

# X = {key1:a, key2:b} 값 지정

# X[key1] = c 다른걸로 변경 가능
# X[key3] = d 새 key 추가 가능

# key 들만 출력
# print (cabinet.keys())

# # value 들만 출력
# print (cabinet.values())

# # key, value 쌍으로 출력
# print (cabinet.items())

