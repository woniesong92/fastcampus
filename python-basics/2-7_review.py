#!/usr/bin/python
# -*- coding: utf-8 -*-

# CH. 리뷰

# 타입 캐스팅을 해야할때는?
x = 1 + "hello"

# 같은 이름 5개가 들어있는 리스트?
names = ['철수', '영희', '민희', '제니', '워니']

# 이 리스트를 반복하는 방법은?
for name in names:
  print(name)

for i in range(len(names)):
  print(names[i])

i = 0
while i < len(names):
  print(names[i])
  i += 1

# list vs tuple 의 공통점, 차이점, 사용용도?
# dict vs set 의 공통점, 차이점, 사용용도?

# 똑같은 이름이 몇개인지 세려면?
names = ['철수', '철수', '영희', '영희', '민희']
counter = {}
for name in names:
  counter[name] += 1
print(counter)

# 클래스와 오브젝트의 차이는?
class Person:
  def __init__(self, name):
    self.name = name

  def say_hi(self):
    print("안녕 난 " + name)

p1 = Person("철수")
p2 = Person("민희")

# 모르는게 있을땐?
# 구글에 에러를 검색해보기