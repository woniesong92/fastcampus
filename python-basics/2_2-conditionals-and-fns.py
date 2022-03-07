#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. 조건문, 함수

# Section. 조건문

# 파이썬에서는 이꼴 사인 두개로 왼쪽과 오른쪽이 동일한지 나타냄
if (1 + 1 == 2):
  print("1+1 는 2 가 맞지!")

# 반대로 왼쪽과 오른쪽이 다르다는걸 나타내는건 !=
if (1 + 1 != 3):
  print("1+1 가 3 은 아니지!")

# 그 외에 수학에서 쓰는 부등호 사용 가능
# >, <, >=. <=

# 미성년자인지 확인하려면?
brad_age = 19
if (brad_age >= 19):
  print("브래드는 성인입니다")
else:
  print("브래드는 미성년자입니다")

# 아재인지 확인하려면?
chuck_age = 19
if (chuck_age >= 30):
  print("척은 아재입니다")
elif (chuck_age >= 19): # 위에 if 가 참이 아니면 elif 가 참인지 체크
  print("척은 성인입니다")
else: # 위에 if 와 elif 들이 참이 아니면 else 실행
  print("척은 미성년자입니다")

# 여러개의 elif도 사용 가능
name = "Wonie"
if (name == "Brad"):
  print("이름은 Brad 입니다")
elif (name == "Chuck"):
  print("이름은 Chuck 입니다")
elif (name == "Wonie"):
  print("이름은 Wonie 입니다")
else:
  print("잘못된 이름입니다")

# Section. 함수
print("안녕 영희야, 잘 지내니?")
print("안녕 철수야, 잘 지내니?")
print("안녕 제니야, 잘 지내니?")

# 함수 = 코드 재사용을 위해 만들어 낸 개념
# 인풋을 받아서 아웃풋을 냄 (인자를 받아서 결과값을 도출)

def greet(name):
  print(f'안녕 {name}야, 잘 지내니?')

greet("영희")
greet("철수")
greet("제니")

def hello_world():
  print("Hello World!")
hello_world()

# 인자를 몇개를 받아야 할지 모를때
def greet(*names):
  print(f"안녕 {', '.join(names)}!")
greet("영희", "철수", "제니")

# 인자를 순서대로 받는게 헷갈릴 경우
def greet(name, age, location):
  print(f"안녕 {name} 아, 넌 {age} 살이고 {location} 에 사는구나!")

# 함수를 잘 사용한 예시
greet("철수", 19, "서울")

# 함수를 잘못 사용한 예시
greet("철수", "서울", 19)

# 키워드 아규먼트 (kwargs) 를 사용해서 실수를 줄일 수 있음
greet(name="철수", location="서울", age=19)
